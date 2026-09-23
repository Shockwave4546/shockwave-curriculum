BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 4 &middot; Using Objects &amp; Calling Methods</div>
      <h1>Methods, Signatures &amp; Parameters</h1>
      <p class="scr-sub">The vocabulary for talking precisely about a method call.</p>
    </div>''',
        "speak": "You've been calling methods since lesson 1.2 without ever needing to know how print line works internally. That's the whole benefit of a method, you use it by its name and what it does, not by reading its insides. Let's put precise words to all the pieces.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">What a Method Is</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">A named block of code that runs when you call it.</p>''',
        "speak": "A method is a named block of code that runs when you call it. Nothing more mysterious than that.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">void</span> rampTo(<span class="k">double</span> targetSpeed) { ... }</code></pre>''',
        "speak": "A method's signature is its name plus its parameter types, exactly what you need to know to call it correctly. Here, ramp to takes one double, called target speed. target speed is a parameter, a variable declared right in the method's own header, usable inside the method's body.",
    },
    {
        "screen": '''<pre class="code"><code>drivetrain.rampTo(<span class="n">0.8</span>);</code></pre>''',
        "speak": "Now here's a real call. drive train dot ramp to, 0 point 8. That 0 point 8 is the argument, the actual value being passed in. Parameter and argument describe the same slot from two different sides, the parameter is the variable inside the method, the argument is the value at the call site.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Call by Value</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Java copies the argument's value into the parameter &mdash; the original is never touched.</p>''',
        "speak": "Java copies the argument's value into the parameter, this is called call by value. If a method changes its own parameter internally, the original value the caller passed in is completely unaffected, only a copy ever went in.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Overloading</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Two methods can share a name if their parameter lists differ in number or type.</p>''',
        "speak": "Two methods can actually share the same name, as long as their parameter lists differ in number or type. This is called overloading.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">void</span> println()          <span class="c">// no parameters</span></code></pre>''',
        "speak": "print line is a real example of this in the wild. There's a version that takes no parameters at all.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">void</span> println()          <span class="c">// no parameters</span>
<span class="k">void</span> println(<span class="t">String</span> x)  <span class="c">// takes a String</span></code></pre>''',
        "speak": "One that takes a String.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">void</span> println()          <span class="c">// no parameters</span>
<span class="k">void</span> println(<span class="t">String</span> x)  <span class="c">// takes a String</span>
<span class="k">void</span> println(<span class="k">int</span> x)     <span class="c">// takes an int</span></code></pre>''',
        "speak": "And one that takes an int, plus several more we're not showing here. Java looks at what you actually passed in, and picks the matching version automatically.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Mixing up parameter and argument &mdash; parameter is the variable in the method header, argument is the value at the call site.</li>
      <li><span class="check">!</span>Assuming a method can change the caller's original value &mdash; call by value means only a copy ever goes in.</li>
      <li><span class="check">!</span>Wrong argument count or type &mdash; the compiler checks a call against the method's signature, and mismatches won't compile.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Mixing up parameter and argument, precisely, parameter is the variable in the method's header, argument is the value at the call site. Assuming a method can reach back and change the caller's original value, call by value means the method only ever gets a copy, reassigning a parameter inside never touches the variable the caller passed in. And getting the argument count or type wrong, the compiler checks every call against the method's signature, and any mismatch simply won't compile.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A signature is a method's name plus its parameter types.</li>
      <li><span class="check">&#10003;</span>Parameter = variable in the header; argument = value at the call site.</li>
      <li><span class="check">&#10003;</span>Java uses call by value &mdash; a method gets a copy, never the original.</li>
      <li><span class="check">&#10003;</span>Overloading lets multiple methods share a name with different parameter lists.</li>
    </ul></div>''',
        "speak": "So: a signature is a method's name plus its parameter types. Parameter is the variable in the header, argument is the value at the call site. Java uses call by value, a method always gets a copy, never the original. And overloading lets multiple methods share one name with different parameter lists, Java picks the right one for you. Next up, lesson 4.2, actually calling static class methods and working with what they return.",
    },
]
