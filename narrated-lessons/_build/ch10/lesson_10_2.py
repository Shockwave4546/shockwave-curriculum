BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 10 &middot; 2D Arrays</div>
      <h1>2D Array Traversals: Nested Loops</h1>
      <p class="scr-sub">A loop inside a loop &mdash; rows on the outside, columns on the inside.</p>
    </div>''',
        "speak": "Last lesson we created and indexed two-D arrays one cell at a time. But to actually walk through every single value, you need a loop inside a loop, and that's lesson 10.2.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">double</span>[][] moduleCurrents = { {12.1, 11.8, 40.2}, {12.0, 11.9, 12.1} };
<span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; moduleCurrents.length; row++)
{</code></pre>''',
        "speak": "Since a two-D array really is an array of arrays, the outer loop walks the rows. It runs from zero up to moduleCurrents dot length, exactly like a one-D loop, just now it's only stepping through the rows.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">double</span>[][] moduleCurrents = { {12.1, 11.8, 40.2}, {12.0, 11.9, 12.1} };
<span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; moduleCurrents.length; row++)
{
    <span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; moduleCurrents[0].length; col++)
    {</code></pre>''',
        "speak": "Nested right inside it, the inner loop walks the columns of whichever row the outer loop is currently sitting on. Its bound is moduleCurrents bracket zero dot length, the column count, not the row count.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="t">double</span>[][] moduleCurrents = { {12.1, 11.8, 40.2}, {12.0, 11.9, 12.1} };
<span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; moduleCurrents.length; row++)
{
    <span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; moduleCurrents[0].length; col++)
    {
        System.out.println(moduleCurrents[row][col]);
    }
}</code></pre>''',
        "speak": "And inside both loops, moduleCurrents at row, col gets you the current cell. Put together, the loop body runs rows times columns total, here that's two rows by three columns, six values printed.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Row-Major: One Module at a Time</div>
    <pre class="code"><code><span class="c">// Row-major: finish one module's samples before moving to the next module</span>
<span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; moduleCurrents.length; row++)
    <span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; moduleCurrents[0].length; col++)
        process(moduleCurrents[row][col]);</code></pre>''',
        "speak": "Now here's something new that one-D arrays never had to worry about: which index changes in the outer loop decides your traversal order. Rows on the outside, like we just saw, is called row-major, and it finishes one module's entire sample history before moving on to the next module.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Column-Major: One Instant, Every Module</div>
    <pre class="code"><code><span class="c">// Row-major: finish one module's samples before moving to the next module</span>
<span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; moduleCurrents.length; row++)
    <span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; moduleCurrents[0].length; col++)
        process(moduleCurrents[row][col]);

<span class="c">// Column-major: look at sample #0 across ALL modules, then sample #1 across all modules...</span>
<span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; moduleCurrents[0].length; col++)
    <span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; moduleCurrents.length; row++)
        process(moduleCurrents[row][col]);</code></pre>''',
        "speak": "Flip which loop is on the outside, and you get column-major: for a given sample number, look across every module, then move to the next sample number. This is exactly what you'd want if you're asking, at this one instant, were all four modules spiking at once, a brownout risk that row-major order would never surface directly.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Neither Order Is &ldquo;Correct&rdquo;</h2><ul>
      <li><span class="num">1</span><span>Row-major &mdash; how did <em>this one module</em> behave over time?</span></li>
      <li><span class="num">2</span><span>Column-major &mdash; what was total current draw <em>at this one instant</em>?</span></li>
    </ul></div>''',
        "speak": "Neither order is right or wrong on its own. Pick row-major when the question is about one module's behavior over time, and column-major when the question is about one instant across every module.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="t">double</span>[] moduleRow : moduleCurrents)  <span class="c">// outer variable is a 1D array — one row</span>
{
    <span class="k">for</span> (<span class="t">double</span> sample : moduleRow)        <span class="c">// inner variable matches the element type</span>
    {
        System.out.println(sample);
    }
}</code></pre>''',
        "speak": "A nested enhanced for-each traverses a two-D array too, with no indices at all, but only when you don't need row or column numbers, and don't need to modify the values in place. The pattern to remember: the outer loop variable is typed as a whole one-D array, one entire row, and the inner loop variable matches the actual element type.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">One Catch: Reassignment Doesn&rsquo;t Stick</h2><ul>
      <li><span class="check">!</span>Just like 1D for-each, reassigning the loop variable never changes what's stored in the array.</li>
    </ul></div>''',
        "speak": "And just like one-D for-each, reassigning that inner loop variable inside the loop body does not change what's actually stored in the array. It only overwrites a local copy.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (TalonFX[] moduleRow : driveMotors)
{
    <span class="k">for</span> (TalonFX motor : moduleRow)
    {
        motor.setNeutralMode(NeutralModeValue.Brake); <span class="c">// mutates the real object — this works</span>
    }
}</code></pre>''',
        "speak": "That modification limit is specifically about primitives, though. Give the for-each a two-D array of objects instead, say, a grid of motor controller wrapper objects, and calling a method on the loop variable absolutely does mutate the real thing, because you're not reassigning the array slot, you're calling a method on the object it already refers to. Setting every motor's neutral mode to brake, right here, actually works.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using the row count as the inner loop's bound &mdash; the inner loop walks columns, so it needs the column-length bound, not the row-length one.</li>
      <li><span class="check">!</span>Expecting for-each to let you assign into a primitive 2D array &mdash; same rule as 1D, it changes nothing.</li>
      <li><span class="check">!</span>Treating row-major vs. column-major as "correct" vs. "incorrect" &mdash; neither is wrong, it depends on the question being asked.</li>
    </ul></div>''',
        "speak": "Common pitfalls here. Don't use the row count as the inner loop's bound, the inner loop walks columns, so it needs the column-length bound instead. Don't expect a for-each to let you assign into a primitive two-D array, same rule as one-D, it changes nothing. And don't treat row-major and column-major as one being correct and the other wrong, they're just two different questions.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Traversing a full 2D array needs nested loops: outer for rows, inner for columns.</li>
      <li><span class="check">&#10003;</span>Row-major finishes one row before the next; column-major finishes one column across all rows first.</li>
      <li><span class="check">&#10003;</span>Nested for-each traverses with no indices: outer variable is a row, inner variable is one element.</li>
      <li><span class="check">&#10003;</span>For-each can't modify primitive values, but it can call mutator methods on objects the array holds.</li>
    </ul></div>''',
        "speak": "So, to recap. Traversing a whole two-D array takes nested loops, outer for rows, inner for columns, running rows times columns total. Row-major finishes one row before moving to the next; column-major finishes one column, across every row, before moving to the next. A nested for-each does the same traversal with no indices, outer variable is a whole row, inner variable is one element. And for-each can't modify primitive values in place, but it can absolutely call mutator methods on objects the array holds. Next time, lesson 10.3: putting all of this to work in real algorithms.",
    },
]
