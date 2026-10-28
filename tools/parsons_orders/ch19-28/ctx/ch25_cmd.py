IMPORTS = """import java.util.*;
import org.wpilib.command3.*;
import static org.wpilib.units.Units.Seconds;
"""
LOGMAIN = ""
CTX = {}

CTX["25.2-commands-and-command-compositions.md"] = dict(
    main="Main", cp="__WPCP__", replace=(".whenExited(", ".whenCanceled("),
    prefix=IMPORTS + "public class Climber implements Mechanism\n{",
    suffix="""    int topAfter = 2;
    int polls = 0;
    public void extendHook() { Main.log.add("extendHook"); }
    public boolean hookAtTop() { return ++polls > topAfter; }
    public void holdPosition() { Main.log.add("holdPosition"); }
}""",
    extras=[IMPORTS + """public class Main
{
    static final List<String> log = new ArrayList<>();
    public static void main(String[] args)
    {
        TestSupport.init();
        Scheduler s = Scheduler.getDefault();
        Climber c = new Climber();
        Command cmd = c.extendHookCommand();
        System.out.println(cmd.name() + " | requires climber: " + cmd.requires(c));
        s.schedule(cmd);
        for (int i = 1; i <= 5; i++)
        {
            log.clear();
            s.run();
            System.out.println("loop " + i + ": " + log + " running=" + s.isRunning(cmd));
        }
        Climber c2 = new Climber();
        c2.topAfter = 100;
        Command cmd2 = c2.extendHookCommand();
        s.schedule(cmd2);
        for (int i = 1; i <= 3; i++)
        {
            log.clear();
            s.run();
            System.out.println("cancel-run " + i + ": " + log + " running=" + s.isRunning(cmd2));
        }
        log.clear();
        s.cancel(cmd2);
        s.run();
        System.out.println("after cancel: " + log + " running=" + s.isRunning(cmd2));
    }
}
"""])

CTX["25.7-structuring-a-command-based-robot-project.md"] = dict(
    main="Main", cp="__WPCP__",
    prefix=IMPORTS,
    suffix="",
    extras=[IMPORTS + """public class Main
{
    static final List<String> log = new ArrayList<>();
    public static void main(String[] args)
    {
        TestSupport.init();
        Elevator elevator = new Elevator();
        Drive drive = new Drive();
        Command c = Autos.scoreAndBackUp(elevator, drive);
        System.out.println(c.name() + " | requires elevator: " + c.requires(elevator) + ", drive: " + c.requires(drive));
        Scheduler s = Scheduler.getDefault();
        s.schedule(c);
        for (int t = 0; t <= 5; t++)
        {
            log.clear();
            s.run();
            System.out.println("t=" + t + ": " + log + " running=" + s.isRunning(c));
            TestSupport.advance(1.0);
        }
    }
}
""", IMPORTS + """class Elevator implements Mechanism
{
    public Command raiseCommand() { return run(co -> Main.log.add("raise")).named("Raise"); }
    public Command releaseCommand() { return run(co -> Main.log.add("release")).named("Release"); }
}
""", IMPORTS + """class Drive implements Mechanism
{
    public Command driveBackwardCommand()
    {
        return run(co -> { while (true) { Main.log.add("back"); co.yield(); } }).named("Drive Backward");
    }
}
"""])

CTX["25.6-binding-commands-to-triggers.md"] = dict(
    main="Main", cp="__WPCP__",
    prefix=IMPORTS + "import org.wpilib.units.measure.Time;\n",
    suffix="",
    extras=[IMPORTS + """public class Main
{
    static final List<String> log = new ArrayList<>();
    static double now = 0.0;
    public static void main(String[] args)
    {
        TestSupport.init();
        org.wpilib.math.util.MathSharedStore.setMathShared(new org.wpilib.math.util.MathShared()
        {
            public void reportError(String e, StackTraceElement[] st) {}
            public double getTimestamp() { return now; }
        });
        OperatorControls oc = new OperatorControls();
        Scheduler s = Scheduler.getDefault();
        int[][] script = { {0,0}, {1,0}, {1,1}, {1,1}, {1,1}, {1,1}, {1,0}, {0,1}, {1,1}, {1,1}, {1,1}, {1,1}, {1,1}, {0,0}, {0,0} };
        s.run();
        for (int i = 0; i < script.length; i++)
        {
            CommandXboxController.left = script[i][0] == 1;
            CommandXboxController.right = script[i][1] == 1;
            log.clear();
            s.run();
            System.out.println("loop " + i + ": " + log);
            TestSupport.advance(0.1);
            now += 0.1;
        }
    }
}
""", IMPORTS + """class Climber implements Mechanism
{
    public Command climbCommand()
    {
        return run(co -> { try { while (true) { Main.log.add("climb"); co.yield(); } } finally { Main.log.add("climb stopped"); } }).named("Climb");
    }
}
""", IMPORTS + """class CommandXboxController
{
    static boolean left = false, right = false;
    CommandXboxController(int port) {}
    Trigger leftBumper() { return new Trigger(Scheduler.getDefault(), () -> left); }
    Trigger rightBumper() { return new Trigger(Scheduler.getDefault(), () -> right); }
}
"""])

for v in CTX.values():
    pass
