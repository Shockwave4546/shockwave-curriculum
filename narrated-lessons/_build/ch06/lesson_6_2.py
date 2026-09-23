BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 6 &middot; Strings</div>
      <h1>String Algorithms</h1>
      <p class="scr-sub">Scanning, searching, and building strings with loops.</p>
    </div>''',
        "speak": "Last time we met the core string methods. Now let's put them inside loops, because that's where strings really come alive, scanning them character by character, finding and replacing text, and building brand new strings from scratch.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> autoName = <span class="s">"BlueAlliance-Left"</span>;
<span class="k">int</span> dashCount = <span class="n">0</span>;
<span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; autoName.length(); i++)
{
    <span class="k">if</span> (autoName.substring(i, i + <span class="n">1</span>).equals(<span class="s">"-"</span>))
    {
        dashCount++;
    }
}</code></pre>''',
        "speak": "A for loop is the standard way to visit every character of a string. Start the loop variable at 0, and stop before length, so it never runs off the end. Here, i does double duty, it's the loop counter, and it's also the index we hand to sub string, pulling out one character at a time to check against a dash.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">For vs. While, for Strings</h2><ul>
      <li><span class="num">1</span><span>Use a <strong>for</strong> loop when you know you want to check every character.</span></li>
    </ul></div>''',
        "speak": "That raises a question worth pausing on: when do you reach for a for loop versus a while loop on a string? Use a for loop whenever you know up front that you want to check every single character, exactly like the dash-counting example.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">For vs. While, for Strings</h2><ul>
      <li><span class="num">1</span><span>Use a <strong>for</strong> loop when you know you want to check every character.</span></li>
      <li><span class="num">2</span><span>Use a <strong>while</strong> loop when you're searching, and don't know in advance how many characters you'll need.</span></li>
    </ul></div>''',
        "speak": "Use a while loop instead when you're searching for something and you genuinely don't know in advance how many characters it'll take to find it, or how many times you'll need to repeat the search. That's exactly the shape of the find-and-replace pattern, coming up next.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> name = <span class="s">"Alli1ance"</span>;
<span class="k">int</span> i = <span class="n">0</span>;
<span class="k">while</span> (name.indexOf(<span class="s">"1"</span>) &gt;= <span class="n">0</span>)
{
    i = name.indexOf(<span class="s">"1"</span>);
    <span class="t">String</span> firstPart = name.substring(<span class="n">0</span>, i);
    <span class="t">String</span> lastPart = name.substring(i + <span class="n">1</span>);
    name = firstPart + <span class="s">"l"</span> + lastPart; <span class="c">// replace the "1" with "l"</span>
}</code></pre>''',
        "speak": "Here's find-and-replace, pairing a while loop with index of. As long as index of still finds a match, keep going. Each pass, split the string into the part before the match and the part after it, then glue them back together with the replacement text in between.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">name</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox active">reassigned</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox">search again</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Each pass searches against the current, already-updated value of name.</p>''',
        "speak": "The key thing to notice: each pass finds the next occurrence, because name was already reassigned at the end of the previous pass. The while loop's condition always runs its search against whatever name currently holds, not whatever it held when the loop started.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> reversed = <span class="s">""</span>;
<span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; autoName.length(); i++)
{
    <span class="t">String</span> letter = autoName.substring(i, i + <span class="n">1</span>);
    reversed = letter + reversed; <span class="c">// prepend — builds the string backwards</span>
}</code></pre>''',
        "speak": "Since strings can't be changed in place, building one really means starting from an empty string and concatenating onto it inside a loop. Here's a nice trick, to reverse a string, prepend each letter instead of appending it, put the new letter in front of what's already been built, and the whole thing comes out backwards.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Starting a string-scanning loop at 1 instead of 0 &mdash; the first character always sits at index 0.</li>
      <li><span class="check">!</span>Using less-than-or-equal instead of less-than against length &mdash; that reads one index past the end.</li>
      <li><span class="check">!</span>An infinite loop in find-and-replace, if the replacement text still contains what you searched for.</li>
    </ul></div>''',
        "speak": "A few pitfalls to watch for. Don't start a string-scanning loop at 1, the first character is always at index 0, and starting at 1 quietly skips it. Don't use less-than-or-equal-to against length, only strictly less-than, one index past the end throws an Index Out Of Bounds Exception. And watch for an infinite loop in a find-and-replace pattern, if what you're replacing something with still contains the thing you searched for, index of will keep finding it forever.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>For loops fit scanning every character; while loops fit searching for an unknown number of matches.</li>
      <li><span class="check">&#10003;</span>Find-and-replace combines index of (to locate) with sub string (to rebuild around the match).</li>
      <li><span class="check">&#10003;</span>Building a new string means starting empty and concatenating inside a loop.</li>
    </ul></div>''',
        "speak": "So, to recap. For loops fit scanning every character of a string; while loops fit searching for some unknown number of matches. A find-and-replace loop combines index of, to locate the match, with sub string, to rebuild around it, reassigning the string every single pass. And building a brand new string always means starting empty and concatenating inside a loop, since strings themselves can never be modified in place. Next up, Chapter 7, where we start writing our own classes from scratch.",
    },
]
