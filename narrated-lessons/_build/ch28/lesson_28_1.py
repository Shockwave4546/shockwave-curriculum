BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 28 &middot; Algorithms: Searching, Sorting &amp; Recursion</div>
      <h1>Searching Algorithms</h1>
      <p class="scr-sub">Check every element &mdash; or cut the problem in half, again and again.</p>
    </div>''',
        "speak": "This is an optional chapter. It deepens the array and two-D array work from chapters 9 and 10 with two classic algorithms. It's informational, not required for FRC programming itself. First up, searching.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Linear (Sequential) Search</h2><ul>
      <li><span class="num">1</span><span>Check each element in order, until you find the target or run out of elements</span></li>
    </ul></div>''',
        "speak": "Linear search, also called sequential search, checks each element in order, until it either finds the target, or runs out of elements. It's the same check-every-element shape from lesson 9.5, applied specifically to finding a value.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="t">int</span> <span class="me">sequentialSearch</span>(<span class="t">int</span>[] canBusIds, <span class="t">int</span> target)
{
    <span class="k">for</span> (<span class="t">int</span> j = <span class="n">0</span>; j &lt; canBusIds.length; j++)
    {
        <span class="k">if</span> (canBusIds[j] == target)
        {
            <span class="k">return</span> j;
        }
    }
    <span class="k">return</span> -<span class="n">1</span>; <span class="c">// not found</span>
}</code></pre>''',
        "speak": "Here it is, searching an array of CAN bus ID numbers. The loop walks every index, j, and the moment the element at j equals the target, it returns that index right away. If the loop finishes without a match, it returns negative one, meaning not found.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Searching for a String?</div>
    <div class="scr-naming">
      <div class="namerow"><code>==</code><span class="nlabel">compares identity &mdash; not what you want here</span></div>
      <div class="namerow"><code>.equals()</code><span class="nlabel">compares content &mdash; use this for Strings</span></div>
    </div>''',
        "speak": "Searching for a String instead, like an autonomous route name, needs dot equals, instead of double equals, from lesson 6.1 and chapter 13. You want to compare the object's content, not its identity.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Best and Worst Case</h2><ul>
      <li><span class="num">1</span><span>Slowest: the target isn&rsquo;t present at all &mdash; every element gets checked</span></li>
      <li><span class="num">2</span><span>Fastest: the target sits at index 0</span></li>
    </ul></div>''',
        "speak": "Linear search's slowest case is a target that isn't present at all. The loop has to check every single element before it can conclude that. Its fastest case is the target sitting right at index zero.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Linear Search Over a 2D Array</div>
    <pre class="code"><code><span class="k">private</span> <span class="k">static</span> <span class="k">final</span> <span class="t">double</span> TOLERANCE = <span class="n">1e-9</span>;

<span class="k">public</span> <span class="k">static</span> <span class="t">boolean</span> <span class="me">containsFault</span>(<span class="t">double</span>[][] moduleCurrents, <span class="t">double</span> faultValue)
{
    <span class="k">for</span> (<span class="t">int</span> row = <span class="n">0</span>; row &lt; moduleCurrents.length; row++)
    {
        <span class="k">for</span> (<span class="t">int</span> col = <span class="n">0</span>; col &lt; moduleCurrents[row].length; col++)
        {</code></pre>''',
        "speak": "Extending linear search to a two-D array, from chapter 10, just means looping through every row, and searching within it. It's the same nested-loop shape from lesson 10.3: the outer loop walks the rows, and the inner loop walks the columns. Notice the inner bound reads moduleCurrents bracket row, not bracket zero: a jagged 2D array doesn't guarantee every row is the same length.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Linear Search Over a 2D Array, continued</div>
    <pre class="code"><code>            <span class="k">if</span> (Math.<span class="me">abs</span>(moduleCurrents[row][col] - faultValue) &lt; TOLERANCE)
            {
                <span class="k">return</span> <span class="k">true</span>;
            }
        }
    }
    <span class="k">return</span> <span class="k">false</span>;
}</code></pre>''',
        "speak": "Inside, each cell gets compared against the fault value, within a small tolerance, instead of with double equals. Comparing doubles for exact equality is exactly the trap lesson 2.4 warns about, and it applies here too. The first match within tolerance returns true, right away. If both loops run all the way through with no match, the method returns false.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Binary Search: Only Works on Sorted Data</h2><ul>
      <li><span class="num">1</span><span>Dramatically faster than linear search &mdash; but only on data that&rsquo;s already sorted</span></li>
    </ul></div>''',
        "speak": "Binary search is dramatically faster than linear search, but it only works on data that's already sorted. Think of looking up a name in a phone book. You jump to roughly the right spot, instead of checking every page from the start.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Binary Search: Only Works on Sorted Data</h2><ul>
      <li><span class="num">1</span><span>Dramatically faster than linear search &mdash; but only on data that&rsquo;s already sorted</span></li>
      <li><span class="num">2</span><span>Keep left/right bounds, check the middle, eliminate half the remaining range each time</span></li>
    </ul></div>''',
        "speak": "It keeps a left bound and a right bound, checks the middle element, and eliminates half of the remaining range, every single time.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="t">int</span> <span class="me">binarySearch</span>(<span class="t">int</span>[] sortedTemps, <span class="t">int</span> target)
{
    <span class="t">int</span> left = <span class="n">0</span>;
    <span class="t">int</span> right = sortedTemps.length - <span class="n">1</span>;
    <span class="k">while</span> (left &lt;= right)
    {
        <span class="t">int</span> middle = (left + right) / <span class="n">2</span>;
        <span class="k">if</span> (target &lt; sortedTemps[middle])
        {
            right = middle - <span class="n">1</span>; <span class="c">// target must be in the left half</span>
        }</code></pre>''',
        "speak": "Left starts at zero, and right at the last index. While left is still less than or equal to right, compute the middle. If the target is less than the middle element, it must be in the left half, so right moves down to middle minus one.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">binarySearch, continued</div>
    <pre class="code"><code>        <span class="k">else</span> <span class="k">if</span> (target &gt; sortedTemps[middle])
        {
            left = middle + <span class="n">1</span>;  <span class="c">// target must be in the right half</span>
        }
        <span class="k">else</span>
        {
            <span class="k">return</span> middle;      <span class="c">// found it</span>
        }
    }
    <span class="k">return</span> -<span class="n">1</span>; <span class="c">// left &gt; right means the range is exhausted &mdash; not found</span>
}</code></pre>''',
        "speak": "If the target is greater, it must be in the right half, so left moves up to middle plus one. Otherwise, it's neither less nor greater, so it's a match: return middle. And if left ever passes right, the range is exhausted, and the method returns negative one, not found.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Binary Search on a String[]</div>
    <div class="scr-naming">
      <div class="namerow"><code>str.compareTo(other)</code><span class="nlabel">negative, zero, or positive</span></div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;max-width:52ch;margin:14px auto 0;">Sorts before, equal to, or after &mdash; &lt; and &gt; only work on primitives.</p>''',
        "speak": "For an array of Strings, compare to, from lesson 6.1, replaces less-than and greater-than, which only work on primitives. Calling compare to on one string, passing in another, returns negative, zero, or positive, depending on whether the first string sorts before, equal to, or after the other one.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Binary Search Is So Much Faster</h2><ul>
      <li><span class="num">1</span><span>Linear search, worst case: <strong>n</strong> comparisons for n elements</span></li>
      <li><span class="num">2</span><span>Binary search, worst case: roughly <strong>log&#8322;(n)</strong> &mdash; each comparison halves the data</span></li>
    </ul></div>''',
        "speak": "Why is binary search so much faster? Linear search's worst case takes n comparisons for n elements. Binary search's worst case only takes roughly log base two of n, because each comparison eliminates half the remaining data, not just one element.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Worst-Case Comparisons</div>
    <div class="scr-naming">
      <div class="namerow"><code>n = 8</code><span class="nlabel">linear: 8 &nbsp;&middot;&nbsp; binary: 4</span></div>
      <div class="namerow"><code>n = 16</code><span class="nlabel">linear: 16 &nbsp;&middot;&nbsp; binary: 5</span></div>
      <div class="namerow"><code>n = 100</code><span class="nlabel">linear: 100 &nbsp;&middot;&nbsp; binary: 7</span></div>
      <div class="namerow"><code>n = 500</code><span class="nlabel">linear: 500 &nbsp;&middot;&nbsp; binary: ~9</span></div>
    </div>''',
        "speak": "Here are the numbers. Eight elements: linear search takes eight comparisons, binary search takes four. Sixteen elements: sixteen, versus five. A hundred: a hundred, versus seven. And five hundred: five hundred, versus about nine.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Growth Rate</h2><ul>
      <li><span class="num">1</span><span>Double the data: linear does twice the work, binary does <em>one more</em> comparison</span></li>
      <li><span class="num">2</span><span>O(n) vs. O(log n) &mdash; why frequently-searched data is worth keeping sorted</span></li>
    </ul></div>''',
        "speak": "Doubling the data size costs linear search twice the work, but only costs binary search one more comparison. In formal terms, that's big O of n, versus big O of log n. And that growth-rate difference is exactly why sorted, frequently searched data, like a large lookup table, or a big sorted config file, is worth keeping sorted, specifically so binary search stays available.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Running binary search on unsorted data &mdash; it returns wrong or missing results.</li>
      <li><span class="check">!</span>Assuming binary search requires integers &mdash; anything with an ordering works, Strings via compareTo.</li>
      <li><span class="check">!</span>Forgetting the loop-ending condition &mdash; while (left &lt;= right) must end a not-found search, not loop forever.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Running binary search on unsorted data. It'll return wrong or missing results, because its entire correctness depends on the data already being sorted. Assuming binary search requires integers. It works on anything with a well-defined ordering, Strings through compare to, for instance. And forgetting the loop-ending condition. While left is less than or equal to right stops the moment the range is exhausted, and a search for something that isn't there still has to terminate, not loop forever.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Linear search checks every element in order &mdash; worst case, all n of them.</li>
      <li><span class="check">&#10003;</span>Binary search needs sorted data, but halves the range each comparison &mdash; roughly log&#8322;(n) worst case.</li>
      <li><span class="check">&#10003;</span>Compare Strings with .equals() and compareTo(), never == or &lt; and &gt;.</li>
      <li><span class="check">&#10003;</span>That growth-rate gap is why frequently-searched data is worth keeping sorted.</li>
    </ul></div>''',
        "speak": "So, to recap. Linear search checks every element in order, and its worst case, not found, means checking all n elements. Binary search only works on sorted data, but eliminates half the remaining range with each comparison, roughly log base two of n comparisons in the worst case, vastly faster for large data sets. For Strings, in either algorithm, use dot equals and compare to, never double equals, less-than, or greater-than. And the gap between those two growth rates is exactly why sorted data is worth maintaining when it's searched often. Next up, lesson 28.2: sorting, how to get data sorted in the first place.",
    },
]
