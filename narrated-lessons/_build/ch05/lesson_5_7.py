BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Comparing Boolean Expressions: De Morgan's Laws</h1>
      <p class="scr-sub">The exact rule for flipping a negated compound condition correctly.</p>
    </div>''',
        "speak": "Last lesson ended on a warning, not of a-and-b isn't the same as not-a-and-not-b. So what is it equal to? There's an exact rule, and it's worth memorizing properly.",
    },
    {
        "screen": '''<pre class="code"><code>!(a &amp;&amp; b)  is equivalent to  !a || !b</code></pre>''',
        "speak": "Not, open-paren, a and b, is equivalent to, not a, or not b. Negating a compound condition flips both the operator and each individual comparison inside it.",
    },
    {
        "screen": '''<pre class="code"><code>!(a &amp;&amp; b)  is equivalent to  !a || !b
!(a || b)  is equivalent to  !a &amp;&amp; !b</code></pre>''',
        "speak": "And the mirror image, not, open-paren, a or b, is equivalent to, not a, and not b. A simple way to remember it, push the not inward, and flip and to or, or or to and, as it moves in.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Flipping Relational Operators Under Negation</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Negating a comparison flips its sign, not just adds a "not."</p>''',
        "speak": "The same idea applies to relational operators, negating a comparison flips its sign entirely, it doesn't just slap a not in front of it.",
    },
    {
        "screen": '''<pre class="code"><code>!(c == d)  is  c != d</code></pre>''',
        "speak": "Not, c double-equals d, is exactly c not-equals d.",
    },
    {
        "screen": '''<pre class="code"><code>!(c == d)  is  c != d
!(c &lt; d)   is  c &gt;= d</code></pre>''',
        "speak": "Not, c less-than d, is c greater-than-or-equal-to d, not c greater-than d, that would miss the equal case entirely.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>!(c == d)  is  c != d
!(c &lt; d)   is  c &gt;= d
!(c &gt; d)   is  c &lt;= d</code></pre>''',
        "speak": "And not, c greater-than d, is c less-than-or-equal-to d. Put both rules together and negate x less-than 3, and y greater-than 2, and you'd get not-x-less-than-3, or, not-y-greater-than-2, which simplifies further down to x greater-than-or-equal-to 3, or y less-than-or-equal-to 2.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Why Bother Simplifying</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Same result, but "either one isn't ready" reads far more directly than "not true that both are ready."</p>''',
        "speak": "Not, open-paren, ready and armed, and not-ready or not-armed always evaluate to the exact same result. But the second one reads far more directly, either one isn't ready, instead of it's not true that both are ready. Simplifying a negated condition often makes the code's actual intent clearer to the next person reading it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (!ready || !armed) {
    abort();
}</code></pre>''',
        "speak": "Not ready, or not armed, abort. Clean, direct, and logically identical to the negated version from last lesson.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">A Preview: Comparing Objects</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Use .equals() to compare contents; reserve == for checking against null.</p>''',
        "speak": "One more preview before we close out. Double equals on objects, which we first flagged back in lesson 5.4, compares whether two variables point at the same object, not whether their contents match. This matters especially for Strings, which get a full treatment in Chapter 6. For now, the short version, use dot equals to compare what two objects actually contain, and reserve double-equals and not-equals for checking against null specifically.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (sensor != <span class="k">null</span> &amp;&amp; sensor.isFaulty()) { ... } <span class="c">// == used correctly, against null</span></code></pre>''',
        "speak": "This should look familiar, sensor not-equals null, and sensor dot is faulty, from lesson 5.6. That's double-equals, or here its opposite, not-equals, used exactly the way it should be, checking against null, not comparing content.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting to flip the operator, not just add a ! &mdash; !(x < 3) is x >= 3, not x > 3, which misses the equal case.</li>
      <li><span class="check">!</span>Applying De Morgan's Law to only one side &mdash; both the operator and both comparisons must flip, or the result isn't equivalent.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Forgetting to flip the operator, not just add a not, not, x less-than 3, is x greater-than-or-equal-to 3, not x greater-than 3, which quietly misses the equal case. And applying De Morgan's Law to only one side, both the operator and both individual comparisons have to flip, doing only one produces a wrong, non-equivalent expression.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>!(a && b) is !a || !b; !(a || b) is !a && !b.</li>
      <li><span class="check">&#10003;</span>Negating a relational operator flips its sign: &lt; becomes &gt;=, &gt; becomes &lt;=, == becomes !=.</li>
      <li><span class="check">&#10003;</span>Simplifying a negated condition often makes intent easier to read.</li>
      <li><span class="check">&#10003;</span>== on objects checks identity, not content &mdash; .equals() is for comparing what's inside.</li>
    </ul></div>''',
        "speak": "So: not-open-paren-a-and-b is not-a-or-not-b, and not-open-paren-a-or-b is not-a-and-not-b. Negating a relational operator flips its sign, less-than becomes greater-than-or-equal-to, greater-than becomes less-than-or-equal-to, double-equals becomes not-equals. Simplifying a negated condition often makes intent easier to read, even though it's logically identical either way. And double-equals on objects checks identity, not content, dot equals is for comparing what's actually inside, full details in Chapter 6. Next up, lesson 5.8, while loops, repetition without a fixed number of passes.",
    },
]
