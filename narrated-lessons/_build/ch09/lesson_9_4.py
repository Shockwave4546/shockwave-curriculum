BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>Array Traversals</h1>
      <p class="scr-sub">Visiting every element of an array, the right way.</p>
    </div>''',
        "speak": "An array is only useful once you can actually walk through it. Traversing an array means visiting its elements, almost always with a loop, and the loop variable does double duty as the index.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span>[] sensorReadings = {<span class="n">2.1</span>, <span class="n">2.4</span>, <span class="n">1.9</span>, <span class="n">2.2</span>};
<span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; sensorReadings.length; i++)
{
    System.out.println(sensorReadings[i]);
}</code></pre>''',
        "speak": "Writing the loop bound against dot length, not some hardcoded number, means this exact same code keeps working no matter how many elements the array actually ends up having.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static void</span> zeroOut(<span class="k">double</span>[] values)
{
    <span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; values.length; i++)
    {
        values[i] = <span class="n">0.0</span>; <span class="c">// this really does change the caller's array</span>
    }
}</code></pre>''',
        "speak": "Remember, an array is an object, so passing one into a method passes its reference. Changes a method makes to the array's actual contents are visible back in the caller too, exactly like any mutable object from Chapter 7. Zero out here really does zero out the caller's real array, not some throwaway local copy.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">double</span> reading : sensorReadings)
{
    System.out.println(reading);
}</code></pre>''',
        "speak": "When you just need every value, with no index and no plan to change any elements, the enhanced for-each form is simpler. It's genuinely equivalent to an indexed loop, it always starts at index 0 and runs through every element in order, just more concise when the index itself isn't something you need.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What For-Each Can't Do</h2><ul>
      <li><span class="num">1</span><span>Can't modify a primitive array's elements &mdash; the loop variable is only a copy.</span></li>
    </ul></div>''',
        "speak": "For-each has real limits though, worth knowing up front. First, it can't modify a primitive array's elements, assigning to the loop variable only changes a local copy, never the real array.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What For-Each Can't Do</h2><ul>
      <li><span class="num">1</span><span>Can't modify a primitive array's elements &mdash; the loop variable is only a copy.</span></li>
      <li><span class="num">2</span><span>Can't get the index &mdash; if you need to know where something is, use an indexed loop.</span></li>
    </ul></div>''',
        "speak": "Second, it can't hand you the index at all, if you ever need to know where something sits, you're back to an indexed loop.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What For-Each Can't Do</h2><ul>
      <li><span class="num">1</span><span>Can't modify a primitive array's elements &mdash; the loop variable is only a copy.</span></li>
      <li><span class="num">2</span><span>Can't get the index &mdash; if you need to know where something is, use an indexed loop.</span></li>
      <li><span class="num">3</span><span>Can't skip around or go partway &mdash; always visits every element, front to back.</span></li>
    </ul></div>''',
        "speak": "And third, it can't skip around or stop partway, it always visits every element, front to back, no exceptions.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Off-by-one on the loop bound &mdash; less-than-or-equal reads one iteration too many.</li>
      <li><span class="check">!</span>Expecting a for-each loop to change array values &mdash; it compiles, runs, and does nothing.</li>
      <li><span class="check">!</span>Returning "not found" too early in a search &mdash; must check every element first.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Watch the off-by-one on the loop bound, less-than-or-equal-to reads one iteration too many, and throws an Array Index Out Of Bounds Exception, the correct bound is always strictly less-than. Don't expect a for-each loop to change array values, assigning to the loop variable compiles, runs, and does absolutely nothing to the real array. And in a search, don't return not-found too early, a search has to check every single element before it can honestly conclude something isn't there.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Traversing means looping index by index, with the bound written against .length.</li>
      <li><span class="check">&#10003;</span>Arrays are objects &mdash; a method that changes array elements changes the caller's real array too.</li>
      <li><span class="check">&#10003;</span>For-each is simpler when you don't need the index and won't modify elements.</li>
      <li><span class="check">&#10003;</span>For-each cannot modify primitive elements or provide the index.</li>
    </ul></div>''',
        "speak": "So, to recap. Traversing an array means looping through it index by index, with the bound always written against dot length. Arrays are objects, so a method that changes array elements changes the caller's real array too. For-each is simpler whenever you don't need the index and won't modify elements. And for-each can't modify primitive elements or hand you the index, that's when you fall back to an indexed loop. Next up, lesson 9.5, putting all of this to work in real array algorithms.",
    },
]
