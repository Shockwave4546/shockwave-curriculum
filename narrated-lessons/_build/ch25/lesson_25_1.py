BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25 &middot; Command-Based Programming</div>
      <h1>What Is Command-Based Programming?</h1>
      <p class="scr-sub">WPILib&rsquo;s own declarative architecture for structuring a robot&rsquo;s code &mdash; Commands v3.</p>
    </div>''',
        "speak": "Every idea we've covered since Chapter 17, inheritance, interfaces, the IO-Layer Pattern, static factories, builders, leads here. Command-based programming is WPILib's own official architecture for structuring an entire robot's code. It's not the only way to write a robot program, but it's the one WPILib gives deep library support for, and the one most competitive FRC codebases are built around. This chapter teaches Commands v3, the version built for WPILib 2027. Its older sibling, Commands v2, is what most existing team code, including our own older code, still uses. You'll write v3, but you'll read plenty of v2, so the last lesson of this chapter ends with a guide to recognizing it.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Declarative, Not Imperative</div>
    <pre class="code"><code><span class="c">// Declarative (command-based): say what should happen, once</span>
<span class="k">new</span> Trigger(condition::get).onTrue(pneumatics.extendCommand());</code></pre>''',
        "speak": "Command-based is a declarative paradigm. You describe what should happen under what condition, once, and the library checks that condition every single loop on your behalf. Here's the declarative way to say extend the piston when a condition becomes true: one line, a trigger, and what to do when it fires.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">&hellip;vs. Imperative</div>
    <pre class="code"><code><span class="c">// Imperative (without command-based): manually track state every single loop</span>
<span class="k">if</span> (condition.get())
{
    <span class="k">if</span> (!pressed)
    {
        piston.set(FORWARD);
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
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Core Abstractions</h2><ul>
      <li><span class="num">1</span><span><strong>Mechanism</strong> &mdash; an independently-controlled piece of hardware: a drivetrain, an intake, a climber. It's an interface &mdash; your class implements it.</span></li>
    </ul></div>''',
        "speak": "Command-based organizes the whole robot around three ideas. A Mechanism represents an independently-controlled piece of hardware, a drivetrain, an intake, a climber. It's an interface in v3, and your class implements it. Chapter 20's IO-Layer Pattern already showed how a mechanism can hide its hardware details behind a clean interface, and command-based builds directly on that.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Core Abstractions</h2><ul>
      <li><span class="num">1</span><span><strong>Mechanism</strong> &mdash; an independently-controlled piece of hardware: a drivetrain, an intake, a climber. It's an interface &mdash; your class implements it.</span></li>
      <li><span class="num">2</span><span><strong>Command</strong> &mdash; an action the robot can take. In v3, one block of ordinary Java that pauses once per loop.</span></li>
      <li><span class="num">3</span><span><strong>Scheduler</strong> &mdash; the engine that runs every command, once per loop.</span></li>
    </ul></div>''',
        "speak": "A Command represents an action the robot can take. In v3, a command's whole behavior is one ordinary block of Java, it can use normal loops and if statements, that pauses once per loop so the rest of the robot keeps running. And the Scheduler is the engine that runs every command, once per loop. We go deep on both of those in the next two lessons.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Requirements</div>
    <pre class="code"><code><span class="k">public class</span> Pneumatics <span class="k">implements</span> Mechanism
{
    <span class="k">private final</span> DoubleSolenoid piston; <span class="c">// created in the constructor (left out here)</span>

    <span class="k">public</span> Command extendCommand()
    {
        <span class="k">return</span> run(coroutine -&gt; piston.set(FORWARD)).named(<span class="s">"Extend Piston"</span>);
    }
}</code></pre>''',
        "speak": "Here's that extend command, written inside the mechanism that actually owns the piston. run is a default method the Mechanism interface provides, and a command built with it automatically requires this mechanism, it claims the pneumatics while it runs. Requirements are what make resource management automatic: only one command can control a given mechanism at a time, so two different pieces of code can never fight over the same motor's output. When two commands do collide, the scheduler compares their priorities to decide which one wins, that's Lesson 25.3.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox active">Scheduler.getDefault()</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;margin-top:16px;">Runs once every 20 milliseconds &mdash; checks triggers, runs active commands.</p>''',
        "speak": "The default Scheduler is the engine underneath all of this. Once per loop, every 20 milliseconds, your robot calls its run method, and it checks all registered triggers for commands that should start, then runs every active command until that command pauses or finishes. Lesson 25.3 covers the scheduler's actual run sequence in real depth.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">Intake</div><div class="darrow">&rarr;</div>
      <div class="dbox">Aim</div><div class="darrow">&rarr;</div>
      <div class="dbox active">Fire</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">A composite of small commands is itself just another command.</p>''',
        "speak": "And commands are recursively composable. A complex action, intake a game piece, then aim the shooter, then fire, can be built out of several small commands combined together, and that composite is itself just another command, usable anywhere a command is expected. Lesson 25.2 covers this in real depth.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Writing large amounts of imperative logic directly in Robot dot java &mdash; this fights the entire declarative philosophy.</li>
      <li><span class="check">!</span>Touching a mechanism's hardware from a command that doesn't require it &mdash; that bypasses resource management entirely.</li>
      <li><span class="check">!</span>Assuming command-based is the only valid way to write robot code &mdash; it isn't, but it's what WPILib is built to support.</li>
    </ul></div>''',
        "speak": "A few common pitfalls. Don't write large amounts of imperative logic directly in Robot dot java, that fights the entire declarative philosophy. Don't touch a mechanism's hardware from a command that doesn't require it, that bypasses the whole resource-management system. And don't assume command-based is the only valid way to write robot code, it isn't, but it's what WPILib itself is built to support, so it's what we're focusing on here.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Command-based is WPILib's own declarative architecture pattern &mdash; Commands v3 for WPILib 2027.</li>
      <li><span class="check">&#10003;</span>Three core abstractions: Mechanisms (hardware interfaces), Commands (named actions), and the Scheduler.</li>
      <li><span class="check">&#10003;</span>Requirements let the scheduler guarantee exclusive control; priorities settle conflicts.</li>
      <li><span class="check">&#10003;</span>Commands are recursively composable into bigger commands.</li>
    </ul></div>''',
        "speak": "So that's the foundation. Command-based is WPILib's own declarative architecture pattern, describe what should happen, once, and let the scheduler handle it every loop. Three core abstractions, Mechanisms for hardware, Commands for actions, and the Scheduler that ties them together. Requirements let the scheduler guarantee exclusive control over each mechanism, and priorities settle any conflict. And commands are recursively composable into bigger ones. Next time, we go deep on exactly how a command's body is written. Nice work, see you in Lesson 25.2.",
    },
]
