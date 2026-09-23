BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>ArrayList and its Methods</h1>
      <p class="scr-sub">Java's resizable alternative to the fixed-size array.</p>
    </div>''',
        "speak": "An array's size is fixed forever, the moment you create it. That's a problem whenever you don't know the final size up front, or items will be added and removed while the program's actually running, a growing log of events, for instance. That's exactly what array list is for.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">import</span> java.util.ArrayList;

<span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt; logs = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt;();
logs.add(<span class="s">"Robot Initialized"</span>);</code></pre>''',
        "speak": "Array list lives in java's util package, so it needs an import. Reach for it whenever the size isn't known up front, or will change at runtime.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">Double</span>&gt; sensorReadings = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">Double</span>&gt;();
sensorReadings.add(<span class="n">2.4</span>); <span class="c">// autoboxed into a Double automatically</span></code></pre>''',
        "speak": "The type in angle brackets says what kind of object the list holds. And that word object matters, array list can only hold objects, never primitives directly. A list of numbers uses the wrapper types, Integer or Double, and Java auto-converts back and forth for you, adding a plain 2.4 here automatically wraps it into a Double. That conversion is called autoboxing, going the other direction is unboxing.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt; logs = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt;();
logs.size();          <span class="c">// number of elements (like length, but a method — () required)</span>
logs.add(<span class="s">"started"</span>);  <span class="c">// appends to the end</span>
logs.add(<span class="n">0</span>, <span class="s">"boot"</span>);  <span class="c">// inserts at index 0, shifting everything else right</span>
logs.get(<span class="n">0</span>);           <span class="c">// reads the element at index 0</span>
logs.set(<span class="n">0</span>, <span class="s">"ready"</span>);  <span class="c">// replaces the element at index 0</span>
logs.remove(<span class="n">0</span>);        <span class="c">// removes the element at index 0, shifting later ones left</span></code></pre>''',
        "speak": "Here are the core methods, all together. Size tells you the element count, like length, but it's a method now, parentheses required. Add appends to the end, or takes an index to insert somewhere in the middle, shifting everything after it to the right. Get reads an element by index, set replaces one, and remove takes one out, shifting everything later back down by one. Notice array list uses methods, get and set, instead of square brackets, it's a real class, not a built-in language feature the way an array is.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">array: length, bracket index</div>
      <div class="darrow">&harr;</div>
      <div class="dbox active">ArrayList: size(), get/set(index)</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Same ideas, different vocabulary &mdash; and array list can grow or shrink, an array never can.</p>''',
        "speak": "Side by side, it's the same set of ideas wearing different vocabulary. Where an array uses the field length and square brackets, array list uses the method size, and get and set. And the one array can never do at all, grow or shrink, is exactly what array list is built for.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using square brackets on an ArrayList &mdash; it doesn't compile, always get and set instead.</li>
      <li><span class="check">!</span>Mixing up length and size() &mdash; arrays use the field, ArrayList uses the method.</li>
      <li><span class="check">!</span>Using an uninitialized ArrayList &mdash; a declared-but-not-new'd list is null, and throws NullPointerException.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Square brackets on an array list simply don't compile, it's always get and set. Don't mix up length and size, arrays use the field length, array list uses the method size. And watch for an uninitialized array list, declaring one without actually calling new leaves it null, and calling any method on that throws a Null Pointer Exception.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>ArrayList is resizable &mdash; use it when the size isn't known up front or will change.</li>
      <li><span class="check">&#10003;</span>The type parameter says what it holds; primitives need their wrapper type.</li>
      <li><span class="check">&#10003;</span>Core methods: size(), add(), add(index, obj), get(index), set(index, obj), remove(index).</li>
      <li><span class="check">&#10003;</span>Arrays use length and brackets; ArrayList uses size() and get/set.</li>
    </ul></div>''',
        "speak": "So, to recap. Array list is resizable, reach for it whenever the size isn't known up front or will change while the program runs. The type parameter says what it holds, and primitives need their wrapper type to go inside one. The core methods are size, add, add at an index, get, set, and remove. And where arrays use length and square brackets, array list uses size, and get and set instead. Next up, lesson 9.3, hash map, for when position isn't how you want to look something up at all.",
    },
]
