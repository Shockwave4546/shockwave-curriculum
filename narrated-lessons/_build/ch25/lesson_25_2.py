BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.2 &middot; Command-Based Programming</div>
      <h1>Commands &amp; Command Compositions</h1>
      <p class="scr-sub">A v3 command is one block of ordinary Java &mdash; and small commands combine into bigger ones.</p>
    </div>''',
        "speak": "In Commands v3, a command's entire behavior is one block of code, a lambda that receives a Coroutine object. The body reads top to bottom like any method you've written: code before a loop runs once when the command starts, the loop runs once per scheduler loop, and code after the loop runs once when the goal is reached.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">One Body, Written Like a Normal Method</div>
    <pre class="code"><code><span class="k">public</span> Command raiseCommand()
{
    <span class="k">return</span> run(coroutine -&gt; {
        motor.setThrottle(0.5);       <span class="c">// once, when the command starts</span>
        <span class="k">while</span> (!topLimit.get())
        {
            coroutine.yield();        <span class="c">// pause here until the next loop</span>
        }
        motor.setThrottle(0.0);       <span class="c">// once, when the top limit switch trips</span>
    }).named(<span class="s">"Raise Elevator"</span>);
}</code></pre>''',
        "speak": "Here it is: raiseCommand starts the motor once, loops calling coroutine dot yield until the top limit switch trips, then stops the motor once. In v2 code you'd see this same shape spread across four separate override methods, initialize, execute, isFinished, end. v3 folds all four into this one body, and it needs a name: run doesn't return a finished Command until you call dot named on it.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Requirements Come From How You Build It</h2><ul>
      <li><span class="num">1</span><span><strong>mechanism.run(...)</strong> &mdash; requires that mechanism, automatically.</span></li>
      <li><span class="num">2</span><span><strong>Command.requiring(a, b)</strong> &mdash; requires several mechanisms at once.</span></li>
      <li><span class="num">3</span><span><strong>Command.noRequirements(...)</strong> &mdash; requires nothing, for commands that don't touch hardware.</span></li>
    </ul></div>''',
        "speak": "Requirements come from how you build the command, not from a separate declaration step. Calling run on a mechanism requires that mechanism automatically. Command dot requiring takes several mechanisms at once. And Command dot no requirements is for commands that don't touch hardware at all, like resetting a software value. There's no separate declare-my-requirements step to forget, which is exactly the mistake v2's addRequirements made easy.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Built-In Factories: Most Commands Are One Statement</div>
    <pre class="code"><code>hatch.run(coroutine -&gt; hatch.grab()).named(<span class="s">"Grab Hatch"</span>);     <span class="c">// runs once, then ends</span>
drive.runRepeatedly(() -&gt; drive.arcade(forward.getAsDouble(), turn.getAsDouble()))
    .named(<span class="s">"Arcade Drive"</span>);                                   <span class="c">// repeats until interrupted</span>
intake.idle();                                                <span class="c">// owns the intake, idles</span>
Command.waitFor(Seconds.of(5)).named(<span class="s">"Wait 5 s"</span>);             <span class="c">// ends after 5 seconds</span>
Command.waitUntil(limitSwitch::get).named(<span class="s">"Wait for Switch"</span>); <span class="c">// ends once this is true</span></code></pre>''',
        "speak": "Most commands you'll actually write are one statement. run for a one-shot action, runRepeatedly for something that repeats every loop until it's interrupted, a natural fit for a default command. Command dot waitFor and waitUntil handle plain waiting. And every one of these needs a Time value for its duration, never a bare number, that's brought in with a static import, the same way you learned in Lesson 3.3.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Cleaning Up When a Command Ends</div>
    <pre class="code"><code><span class="k">public</span> Command spinCommand()
{
    <span class="k">return</span> run(coroutine -&gt; {
        motor.setThrottle(0.8);
        coroutine.park();             <span class="c">// keep spinning until something stops this command</span>
    }).whenExited(() -&gt; motor.setThrottle(0.0)).named(<span class="s">"Spin Shooter"</span>);
}</code></pre>''',
        "speak": "A command that starts a motor usually has to stop it however the command ends, finished, canceled, or interrupted by another command. whenExited runs on every single exit, so it's the right home for that cleanup, never code placed after the loop, since a canceled command never reaches code after its loop at all.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Durations Are Time Values</div>
    <pre class="code"><code><span class="k">import static</span> org.wpilib.units.Units.Milliseconds;
<span class="k">import static</span> org.wpilib.units.Units.Seconds;

Time autoDelay = Seconds.of(2);        <span class="c">// 2 seconds</span>
Time nudge = Milliseconds.of(100);     <span class="c">// 0.1 seconds</span></code></pre>''',
        "speak": "Every v3 method that takes a duration takes a Time, not a plain double. You make one from a unit constant in WPILib's Units class. The payoff: a bare withTimeout of 5 simply can't compile, so nobody can ever wonder whether that 5 meant seconds or milliseconds.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Three Shapes of Composition</div>
    <pre class="code"><code>fooCommand.andThen(barCommand).withAutomaticName(); <span class="c">// runs fooCommand, then barCommand</span></code></pre>
    <pre class="code"><code>Command.parallel(twoSec, oneSec, threeSec).named(<span class="s">"All Three"</span>); <span class="c">// ends after 3 seconds</span></code></pre>
    <pre class="code"><code>Command.race(twoSec, oneSec, threeSec).named(<span class="s">"First Done"</span>); <span class="c">// ends after 1 second</span></code></pre>''',
        "speak": "A command composition combines several commands into one, and since a composition is itself a Command, they nest arbitrarily deep. Sequential runs each command in order. Parallel runs several at once and finishes once all of them finish. Race runs several at once and finishes as soon as any one of them finishes, canceling the rest. Compositions are built with builders too, so they also need a name, either explicit or automatic.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Decorators: until and withTimeout</div>
    <pre class="code"><code>raise.until(limitSwitch::get).named(<span class="s">"Raise to Switch"</span>); <span class="c">// ends early if the switch trips</span>
raise.withTimeout(Seconds.of(5));                       <span class="c">// ends after 5 s, no matter what</span></code></pre>''',
        "speak": "Two decorators add extra end conditions to any command. until ends the command early the moment a condition becomes true. withTimeout ends it after a fixed duration no matter what, and it already returns a finished, automatically-named Command, so it needs no dot named of its own.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The await Alternative</div>
    <pre class="code"><code>Command.noRequirements(coroutine -&gt; {
    coroutine.await(intake.intakeCommand());   <span class="c">// intake is claimed only during this step</span>
    coroutine.await(shooter.fireCommand());    <span class="c">// then the shooter, only during this step</span>
}).named(<span class="s">"Intake Then Fire"</span>);</code></pre>''',
        "speak": "A built-in composition holds every mechanism its members require for its entire duration, even the ones sitting idle between steps. v3's finer-grained alternative is a command with no requirements of its own that awaits other commands from inside its body, each one claims its mechanism only while it's actually running.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>A loop that never calls coroutine dot yield &mdash; the whole robot hangs, nothing else ever runs.</li>
      <li><span class="check">!</span>Writing yield without coroutine in front &mdash; yield is a restricted word in Java, a bare call is a compile error.</li>
      <li><span class="check">!</span>Forgetting that a sequential composition needs every step to actually finish.</li>
    </ul></div>''',
        "speak": "A few pitfalls that really matter here. A while loop that never calls coroutine dot yield never gives control back, so the whole robot hangs, not just this command. And yield is a restricted word in Java, so a bare yield call without coroutine in front of it is a compile error, it has to be written coroutine dot yield. Finally, if one command in a sequence never finishes, every command after it in that sequence never runs either.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A v3 command is one body, ending each loop with coroutine.yield().</li>
      <li><span class="check">&#10003;</span>Every command needs a name &mdash; enforced by a staged builder.</li>
      <li><span class="check">&#10003;</span>Requirements come from how you build it: run, requiring, or noRequirements.</li>
      <li><span class="check">&#10003;</span>Durations are Time values; compositions (sequence, parallel, race) are commands too.</li>
    </ul></div>''',
        "speak": "So: a v3 command is one body, code before the loop, a loop that ends with coroutine dot yield, code after. Every command needs a name, and requirements come straight from how you build it. Durations are always Time values, and compositions, sequence, parallel, race, are themselves ordinary commands you can nest as deep as you like. Next time, we open up the scheduler itself and trace exactly how it runs, step by step. See you in Lesson 25.3.",
    },
]
