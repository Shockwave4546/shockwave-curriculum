BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Nested Iteration</h1>
      <p class="scr-sub">A loop inside a loop &mdash; the standard shape for anything grid-like.</p>
    </div>''',
        "speak": "Loops can nest inside each other, just like ifs could. This turns out to be exactly the shape you need for anything grid-shaped, and grids show up constantly in vision processing.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> row = <span class="n">0</span>; row &lt; <span class="n">8</span>; row++)
{</code></pre>''',
        "speak": "Here's the outer loop, row runs from 0 up to 7, eight rows total.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> row = <span class="n">0</span>; row &lt; <span class="n">8</span>; row++)
{
    <span class="k">for</span> (<span class="k">int</span> col = <span class="n">0</span>; col &lt; <span class="n">8</span>; col++)
    {</code></pre>''',
        "speak": "And nested right inside it, an inner loop, col, also running 0 through 7. For every single value of row, this inner loop runs all the way through every col value, from start to finish, before the outer loop ever advances to the next row.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> row = <span class="n">0</span>; row &lt; <span class="n">8</span>; row++)
{
    <span class="k">for</span> (<span class="k">int</span> col = <span class="n">0</span>; col &lt; <span class="n">8</span>; col++)
    {
        visionGrid[row][col] = sampleCell(row, col);
    }
}</code></pre>''',
        "speak": "Inside both, we sample one specific cell for each row-col pair. The inner loop restarts completely from scratch every single time the outer loop takes a step, col goes back down to 0 for every new row.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Why This Matters</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Scanning a 2D vision frame, checking every pair of sensors, generating a table of test cases.</p>''',
        "speak": "Nested loops are the natural shape for anything grid-like, scanning a 2D vision frame like we just did, checking every pair of sensors against each other, or generating a table of test cases. 2D arrays, which pair naturally with nested loops like this, get their own full chapter, Chapter 10.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Reusing the same loop variable name for both loops &mdash; it won't compile; the inner declaration conflicts with the outer one.</li>
      <li><span class="check">!</span>Assuming the inner loop's variable persists across outer iterations &mdash; it doesn't; it's freshly initialized every restart.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Reusing the same loop variable name for both loops, a for loop declaring i nested inside another for loop also declaring i simply won't compile, the inner declaration conflicts with the outer one in the same scope, use distinct names, row and col, or i and j. And assuming the inner loop's variable persists across outer iterations, it doesn't, a loop variable declared in a for header is freshly initialized every single time that loop starts, including every restart of an inner loop.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A nested loop runs completely, every single time the outer loop takes one step.</li>
      <li><span class="check">&#10003;</span>Nested loops are the standard shape for anything grid-shaped.</li>
      <li><span class="check">&#10003;</span>Use distinct loop variable names for nested loops.</li>
    </ul></div>''',
        "speak": "So: a nested loop runs completely, every single time the outer loop takes one step. Nested loops are the standard shape for anything grid-shaped, rows and columns, pairs of items, tables of test cases. And always use distinct loop variable names for nested loops. Next up, lesson 5.11, actually predicting how many times a loop runs, just by reading its header.",
    },
]
