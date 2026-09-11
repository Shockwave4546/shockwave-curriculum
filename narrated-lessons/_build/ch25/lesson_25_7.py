BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.7 &middot; Command-Based Programming</div>
      <h1>Structuring a Command-Based Project</h1>
      <p class="scr-sub">Putting Subsystems, Commands, the Scheduler, and Triggers together.</p>
    </div>''',
        "speak": "WPILib's own project template organizes a command-based robot around four root-level classes, plus two subdirectories.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Standard Project Shape</h2><ul>
      <li><span class="num">1</span><span><strong>Robot</strong> &mdash; the entry point, kept intentionally thin.</span></li>
      <li><span class="num">2</span><span><strong>RobotContainer</strong> &mdash; subsystems, commands, and trigger bindings.</span></li>
      <li><span class="num">3</span><span><strong>Constants</strong> &mdash; every tunable number, in one place.</span></li>
      <li><span class="num">4</span><span><strong>Subsystems / Commands</strong> &mdash; one file per class.</span></li>
    </ul></div>''',
        "speak": "Robot is the entry point, kept intentionally thin. RobotContainer is where subsystems, commands, and trigger bindings actually get declared. Constants holds globally accessible constants, motor ports, PID gains, speeds. And Subsystems and Commands are subdirectories, one file per user-defined subsystem or command class.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> Robot()
{
    robotContainer = <span class="k">new</span> RobotContainer(); <span class="c">// performs all the actual setup</span>
}

<span class="me">@Override</span>
<span class="k">public void</span> robotPeriodic()
{
    CommandScheduler.getInstance().run(); <span class="c">// THE single most important line in the whole project</span>
}</code></pre>''',
        "speak": "Because command-based is declarative, Robot dot java should contain almost nothing beyond a handful of required calls. The constructor builds a RobotContainer, which does all the real setup. Robot periodic calls CommandScheduler dot get instance dot run, genuinely the single most important line in the whole project.",
    },
    {
        "screen": '''<pre class="code"><code><span class="me">@Override</span>
<span class="k">public void</span> autonomousInit()
{
    autonomousCommand = robotContainer.getAutonomousCommand();
    <span class="k">if</span> (autonomousCommand != <span class="k">null</span>)
    {
        CommandScheduler.getInstance().schedule(autonomousCommand);
    }
}

<span class="me">@Override</span>
<span class="k">public void</span> teleopInit()
{
    <span class="k">if</span> (autonomousCommand != <span class="k">null</span>)
    {
        autonomousCommand.cancel(); <span class="c">// stop auto once teleop begins</span>
    }
}</code></pre>''',
        "speak": "Two more overrides matter here. Autonomous init grabs the autonomous command from RobotContainer and schedules it. And teleop init cancels that autonomous command, so it doesn't keep running once teleop begins. Piling large amounts of imperative logic directly into Robot dot java fights the entire declarative philosophy from lesson 25.1, real setup belongs in RobotContainer.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">private final</span> <span class="t">Intake</span> intake = <span class="k">new</span> Intake();

<span class="k">private void</span> configureBindings()
{
    driverController.b().whileTrue(intake.runIntakeCommand());
}

<span class="k">public</span> Command getAutonomousCommand()
{
    <span class="k">return</span> AutoRoutines.driveAndIntake(drivetrain, intake);
}</code></pre>''',
        "speak": "RobotContainer is where subsystems get declared as private fields, deliberately not global variables. That's dependency injection again, and it's deliberate: if subsystems were globally accessible, any code anywhere could call subsystem methods directly, completely bypassing the scheduler's resource-management guarantees, exactly the two-commands-fighting-over-one-motor problem command-based exists to prevent.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static final class</span> <span class="t">IntakeConstants</span>
{
    <span class="k">public static final int</span> kMotorId = 5;
    <span class="k">public static final double</span> kIntakeSpeed = 0.8;
}</code></pre>''',
        "speak": "Constants get grouped as public static final fields, often nested into classes per subsystem, one intake constants class holding a motor ID and an intake speed, for example. Public static final means it's globally reachable and impossible to accidentally reassign, which you'll remember from Chapter 23's discussion of final.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Choosing How to Define a Command</h2><ul>
      <li><span class="num">1</span><span><strong>Instance factory</strong> &mdash; best for a command tied to exactly one subsystem.</span></li>
      <li><span class="num">2</span><span><strong>Static factory</strong> &mdash; best when coordinating multiple subsystems at once.</span></li>
      <li><span class="num">3</span><span><strong>Full Command subclass</strong> &mdash; best for genuine internal state or complex logic.</span></li>
    </ul></div>''',
        "speak": "When a command needs to be reused in more than one place, a button binding, an autonomous routine, a self-test, you've got a few options, each suited to a different case. An instance factory method on a single subsystem is best when the command is tied to exactly one subsystem. A static factory method is best when a command needs to coordinate multiple subsystems at once, so it doesn't naturally belong to any single one of them. And a full command subclass is best when a command needs its own genuine internal state, or unusually complex logic.",
    },
    {
        "screen": '''<pre class="code" style="font-size:11.5px;"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">SubsystemBase</span>
{
    <span class="k">public</span> Command runIntakeCommand()
    {
        <span class="k">return this</span>.startEnd(() -&gt; <span class="k">this</span>.set(<span class="n">1.0</span>), () -&gt; <span class="k">this</span>.set(<span class="n">0.0</span>)); <span class="c">// implicitly requires this</span>
    }
}</code></pre>''',
        "speak": "Here's what that looks like in code. Intake defines an instance factory, runIntakeCommand, tied to itself.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code" style="font-size:11.5px;"><code><span class="k">public class</span> <span class="t">AutoRoutines</span>
{
    <span class="k">public static</span> Command driveAndIntake(<span class="t">Drivetrain</span> drivetrain, <span class="t">Intake</span> intake)
    {
        <span class="k">return</span> Commands.sequence(
            Commands.parallel(drivetrain.driveCommand(<span class="n">0.5</span>, <span class="n">0.5</span>), intake.runIntakeCommand()).withTimeout(<span class="n">5.0</span>),
            Commands.parallel(drivetrain.stopCommand(), intake.stopCommand())
        );
    }
}</code></pre>''',
        "speak": "And AutoRoutines defines a static factory, driveAndIntake, coordinating both a drivetrain and an intake together, exactly the multiple-subsystem case a static factory is built for.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Declaring subsystems as global or static fields for easy access.</li>
      <li><span class="check">!</span>Forgetting to cancel the autonomous command in teleopInit().</li>
      <li><span class="check">!</span>Scattering constants across many files instead of one Constants class.</li>
    </ul></div>''',
        "speak": "A few pitfalls to close on. Don't declare subsystems as global or static fields for easy access, that defeats the entire resource-management system's purpose, pass subsystems explicitly instead. Don't forget to cancel the autonomous command in teleop init, without it, an unfinished autonomous command can keep running, and keep its subsystem requirements locked, right into teleop. And don't scatter constants across many files instead of one Constants class, changing one tunable value should mean editing exactly one line, not hunting across the whole codebase.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap: Ch. 25</h2><ul>
      <li><span class="check">&#10003;</span>Command-based: describe what happens, once, and let the scheduler handle it.</li>
      <li><span class="check">&#10003;</span>Commands: four lifecycle methods, built-in factories, composable.</li>
      <li><span class="check">&#10003;</span>The scheduler runs a fixed 4-step order, every 20 milliseconds.</li>
      <li><span class="check">&#10003;</span>State machines: an enum field, read and transitioned in periodic().</li>
      <li><span class="check">&#10003;</span>Triggers bind conditions to commands, declaratively.</li>
      <li><span class="check">&#10003;</span>Robot stays thin; RobotContainer, Constants, Subsystems, Commands hold the rest.</li>
    </ul></div>''',
        "speak": "So that's the whole of Chapter 25. Command-based programming describes what should happen, once, and lets the scheduler handle it every loop. Commands are built from four lifecycle methods, mostly through built-in factories, and compose into bigger commands. The scheduler runs a fixed four-step order, every 20 milliseconds. State machines use a single enum field, read and transitioned inside periodic. Triggers bind conditions to commands, declaratively, no manual polling. And a real project keeps Robot thin, with RobotContainer, Constants, Subsystems, and Commands holding everything else. That's command-based programming, start to finish. Nice work, see you in Chapter 26.",
    },
]
