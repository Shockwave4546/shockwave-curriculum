BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.2 &middot; Command-Based Programming</div>
      <h1>Commands &amp; Command Compositions</h1>
      <p class="scr-sub">The four lifecycle methods, built-in factories, and combining commands into bigger ones.</p>
    </div>''',
        "speak": "Last time we met the two core abstractions: Subsystems and Commands. Now let's look at exactly what makes a Command tick, and how to combine several of them into one bigger action.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Four Lifecycle Methods</h2><ul>
      <li><span class="num">1</span><span><strong>initialize()</strong> &mdash; called exactly once, when the command starts.</span></li>
    </ul></div>''',
        "speak": "A Command's behavior comes from four overridable lifecycle methods, and all of them default to doing nothing, so you only override what you actually need. Initialize runs exactly once, when the command starts, use it to set up starting state.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Four Lifecycle Methods</h2><ul>
      <li><span class="num">1</span><span><strong>initialize()</strong> &mdash; called exactly once, when the command starts.</span></li>
      <li><span class="num">2</span><span><strong>execute()</strong> &mdash; called repeatedly, once per scheduler loop, for as long as it's scheduled.</span></li>
    </ul></div>''',
        "speak": "Execute runs repeatedly, once every scheduler loop, for as long as the command is scheduled, that's where continuous behavior lives, like following joystick input.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Four Lifecycle Methods</h2><ul>
      <li><span class="num">1</span><span><strong>initialize()</strong> &mdash; called exactly once, when the command starts.</span></li>
      <li><span class="num">2</span><span><strong>execute()</strong> &mdash; called repeatedly, once per scheduler loop, for as long as it's scheduled.</span></li>
      <li><span class="num">3</span><span><strong>isFinished()</strong> &mdash; checked every loop; returning true ends the command.</span></li>
    </ul></div>''',
        "speak": "IsFinished gets checked every loop right after execute, and the moment it returns true, the command ends, by default it's false, meaning a command runs forever unless something else interrupts it.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Four Lifecycle Methods</h2><ul>
      <li><span class="num">1</span><span><strong>initialize()</strong> &mdash; called exactly once, when the command starts.</span></li>
      <li><span class="num">2</span><span><strong>execute()</strong> &mdash; called repeatedly, once per scheduler loop, for as long as it's scheduled.</span></li>
      <li><span class="num">3</span><span><strong>isFinished()</strong> &mdash; checked every loop; returning true ends the command.</span></li>
      <li><span class="num">4</span><span><strong>end(interrupted)</strong> &mdash; called once when it stops, naturally or interrupted.</span></li>
    </ul></div>''',
        "speak": "And end, which takes a boolean called interrupted, runs exactly once when the command stops, whether it finished naturally or got interrupted, that's your cleanup spot, stopping a motor, resetting a flag.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code" style="font-size:12.5px;"><code><span class="k">public class</span> <span class="t">GrabHatch</span> <span class="k">extends</span> <span class="t">Command</span>
{
    <span class="k">private final</span> <span class="t">HatchSubsystem</span> hatchSubsystem;

    <span class="k">public</span> GrabHatch(<span class="t">HatchSubsystem</span> subsystem)
    {
        hatchSubsystem = subsystem;
        addRequirements(hatchSubsystem); <span class="c">// declares the resource this command needs</span>
    }

    <span class="me">@Override</span>
    <span class="k">public void</span> initialize() { hatchSubsystem.grabHatch(); }

    <span class="me">@Override</span>
    <span class="k">public boolean</span> isFinished() { <span class="k">return true</span>; } <span class="c">// runs once, then immediately ends</span>
}</code></pre>''',
        "speak": "Notice the subsystem gets passed into the command's constructor. That's dependency injection, you'll see it again when we structure a whole project, and it's what lets a command reach a subsystem's methods without that subsystem being some global variable floating around. Every command declares which subsystems it needs through add requirements, that's the resource-management backbone, it's exactly what backs the scheduler's promise that no two commands ever fight over the same subsystem at once.",
    },
    {
        "screen": '''<h2 class="scr-h2" style="text-align:center;">You Rarely Need a Custom Class</h2>
    <pre class="code" style="font-size:11px;"><code><span class="t">Commands</span>.runOnce(() -&gt; hatchSolenoid.set(kForward), hatchSubsystem);       <span class="c">// runs a lambda once, then finishes</span>
<span class="t">Commands</span>.run(() -&gt; drive.arcadeDrive(joystick.getY(), joystick.getX()), drive); <span class="c">// repeats until interrupted — a natural default command</span>
<span class="t">Commands</span>.startEnd(
    () -&gt; shooter.setSpeed(<span class="n">0.5</span>),  <span class="c">// runs once at the start</span>
    () -&gt; shooter.setSpeed(<span class="n">0.0</span>),  <span class="c">// runs once when the command ends</span>
    shooter
);
<span class="t">Commands</span>.waitSeconds(<span class="n">5.0</span>);       <span class="c">// finishes 5 seconds after being scheduled</span>
<span class="t">Commands</span>.waitUntil(limitSwitch::get); <span class="c">// finishes once the given condition becomes true</span></code></pre>''',
        "speak": "Here's the good news: you'll rarely need to write a full custom command class. The library ships factory methods built on lambdas that cover almost every real case. Commands dot run once, for something that fires once and finishes. Commands dot run, for something that repeats until interrupted, a natural default command. Commands dot start end, for a pair of actions, one when it starts, one when it ends. And commands dot wait seconds, or wait until, for simple timing and condition-based waits. When you genuinely need custom behavior in more than one lifecycle method, functional command covers the general case with four lambdas, one per method.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">A</div><div class="darrow">&rarr;</div>
      <div class="dbox">B</div><div class="darrow">&rarr;</div>
      <div class="dbox active">C</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:14px;"><strong style="color:var(--accent);">Sequential</strong> &mdash; runs each in order, finishes when the last one finishes.</p>
    <pre class="code" style="font-size:12.5px;margin-top:10px;"><code>fooCommand.andThen(barCommand); <span class="c">// runs fooCommand, then barCommand</span></code></pre>''',
        "speak": "Now, command compositions. A composition combines several commands into one, and because a composition is itself a command, you can nest them arbitrarily deep. Three shapes matter most. Sequential runs each command in order, finishing when the last one finishes.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox active">A</div>
      <div class="dbox active">B</div>
      <div class="dbox active">C</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:14px;"><strong style="color:var(--accent);">Parallel</strong> &mdash; runs all at once, finishes once every one finishes.</p>
    <pre class="code" style="font-size:12.5px;margin-top:10px;"><code><span class="t">Commands</span>.parallel(twoSecCommand, oneSecCommand, threeSecCommand); <span class="c">// finishes after 3 seconds</span></code></pre>''',
        "speak": "Parallel runs several at once, finishing once all of them finish.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox err">A</div>
      <div class="dbox">B</div>
      <div class="dbox">C</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:14px;"><strong style="color:var(--accent);">Race</strong> &mdash; runs all at once, finishes (and interrupts the rest) as soon as any one finishes.</p>
    <pre class="code" style="font-size:12.5px;margin-top:10px;"><code><span class="t">Commands</span>.race(twoSecCommand, oneSecCommand, threeSecCommand); <span class="c">// finishes after 1 second</span></code></pre>
    <pre class="code" style="font-size:12.5px;margin-top:8px;"><code>command.until(limitSwitch::get); <span class="c">// ends early if the limit switch trips</span>
command.withTimeout(<span class="n">5</span>);          <span class="c">// ends after 5 seconds no matter what</span></code></pre>''',
        "speak": "And race runs several at once, finishing as soon as any one of them finishes, interrupting the rest. Two decorators are worth knowing too: until, which ends a command early if some condition trips, and with timeout, which ends it after a fixed time no matter what. One important detail: a composition inherits the union of every component's requirements. A sequence that uses the intake, then the indexer, then the shooter reserves all three subsystems for the composition's entire duration, not just while each one is actively in use.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Scheduling a command that's already inside a composition &mdash; throws and crashes the program.</li>
      <li><span class="check">!</span>Writing a full custom class for something a factory already covers.</li>
      <li><span class="check">!</span>Forgetting a sequential composition needs every step to actually finish.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Never try to schedule a command that's already inside a composition, that throws and crashes the program, since the same instance would be running from two places at once. Don't write a full custom command class for something a factory already covers. And remember, a sequential composition needs every step to actually finish, if one command in the middle never returns true from isFinished, everything after it in the sequence never runs.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Four lifecycle methods: initialize, execute, isFinished, end.</li>
      <li><span class="check">&#10003;</span>addRequirements backs the scheduler's conflict prevention.</li>
      <li><span class="check">&#10003;</span>Built-in factories cover almost every case without a custom class.</li>
      <li><span class="check">&#10003;</span>Sequential, parallel, and race compositions nest recursively.</li>
    </ul></div>''',
        "speak": "So that's commands and compositions. Four lifecycle methods: initialize, execute, isFinished, and end. Add requirements backs the scheduler's promise that commands never fight over a subsystem. Built-in factories cover almost every case without writing a custom class. And sequential, parallel, and race compositions combine commands into bigger ones, nesting as deep as you need. Next time, we go inside the scheduler itself, step by step. Nice work, see you in lesson 25.3.",
    },
]
