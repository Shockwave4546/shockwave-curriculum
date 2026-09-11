BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25 &middot; Command-Based Programming</div>
      <h1>What Is Command-Based Programming?</h1>
      <p class="scr-sub">WPILib&rsquo;s official architecture for structuring a robot&rsquo;s code.</p>
    </div>''',
        "speak": "Every idea we've covered since Chapter 17, inheritance, interfaces, the IO-Layer Pattern, static factories, builders, has been building toward this. Command-based programming is WPILib's own official architecture for structuring an entire robot's code. It's not the only way to write a robot program, but it's the one WPILib gives you deep library support for, and the one most competitive FRC codebases are built around.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Declarative, Not Imperative</div>
    <pre class="code"><code><span class="c">// Declarative (command-based): say what should happen, once</span>
<span class="k">new</span> Trigger(condition::get).onTrue(Commands.runOnce(() -&gt; piston.set(DoubleSolenoid.Value.kForward)));</code></pre>''',
        "speak": "Command-based is a declarative paradigm. You describe what should happen under what condition, once, and the library checks that condition every single loop on your behalf. Here's the declarative way to say extend the piston when a condition becomes true: one line, a trigger, and what to do when it fires.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">&hellip;vs. Imperative</div>
    <pre class="code"><code><span class="c">// Imperative (without command-based): manually track state every single loop</span>
<span class="k">if</span> (condition.get())
{
    <span class="k">if</span> (!pressed)
    {
        piston.set(DoubleSolenoid.Value.kForward);
        pressed = <span class="k">true</span>;
    }
}
<span class="k">else</span>
{
    pressed = <span class="k">false</span>;
}</code></pre>''',
        "speak": "The imperative version means manually tracking a pressed flag yourself, in every single place a similar check comes up. Multiply that by dozens of buttons and sensors on a real robot, and the difference in maintainability is enormous.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Core Abstractions</h2><ul>
      <li><span class="num">1</span><span><strong>Subsystem</strong> &mdash; an independently controlled piece of hardware: a drivetrain, an intake, a climber.</span></li>
    </ul></div>''',
        "speak": "Command-based organizes the whole robot around exactly two ideas. A Subsystem represents an independently controlled piece of hardware, a drivetrain, an intake, a climber. Chapter 20's IO-Layer Pattern already showed how a subsystem hides its hardware details behind a clean interface, and command-based builds directly on that.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Core Abstractions</h2><ul>
      <li><span class="num">1</span><span><strong>Subsystem</strong> &mdash; an independently controlled piece of hardware: a drivetrain, an intake, a climber.</span></li>
      <li><span class="num">2</span><span><strong>Command</strong> &mdash; an action the robot can take, until it's interrupted or its own end condition is met.</span></li>
    </ul></div>''',
        "speak": "A Command represents an action the robot can take, something that runs when scheduled, until it's interrupted or its own end condition is met.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">Command A</div>
      <div class="darrow">&times;</div>
      <div class="dbox err">Command B</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Two commands can never fight over the same subsystem at once.</p>''',
        "speak": "Commands declare which subsystems they need, their requirements, and that's what makes resource management automatic. The scheduler guarantees only one command can control a given subsystem at a time, so two different pieces of code can never fight over the same motor.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox active">CommandScheduler</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;margin-top:16px;">Runs once every 20 milliseconds &mdash; checks triggers, runs active commands, ends the ones that finished.</p>''',
        "speak": "The CommandScheduler is the engine underneath all of this, a singleton that runs once every 20 milliseconds, checking triggers, running active commands, and ending the ones that finished. We'll go deep on exactly how it runs in the next lesson.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">Intake</div><div class="darrow">&rarr;</div>
      <div class="dbox">Aim</div><div class="darrow">&rarr;</div>
      <div class="dbox active">Fire</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">A composite of small commands is itself just another command.</p>''',
        "speak": "And commands are recursively composable. A complex action, like intake a game piece, then aim the shooter, then fire, can be built out of several small commands combined together, and that composite is itself just another command, usable anywhere a command is expected.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Writing large amounts of imperative logic directly in Robot.java &mdash; this fights the entire declarative philosophy.</li>
      <li><span class="check">!</span>Forgetting a command's requirements &mdash; touching a subsystem without declaring it bypasses resource management.</li>
      <li><span class="check">!</span>Assuming command-based is the only valid way to write robot code &mdash; it isn't, but it's what WPILib is built to support.</li>
    </ul></div>''',
        "speak": "A few common pitfalls. Don't write large amounts of imperative logic directly in Robot dot java, that fights the entire declarative philosophy. Don't forget a command's requirements, a command that touches a subsystem without declaring it bypasses the whole resource-management system. And don't assume command-based is the only valid way to write robot code, it isn't, but it's what WPILib itself is built to support, so it's what we're focusing on here.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Command-based is WPILib's own declarative architecture pattern.</li>
      <li><span class="check">&#10003;</span>Two core abstractions: Subsystems (hardware) and Commands (actions).</li>
      <li><span class="check">&#10003;</span>Requirements let the scheduler guarantee exclusive subsystem control.</li>
      <li><span class="check">&#10003;</span>Commands are recursively composable into bigger commands.</li>
    </ul></div>''',
        "speak": "So that's the foundation. Command-based is WPILib's own declarative architecture pattern, describe what should happen, once, and let the scheduler handle it every loop. Two core abstractions, Subsystems for hardware and Commands for actions, tied together by the CommandScheduler. Requirements let the scheduler guarantee exclusive control over each subsystem. And commands are recursively composable into bigger ones. Next time, we go deep on exactly how the scheduler runs, step by step. Nice work, see you in lesson 25.2.",
    },
]
