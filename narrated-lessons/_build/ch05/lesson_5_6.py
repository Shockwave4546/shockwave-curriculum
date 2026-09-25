BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Compound Boolean Expressions</h1>
      <p class="scr-sub">Combining conditions with and, or, and not &mdash; and a genuine safety trick hiding inside how Java evaluates them.</p>
    </div>''',
        "speak": "Real conditions are rarely just one comparison. Usually you need several things true at once, or any one of a few. Let's combine boolean expressions properly.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (armReady &amp;&amp; intakeReady)
{
    shooter.score();
}</code></pre>''',
        "speak": "Two ampersands mean and, needs both sides true. arm ready and intake ready, the shooter only scores when both conditions actually hold at once. Two pipe characters mean or, needs just one side true, maybe both. And a single exclamation point flips a boolean's value entirely.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Short-Circuit Evaluation</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Java stops checking as soon as the answer is already known.</p>''',
        "speak": "Here's something genuinely useful, not just an implementation detail. Java stops checking as soon as the answer is already known, it never evaluates more than it has to. In a and b, if a is false, b never even gets checked, the whole thing is already false. In a or b, if a is true, b never gets checked, the whole thing is already true.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (sensor != <span class="k">null</span> &amp;&amp; sensor.isFaulty())
{
    report(sensor);
}</code></pre>''',
        "speak": "Here's the real safety pattern this enables. sensor not-equals null, and sensor dot is faulty. If sensor is null, the left side is already false, so the and operator never even evaluates sensor dot is faulty, which would otherwise crash with a Null Pointer Exception. The order here genuinely matters, the null check has to come first for this protection to work.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Operator Precedence</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Not binds tightest, then and, then or &mdash; parentheses override all of it.</p>''',
        "speak": "Not binds tightest, then and, then or, and parentheses override all of it, making your actual intent explicit whenever there's any doubt.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (!ready &amp;&amp; !armed) { ... }        <span class="c">// ! applies to each: true only if BOTH are false</span></code></pre>''',
        "speak": "Not ready, and not armed. Here the not applies to each variable individually, before the and ever gets involved, so this is true only when both ready and armed are false.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (!ready &amp;&amp; !armed) { ... }        <span class="c">// ! applies to each: true only if BOTH are false</span>
<span class="k">if</span> (!(ready &amp;&amp; armed)) { ... }       <span class="c">// different! true if EITHER one is false</span></code></pre>''',
        "speak": "But this second one is genuinely different. The not wraps the entire parenthesized ready-and-armed expression, so it's true whenever either one of them is false. If ready is true but armed is false, the first line is false, and the second is true. Same variables, different grouping, different answer, which is exactly why mixing up which one you meant is a real risk.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Putting the null check on the wrong side &mdash; sensor.isFaulty() && sensor != null checks the faulty status first, and crashes before the null check runs.</li>
      <li><span class="check">!</span>Assuming !(a && b) is the same as !a && !b &mdash; it's not, that's a real logic error.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Putting the null check on the wrong side, sensor dot is faulty and sensor not-equals null checks the faulty status first, and if sensor really is null, it crashes before the null check ever gets a chance to run. The null check must always come first for short-circuiting to protect you. And assuming not-open-paren a and b is the same as not a, and not b, it's genuinely not, that's a real logic error, the correct equivalent, De Morgan's Law, is exactly what's coming up next lesson.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>&amp;&amp; requires both sides true; || requires at least one; ! flips a boolean.</li>
      <li><span class="check">&#10003;</span>Short-circuit evaluation skips the right side once the left side already decides the result.</li>
      <li><span class="check">&#10003;</span>! binds tightest, then &amp;&amp;, then || &mdash; use parentheses when the default grouping isn't what you mean.</li>
    </ul></div>''',
        "speak": "So: and requires both sides true, or requires at least one, not flips a boolean. Short-circuit evaluation skips the right side entirely once the left side already decides the result, and that's exactly what lets a null-check-first pattern protect you safely. And not binds tightest, then and, then or, use parentheses whenever the default grouping isn't what you actually mean. Next up, lesson 5.7, De Morgan's Laws, the exact rule for flipping a negated compound condition correctly.",
    },
]
