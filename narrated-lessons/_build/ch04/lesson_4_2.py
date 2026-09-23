BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 4 &middot; Using Objects &amp; Calling Methods</div>
      <h1>Calling Class Methods</h1>
      <p class="scr-sub">Static methods, and the difference between a method that returns something and one that doesn't.</p>
    </div>''',
        "speak": "Now let's actually call some methods. We'll start with the kind that belongs to a class itself, rather than to any particular object.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Class Methods (Static Methods)</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Belongs to the class itself, not to any object. main is always static.</p>''',
        "speak": "A method marked static belongs to the class itself, not to any particular object built from it, that's why it's called a class method, or a static method. Main is always static, that's exactly why it can run before a single object exists yet.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> distance = <span class="t">Math</span>.<span class="me">abs</span>(target - current);</code></pre>''',
        "speak": "You call a static method using the class name and the dot operator. Math dot abs, target minus current. No object required anywhere, just the class name itself. Inside the same class that defines a method, you can even drop the class name and call it bare.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Void vs. Non-Void</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">void returns nothing; a non-void method computes and returns a value.</p>''',
        "speak": "A void method doesn't return anything, you call it purely for its side effect, printing something, setting a motor's speed. A non-void method computes and returns a value, one the caller actually has to do something with.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="k">int</span> square(<span class="k">int</span> number)
{
    <span class="k">int</span> result = number * number;
    <span class="k">return</span> result;
}</code></pre>''',
        "speak": "Here's a non-void method, square, which takes a number, multiplies it by itself, and returns the result. Return sends that value back to whoever called the method, and ends the method immediately, nothing written after return ever runs.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> y = square(<span class="n">5</span>);        <span class="c">// stored in a variable</span></code></pre>''',
        "speak": "Call it, and you have to actually use what comes back. y equals square of 5 stores the returned value in a variable.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> y = square(<span class="n">5</span>);        <span class="c">// stored in a variable</span>
System.out.<span class="me">println</span>(square(<span class="n">4</span>)); <span class="c">// used directly in an expression</span></code></pre>''',
        "speak": "Or use it directly inside another expression, print lining square of 4 right in place, no separate variable needed.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> total = calculateChecksum(data); <span class="c">// fine &mdash; assuming calculateChecksum returns an int</span></code></pre>''',
        "speak": "Here calculate checksum's returned int gets stored properly in total, exactly as it should be.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> total = calculateChecksum(data); <span class="c">// fine &mdash; assuming calculateChecksum returns an int</span>
calculateChecksum(data);             <span class="c">// compiles, but the returned value is silently thrown away</span></code></pre>''',
        "speak": "But this second line compiles just fine too, and that's exactly the trap, calculate checksum still runs, but whatever it returns gets silently thrown away, no error, no warning, just a wasted computation and a bug waiting to be noticed.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Calling a non-void method and doing nothing with the result &mdash; it still compiles, which makes it easy to miss.</li>
      <li><span class="check">!</span>Assigning a return value to the wrong type &mdash; a double result can't go straight into an int without an explicit cast.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Calling a non-void method and doing absolutely nothing with the result, Java doesn't force you to use a return value, and that's exactly what makes this so easy to miss. And assigning a return value to the wrong type, a double-returning method's result can't go straight into an int variable without an explicit cast, and remember, that cast truncates the decimal, which may not be what you actually wanted.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A static method is a class method, called via the class name.</li>
      <li><span class="check">&#10003;</span>void returns nothing; non-void computes a value that must be stored or used.</li>
      <li><span class="check">&#10003;</span>return sends a value back to the caller and ends the method immediately.</li>
      <li><span class="check">&#10003;</span>An ignored return value still compiles &mdash; a real, easy-to-miss bug.</li>
    </ul></div>''',
        "speak": "So: a static method is a class method, called through the class name, or bare from inside that same class. Void returns nothing, non-void computes a value that must be stored or used. Return sends a value back to the caller and ends the method right there. And an ignored return value still compiles, quietly, which makes it a real bug to watch for in your own code. Next up, lesson 4.3, a whole class built entirely out of static methods, Math itself.",
    },
]
