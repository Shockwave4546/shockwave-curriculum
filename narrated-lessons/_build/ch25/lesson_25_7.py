BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.7 &middot; Command-Based Programming</div>
      <h1>Structuring a Command-Based Project</h1>
      <p class="scr-sub">The official WPILib 2027 v3 template &mdash; plus a guide to reading v2 code.</p>
    </div>''',
        "speak": "WPILib 2027's official Commands v3 project template organizes a robot around a thin Robot class, one class per opmode, and two packages.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Standard Project Shape</div>
    <pre class="code"><code>Robot.java          the entry point: mechanisms, controllers, and the scheduler call
ExampleAuto.java    an autonomous opmode, marked @Autonomous
ExampleTeleop.java  a teleop opmode, marked @Teleop
constants/          one small constants class per topic, like DriverConstants
mechanisms/         one file per mechanism, like ExampleMechanism</code></pre>''',
        "speak": "An opmode is one selectable mode of robot behavior, score and back up or two-piece auto for autonomous, driver teleop for teleop. The drive team picks one on the Driver Station before enabling. This OpModeRobot framework is new for 2027, so details may still shift before the season.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Robot: Deliberately Thin</div>
    <pre class="code"><code><span class="k">public class</span> Robot <span class="k">extends</span> OpModeRobot
{
    <span class="k">final</span> CommandXboxController driverController =
        <span class="k">new</span> CommandXboxController(DriverConstants.DRIVER_CONTROLLER_PORT);
    <span class="k">final</span> Intake intake = <span class="k">new</span> Intake(driverController.a(), driverController.b());
    <span class="k">final</span> Drive drive = <span class="k">new</span> Drive();
    <span class="k">final</span> Shooter shooter = <span class="k">new</span> Shooter();

    <span class="k">public</span> Robot()
    {
        intake.setDefaultCommand(intake.stateMachineCommand()); <span class="c">// Lesson 25.5's machine</span>
    }

    <span class="me">@Override</span>
    <span class="k">public void</span> robotPeriodic()
    {
        Scheduler.getDefault().run(); <span class="c">// the most important line in the project</span>
    }
}</code></pre>''',
        "speak": "Robot extends WPILib's OpModeRobot. It creates the mechanisms and controllers, sets any default commands that apply everywhere, and runs the scheduler, and almost nothing else. The fields are final and package-private, so opmode classes in the same package can read robot dot intake, but code outside the package can't. Piling large amounts of imperative logic directly into Robot dot java fights the entire declarative philosophy from Lesson 25.1.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">One Class per Mode</div>
    <pre class="code"><code><span class="me">@Teleop</span>
<span class="k">public class</span> DriverTeleop <span class="k">implements</span> OpMode
{
    <span class="k">public</span> DriverTeleop(Robot robot)
    {
        robot.driverController.rightBumper().whileTrue(robot.intake.ejectCommand());
    }
}</code></pre>''',
        "speak": "An opmode implements WPILib's OpMode interface and is marked with an annotation, Autonomous or Teleop, so the framework finds it automatically. Its constructor receives the Robot, and bindings made there belong to that opmode's scope, they only work while it's selected. Passing the Robot into each opmode's constructor is dependency injection, first seen in Lesson 25.2's factories.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Autonomous: Scheduled in start()</div>
    <pre class="code"><code><span class="me">@Autonomous</span>(name = <span class="s">"Drive Then Shoot"</span>)
<span class="k">public class</span> DriveThenShoot <span class="k">implements</span> OpMode
{
    <span class="k">private final</span> Command routine;

    <span class="k">public</span> DriveThenShoot(Robot robot)
    {
        routine = Autos.driveThenShoot(robot.drive, robot.shooter);
    }

    <span class="me">@Override</span>
    <span class="k">public void</span> start()
    {
        Scheduler.getDefault().schedule(routine);
    }
}</code></pre>''',
        "speak": "An autonomous opmode usually schedules its routine in start, which runs once, when the robot is enabled, not in the constructor, which runs when the opmode is merely selected while the robot is still disabled. Because the routine is scheduled inside the autonomous opmode, the scheduler cancels it automatically when autonomous ends, there's no separate cancel-in-teleop step to remember.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Constants: One Place for Every Tunable Number</div>
    <pre class="code"><code><span class="k">public final class</span> IntakeConstants
{
    <span class="k">public static final int</span> MOTOR_CHANNEL = 5; <span class="c">// PWM channel</span>
    <span class="k">public static final double</span> INTAKE_SPEED = 0.8;
}</code></pre>''',
        "speak": "Every constant is public static final and named in ALL CAPS, the constants convention from Lesson 7.4, which WPILib 2027's own template uses too. The template gives each topic its own small class in the constants package. Changing one tunable value, like the intake speed, means editing exactly one line.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Choosing How to Define a Reusable Command</div>
    <pre class="code"><code><span class="k">public class</span> Shooter <span class="k">implements</span> Mechanism
{
    <span class="c">// built with run(...), so it implicitly requires this shooter</span>
    <span class="k">public</span> Command spinUpCommand()
    {
        <span class="k">return</span> run(coroutine -&gt; {
            setSpeed(ShooterConstants.SPIN_SPEED);
            coroutine.park();
        }).whenExited(() -&gt; setSpeed(0.0)).named(<span class="s">"Spin Up"</span>);
    }
}</code></pre>''',
        "speak": "For a command tied to exactly one mechanism, an instance factory method like this one is the natural home. A command that needs to coordinate several mechanisms at once is better as a static factory, and a class that implements Command directly is for genuine internal state or unusually complex logic.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">A Static Factory for Multiple Mechanisms</div>
    <pre class="code"><code><span class="k">public final class</span> Autos
{
    <span class="k">public static</span> Command driveThenShoot(Drive drive, Shooter shooter)
    {
        <span class="k">return</span> Command.sequence(
            drive.driveForwardCommand().withTimeout(Seconds.of(2)),
            shooter.shootCommand()
        ).named(<span class="s">"Drive Then Shoot"</span>);
    }
}</code></pre>''',
        "speak": "Here, driveThenShoot needs both the drive and the shooter, so it doesn't naturally belong to either one, a static factory taking both as parameters is dependency injection again, the method gets exactly what it needs, explicitly.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Reading Commands v2 Code (2026 and Earlier)</div>
    <pre class="code"><code><span class="c">// Commands v2 (2026 and earlier): for recognizing, not for writing new code</span>
<span class="k">public class</span> Intake <span class="k">extends</span> SubsystemBase    <span class="c">// v3: implements Mechanism</span>
{
    <span class="k">public</span> Command runCommand()
    {
        <span class="c">// v3: run(...) with park(), plus whenExited(...), plus .named(...)</span>
        <span class="k">return</span> startEnd(() -&gt; set(0.8), () -&gt; set(0.0));
    }
}

<span class="k">public class</span> FeedUntilLoaded <span class="k">extends</span> Command  <span class="c">// v3: one factory method with one body</span>
{
    <span class="k">private final</span> Intake intake;

    <span class="k">public</span> FeedUntilLoaded(Intake intake)
    {
        <span class="k">this</span>.intake = intake;
        addRequirements(intake);              <span class="c">// v3: requirements come from the builder</span>
    }

    <span class="me">@Override</span>
    <span class="k">public void</span> initialize() { intake.set(0.6); }            <span class="c">// v3: code before the loop</span>

    <span class="me">@Override</span>
    <span class="k">public boolean</span> isFinished() { <span class="k">return</span> intake.hasPiece(); } <span class="c">// v3: the loop condition</span>

    <span class="me">@Override</span>
    <span class="k">public void</span> end(<span class="k">boolean</span> interrupted) { intake.set(0.0); } <span class="c">// v3: whenExited(...)</span>
}</code></pre>''',
        "speak": "Commands v2 is what most existing team code, including our own older code, still uses, and it's what most examples online show. This section is for recognizing v2 code when you read it, not for writing new code. Here's one v2 mechanism and one v2 command class, extends SubsystemBase becomes implements Mechanism, addRequirements becomes requirements from the builder, and the four lifecycle methods, initialize, isFinished, end, all fold into one coroutine body.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">v2 &rarr; v3, a Few More</h2><ul>
      <li><span class="num">1</span><span><strong>CommandScheduler.getInstance()</strong> &rarr; <strong>Scheduler.getDefault()</strong></span></li>
      <li><span class="num">2</span><span><strong>RobotContainer</strong> &rarr; <strong>Robot extends OpModeRobot</strong>, plus opmode classes</span></li>
      <li><span class="num">3</span><span><strong>InterruptionBehavior</strong> &rarr; priorities; <strong>kMotorId</strong> &rarr; <strong>MOTOR_CHANNEL</strong></span></li>
    </ul></div>''',
        "speak": "A few more mappings worth knowing by sight. CommandScheduler dot getInstance becomes Scheduler dot getDefault. RobotContainer becomes Robot extending OpModeRobot, plus separate opmode classes. Interruption behavior becomes priorities, and the old kMotorId constant style becomes ALL CAPS names like MOTOR underscore CHANNEL. Two more habits you'll spot: v2 commands don't have to be named, and v2 compositions return a finished command with no dot named at the end.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Declaring mechanisms as static fields for easy access.</li>
      <li><span class="check">!</span>Scheduling an autonomous routine in the opmode's constructor instead of start().</li>
      <li><span class="check">!</span>Pasting v2 code into a v3 project &mdash; translate it with the mapping table instead.</li>
    </ul></div>''',
        "speak": "A few pitfalls. Declaring mechanisms as static fields for easy access, that bypasses the scheduler's resource management entirely. Scheduling an autonomous routine in the opmode's constructor instead of start, the constructor runs while the robot is still disabled. And pasting v2 code straight into a v3 project, names like SubsystemBase and CommandScheduler simply don't exist in v3, translate the code instead of mixing the two frameworks.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A thin Robot (extends OpModeRobot), one class per opmode, a constants and a mechanisms package.</li>
      <li><span class="check">&#10003;</span>robotPeriodic() must call Scheduler.getDefault().run() &mdash; nothing works without it.</li>
      <li><span class="check">&#10003;</span>Choose instance factory, static factory, or a Command class based on the command's shape.</li>
      <li><span class="check">&#10003;</span>Most existing team code is still v2 &mdash; recognize it, translate it, don't mix it with v3.</li>
    </ul></div>''',
        "speak": "So: a thin Robot extending OpModeRobot, one class per opmode marked Autonomous or Teleop, a constants package and a mechanisms package, and that one robotPeriodic call that makes everything else in this entire chapter actually run. That wraps up Chapter 25. Great work making it through command-based programming, from a single command all the way to a full v3 project. See you in the next chapter.",
    },
]
