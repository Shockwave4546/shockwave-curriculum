import javax.tools.*;
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import java.util.concurrent.*;

/**
 * Batch compile-and-run for Parsons order checking (ch19-28 harness).
 *
 * usage: java [--add-opens ...] Runner.java <candidates-file> <results-file> <mainSimpleName> <stdin-file|-> [jar:jar:...]
 *
 * candidates file: blocks of
 *   @@@CAND <id>
 *   @@@UNIT
 *   <source text of a compilation unit, already starting with "package pN;">
 *   @@@UNIT
 *   ...
 * Candidate <id> is compiled as package p<id>; main class is p<id>.<mainSimpleName>.
 * results file: one line per candidate: id TAB status TAB exit TAB base64(stdout)
 *   status: CE (compile error), OK (ran, exit 0), EXC (uncaught exception, exit 1), TIMEOUT
 */
public class Runner
{
    static class Src extends SimpleJavaFileObject
    {
        final String code;
        Src(String name, String code)
        {
            super(URI.create("string:///" + name.replace('.', '/') + ".java"), Kind.SOURCE);
            this.code = code;
        }
        @Override public CharSequence getCharContent(boolean b) { return code; }
        @Override public boolean isNameCompatible(String simpleName, Kind kind) { return true; }
    }

    static class Out extends SimpleJavaFileObject
    {
        final ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        Out(String name) { super(URI.create("mem:///" + name.replace('.', '/') + ".class"), Kind.CLASS); }
        @Override public OutputStream openOutputStream() { return bytes; }
    }

    static class MemFM extends ForwardingJavaFileManager<StandardJavaFileManager>
    {
        final Map<String, Out> outs = new ConcurrentHashMap<>();
        MemFM(StandardJavaFileManager fm) { super(fm); }
        @Override public JavaFileObject getJavaFileForOutput(Location l, String cn, JavaFileObject.Kind k, FileObject sib)
        {
            Out o = new Out(cn);
            outs.put(cn, o);
            return o;
        }
    }

    static class MemLoader extends URLClassLoader
    {
        final Map<String, byte[]> classes;
        MemLoader(Map<String, byte[]> classes, URL[] urls, ClassLoader parent)
        {
            super(urls, parent);
            this.classes = classes;
        }
        @Override protected Class<?> findClass(String name) throws ClassNotFoundException
        {
            byte[] b = classes.get(name);
            if (b == null) return super.findClass(name);
            return defineClass(name, b, 0, b.length);
        }
    }

    // per-thread stdout routing, so a runaway thread cannot pollute later runs
    static final Map<Thread, ByteArrayOutputStream> sinks = new ConcurrentHashMap<>();
    static final long CAP = 200_000;

    static class Router extends OutputStream
    {
        @Override public void write(int b)
        {
            ByteArrayOutputStream s = sinks.get(Thread.currentThread());
            if (s == null) return;
            if (s.size() > CAP) throw new RuntimeException("output cap");
            s.write(b);
        }
    }

    public static void main(String[] a) throws Exception
    {
        String candFile = a[0], resFile = a[1], mainName = a[2];
        byte[] stdin = a[3].equals("-") ? new byte[0] : Files.readAllBytes(Path.of(a[3]));
        String cp = a.length > 4 ? a[4] : "";
        List<URL> urls = new ArrayList<>();
        List<String> cpOpts = new ArrayList<>();
        if (!cp.isEmpty())
        {
            for (String j : cp.split(":")) urls.add(Path.of(j).toUri().toURL());
            cpOpts.add("-classpath");
            cpOpts.add(cp);
        }
        cpOpts.add("-proc:none");
        cpOpts.add("-nowarn");

        Map<String, List<String[]>> cands = new LinkedHashMap<>(); // id -> list of {name, code}
        String text = Files.readString(Path.of(candFile));
        for (String block : text.split("(?m)^@@@CAND ", -1))
        {
            if (block.isBlank()) continue;
            int nl = block.indexOf('\n');
            String id = block.substring(0, nl).trim();
            String rest = block.substring(nl + 1);
            List<String[]> units = new ArrayList<>();
            int k = 0;
            for (String u : rest.split("(?m)^@@@UNIT\n", -1))
            {
                if (u.isBlank()) continue;
                units.add(new String[] { "p" + id + ".U" + (k++), u });
            }
            cands.put(id, units);
        }

        System.setOut(new PrintStream(new Router(), true));
        JavaCompiler jc = ToolProvider.getSystemJavaCompiler();

        // compile; drop candidates with errors, repeat until the rest compile clean
        Set<String> alive = new LinkedHashSet<>(cands.keySet());
        Set<String> failed = new HashSet<>();
        Map<String, byte[]> allClasses = new HashMap<>();
        while (!alive.isEmpty())
        {
            List<Src> srcs = new ArrayList<>();
            Map<String, String> uriToId = new HashMap<>();
            for (String id : alive)
                for (String[] u : cands.get(id))
                {
                    Src s = new Src(u[0], u[1]);
                    srcs.add(s);
                    uriToId.put(s.toUri().toString(), id);
                }
            DiagnosticCollector<JavaFileObject> dc = new DiagnosticCollector<>();
            StandardJavaFileManager std = jc.getStandardFileManager(null, null, StandardCharsets.UTF_8);
            MemFM fm = new MemFM(std);
            boolean ok = jc.getTask(null, fm, dc, cpOpts, null, srcs).call();
            Set<String> bad = new HashSet<>();
            for (Diagnostic<? extends JavaFileObject> d : dc.getDiagnostics())
            {
                if (d.getKind() != Diagnostic.Kind.ERROR) continue;
                if (System.getenv("PO_DEBUG") != null) System.err.println(d);
                if (d.getSource() == null) continue;
                String id = uriToId.get(d.getSource().toUri().toString());
                if (id != null) bad.add(id);
            }
            if (ok || bad.isEmpty())
            {
                for (Map.Entry<String, Out> e : fm.outs.entrySet()) allClasses.put(e.getKey(), e.getValue().bytes.toByteArray());
                break;
            }
            failed.addAll(bad);
            alive.removeAll(bad);
        }

        try (PrintWriter w = new PrintWriter(Files.newBufferedWriter(Path.of(resFile))))
        {
            for (String id : cands.keySet())
            {
                if (failed.contains(id)) { w.println(id + "\tCE\t-\t"); continue; }
                String pkg = "p" + id + ".";
                Map<String, byte[]> mine = new HashMap<>();
                for (Map.Entry<String, byte[]> e : allClasses.entrySet())
                    if (e.getKey().startsWith(pkg)) mine.put(e.getKey(), e.getValue());
                final ByteArrayOutputStream sink = new ByteArrayOutputStream();
                final int[] exit = { -1 };
                Thread t = new Thread(() ->
                {
                    try
                    {
                        System.setIn(new ByteArrayInputStream(stdin));
                        MemLoader ml = new MemLoader(mine, urls.toArray(new URL[0]), ClassLoader.getPlatformClassLoader());
                        Class<?> c = Class.forName(pkg + mainName, true, ml);
                        java.lang.reflect.Method m = c.getMethod("main", String[].class);
                        m.invoke(null, (Object) new String[0]);
                        exit[0] = 0;
                    }
                    catch (Throwable ex)
                    {
                        exit[0] = 1;
                        if (System.getenv("PO_DEBUG") != null) { Throwable r = ex; while (r.getCause() != null) r = r.getCause(); System.err.println("EXC: " + r); }
                    }
                });
                t.setDaemon(true);
                sinks.put(t, sink);
                t.start();
                t.join(5000);
                String status;
                if (t.isAlive()) status = "TIMEOUT";
                else status = exit[0] == 0 ? "OK" : "EXC";
                byte[] out = sink.toByteArray();
                w.println(id + "\t" + status + "\t" + exit[0] + "\t" + Base64.getEncoder().encodeToString(out));
            }
        }
        System.exit(0);
    }
}
