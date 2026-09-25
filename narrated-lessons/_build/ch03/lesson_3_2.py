BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 3 &middot; APIs, Libraries &amp; Documentation</div>
      <h1>Documentation with Comments and Preconditions</h1>
      <p class="scr-sub">Writing down what a method expects &mdash; because Java itself won't check it for you.</p>
    </div>''',
        "speak": "Last lesson we used someone else's library without ever reading its source code. That only works because good libraries document themselves well. Today we look at how, and start doing it in our own code too.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// single-line comment</span></code></pre>''',
        "speak": "Java has three comment styles, and the compiler ignores every single one of them completely, they exist purely for whoever reads the code next, including future you. Two slashes starts a single-line comment.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// single-line comment</span>
<span class="c">/* multi-line
   comment */</span></code></pre>''',
        "speak": "Slash-star, star-slash wraps a comment that can stretch across multiple lines.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// single-line comment</span>
<span class="c">/* multi-line
   comment */</span>
<span class="c">/** a documentation comment &mdash; describes a class or method for other programmers */</span></code></pre>''',
        "speak": "And slash-star-star, still closed with star-slash, is a documentation comment, specifically meant to describe a class or method for other programmers, which is exactly what we're building toward next.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Java 25 Note</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Java 23 added /// Markdown documentation comments. This course uses /** */, which works on every version.</p>''',
        "speak": "One version note. Java 23 added a fourth style, triple-slash Markdown documentation comments, where every line of the comment starts with three slashes. This course sticks with slash-star-star, which works on every Java version, on Java 17, a triple-slash line is just an ordinary two-slash comment.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Preconditions &amp; Postconditions</h2><ul>
      <li><span class="num">1</span><span><strong>Precondition</strong> &mdash; what has to be true before a method is called for it to work correctly.</span></li>
    </ul></div>''',
        "speak": "Two new terms. A precondition is what has to be true before you call a method, in order for it to actually work correctly.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Preconditions &amp; Postconditions</h2><ul>
      <li><span class="num">1</span><span><strong>Precondition</strong> &mdash; what has to be true before a method is called for it to work correctly.</span></li>
      <li><span class="num">2</span><span><strong>Postcondition</strong> &mdash; what's guaranteed true after it runs.</span></li>
    </ul></div>''',
        "speak": "And a postcondition is what's guaranteed to be true after the method finishes running.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="c">/**
 * Spins the shooter up toward a target speed.
 * Precondition: targetRPM is between 0 and the motor's max RPM.
 * Postcondition: the motor ramps toward targetRPM.
 *
 * @param targetRPM the speed to spin up to
 */</span>
<span class="k">public</span> <span class="k">void</span> spinUpTo(<span class="k">double</span> targetRPM) { ... }</code></pre>''',
        "speak": "Here's what that looks like in practice, a documentation comment above spin up to. The method takes a parameter, which lesson 4.1 covers properly, for now, just look at the comment. It starts with a plain description, what the method does, the precondition, target R P M has to sit between 0 and the motor's max R P M, and the postcondition, the motor ramps toward that target. Then comes the tag, at param, describing the parameter, target R P M. Keep the tags last, everything written after a tag counts as part of that tag's description.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Documented, Not Enforced</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Nothing stops you from calling spinUpTo with negative 500 &mdash; Java doesn't check preconditions automatically.</p>''',
        "speak": "Here's the part that catches people, Java doesn't enforce any of this automatically. Nothing physically stops you from calling spin up to with negative 500. A precondition is a documented expectation, not a guarantee the method itself checks.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">A Real Example</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Math.sqrt(-4) doesn't crash &mdash; its documentation says a negative input gives NaN, &ldquo;not a number.&rdquo;</p>''',
        "speak": "A real library shows the same effect. Math dot square root of negative 4 doesn't crash, its documentation says a negative input gives nan, short for not a number. If your code needed a real distance, nan is a silent wrong answer, not a loud error.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">/**
 * Converts a battery voltage into an approximate charge percentage.
 *
 * @param volts the measured battery voltage
 * @return the charge, from 0 to 100
 * @throws IllegalArgumentException if volts is negative
 */</span>
<span class="k">public</span> <span class="k">static</span> <span class="k">double</span> batteryPercent(<span class="k">double</span> volts) { ... }</code></pre>''',
        "speak": "Two more tags show up constantly in library documentation. At return describes the value the method hands back, return values are lesson 4.2. And at throws names an error, called an exception, that the method can throw, and when it happens, exceptions get their own chapter, chapter 12.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Your IDE Reads These Too</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Hover over a call and the IDE shows the description and tags. The javadoc tool turns the same comments into web pages.</p>''',
        "speak": "Your I D E reads these comments too. Hover over a call to battery percent, and it shows you the description and the tags. And the java doc tool turns the very same comments into web pages, which is exactly how a library's API pages are made.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Reading an API Page: Timer</h2><ul>
      <li><span class="num">1</span><span><strong>Package and class</strong> &mdash; org.wpilib.system, class Timer. The package tells you what to import.</span></li>
    </ul></div>''',
        "speak": "So let's read one. W P I Lib's API pages are generated from its own documentation comments, and the 2027 pages live at github dot W P I Lib dot org, slash all W P I Lib, slash docs, slash beta, slash java. Search there for a class by name. The page for W P I Lib's Timer class starts with its package and class, org dot W P I Lib dot system, class Timer. That package is exactly what you'll import, in lesson 3.3. Right under it is a one-line class description, a timer class.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Reading an API Page: Timer</h2><ul>
      <li><span class="num">1</span><span><strong>Package and class</strong> &mdash; org.wpilib.system, class Timer. The package tells you what to import.</span></li>
      <li><span class="num">2</span><span><strong>Constructor Summary</strong> &mdash; Timer(): how to build one with new (no arguments).</span></li>
    </ul></div>''',
        "speak": "Next, the constructor summary. Timer, with empty parentheses, tells you how to build one with new, and that it needs no arguments.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Reading an API Page: Timer</h2><ul>
      <li><span class="num">1</span><span><strong>Package and class</strong> &mdash; org.wpilib.system, class Timer. The package tells you what to import.</span></li>
      <li><span class="num">2</span><span><strong>Constructor Summary</strong> &mdash; Timer(): how to build one with new (no arguments).</span></li>
      <li><span class="num">3</span><span><strong>Method Summary</strong> &mdash; return type, name and parameters, one-line description: double get(), void start(), boolean hasElapsed(double seconds).</span></li>
    </ul></div>''',
        "speak": "Then the method summary, one row per method, its return type, its name and parameters, and a one-line description. double get, get the current time from the timer. void start, start the timer running. boolean has elapsed, taking a double called seconds, check if the period specified has passed.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Reading an API Page: Timer</h2><ul>
      <li><span class="num">1</span><span><strong>Package and class</strong> &mdash; org.wpilib.system, class Timer. The package tells you what to import.</span></li>
      <li><span class="num">2</span><span><strong>Constructor Summary</strong> &mdash; Timer(): how to build one with new (no arguments).</span></li>
      <li><span class="num">3</span><span><strong>Method Summary</strong> &mdash; return type, name and parameters, one-line description: double get(), void start(), boolean hasElapsed(double seconds).</span></li>
      <li><span class="num">4</span><span><strong>Method Details</strong> &mdash; each method's full comment, including its @param and @return text.</span></li>
    </ul></div>''',
        "speak": "And last, the method details, each method's full comment, including its at param and at return text. That one row, double get, tells you everything you need to call it: no arguments, and it hands back a double, the timer's elapsed time in seconds.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Why Bother Documenting This</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Other people, and future you, will call your methods without ever reading their insides.</p>''',
        "speak": "Once you write a method, other people, your whole team, and future you, will call it without reading its implementation. Documenting preconditions and postconditions is how they know what's safe to pass in and what to expect back, without documentation, the only way to find out is reading the whole method's source, or just guessing.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assuming a precondition is enforced &mdash; a bad value can still silently produce a wrong result like NaN.</li>
      <li><span class="check">!</span>Skipping documentation on methods other people will call &mdash; a two-line comment is cheaper than a teammate guessing wrong.</li>
      <li><span class="check">!</span>Putting description text after the tags &mdash; anything after @param becomes part of that parameter's description.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Assuming a precondition is enforced, documenting it doesn't make Java check it, a bad value passed in can still silently produce a wrong result like nan instead of an error. And skipping documentation on methods other people will call, the cost of a two-line comment is far smaller than the cost of a teammate guessing wrong about what a method expects. And putting description text after the tags, anything written after at param becomes part of that parameter's description, so write the description first, then the tags.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>//, /* */, and /** */ are the three comment styles; the compiler ignores all of them.</li>
      <li><span class="check">&#10003;</span>A precondition is what must be true before calling a method; a postcondition is guaranteed true after.</li>
      <li><span class="check">&#10003;</span>Preconditions are documented, not automatically enforced &mdash; violating one can silently produce a wrong result.</li>
      <li><span class="check">&#10003;</span>A /** */ comment: description first, then @param, @return, @throws.</li>
      <li><span class="check">&#10003;</span>An API page lists a class's package, constructors, and methods &mdash; generated from comments like these.</li>
    </ul></div>''',
        "speak": "So: two slashes, slash-star star-slash, and slash-star-star star-slash are the three comment styles, and the compiler ignores every one of them. A precondition is what must be true before you call a method, a postcondition is what's guaranteed true after it returns. Preconditions are documented expectations, not automatic enforcement, violating one can silently hand you back a wrong result instead of an error. A documentation comment starts with its description, then its tags, at param, at return, and at throws. And an API page lists a class's package, constructors, and methods, all generated from comments just like these. Next up, lesson 3.3, packages and imports, how Java organizes all these classes so you can find and use them.",
    },
]
