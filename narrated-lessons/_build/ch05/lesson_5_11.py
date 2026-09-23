BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Informal Runtime Analysis of Loops</h1>
      <p class="scr-sub">Predicting exactly how many times a loop runs &mdash; without ever running it.</p>
    </div>''',
        "speak": "To close out Chapter 5, one last, very practical skill, reading a loop's header and knowing exactly how many times it'll run, before you ever hit run.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> i = <span class="n">3</span>; i &lt; <span class="n">7</span>; i++) { ... } <span class="c">// runs 6 - 3 + 1 = 4 times</span></code></pre>''',
        "speak": "i starts at 3, and stops before reaching 7. It actually takes the values 3, 4, 5, and 6, four values total. The formula, largest value the loop variable reaches, minus the smallest value, plus 1. Here that's 6 minus 3 plus 1, which is 4. For a less-than bound, the largest value it actually reaches is one less than the limit written in the header, for a less-than-or-equal bound, it's exactly the limit itself.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Nested Loops Multiply</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Total iterations = outer count times inner count.</p>''',
        "speak": "And when loops are nested, like we just saw last lesson, the total iteration count is outer iterations, times inner iterations.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// 5 outer passes &times; 10 inner passes = 50 total iterations</span>
<span class="k">for</span> (<span class="k">int</span> row = <span class="n">0</span>; row &lt; <span class="n">5</span>; row++)
    <span class="k">for</span> (<span class="k">int</span> col = <span class="n">0</span>; col &lt; <span class="n">10</span>; col++) { ... }</code></pre>''',
        "speak": "row runs 5 times, col runs 10 times for every single one of those, so the inner body actually executes 5 times 10, 50 times total, not 5 plus 10.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Why This Matters</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Faster than adding print statements and re-running, tracing this by hand usually finds the bug immediately.</p>''',
        "speak": "Being able to predict a loop's iteration count without running it is a genuinely real debugging tool. If a loop runs way more, or way fewer, times than you expected, tracing through this exact formula by hand usually finds the off-by-one or the wrong bound immediately, faster than sprinkling print statements everywhere and re-running the whole thing.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting to subtract 1 for a < bound &mdash; i < 7 starting at 3 reaches four values, not seven minus three.</li>
      <li><span class="check">!</span>Multiplying the wrong two numbers for a nested loop &mdash; it's outer-count times inner-count-per-pass, not outer-count plus inner-count.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Forgetting to subtract 1 for a less-than bound, i less-than 7, starting at 3, reaches four values, 3, 4, 5, 6, not seven minus three raw. And multiplying the wrong two numbers for a nested loop, it's outer count times inner count per pass, not outer count plus inner count, addition badly undercounts what a nested loop actually does.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Iteration count = largest reachable value − smallest value + 1.</li>
      <li><span class="check">&#10003;</span>Nested loops multiply: total iterations = outer count × inner count.</li>
      <li><span class="check">&#10003;</span>Counting iterations by hand is a fast way to catch an off-by-one bug.</li>
    </ul></div>''',
        "speak": "So: a loop's iteration count is the largest reachable value, minus the smallest value, plus 1. Nested loops multiply, total iterations is outer count times inner count. And counting iterations by hand is a fast, reliable way to catch an off-by-one bug before it ever turns into a mysterious runtime problem. That wraps up Chapter 5, control structures, if statements, for loops, while loops, boolean logic, and now, predicting exactly how they run. Nice work getting through all of it.",
    },
]
