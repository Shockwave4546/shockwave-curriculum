BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 10 &middot; 2D Arrays</div>
      <h1>Implementing 2D Array Algorithms</h1>
      <p class="scr-sub">Every algorithm shape you already know, now in two dimensions.</p>
    </div>''',
        "speak": "Sum, average, min, max, property checks, duplicates, we built all of those algorithm shapes for one-D arrays back in lesson 9.5. Good news: every single one of them extends to two-D arrays, applied to the whole grid, or to just one row, one column, or a smaller subsection. That's lesson 10.3.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static</span> <span class="t">double</span> <span class="me">getTotalForModule</span>(<span class="t">int</span> row, <span class="t">double</span>[][] a)
{
    <span class="t">double</span> total = 0;
    <span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; a[0].length; col++)
    {
        total = total + a[row][col];
    }
    <span class="k">return</span> total;
}</code></pre>''',
        "speak": "First up, summing. Fix the row you care about, and loop over the columns, adding up every sample in that one module's history. That's getTotalForModule, one module summed across all its samples.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static</span> <span class="t">double</span> <span class="me">getTotalForModule</span>(<span class="t">int</span> row, <span class="t">double</span>[][] a)
{
    <span class="t">double</span> total = 0;
    <span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; a[0].length; col++)
    {
        total = total + a[row][col];
    }
    <span class="k">return</span> total;
}

<span class="k">public static</span> <span class="t">double</span> <span class="me">getTotalForSample</span>(<span class="t">int</span> col, <span class="t">double</span>[][] a)
{
    <span class="t">double</span> total = 0;
    <span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; a.length; row++)
    {
        total = total + a[row][col];
    }
    <span class="k">return</span> total;
}</code></pre>''',
        "speak": "Flip it around and you get getTotalForSample: fix the column, this one instant in time, and loop over the rows instead, summing that same sample number across all four modules. Useful for spotting a simultaneous spike, a brownout risk.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static</span> <span class="t">double</span> <span class="me">getPeakCurrent</span>(<span class="t">double</span>[][] a)
{
    <span class="t">double</span> peak = a[0][0];
    <span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; a.length; row++)
    {
        <span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; a[0].length; col++)
        {
            <span class="k">if</span> (a[row][col] &gt; peak)
            {
                peak = a[row][col];
            }
        }
    }
    <span class="k">return</span> peak;
}</code></pre>''',
        "speak": "For a max across the whole array, both loops nest together, and you seed peak with a real value, a-zero-zero, not with zero itself. That's the same rule from lesson 9.5: if every reading happened to be negative, seeding with zero would give you a wrong, too-generous answer.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Loop Bounds Don&rsquo;t Have to Cover Everything</h2><ul>
      <li><span class="num">1</span><span>Narrow the start and end of each loop to check just a subsection</span></li>
    </ul></div>''',
        "speak": "Here's something new for two-D: your loop bounds don't have to sweep the entire array. Narrow the start and end of each loop, and you're checking just a rectangular subsection instead.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static</span> <span class="t">int</span> <span class="me">countSpikes</span>(<span class="t">double</span> threshold, <span class="t">double</span>[][] a,
                               <span class="t">int</span> rowStart, <span class="t">int</span> rowEnd, <span class="t">int</span> colStart, <span class="t">int</span> colEnd)
{
    <span class="t">int</span> count = 0;
    <span class="k">for</span> (<span class="t">int</span> row = rowStart; row &lt;= rowEnd; row++)
    {
        <span class="k">for</span> (<span class="t">int</span> col = colStart; col &lt;= colEnd; col++)
        {
            <span class="k">if</span> (a[row][col] &gt; threshold)
            {
                count++;
            }
        }
    }
    <span class="k">return</span> count;
}</code></pre>''',
        "speak": "countSpikes takes four extra bounds, a row range and a column range, and only scans inside that window. Notice both loops use less-than-or-equal-to, not just less-than, because rowEnd and colEnd here are meant to be inclusive bounds.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Duplicates Need 4 Nested Loops</h2><ul>
      <li><span class="num">1</span><span>Two loops to pick a starting cell &mdash; row, col</span></li>
    </ul></div>''',
        "speak": "Now, duplicates. A one-D duplicate check needed two nested loops. A full two-D duplicate check needs four. Two of them just to pick a starting cell, a row and a column.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Duplicates Need 4 Nested Loops</h2><ul>
      <li><span class="num">1</span><span>Two loops to pick a starting cell &mdash; row, col</span></li>
      <li><span class="num">2</span><span>Two more to compare it against every cell that comes <em>after</em> it</span></li>
    </ul></div>''',
        "speak": "And two more loops to compare that candidate against every cell that comes after it, later columns in the same row, plus every cell in every later row.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static boolean</span> <span class="me">hasDuplicateReading</span>(<span class="t">double</span>[][] a)
{
    <span class="k">for</span> (<span class="t">int</span> row = 0; row &lt; a.length; row++)
    {
        <span class="k">for</span> (<span class="t">int</span> col = 0; col &lt; a[0].length; col++)
        {
            <span class="k">for</span> (<span class="t">int</span> row2 = row; row2 &lt; a.length; row2++)
            {
                <span class="t">int</span> startCol = (row2 == row) ? col + 1 : 0;
                <span class="k">for</span> (<span class="t">int</span> col2 = startCol; col2 &lt; a[0].length; col2++)
                {
                    <span class="k">if</span> (a[row][col] == a[row2][col2])
                    {
                        <span class="k">return true</span>;
                    }
                }
            }
        }
    }
    <span class="k">return false</span>;
}</code></pre>''',
        "speak": "Here's the whole thing. The key trick is startCol: within the same row as the candidate, only look at columns after its own column; once you're in a genuinely later row, every column is fair game, starting from zero. Skip that trick and you'll either miss valid pairs, or compare the same pair twice.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static void</span> <span class="me">rotateRowRight</span>(<span class="t">double</span>[][] a, <span class="t">int</span> row)
{
    <span class="t">double</span> last = a[row][a[0].length - 1];
    <span class="k">for</span> (<span class="t">int</span> col = a[0].length - 1; col &gt; 0; col--)
    {
        a[row][col] = a[row][col - 1];
    }
    a[row][0] = last;
}</code></pre>''',
        "speak": "Last shape: rotating or reversing. Do it to a single row, or to one fixed column index taken across every row, a kind of virtual column, and it works exactly like the one-D version from lesson 9.5, because at that point you're really only touching one one-D array at a time.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Confusing "sum a row" with "sum a column" &mdash; fixing row and looping col sums a row; fixing col and looping row sums a column.</li>
      <li><span class="check">!</span>Forgetting the duplicate check's startCol trick &mdash; without it you miss pairs or double-compare them.</li>
      <li><span class="check">!</span>Using less-than instead of less-than-or-equal on subsection bounds meant to be inclusive &mdash; that silently skips the last row or column.</li>
    </ul></div>''',
        "speak": "Common pitfalls to close out on. Don't mix up summing a row with summing a column, fixing the row and looping columns sums a row, fixing the column and looping rows sums a column, easy to write the wrong one out of habit. Don't forget the duplicate check's startCol trick, skip it and you either miss valid pairs or double-count the same one. And when a subsection's bounds are meant to be inclusive, use less-than-or-equal-to, not less-than, or you'll silently skip the very last row or column.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Every 1D algorithm shape extends to 2D: whole array, one row, one column, or a bounded subsection.</li>
      <li><span class="check">&#10003;</span>Sum a row: fix the row, loop columns. Sum a column: fix the column, loop rows.</li>
      <li><span class="check">&#10003;</span>A full 2D duplicate check needs 4 nested loops, not 2.</li>
      <li><span class="check">&#10003;</span>Rotating/reversing one row or one fixed column reuses the exact 1D in-place pattern.</li>
    </ul></div>''',
        "speak": "So, to recap Chapter 10 overall. Every one-D array algorithm pattern, accumulator, min-max, property count, duplicates, rotate, extends into two dimensions, whether you're covering the whole array, one row, one column, or a bounded subsection. Summing a row fixes the row and loops columns; summing a column fixes the column and loops rows. A full two-D duplicate check needs four nested loops, not two. And rotating or reversing a single row, or one fixed-column slice, reuses the exact one-D in-place pattern you already know. That wraps up two-D arrays. Next chapter, we're moving on to enums, named choices for a fixed set of states.",
    },
]
