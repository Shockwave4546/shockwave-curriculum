BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>HashMap</h1>
      <p class="scr-sub">A real dictionary &mdash; unique keys mapped to values.</p>
    </div>''',
        "speak": "This one's not on the AP exam, but it's genuinely useful, shows up in real code constantly, and later chapters build right on top of it, so it earns its own full lesson here. Hash map stores pairs, each unique key maps to a value, exactly like a real dictionary maps a word to its definition.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">import</span> java.util.HashMap;

<span class="t">HashMap</span>&lt;<span class="t">Integer</span>, <span class="t">Double</span>&gt; motorOffsets = <span class="k">new</span> <span class="t">HashMap</span>&lt;<span class="t">Integer</span>, <span class="t">Double</span>&gt;();
motorOffsets.put(<span class="n">5</span>, <span class="n">0.02</span>);   <span class="c">// CAN ID 5's calibration offset is 0.02</span>
motorOffsets.put(<span class="n">6</span>, -<span class="n">0.01</span>);

<span class="k">double</span> offset = motorOffsets.get(<span class="n">5</span>); <span class="c">// 0.02</span></code></pre>''',
        "speak": "Put, key then value, adds or replaces a pair. Get, given a key, hands back its value. Here, hash map maps a whole number CAN ID to that motor's own calibration offset, put once per motor, and get whenever you need to look one up later.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">key: 5</div><div class="darrow">&rarr;</div><div class="dbox active">value: 0.02</div>
    </div>
    <div class="scr-diagram" style="margin-top:10px;">
      <div class="dbox">key: 6</div><div class="darrow">&rarr;</div><div class="dbox active">value: -0.01</div>
    </div>''',
        "speak": "Arrays and array list are naturally indexed by position, 0, 1, 2, and so on. Hash map is for when the natural index is something else entirely, a name, an ID number, a label, and you'd rather look values up by that instead of by position.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">HashMap</span>&lt;<span class="t">String</span>, <span class="t">String</span>&gt; subsystemStatus = <span class="k">new</span> <span class="t">HashMap</span>&lt;<span class="t">String</span>, <span class="t">String</span>&gt;();
subsystemStatus.put(<span class="s">"Intake"</span>, <span class="s">"Ready"</span>);
subsystemStatus.put(<span class="s">"Shooter"</span>, <span class="s">"Spinning Up"</span>);</code></pre>''',
        "speak": "Here's exactly that, a subsystem's name as the key, its current status as the value. No position involved anywhere, you look things up by name.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="t">String</span> name : subsystemStatus.keySet())
{
    <span class="t">String</span> status = subsystemStatus.get(name);
    System.out.println(name + <span class="s">": "</span> + status);
}</code></pre>''',
        "speak": "To loop through every pair, key set hands you every key that's currently stored, and inside the loop, get retrieves each one's value in turn. That's the for-each loop form, lesson 9.4 covers it in full, but the short version here, it just visits every key in turn, no index needed. That combination, key set plus get, is the standard way to walk an entire hash map.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Other Useful Methods</h2><ul>
      <li><span class="num">1</span><span>containsKey(key) &mdash; true if that key has a value, no risk of a null get().</span></li>
      <li><span class="num">2</span><span>getOrDefault(key, fallback) &mdash; returns fallback instead of null on a miss.</span></li>
      <li><span class="num">3</span><span>remove(key) and size() round out the common operations.</span></li>
    </ul></div>''',
        "speak": "A few more methods worth knowing. Contains key tells you whether a key has a value at all, with no risk of getting null back. Get or default works like get, but hands you a fallback value instead of null the moment a key is missing. And remove and size do exactly what they sound like, delete a pair by key, and report how many pairs the map holds.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assuming a HashMap remembers insertion order &mdash; it doesn't guarantee any particular order.</li>
      <li><span class="check">!</span>Calling get() with a key that was never put() &mdash; returns null, which throws once unboxed into a primitive.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Don't assume hash map remembers the order you put things in, unlike array list, looping through key set gives you no guaranteed order at all. And calling get with a key that was never put returns null, not an error right at that line, but if the value type is a primitive wrapper, like those Double offsets from earlier, assigning that null into a double unboxes it and throws a Null Pointer Exception right there. Check with contains key or get or default whenever a lookup might legitimately come up empty.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A HashMap stores unique keys mapped to values.</li>
      <li><span class="check">&#10003;</span>put(key, value) adds or replaces a pair; get(key) retrieves it.</li>
      <li><span class="check">&#10003;</span>Reach for a HashMap when you naturally look things up by name or ID, not position.</li>
      <li><span class="check">&#10003;</span>keySet() gives every key, for looping through all pairs with get() (Ch.9.4).</li>
      <li><span class="check">&#10003;</span>get() on a missing key returns null, which throws once unboxed &mdash; check with containsKey()/getOrDefault().</li>
    </ul></div>''',
        "speak": "So, to recap. Hash map stores unique keys mapped to values. Put adds or replaces a pair, get retrieves one. Reach for a hash map when you naturally look things up by name or ID rather than by position. Key set gives you every key, for looping through the whole thing with get. And get on a missing key returns null, which throws the moment it's unboxed into a primitive, so check with contains key or get or default instead. Next up, lesson 9.4, traversing arrays properly with loops.",
    },
]
