import javax.tools.*;
import java.io.*;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/** Compiles and runs every dir/N.java candidate; prints "N<TAB>STATUS<TAB>base64(stdout)". Usage: java Runner.java dir stubsDir [stdinFile] */
public class Runner {
    static class Src extends SimpleJavaFileObject {
        final String code;
        Src(String name, String code) { super(URI.create("string:///" + name.replace('.', '/') + ".java"), Kind.SOURCE); this.code = code; }
        public CharSequence getCharContent(boolean b) { return code; }
    }
    static class Out extends SimpleJavaFileObject {
        final ByteArrayOutputStream bos = new ByteArrayOutputStream();
        Out(String name) { super(URI.create("mem:///" + name.replace('.', '/') + ".class"), Kind.CLASS); }
        public OutputStream openOutputStream() { return bos; }
    }
    static class FM extends ForwardingJavaFileManager<StandardJavaFileManager> {
        final Map<String, Out> outs = new HashMap<>();
        FM(StandardJavaFileManager m) { super(m); }
        public JavaFileObject getJavaFileForOutput(Location l, String cn, JavaFileObject.Kind k, FileObject s) {
            Out o = new Out(cn); outs.put(cn, o); return o;
        }
    }
    static class Loader extends ClassLoader {
        final Map<String, Out> outs;
        Loader(Map<String, Out> o) { super(Runner.class.getClassLoader()); outs = o; }
        protected Class<?> findClass(String n) throws ClassNotFoundException {
            Out o = outs.get(n);
            if (o == null) throw new ClassNotFoundException(n);
            byte[] b = o.bos.toByteArray();
            return defineClass(n, b, 0, b.length);
        }
    }
    record Compiled(String mainClass, FM fm, String err) {}

    static Compiled compile(String code) {
        Matcher pm = Pattern.compile("(?m)^package\\s+([\\w.]+);").matcher(code);
        String pkg = pm.find() ? pm.group(1) + "." : "";
        Matcher cm = Pattern.compile("public\\s+class\\s+(\\w+)").matcher(code);
        if (!cm.find()) { cm = Pattern.compile("\\bclass\\s+(\\w+)").matcher(code); if (!cm.find()) cm = null; }
        if (cm == null) return new Compiled(null, null, "no class");
        String cn = pkg + cm.group(1);
        JavaCompiler jc = ToolProvider.getSystemJavaCompiler();
        DiagnosticCollector<JavaFileObject> dc = new DiagnosticCollector<>();
        FM fm = new FM(jc.getStandardFileManager(dc, null, StandardCharsets.UTF_8));
        List<String> opts = List.of("-proc:none", "-Xlint:none", "-sourcepath", STUBS);
        boolean ok = jc.getTask(null, fm, dc, opts, null, List.of(new Src(cn, code))).call();
        if (!ok) {
            StringBuilder sb = new StringBuilder();
            for (var d : dc.getDiagnostics()) if (d.getKind() == Diagnostic.Kind.ERROR) sb.append(d.getMessage(null).replace('\n', ' ')).append(" | ");
            return new Compiled(cn, fm, sb.toString());
        }
        return new Compiled(cn, fm, null);
    }

    static String STUBS;
    public static void main(String[] a) throws Exception {
        Path dir = Path.of(a[0]);
        STUBS = a[1];
        byte[] stdin = a.length > 2 ? Files.readAllBytes(Path.of(a[2])) : new byte[0];
        List<Path> files = new ArrayList<>();
        try (var s = Files.list(dir)) { s.filter(p -> p.toString().endsWith(".java")).forEach(files::add); }
        files.sort(Comparator.comparing(p -> Integer.parseInt(p.getFileName().toString().replace(".java", ""))));
        PrintStream realOut = System.out;
        for (int i = 0; i < files.size(); i++) {
            String id = files.get(i).getFileName().toString().replace(".java", "");
            Compiled c = compile(Files.readString(files.get(i)));
            if (c.err() != null) { realOut.println(id + "\tCOMPILE_ERR\t" + Base64.getEncoder().encodeToString(c.err().getBytes(StandardCharsets.UTF_8))); continue; }
            ByteArrayOutputStream bos = new ByteArrayOutputStream() {
                public synchronized void write(int b) { if (count > 100000) throw new RuntimeException("OUTPUT_LIMIT"); super.write(b); }
                public synchronized void write(byte[] b, int o, int l) { if (count > 100000) throw new RuntimeException("OUTPUT_LIMIT"); super.write(b, o, l); }
            };
            String[] status = {"OK"};
            Thread t = new Thread(() -> {
                try {
                    Class<?> k = new Loader(c.fm().outs).loadClass(c.mainClass());
                    k.getMethod("main", String[].class).invoke(null, (Object) new String[0]);
                } catch (java.lang.reflect.InvocationTargetException e) { status[0] = "EXC:" + e.getCause().getClass().getName();
                } catch (Throwable e) { status[0] = "ERR:" + e; }
            });
            t.setDaemon(true);
            System.setOut(new PrintStream(bos, true));
            System.setIn(new ByteArrayInputStream(stdin));
            t.start(); t.join(2000);
            boolean alive = t.isAlive();
            System.setOut(realOut);
            if (alive) status[0] = "TIMEOUT";
            byte[] out;
            synchronized (bos) { out = bos.toByteArray(); }
            c.fm().outs.clear();
            realOut.println(id + "\t" + status[0] + "\t" + Base64.getEncoder().encodeToString(out));
        }
        System.exit(0);
    }
}
