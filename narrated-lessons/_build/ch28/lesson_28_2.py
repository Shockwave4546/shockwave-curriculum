BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 28 &middot; Algorithms: Searching, Sorting &amp; Recursion</div>
      <h1>Sorting Algorithms</h1>
      <p class="scr-sub">Two ways to put data in order &mdash; and why the starting order matters.</p>
    </div>''',
        "speak": "Another optional lesson. Why sort at all? Binary search, from lesson 28.1, needs sorted data to work. And sorted match scouting data, sensor logs, or leaderboard scores are simply easier for a human to read. Two straightforward sorting algorithms cover the core idea here. A third, more efficient one, merge sort, is covered in lesson 28.4.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Selection Sort</h2><ul>
      <li><span class="num">1</span><span>Find the smallest remaining value, and swap it into its final position</span></li>
    </ul></div>''',
        "speak": "Selection sort repeatedly finds the smallest remaining value, and swaps it into its correct, final position.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Selection Sort</h2><ul>
      <li><span class="num">1</span><span>Find the smallest remaining value, and swap it into its final position</span></li>
      <li><span class="num">2</span><span>Position 0 first, then position 1, and so on</span></li>
    </ul></div>''',
        "speak": "First position zero, then position one, and so on, until the whole array is in order.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="k">void</span> <span class="me">selectionSort</span>(<span class="t">double</span>[] sensorReadings)
{
    <span class="k">for</span> (<span class="t">int</span> j = <span class="n">0</span>; j &lt; sensorReadings.length - <span class="n">1</span>; j++)
    {
        <span class="t">int</span> minIndex = j; <span class="c">// assume the current position holds the smallest remaining value</span>
        <span class="k">for</span> (<span class="t">int</span> k = j + <span class="n">1</span>; k &lt; sensorReadings.length; k++)
        {
            <span class="k">if</span> (sensorReadings[k] &lt; sensorReadings[minIndex])
            {
                minIndex = k; <span class="c">// found something smaller &mdash; remember its index</span>
            }
        }</code></pre>''',
        "speak": "The outer loop, j, tracks which position is being filled next. Min index starts out as j, assuming the current position holds the smallest remaining value. Then the inner loop, k, scans everything after it, and any time it finds something smaller, it remembers that index.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">selectionSort, continued</div>
    <pre class="code"><code>        <span class="t">double</span> temp = sensorReadings[j];
        sensorReadings[j] = sensorReadings[minIndex];
        sensorReadings[minIndex] = temp;
    }
}</code></pre>''',
        "speak": "Then comes the swap. Save the value at j in temp, move the minimum into position j, and put temp where the minimum used to be. Position j now holds its final value.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">How Selection Sort Works</h2><ul>
      <li><span class="num">1</span><span>The exact findMin pattern from Ch.9.5 &mdash; done once per position</span></li>
      <li><span class="num">2</span><span>Inner loop starts at <strong>j + 1</strong> &mdash; everything before j is already sorted</span></li>
    </ul></div>''',
        "speak": "This is the exact find min pattern from lesson 9.5, just done once per position. The outer loop tracks which position is being filled next, and the inner loop always starts at j plus one, since everything before j is already sorted, and shouldn't be re-scanned.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">How Selection Sort Works</h2><ul>
      <li><span class="num">1</span><span>The exact findMin pattern from Ch.9.5 &mdash; done once per position</span></li>
      <li><span class="num">2</span><span>Inner loop starts at <strong>j + 1</strong> &mdash; everything before j is already sorted</span></li>
      <li><span class="num">3</span><span>Same work regardless of the data&rsquo;s initial order</span></li>
    </ul></div>''',
        "speak": "And selection sort takes the same amount of work regardless of the data's initial order. It always scans the entire unsorted remainder to find the minimum, every single pass.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Insertion Sort</h2><ul>
      <li><span class="num">1</span><span>Take each element and insert it among the already-sorted elements to its left</span></li>
    </ul></div>''',
        "speak": "Insertion sort works differently. It takes each element, and inserts it into its correct position among the already-sorted elements to its left.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Insertion Sort</h2><ul>
      <li><span class="num">1</span><span>Take each element and insert it among the already-sorted elements to its left</span></li>
      <li><span class="num">2</span><span>Shift larger values right to make room</span></li>
    </ul></div>''',
        "speak": "To make room, it shifts the larger values one spot to the right.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="k">void</span> <span class="me">insertionSort</span>(<span class="t">double</span>[] sensorReadings)
{
    <span class="k">for</span> (<span class="t">int</span> j = <span class="n">1</span>; j &lt; sensorReadings.length; j++)
    {
        <span class="t">double</span> temp = sensorReadings[j];
        <span class="t">int</span> possibleIndex = j;</code></pre>''',
        "speak": "The outer loop starts at index one. Each pass copies the current element into temp, and possible index starts at j, the spot temp might end up in.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">insertionSort, continued</div>
    <pre class="code"><code>        <span class="k">while</span> (possibleIndex &gt; <span class="n">0</span> &amp;&amp; temp &lt; sensorReadings[possibleIndex - <span class="n">1</span>])
        {
            sensorReadings[possibleIndex] = sensorReadings[possibleIndex - <span class="n">1</span>]; <span class="c">// shift right</span>
            possibleIndex--;
        }
        sensorReadings[possibleIndex] = temp; <span class="c">// place temp in its final spot for this pass</span>
    }
}</code></pre>''',
        "speak": "The while loop keeps going as long as there's still room to the left, and temp is smaller than the element there. Each time, that larger element shifts right one spot, and possible index moves left. When the loop stops, temp drops into its final spot for this pass.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Insertion Sort Is Adaptive</h2><ul>
      <li><span class="num">1</span><span>Already (or nearly) sorted: the while condition fails almost immediately</span></li>
    </ul></div>''',
        "speak": "Unlike selection sort, insertion sort is adaptive. If the data is already sorted, or nearly sorted, the while loop's condition fails almost immediately for most elements, so it does very little actual shifting.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Insertion Sort Is Adaptive</h2><ul>
      <li><span class="num">1</span><span>Already (or nearly) sorted: the while condition fails almost immediately</span></li>
      <li><span class="num">2</span><span>Sorted descending: the worst case &mdash; every element shifts all the way to the front</span></li>
    </ul></div>''',
        "speak": "Data that's already sorted in descending order is insertion sort's worst case, since every element has to shift all the way to the front.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Comparing the Two</h2><ul>
      <li><span class="num">1</span><span>Both: roughly <strong>n&sup2;</strong> comparisons for n elements, in the worst case</span></li>
    </ul></div>''',
        "speak": "Both algorithms have similar overall growth, roughly n squared comparisons for n elements, in the worst case. But they behave differently depending on the input.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Selection vs. Insertion</div>
    <div class="scr-naming">
      <div class="namerow"><code>sorted ascending</code><span class="nlabel">selection: no speedup &nbsp;&middot;&nbsp; insertion: much faster</span></div>
      <div class="namerow"><code>sorted descending</code><span class="nlabel">selection: no speedup &nbsp;&middot;&nbsp; insertion: worst case</span></div>
      <div class="namerow"><code>typical use</code><span class="nlabel">selection: predictable cost &nbsp;&middot;&nbsp; insertion: mostly-sorted data</span></div>
    </div>''',
        "speak": "Already sorted ascending? Selection sort gets no speedup, it's the same work every time, while insertion sort is much faster, because it's adaptive. Already sorted descending? Selection sort, still no change. Insertion sort, worst case, maximum shifting. So selection sort is simple, with a predictable cost, and insertion sort is a good fit when the data's already mostly sorted.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Starting selection sort&rsquo;s inner loop at 0 instead of j + 1 &mdash; it re-scans, and can undo, already-placed elements.</li>
      <li><span class="check">!</span>Stopping insertion sort&rsquo;s outer loop at length - 1 &mdash; the last element never gets inserted.</li>
      <li><span class="check">!</span>Assuming input order affects both the same way &mdash; selection&rsquo;s cost is fixed; insertion&rsquo;s isn&rsquo;t.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Starting selection sort's inner loop at index zero, instead of j plus one. That re-scans, and can even undo, elements already placed correctly in earlier passes. Stopping insertion sort's outer loop one element too early. It has to run through the entire array, j less than length, not length minus one, or the very last element never gets inserted into its sorted position. And assuming input order affects both algorithms the same way. Selection sort's cost is fixed regardless of order, and insertion sort's genuinely isn't. That's the entire point of calling it adaptive.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Selection sort: swap the minimum of the unsorted remainder into place &mdash; same cost regardless of order.</li>
      <li><span class="check">&#10003;</span>Insertion sort: insert each element among the sorted ones to its left &mdash; adaptive, fast on nearly-sorted data.</li>
      <li><span class="check">&#10003;</span>Both are roughly n&sup2; worst case, but real performance depends on how sorted the input already is.</li>
      <li><span class="check">&#10003;</span>Sorted data unlocks binary search (Lesson 28.1).</li>
    </ul></div>''',
        "speak": "So, to recap. Selection sort repeatedly finds the minimum of the remaining unsorted portion and swaps it into place, at the same cost regardless of initial order. Insertion sort inserts each element into its correct position among the already-sorted elements to its left, shifting as needed. It's adaptive, and much faster on nearly-sorted data. Both run roughly n squared in the worst case, but real-world performance can differ a lot depending on how sorted the input already is. And sorted data unlocks binary search, from lesson 28.1, one reason sorting matters beyond just readability. Next up, lesson 28.3: recursion.",
    },
]
