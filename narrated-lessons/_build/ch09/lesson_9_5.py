BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>Implementing Array Algorithms</h1>
      <p class="scr-sub">A handful of loop-plus-bookkeeping patterns cover almost everything.</p>
    </div>''',
        "speak": "A small set of patterns, each just a loop plus a little bookkeeping, covers almost everything you'll ever want to do with an array. Let's go through them one at a time.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> sum = <span class="n">0</span>;
<span class="k">for</span> (<span class="k">double</span> reading : sensorReadings)
{
    sum += reading;
}
<span class="k">double</span> average = sum / sensorReadings.length;</code></pre>''',
        "speak": "First, the accumulator pattern, for a sum or an average. Start a running total at 0, add every element to it inside the loop, and divide by the count once you're done.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> max = sensorReadings[<span class="n">0</span>]; <span class="c">// seed with the first element, not 0 — a reading could be negative</span>
<span class="k">for</span> (<span class="k">double</span> reading : sensorReadings)
{
    <span class="k">if</span> (reading &gt; max)
    {
        max = reading;
    }
}</code></pre>''',
        "speak": "Min and max work the same way, but pay close attention to how you seed the starting value. Seed it with the actual first element, not 0, because a real reading could easily be negative, and 0 would be a wrong starting point that never gets corrected.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static boolean</span> contains(<span class="k">double</span>[] values, <span class="k">double</span> target)
{
    <span class="k">for</span> (<span class="k">double</span> v : values)
    {
        <span class="k">if</span> (v == target)
        {
            <span class="k">return true</span>; <span class="c">// fine to return early on a MATCH</span>
        }
    }
    <span class="k">return false</span>; <span class="c">// only after checking every element</span>
}</code></pre>''',
        "speak": "Search has a rule that trips people up constantly: it's fine to return early the instant you find a match, but you can only return not-found after the loop has genuinely checked every single element. Returning false from inside the loop, on the first non-match, only ever actually checks the first element.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> i = values.length - <span class="n">1</span>; i &gt;= <span class="n">0</span>; i--)
{
    <span class="c">// process values[i], starting from the end</span>
}</code></pre>''',
        "speak": "The exact same shape works running backward, just start the counter at length minus 1 and count down to 0 instead of up.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// at least one has the property</span>
<span class="k">for</span> (<span class="k">double</span> v : values) { <span class="k">if</span> (isFaulty(v)) <span class="k">return true</span>; }
<span class="k">return false</span>;

<span class="c">// all have the property (check the NEGATION, bail early on a counter-example)</span>
<span class="k">for</span> (<span class="k">double</span> v : values) { <span class="k">if</span> (!isFaulty(v)) <span class="k">return false</span>; }
<span class="k">return true</span>;

<span class="c">// count how many have the property</span>
<span class="k">int</span> count = <span class="n">0</span>;
<span class="k">for</span> (<span class="k">double</span> v : values) { <span class="k">if</span> (isFaulty(v)) count++; }</code></pre>''',
        "speak": "Three closely related patterns. At least one has some property, return true the moment you find one, and only fall through to false at the very end. All have the property, flip it around, check the negation, and bail out false the instant you find a single counter-example. And counting how many have the property is just the accumulator pattern again, with a counter instead of a sum.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; values.length - <span class="n">1</span>; i++)
{
    <span class="k">if</span> (values[i] == values[i + <span class="n">1</span>]) <span class="k">return true</span>;
}</code></pre>''',
        "speak": "Checking for duplicates sitting right next to each other is a single loop comparing each element to its neighbor. Notice the bound, length minus 1, not length, comparing the last element to one past the end would run off the array entirely.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; values.length; i++)
{
    <span class="k">for</span> (<span class="k">int</span> j = i + <span class="n">1</span>; j &lt; values.length; j++)
    {
        <span class="k">if</span> (values[i] == values[j]) <span class="k">return true</span>;
    }
}</code></pre>''',
        "speak": "But duplicates could be anywhere, not just next to each other, and catching that needs a nested loop, comparing every single pair. j always starts one past i, so no pair ever gets compared against itself, or checked twice.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> start = <span class="n">0</span>, end = values.length - <span class="n">1</span>;
<span class="k">while</span> (start &lt; end)
{
    <span class="k">double</span> temp = values[start];
    values[start] = values[end];
    values[end] = temp;
    start++;
    end--;
}</code></pre>''',
        "speak": "And reversing in place, swap from both ends working toward the middle. A temporary variable holds one value while it's overwritten, without it, that value would just be lost the moment you assigned over it.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Seeding min/max with 0 instead of the first element.</li>
      <li><span class="check">!</span>Returning "not found" from inside the loop, before every element's been checked.</li>
      <li><span class="check">!</span>Comparing values[i] to values[i+1] all the way to the last index &mdash; reads one past the end.</li>
    </ul></div>''',
        "speak": "Three pitfalls to keep in mind. Don't seed min or max with 0, if every real value happens to be negative, or all sit above some baseline, 0 is simply the wrong starting point. Don't return not-found from inside the loop, only a genuine match should return early, not-found has to wait for the loop to finish. And don't let an adjacent-duplicate check compare all the way to the very last index, that reads one element past the end, the loop has to stop at length minus 2.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Sum/average, min/max, search, and counting are all a loop plus a little state.</li>
      <li><span class="check">&#10003;</span>A "not found" search must check every element; a match can return the instant it's found.</li>
      <li><span class="check">&#10003;</span>Adjacent-duplicate checks are one loop; any-pair checks need a nested loop.</li>
      <li><span class="check">&#10003;</span>Reversing in place swaps from both ends toward the middle.</li>
    </ul></div>''',
        "speak": "So, to recap. Sum, average, min, max, search, and counting are all the exact same basic shape, a loop plus a little bit of state. A not-found search must check every element first; a match can return the instant it's found. Adjacent-duplicate checks are a single loop; checking for duplicates anywhere needs a nested one. And reversing in place swaps from both ends toward the middle, using a temporary variable. Next up, lesson 9.6, the same ideas, but on array list.",
    },
]
