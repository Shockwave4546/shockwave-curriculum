BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>Optional: HashMap</h1>
      <p class="scr-sub">A real dictionary &mdash; unique keys mapped to values.</p>
    </div>''',
        "speak": "This one's marked optional, it's not on the AP exam, but it's genuinely useful and shows up in real code constantly, so it earns its own lesson. Hash map stores pairs, each unique key maps to a value, exactly like a real dictionary maps a word to its definition.",
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
        "speak": "To loop through every pair, key set hands you every key that's currently stored, and inside the loop, get retrieves each one's value in turn. That combination, key set plus get, is the standard way to walk an entire hash map.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assuming a HashMap remembers insertion order &mdash; it doesn't guarantee any particular order.</li>
      <li><span class="check">!</span>Calling get() with a key that was never put() &mdash; returns null rather than throwing an error.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Don't assume hash map remembers the order you put things in, unlike array list, looping through key set gives you no guaranteed order at all. And calling get with a key that was never put returns null rather than throwing an error, so check for that if a lookup might legitimately come up empty.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A HashMap stores unique keys mapped to values.</li>
      <li><span class="check">&#10003;</span>put(key, value) adds or replaces a pair; get(key) retrieves it.</li>
      <li><span class="check">&#10003;</span>Reach for a HashMap when you naturally look things up by name or ID, not position.</li>
      <li><span class="check">&#10003;</span>keySet() gives every key, for looping through all pairs with get().</li>
    </ul></div>''',
        "speak": "So, to recap. Hash map stores unique keys mapped to values. Put adds or replaces a pair, get retrieves one. Reach for a hash map when you naturally look things up by name or ID rather than by position. And key set gives you every key, for looping through the whole thing with get. Next up, lesson 9.4, traversing arrays properly with loops.",
    },
]
