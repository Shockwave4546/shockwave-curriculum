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
 * @param targetRPM the speed to spin up to
 * Precondition: targetRPM is between 0 and the motor's max RPM.
 * Postcondition: the motor ramps toward targetRPM.
 */</span>
<span class="k">public</span> <span class="k">void</span> spinUpTo(<span class="k">double</span> targetRPM) { ... }</code></pre>''',
        "speak": "Here's what that looks like in practice, a documentation comment above spin up to. It names the parameter, target R P M, states the precondition, target R P M has to sit between 0 and the motor's max R P M, and the postcondition, the motor ramps toward that target.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Documented, Not Enforced</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Nothing stops you from calling spinUpTo with negative 500 &mdash; Java doesn't check preconditions automatically.</p>''',
        "speak": "Here's the part that catches people, Java doesn't enforce any of this automatically. Nothing physically stops you from calling spin up to with negative 500. A precondition is a documented expectation, not a guarantee the method itself checks.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">A Real Example</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Math dot square root of negative 4 doesn't crash &mdash; it quietly returns NaN, "not a number."</p>''',
        "speak": "Math dot square root of negative 4 is a real example of this. Nothing crashes. But negative input violates square root's precondition, so the result comes back as nan, short for not a number, a silent wrong answer instead of a loud error.",
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
    </ul></div>''',
        "speak": "Two pitfalls. Assuming a precondition is enforced, documenting it doesn't make Java check it, a bad value passed in can still silently produce a wrong result like nan instead of an error. And skipping documentation on methods other people will call, the cost of a two-line comment is far smaller than the cost of a teammate guessing wrong about what a method expects.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>//, /* */, and /** */ are the three comment styles; the compiler ignores all of them.</li>
      <li><span class="check">&#10003;</span>A precondition is what must be true before calling a method; a postcondition is guaranteed true after.</li>
      <li><span class="check">&#10003;</span>Preconditions are documented, not automatically enforced &mdash; violating one can silently produce a wrong result.</li>
    </ul></div>''',
        "speak": "So: two slashes, slash-star star-slash, and slash-star-star star-slash are the three comment styles, and the compiler ignores every one of them. A precondition is what must be true before you call a method, a postcondition is what's guaranteed true after it returns. And preconditions are documented expectations, not automatic enforcement, violating one can silently hand you back a wrong result instead of an error. Next up, lesson 3.3, packages and imports, how Java organizes all these classes so you can find and use them.",
    },
]
