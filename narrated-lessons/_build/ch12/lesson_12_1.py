BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 12 &middot; Exceptions</div>
      <h1>Exceptions &amp; try/catch</h1>
      <p class="scr-sub">What happens when something goes wrong while your program is running.</p>
    </div>''',
        "speak": "Chapter 12 is about exceptions, what Java does when something goes wrong while your program is actually running, a missing file, an out-of-range array index, dividing by zero, and how try and catch let you deal with it instead of just crashing.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What an Exception Is</h2><ul>
      <li><span class="num">1</span><span>An &ldquo;exceptional event&rdquo; &mdash; something that disrupts normal program flow</span></li>
    </ul></div>''',
        "speak": "An exception is literally an exceptional event, something that disrupts your program's normal flow while it's running.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What an Exception Is</h2><ul>
      <li><span class="num">1</span><span>An &ldquo;exceptional event&rdquo; &mdash; something that disrupts normal program flow</span></li>
      <li><span class="num">2</span><span>The method creates an <strong>exception object</strong> and hands it to the runtime &mdash; this is <strong>throwing</strong></span></li>
    </ul></div>''',
        "speak": "When one occurs, the method that hit the problem creates an exception object describing exactly what went wrong, and hands it off to the Java runtime. That handoff is called throwing the exception.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">methodC</div><div class="darrow">&rarr;</div>
      <div class="dbox">methodB</div><div class="darrow">&rarr;</div>
      <div class="dbox err">methodA (throws)</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">The runtime searches back up the call stack for a matching handler.</p>''',
        "speak": "From there, the runtime searches back up the call stack, the chain of methods that led to this point, looking for an exception handler, a block of code able to deal with that specific type of problem. The first matching handler it finds is said to catch the exception.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox err">Uncaught!</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">On a robot, this is exactly what turns the Driver Station&rsquo;s Robot Code indicator red.</p>''',
        "speak": "And if nothing anywhere on the call stack can handle it, the runtime just terminates the program. On a real robot, an uncaught exception inside periodic is exactly what turns the Driver Station's Robot Code indicator red mid-match.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">try</span>
{
    config = loadFromFile("tuning.json");
}
<span class="k">catch</span> (IOException e)
{
    <span class="c">// Recover: fall back to defaults</span>
    config = Config.defaults();
    reportWarning("Using default tuning");
}</code></pre>''',
        "speak": "The actual syntax: a try block wraps code that might throw. Right after it, a catch block names a specific exception type, here IO Exception, and handles it if one actually occurs. If loadFromFile throws, execution jumps straight into that matching catch block, skipping the rest of the try. And if nothing goes wrong at all, the catch block never runs, period.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">try</span>
{
    camera = <span class="k">new</span> UsbCamera("Camera 1", 0);
}
<span class="k">catch</span> (VideoException e)
{
    reportWarning("Camera unavailable — skipping vision this match");
}
<span class="k">catch</span> (NullPointerException e)
{
    reportWarning("Camera name was null");
}</code></pre>''',
        "speak": "A single try can have multiple catch blocks stacked up, checked in order, so you can handle different exception types differently. Here, a camera that's simply unavailable gets one message, a null camera name gets a completely different one. VideoException itself is unchecked, it extends RuntimeException, so catching it here is optional, not compiler-required, but doing so lets the robot keep running with vision disabled instead of crashing outright.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">catch</span> (VideoException | NullPointerException e)
{
    reportWarning("Camera unavailable — skipping vision this match");
}</code></pre>''',
        "speak": "When two exception types with no inheritance relationship should be handled identically, multi-catch combines them into one block with a pipe. And when catch blocks DO relate, order matters: a catch for a more general type has to come after every more specific catch for one of its subclasses, or the compiler rejects it, that more specific catch would be unreachable.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 12 &middot; Exceptions</div>
      <h1>finally</h1>
      <p class="scr-sub">Runs no matter what &mdash; exception or not.</p>
    </div>''',
        "speak": "There's a third, optional block: finally. It goes after all the catch blocks, and it always runs, whether an exception was thrown or not, and even if a catch block itself returns early. It's the right home for cleanup that absolutely has to happen no matter what, closing a file, releasing a resource.",
    },
    {
        "screen": '''<pre class="code"><code>Scanner scan = <span class="k">null</span>;
<span class="k">try</span>
{
    scan = <span class="k">new</span> Scanner(<span class="k">new</span> File("auto_config.csv"));
    <span class="c">// ... read the file ...</span>
}
<span class="k">catch</span> (FileNotFoundException e)
{
    reportWarning("Missing auto_config.csv — using default route");
}
<span class="k">finally</span>
{
    <span class="k">if</span> (scan != <span class="k">null</span>)
    {
        scan.close(); <span class="c">// runs whether the try succeeded, failed, or even returned early</span>
    }
}</code></pre>''',
        "speak": "Here, scan starts out null, in case the file genuinely can't be found. But the finally block runs regardless, closing scan if it ever actually got created, whether the read succeeded, failed, or the method returned early somewhere inside that try.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">try</span> (Scanner scan = <span class="k">new</span> Scanner(<span class="k">new</span> File("auto_config.csv")))
{
    <span class="c">// ... read the file ...</span>
}
<span class="k">catch</span> (FileNotFoundException e)
{
    reportWarning("Missing auto_config.csv — using default route");
}</code></pre>''',
        "speak": "That manual finally block is exactly the case try-with-resources exists to replace. Any resource that implements AutoCloseable, like Scanner, can be declared right inside parentheses after try, and Java calls its close method automatically, every time, with no finally block at all. Prefer this form whenever the resource type supports it.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 12 &middot; Exceptions</div>
      <h1>Checked vs. Unchecked</h1>
      <p class="scr-sub">The difference the compiler actually enforces.</p>
    </div>''',
        "speak": "Java splits exceptions into two families, and the split matters for what the compiler demands of you.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Checked vs. Unchecked</h2><ul>
      <li><span class="num">1</span><span><strong>Checked</strong> (like IOException) &mdash; must be caught, or declared with <code>throws</code></span></li>
    </ul></div>''',
        "speak": "Checked exceptions, like IO Exception, the compiler forces you to deal with, either catch them, or declare them with a throws clause. These represent problems a caller could reasonably be expected to recover from.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Checked vs. Unchecked</h2><ul>
      <li><span class="num">1</span><span><strong>Checked</strong> (like IOException) &mdash; must be caught, or declared with <code>throws</code></span></li>
      <li><span class="num">2</span><span><strong>Unchecked</strong> (RuntimeException, Error, and subclasses) &mdash; handling is optional</span></li>
    </ul></div>''',
        "speak": "Unchecked exceptions, RuntimeException, Error, and everything under either of them, things like NullPointerException and ArrayIndexOutOfBoundsException, the compiler doesn't require you to handle at all, though nothing stops you. RuntimeException subclasses almost always mean a genuine bug, a null you forgot to check, an index you miscalculated, not something the caller can meaningfully recover from at runtime; Error and its subclasses are serious JVM-level failures ordinary code doesn't catch or throw.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">The Designers&rsquo; Own Rule of Thumb</h2><ul>
      <li><span class="check">&#10003;</span>If a client can reasonably recover from a problem, make it checked.</li>
      <li><span class="check">&#10003;</span>If a client can't do anything useful about it, make it unchecked.</li>
    </ul></div>''',
        "speak": "The language's own designers put it simply: if a client can reasonably be expected to recover from a problem, make it checked. If a client can't do anything useful about it, make it unchecked. CSA covers unchecked-exception concepts, NullPointerException and ArrayIndexOutOfBoundsException, as topics in their own right, without teaching the try-catch mechanism itself, the AP exam doesn't test it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public void</span> <span class="me">writeList</span>() <span class="k">throws</span> IOException
{
    <span class="k">try</span> (PrintWriter out = <span class="k">new</span> PrintWriter(<span class="k">new</span> FileWriter("OutFile.txt")))
    {
        <span class="c">// ...</span>
    }
}</code></pre>''',
        "speak": "If a method doesn't want to handle a checked exception itself, it can push that decision up to whoever calls it, with a throws clause. It goes right after the parameter list, before the method body's opening brace. Unchecked exceptions never need to appear in a throws clause, though nothing stops you from listing one anyway. PrintWriter and FileWriter write text to a file, the counterpart to Scanner, which lesson 9.8 uses to read one, and try-with-resources again means no leaked file handle if something throws partway through.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public void</span> <span class="me">setTargetAngle</span>(<span class="t">double</span> degrees)
{
    <span class="k">if</span> (degrees &lt; 0 || degrees &gt; 180)
    {
        <span class="k">throw new</span> IllegalArgumentException("Angle out of range: " + degrees);
    }
    <span class="k">this</span>.targetAngle = degrees;
}</code></pre>''',
        "speak": "And any code at all, yours, a library's, or the runtime itself, can trigger an exception with the throw statement, given any object that's a Throwable or one of its subclasses. Here, an out-of-range angle throws an IllegalArgumentException immediately, before it ever gets stored.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox active">Throwable</div>
    </div>
    <div class="scr-diagram" style="margin-top:14px;">
      <div class="dbox">Error</div>
      <div class="dbox">Exception</div>
    </div>''',
        "speak": "Every exception type in Java descends from Throwable, each one is a subclass of it, built on top of it, inheriting its behavior, chapter 17 covers what that means in full. It has two direct children: Error, serious JVM-level failures that ordinary code never catches or throws, and Exception, everything an ordinary program actually throws and catches. RuntimeException is the branch of Exception specifically reserved for the unchecked family.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">catch</span> (IllegalArgumentException e)
{
    reportWarning("Rejected: " + e.getMessage()); <span class="c">// "Angle out of range: 240.0"</span>
}</code></pre>''',
        "speak": "Every exception carries a message, and a caught one doesn't have to be handled blind. e dot getMessage returns the exact text passed to the exception's constructor, use it in a log message instead of guessing what failed.",
    },
    {
        "screen": '''<pre class="code"><code>java.lang.IllegalArgumentException: Angle out of range: 240.0
    at Arm.setTargetAngle(Arm.java:107)
    at Robot.teleopPeriodic(Robot.java:42)</code></pre>''',
        "speak": "An uncaught exception instead prints a stack trace, the exception type and message, followed by the chain of method calls, most recent first, that led to it, and that's exactly what shows up when robot code crashes. Read it top down: the first line is the problem, and the first at-line naming your own class, not a library's, is usually where to start looking. Writing your own exception types needs extends, which isn't taught until Chapter 17, lesson 17.2 covers it.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Catch-and-ignore &mdash; an empty catch block silently swallows a real problem; at minimum, log or report it.</li>
      <li><span class="check">!</span>Catching to "fix" a bug instead of fixing it &mdash; wrapping buggy code in try/catch hides the mistake instead of correcting it.</li>
      <li><span class="check">!</span>Forgetting finally runs even on an early return inside try/catch.</li>
    </ul></div>''',
        "speak": "A few pitfalls before we wrap up. Catch-and-ignore, an empty catch block that silently swallows a real problem, is one of the worst habits you can pick up, at minimum, log it or report it. Don't catch an exception just to fix a bug instead of actually fixing it, wrapping buggy code in try-catch to suppress a NullPointerException hides the real mistake instead of correcting it, save catching for genuinely recoverable situations, a missing file, an unreachable camera, not programming errors. And remember, finally runs even on an early return inside try or catch, so cleanup code that must always run belongs there, not duplicated at the end of every branch.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Throwing creates an exception object and hands it to the runtime, which searches the call stack for a handler.</li>
      <li><span class="check">&#10003;</span>try wraps risky code; catch handles specific types, general after specific, or combined with |; finally or try-with-resources handles cleanup.</li>
      <li><span class="check">&#10003;</span>Checked exceptions must be caught or declared with throws; unchecked ones (RuntimeException, Error) don't require either.</li>
      <li><span class="check">&#10003;</span>throw someObject triggers an exception yourself; e.getMessage() and stack traces show what broke &mdash; and never catch-and-ignore.</li>
    </ul></div>''',
        "speak": "So, to recap Chapter 12. Throwing an exception creates an object describing the problem and hands it to the runtime, which searches the call stack for a matching handler, an unhandled one crashes the program entirely. try wraps the risky code, one or more catch blocks handle specific exception types in order, or combined with a pipe, and an optional finally block always runs for cleanup, or try-with-resources handles it automatically. Checked exceptions, like IOException, must be caught or declared with throws; unchecked ones, RuntimeException, Error, and their subclasses, require neither, since they usually mean a real bug rather than a recoverable situation. throw, given any Throwable, triggers an exception yourself, and getMessage plus a stack trace tell you what actually broke. Above all, never catch and ignore, recover meaningfully, or at the very least, report the problem. Next up, Chapter 13: a quick-reference roundup of the most common Java gotchas.",
    },
]
