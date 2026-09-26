BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 28 &middot; Algorithms: Searching, Sorting &amp; Recursion</div>
      <h1>Recursive Searching and Sorting</h1>
      <p class="scr-sub">The same searching and sorting ideas &mdash; rewritten recursively.</p>
    </div>''',
        "speak": "This optional lesson combines lessons 28.1 through 28.3: the same searching and sorting ideas, rewritten recursively.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Recursive Binary Search</h2><ul>
      <li><span class="num">1</span><span>Iterative version: the left/right bounds live in loop variables</span></li>
    </ul></div>''',
        "speak": "The iterative binary search from lesson 28.1 tracks its left and right bounds in loop variables.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Recursive Binary Search</h2><ul>
      <li><span class="num">1</span><span>Iterative version: the left/right bounds live in loop variables</span></li>
      <li><span class="num">2</span><span>Recursive version: the shrinking range is passed as parameters</span></li>
    </ul></div>''',
        "speak": "A recursive version instead passes the shrinking range as parameters, and the range itself does the job the while loop's condition did before.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="t">int</span> <span class="me">recursiveBinarySearch</span>(<span class="t">int</span>[] elements, <span class="t">int</span> start, <span class="t">int</span> end, <span class="t">int</span> target)
{
    <span class="k">if</span> (end &lt; start)                          <span class="c">// base case 1: range is empty &mdash; not found</span>
    {
        <span class="k">return</span> -<span class="n">1</span>;
    }
    <span class="t">int</span> middle = (start + end) / <span class="n">2</span>;
    <span class="k">if</span> (target == elements[middle])            <span class="c">// base case 2: found it</span>
    {
        <span class="k">return</span> middle;
    }</code></pre>''',
        "speak": "Base case one: if end is less than start, the range is empty, so the target isn't here. Return negative one. Otherwise, compute the middle. Base case two: if the target equals the middle element, we found it. Return middle.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">recursiveBinarySearch, continued</div>
    <pre class="code"><code>    <span class="k">else</span> <span class="k">if</span> (target &lt; elements[middle])
    {
        <span class="c">// search the left half</span>
        <span class="k">return</span> <span class="me">recursiveBinarySearch</span>(elements, start, middle - <span class="n">1</span>, target);
    }
    <span class="k">else</span>
    {
        <span class="c">// search the right half</span>
        <span class="k">return</span> <span class="me">recursiveBinarySearch</span>(elements, middle + <span class="n">1</span>, end, target);
    }
}</code></pre>''',
        "speak": "If neither base case hits, recurse into half the range. A smaller target searches the left half, start through middle minus one. A larger one searches the right half, middle plus one through end. Either way, each call passes a smaller range to the next one.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Base Cases</h2><ul>
      <li><span class="num">1</span><span>A match at the middle &mdash; or an exhausted range</span></li>
      <li><span class="num">2</span><span>Remove the <strong>end &lt; start</strong> check, and a not-found search crashes with StackOverflowError</span></li>
    </ul></div>''',
        "speak": "So this method has two base cases: a match at the middle, or an exhausted range. Removing the end less than start check wouldn't cause a true infinite loop. Java would run out of room first. A not-found search keeps calling itself into an already-empty range until it crashes with a Stack Overflow Error, or, if the array is empty to begin with, an immediate Array Index Out Of Bounds Exception, exactly the missing base case bug from lesson 28.3.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Merge Sort: A Third Sorting Algorithm</h2><ul>
      <li><span class="num">1</span><span>Selection and insertion sort: roughly <strong>n&sup2;</strong> in the worst case</span></li>
    </ul></div>''',
        "speak": "Now, sorting. Selection sort and insertion sort, from lesson 28.2, both cost roughly n squared in the worst case.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Merge Sort: A Third Sorting Algorithm</h2><ul>
      <li><span class="num">1</span><span>Selection and insertion sort: roughly <strong>n&sup2;</strong> in the worst case</span></li>
      <li><span class="num">2</span><span>Merge sort: <strong>divide-and-conquer</strong>, like binary search &mdash; roughly <strong>n log n</strong></span></li>
    </ul></div>''',
        "speak": "Merge sort is a divide-and-conquer algorithm. Like binary search, it splits the problem in half repeatedly, which makes it substantially faster on large data, roughly n log n, instead of n squared.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">How Merge Sort Works</div>
    <div class="scr-steps">
      <div class="step"><span class="n">1</span><span>Split the array into two halves.</span></div>
      <div class="step"><span class="n">2</span><span>Recursively sort each half &mdash; a single-element array is already sorted, the base case.</span></div>
      <div class="step"><span class="n">3</span><span><strong>Merge</strong> the two sorted halves back together, in order.</span></div>
    </div>''',
        "speak": "It works in three steps. One: split the array into two halves. Two: recursively sort each half. A single-element array is trivially already sorted, and that's the base case. And three: merge the two now-sorted halves back together, in order.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="k">void</span> <span class="me">mergeSort</span>(<span class="t">int</span>[] elements)
{
    <span class="t">int</span> n = elements.length;
    <span class="t">int</span>[] temp = <span class="k">new</span> <span class="t">int</span>[n]; <span class="c">// scratch space used during merging</span>
    <span class="me">mergeSortHelper</span>(elements, <span class="n">0</span>, n - <span class="n">1</span>, temp);
}</code></pre>''',
        "speak": "In code, the public merge sort method just sets things up. It creates a temp array, the same length as the input, as scratch space for merging, then hands the whole range, zero through n minus one, to a helper.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">private</span> <span class="k">static</span> <span class="k">void</span> <span class="me">mergeSortHelper</span>(<span class="t">int</span>[] elements, <span class="t">int</span> from, <span class="t">int</span> to, <span class="t">int</span>[] temp)
{
    <span class="k">if</span> (from &gt;= to) <span class="k">return</span>; <span class="c">// base case: a range of 0 or 1 elements is already sorted</span>
    <span class="t">int</span> middle = (from + to) / <span class="n">2</span>;
    <span class="me">mergeSortHelper</span>(elements, from, middle, temp);      <span class="c">// recursively sort the left half</span>
    <span class="me">mergeSortHelper</span>(elements, middle + <span class="n">1</span>, to, temp);    <span class="c">// recursively sort the right half</span>
    <span class="me">merge</span>(elements, from, middle, to, temp);            <span class="c">// combine the two sorted halves</span>
}</code></pre>''',
        "speak": "The helper does the real work. Base case: if from is at least to, the range has zero or one elements, so it's already sorted. Otherwise, find the middle, recursively sort the left half, recursively sort the right half, and then merge the two sorted halves together.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">merge Isn&rsquo;t Recursive</div>
    <pre class="code"><code><span class="k">private</span> <span class="k">static</span> <span class="k">void</span> <span class="me">merge</span>(<span class="t">int</span>[] elements, <span class="t">int</span> from, <span class="t">int</span> mid, <span class="t">int</span> to, <span class="t">int</span>[] temp)
{
    <span class="t">int</span> i = from;     <span class="c">// next unmerged element in the left half</span>
    <span class="t">int</span> j = mid + <span class="n">1</span>;  <span class="c">// next unmerged element in the right half</span>
    <span class="t">int</span> k = from;     <span class="c">// next open slot in temp</span>

    <span class="k">while</span> (i &lt;= mid &amp;&amp; j &lt;= to)
    {
        <span class="k">if</span> (elements[i] &lt;= elements[j])
        {
            temp[k++] = elements[i++];
        }</code></pre>''',
        "speak": "Merge itself isn't recursive. It's the ordinary, loop-based step that does the actual combining, using temp as scratch space so it isn't overwriting values it still needs. Two pointers walk the sorted halves: i for the left half, j for the right. Every step, whichever pointer is looking at the smaller value gets copied into temp next.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">merge, continued</div>
    <pre class="code"><code>        <span class="k">else</span>
        {
            temp[k++] = elements[j++];
        }
    }
    <span class="k">while</span> (i &lt;= mid)   <span class="c">// copy over whatever's left of the left half</span>
    {
        temp[k++] = elements[i++];
    }
    <span class="k">while</span> (j &lt;= to)    <span class="c">// copy over whatever's left of the right half</span>
    {
        temp[k++] = elements[j++];
    }
    <span class="k">for</span> (<span class="t">int</span> m = from; m &lt;= to; m++) <span class="c">// copy the merged range back into elements</span>
    {
        elements[m] = temp[m];
    }
}</code></pre>''',
        "speak": "Once one half runs out, whatever's left of the other half is already in order, so it just gets copied straight over. Last step: copy the merged range from temp back into elements, since elements is the array being sorted in place.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Tracing {86, 3, 43, 5}</div>
    <pre class="code"><code>Split:  { {86, 3} , {43, 5} }
Split:  { { {86}, {3} } , { {43}, {5} } }   &lt;- single elements: base case reached
Merge:  { {3, 86} , {5, 43} }
Merge:  { 3, 5, 43, 86 }</code></pre>''',
        "speak": "Here's the split then merge structure, traced on eighty-six, three, forty-three, five. The first split makes two halves: eighty-six and three, and forty-three and five. The next split breaks those into single elements, and that's the base case. Then the merges: three, eighty-six, and five, forty-three. And the final merge gives three, five, forty-three, eighty-six.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">How Merge Sort Performs</h2><ul>
      <li><span class="num">1</span><span>Like selection sort, its structure doesn&rsquo;t depend on the input&rsquo;s initial order</span></li>
      <li><span class="num">2</span><span>Scales far better than n&sup2; &mdash; the fastest of the three, most of the time</span></li>
    </ul></div>''',
        "speak": "Like selection sort, merge sort's structure doesn't depend on the input's initial order. It always splits and merges the same way. But because its divide-and-conquer approach scales so much better than n squared sorting, it's the fastest of the three algorithms in this curriculum, most of the time, especially as the data set grows.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Iterative vs. Recursive</h2><ul>
      <li><span class="num">1</span><span>Binary search exists in both forms &mdash; many algorithms can be written either way</span></li>
    </ul></div>''',
        "speak": "Binary search exists in both forms: the iterative version from lesson 28.1, and this lesson's recursive one. That's a good concrete reminder of the point from lesson 28.3: many algorithms can be written either way.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Iterative vs. Recursive</h2><ul>
      <li><span class="num">1</span><span>Binary search exists in both forms &mdash; many algorithms can be written either way</span></li>
      <li><span class="num">2</span><span><strong>Iteration</strong>: usually preferred &mdash; no StackOverflowError risk, a bit more efficient</span></li>
      <li><span class="num">3</span><span><strong>Recursion</strong>: more compact &mdash; natural for divide-and-conquer, like merge sort</span></li>
    </ul></div>''',
        "speak": "Iteration is usually preferred in real code. There's no risk of a Stack Overflow Error, and it's generally a bit more efficient. But a recursive version can be more compact, and it can make a divide-and-conquer structure, like merge sort's, much more natural to express than an iterative equivalent would be.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting either base case in recursive binary search &mdash; no exhausted-range check risks infinite recursion.</li>
      <li><span class="check">!</span>Merging halves that aren&rsquo;t sorted yet &mdash; merge assumes both inputs already are.</li>
      <li><span class="check">!</span>Assuming recursive is always &ldquo;better&rdquo; than iterative, or vice versa &mdash; it&rsquo;s a real tradeoff.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Forgetting either base case in recursive binary search. Both the found it case and the range exhausted case are needed, and missing the exhausted range check risks infinite recursion on a not-found search. Merging without first making sure both halves are actually sorted. Merge sort's merge step assumes its two inputs are already individually sorted, and that's exactly what the recursive calls before it guarantee. And assuming recursive is always better than iterative, or the other way around. Each has real tradeoffs, stack depth risk versus code clarity, and the right choice depends on the specific algorithm and data size.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Recursive binary search passes a shrinking range as parameters &mdash; two base cases: a match, or an empty range.</li>
      <li><span class="check">&#10003;</span>Merge sort: split in half, recursively sort each half (base case: 1 element), then merge.</li>
      <li><span class="check">&#10003;</span>Merge sort scales better on large data &mdash; n log n vs. n&sup2; &mdash; regardless of initial order.</li>
      <li><span class="check">&#10003;</span>Iterative or recursive is a real tradeoff, not a universal &ldquo;better&rdquo; answer.</li>
    </ul></div>''',
        "speak": "So, to recap. Recursive binary search replaces loop-tracked bounds with a shrinking range passed as parameters, and it needs two base cases: a match, or an exhausted range. Merge sort is a recursive, divide-and-conquer sort: split in half, recursively sort each half, with one element as the base case, then merge the sorted halves back together. It scales better than selection or insertion sort on large data, n log n versus n squared, and its performance doesn't depend on the input's initial order. And the same algorithm can often be written iteratively or recursively. That choice is a real tradeoff, not a universal better answer either way.",
    },
]
