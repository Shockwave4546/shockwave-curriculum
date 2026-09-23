BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 10 &middot; 2D Arrays</div>
      <h1>2D Array Creation and Access</h1>
      <p class="scr-sub">Rows and columns, not just a flat list.</p>
    </div>''',
        "speak": "So far every array we've used has been one long flat list. But some data is naturally rows and columns instead, and that's what we're covering in Chapter 10: two-D arrays.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">A Real Example: Swerve Telemetry</h2><ul>
      <li><span class="num">1</span><span>4 modules &mdash; front-left, front-right, back-left, back-right</span></li>
    </ul></div>''',
        "speak": "Picture swerve drive telemetry. You've got four modules: front-left, front-right, back-left, back-right.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">A Real Example: Swerve Telemetry</h2><ul>
      <li><span class="num">1</span><span>4 modules &mdash; front-left, front-right, back-left, back-right</span></li>
      <li><span class="num">2</span><span>Each one logging several current-draw samples over time</span></li>
    </ul></div>''',
        "speak": "And each module is logging several current-draw samples over time. One row per module, one column per sample, that's a two-D array.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// datatype[][] variableName = new datatype[numberRows][numberCols];</span>
<span class="t">double</span>[][] moduleCurrents = <span class="k">new</span> <span class="t">double</span>[4][5]; <span class="c">// 4 modules, 5 samples each</span></code></pre>''',
        "speak": "The declaration looks like a normal array type, but with a second set of brackets. Datatype, two pairs of square brackets, a name, and then new datatype, rows, columns. Here, four modules by five samples each.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Java Actually Builds</h2><ul>
      <li><span class="num">1</span><span>An <em>array of arrays</em> &mdash; the outer array holds 4 references</span></li>
    </ul></div>''',
        "speak": "Under the hood, Java stores this as an array of arrays. The outer array holds four references.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Java Actually Builds</h2><ul>
      <li><span class="num">1</span><span>An <em>array of arrays</em> &mdash; the outer array holds 4 references</span></li>
      <li><span class="num">2</span><span>Each reference points at its own separate 5-element inner array</span></li>
    </ul></div>''',
        "speak": "And each of those four references points at its own separate five-element inner array. Declared without new, the variable is null, same as any other reference type. Once you do create it with new, every element starts at that type's default, which for double is zero point zero.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">One Inner List Per Row</div>
    <pre class="code"><code><span class="t">double</span>[][] moduleCurrents =
{
    {12.1, 11.8, 40.2, 12.4, 11.9}, <span class="c">// front-left</span>
    {12.0, 11.9, 12.1, 11.7, 12.2}, <span class="c">// front-right</span>
    {11.9, 12.3, 12.0, 11.8, 12.1}, <span class="c">// back-left</span>
    {12.2, 12.0, 11.9, 12.4, 11.9}, <span class="c">// back-right</span>
};</code></pre>''',
        "speak": "You can also fill one in directly with an initializer list. For a two-D array, that's a list of one-D initializer lists, one per row, and Java figures out the size on its own. Here's all four swerve modules, five samples apiece.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>moduleCurrents[row][col]</code><span class="nlabel">first index is the row</span></div>
    </div>''',
        "speak": "To read or write one element, you index it twice: array, row, column. The first index is always the row.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>moduleCurrents[row][col]</code><span class="nlabel">first index is the row</span></div>
      <div class="namerow"><code>moduleCurrents[0][2]</code><span class="nlabel">second index is the column</span></div>
    </div>
    <pre class="code"><code><span class="t">double</span> spike = moduleCurrents[0][2]; <span class="c">// front-left module, 3rd sample -&gt; 40.2</span>
moduleCurrents[0][2] = 0.0;          <span class="c">// overwrite a bad reading</span></code></pre>''',
        "speak": "So moduleCurrents at row zero, column two, is front-left's third sample, that spike value of forty point two. And you can assign into it the exact same way, to overwrite a bad reading. One quick warning: printing the array directly with System dot out dot println just prints its object reference, not the actual numbers. Actually printing every value takes nested loops, which is next lesson.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>moduleCurrents.length</code><span class="nlabel">4 &mdash; number of rows</span></div>
      <div class="namerow"><code>moduleCurrents[0].length</code><span class="nlabel">5 &mdash; number of columns</span></div>
    </div>
    <pre class="code"><code>moduleCurrents.length     <span class="c">// 4  (number of modules / rows)</span>
moduleCurrents[0].length  <span class="c">// 5  (samples per module / columns)</span></code></pre>''',
        "speak": "For sizes: dot length on the whole array gives the row count, four modules. Dot length on any one row, like moduleCurrents bracket zero dot length, gives the column count, five samples. This curriculum, and the AP exam, both assume the array is rectangular, every row the same length, so any row works for that check.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">double</span>[] frontLeftRow = moduleCurrents[0]; <span class="c">// a single row IS a real 1D array on its own</span></code></pre>''',
        "speak": "That's possible because of how Java actually built this thing: one row is a real, complete one-D array all by itself, not just a slice. That's exactly why moduleCurrents bracket zero dot length works, you're calling dot length on a genuine one-D array.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Swapping row and column &mdash; the first index is always the row, never the column.</li>
      <li><span class="check">!</span>Assuming a freshly-created array has real data &mdash; new double bracket 4 bracket 5 gives 20 zeros, not real readings.</li>
      <li><span class="check">!</span>Off-by-one against length &mdash; last valid row is length minus 1, last valid column is row-length minus 1.</li>
    </ul></div>''',
        "speak": "A few pitfalls to watch for. Don't swap row and column, moduleCurrents at row two column zero is back-left's first sample, not front-left's third, the first index is always the row. Don't assume a freshly created array already has usable data, it's all zeros until you fill it in. And watch off-by-one against length, same rule as one-D arrays, just in both directions now. Get either index out of range, in either dimension, and you get the exact same ArrayIndexOutOfBoundsException as a one-D array.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>datatype bracket bracket name = new datatype bracket rows bracket cols.</li>
      <li><span class="check">&#10003;</span>arr[row][col] reads or writes one element &mdash; row first, always.</li>
      <li><span class="check">&#10003;</span>.length gives row count; .length on one row gives column count.</li>
      <li><span class="check">&#10003;</span>Java builds it as an array of arrays &mdash; each row is its own real 1D array.</li>
    </ul></div>''',
        "speak": "So, to recap. A two-D array is datatype, two brackets, a name, equals new datatype, rows, columns, or filled in one shot with a nested initializer list. Arr row col reads or writes one element, and the row always comes first. Dot length gives you the row count, and dot length on any single row gives you the column count. And underneath it all, Java builds this as an array of arrays, where each row is its own genuine one-D array. Next up, lesson 10.2: actually looping over all of this with nested loops.",
    },
]
