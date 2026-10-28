import javax.tools.*;
import java.io.*;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/** Compiles and runs candidate programs in one JVM. Reads a records file, prints "idx\tstatus\tbase64(stdout)\n" per candidate.
 *  Records file: blocks separated by a line containing only \u0001. Block line 1 = idx, line 2 = main class, rest = source.
 *  status: OK0 (ran, exit 0), EXC (uncaught exception, exit 1), CE (compile error). */
public class Runner {
    static class Src extends SimpleJavaFileObject {
        final String code;
        Src(String name, String code) { super(URI.create("string:///" + name + ".java"), Kind.SOURCE); this.code = code; }
        public CharSequence getCharContent(boolean b) { return code; }
    }
    static class Out extends SimpleJavaFileObject {
        final ByteArrayOutputStream bos = new ByteArrayOutputStream();
        Out(String name, Kind k) { super(URI.create("mem:///" + name.replace('.', '/') + k.extension), k); }
        public OutputStream openOutputStream() { return bos; }
    }
    static class Capped extends OutputStream {
        final ByteArrayOutputStream b = new ByteArrayOutputStream();
        public void write(int x) { if (b.size() > 1_000_000) throw new RuntimeException("cap"); b.write(x); }
    }
    public static void main(String[] args) throws Exception {
        String all = new String(Files.readAllBytes(Paths.get(args[0])), StandardCharsets.UTF_8);
        int from = Integer.parseInt(args[1]);
        JavaCompiler jc = ToolProvider.getSystemJavaCompiler();
        PrintStream realOut = System.out;
        PrintStream stdout = new PrintStream(new FileOutputStream(FileDescriptor.out), true);
        System.setIn(new ByteArrayInputStream(new byte[0]));
        for (String rec : all.split("\u0001\n")) {
            if (rec.isEmpty()) continue;
            int n1 = rec.indexOf('\n'), n2 = rec.indexOf('\n', n1 + 1);
            int idx = Integer.parseInt(rec.substring(0, n1));
            if (idx < from) continue;
            String mainClass = rec.substring(n1 + 1, n2);
            String code = rec.substring(n2 + 1);
            String status; byte[] out = new byte[0];
            try {
                final Map<String, Out> classes = new HashMap<>();
                StandardJavaFileManager std = jc.getStandardFileManager(null, null, null);
                JavaFileManager fm = new ForwardingJavaFileManager<JavaFileManager>(std) {
                    public JavaFileObject getJavaFileForOutput(Location l, String cn, JavaFileObject.Kind k, FileObject s) {
                        Out o = new Out(cn, k); classes.put(cn, o); return o;
                    }
                };
                boolean ok = jc.getTask(new StringWriter(), fm, d -> {}, List.of("-proc:none", "-nowarn"), null, List.of(new Src(mainClass, code))).call();
                if (!ok) { status = "CE"; }
                else {
                    ClassLoader cl = new ClassLoader() {
                        protected Class<?> findClass(String name) throws ClassNotFoundException {
                            Out o = classes.get(name);
                            if (o == null) throw new ClassNotFoundException(name);
                            byte[] bs = o.bos.toByteArray();
                            return defineClass(name, bs, 0, bs.length);
                        }
                    };
                    Capped cap = new Capped();
                    System.setOut(new PrintStream(cap, true, "UTF-8"));
                    System.setErr(new PrintStream(new ByteArrayOutputStream()));
                    status = "OK0";
                    try {
                        Class<?> c = cl.loadClass(mainClass);
                        c.getMethod("main", String[].class).invoke(null, (Object) new String[0]);
                    } catch (Throwable t) { status = "EXC"; }
                    System.out.flush();
                    out = cap.b.toByteArray();
                }
                std.close();
            } catch (Throwable t) { status = "RUNNERERR"; }
            System.setOut(realOut);
            stdout.println(idx + "\t" + status + "\t" + Base64.getEncoder().encodeToString(out));
        }
    }
}
