BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Boolean Expressions</h1>
      <p class="scr-sub">The actual conditions that drive every if and every loop.</p>
    </div>''',
        "speak": "Every if and every loop we've written so far needed a true-or-false condition inside its parentheses. Let's look at exactly how those get built.",
    },
    {
        "screen": '''<pre class="code"><code>==   <span class="c">// equals</span>
!=   <span class="c">// does not equal</span>
&lt;    <span class="c">// less than</span></code></pre>''',
        "speak": "Six relational operators compare values and always produce true or false. Double equals tests equality. Not-equals tests inequality. Less-than compares size.",
    },
    {
        "screen": '''<pre class="code"><code>==   <span class="c">// equals</span>
!=   <span class="c">// does not equal</span>
&lt;    <span class="c">// less than</span>
&gt;    <span class="c">// greater than</span>
&lt;=   <span class="c">// less than or equal to</span>
&gt;=   <span class="c">// greater than or equal to</span></code></pre>''',
        "speak": "Greater-than, less-than-or-equal-to, and greater-than-or-equal-to round out the set. All six always produce a genuine boolean, true or false, nothing else.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> battery = <span class="n">11.8</span>;
System.out.<span class="me">println</span>(battery &lt; <span class="n">12.0</span>);  <span class="c">// true &mdash; low battery</span></code></pre>''',
        "speak": "battery at 11 point 8. Battery less than 12 point 0 prints true, that's a genuinely low battery.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> battery = <span class="n">11.8</span>;
System.out.<span class="me">println</span>(battery &lt; <span class="n">12.0</span>);  <span class="c">// true &mdash; low battery</span>
System.out.<span class="me">println</span>(battery &gt;= <span class="n">12.0</span>); <span class="c">// false</span></code></pre>''',
        "speak": "And battery greater-than-or-equal-to 12 point 0 prints false, consistent with the same reading.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Equality: Primitives vs. Objects</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">On objects, double equals compares "same object in memory," not "same contents."</p>''',
        "speak": "One subtlety worth flagging early. Double equals on primitives, int, double, boolean, compares actual values, exactly what you'd expect. But double equals on objects compares whether two variables point at the exact same object in memory, not whether their contents look the same. Two separately built Talon F X objects with identical settings are still two different objects, double equals between them is false. Objects get a full treatment of this in Chapter 6, once Strings are introduced.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Divisibility with %</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">From Ch.2 &mdash; tests whether one number divides evenly into another.</p>''',
        "speak": "The remainder operator from Chapter 2 has a second life here, testing whether a number divides evenly into another.",
    },
    {
        "screen": '''<pre class="code"><code>(number % <span class="n">2</span> == <span class="n">0</span>)  <span class="c">// true if number is even</span></code></pre>''',
        "speak": "number percent 2, double equals 0, is true exactly when number is even.",
    },
    {
        "screen": '''<pre class="code"><code>(number % <span class="n">2</span> == <span class="n">0</span>)  <span class="c">// true if number is even</span>
(number % <span class="n">2</span> != <span class="n">0</span>)  <span class="c">// true if number is odd</span></code></pre>''',
        "speak": "number percent 2, not-equals 0, is true exactly when it's odd.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>(number % <span class="n">2</span> == <span class="n">0</span>)  <span class="c">// true if number is even</span>
(number % <span class="n">2</span> != <span class="n">0</span>)  <span class="c">// true if number is odd</span>
(number % x == <span class="n">0</span>)  <span class="c">// true if number is evenly divisible by x</span></code></pre>''',
        "speak": "And more generally, number percent x, double equals 0, is true whenever number divides evenly by x, for any x you choose.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using == on objects expecting a content comparison &mdash; it checks "same object," not "same values."</li>
      <li><span class="check">!</span>Testing oddness with num % 2 == 1 &mdash; fails for negative odd numbers, whose remainder is -1, not 1. Use != 0 instead.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Using double equals on objects while expecting a content comparison, it checks same object, not same values, two different but identical-looking objects still compare unequal. And testing oddness with number percent 2, double equals 1, that looks right, but fails for negative odd numbers, since their remainder comes out as negative 1, not 1. number percent 2, not-equals 0, works correctly for both signs.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Relational operators always produce a boolean result.</li>
      <li><span class="check">&#10003;</span>== on primitives compares values; == on objects compares identity, not content.</li>
      <li><span class="check">&#10003;</span>% tests divisibility &mdash; use != 0 for odd, not == 1, to handle negatives correctly.</li>
    </ul></div>''',
        "speak": "So: relational operators always produce a genuine boolean result. Double equals on primitives compares values, double equals on objects compares identity, not content. And percent tests divisibility, use not-equals-zero for odd numbers, not equals-one, so negatives behave correctly too. Next up, lesson 5.5, nested if statements, chaining more than two possible paths together.",
    },
]
