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

<span class="c">// &lt;&gt; ("the diamond") repeats the left side's type</span>
<span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt; logs = <span class="k">new</span> <span class="t">ArrayList</span>&lt;&gt;();
logs.add(<span class="s">"Robot Initialized"</span>);</code></pre>''',
        "speak": "Array list lives in java's util package, so it needs an import. Reach for it whenever the size isn't known up front, or will change at runtime. Notice the empty angle brackets on the right, that's called the diamond, Java infers String from the declared type on the left, so you don't have to type it twice. Writing out new ArrayList of String still works too, but the diamond form is what you'll see in real code.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">Double</span>&gt; sensorReadings = <span class="k">new</span> <span class="t">ArrayList</span>&lt;&gt;();
sensorReadings.add(<span class="n">2.4</span>); <span class="c">// autoboxed into a Double automatically</span></code></pre>''',
        "speak": "The type in angle brackets says what kind of object the list holds. And that word object matters, array list can only hold objects, never primitives directly. A list of numbers uses a wrapper type like Integer or Double, and Java auto-converts back and forth for you, adding a plain 2.4 here automatically wraps it into a Double.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Wrapper Classes</h2><ul>
      <li><span class="num">1</span><span><strong>int</strong> &rarr; <strong>Integer</strong>, <strong>double</strong> &rarr; <strong>Double</strong>, <strong>boolean</strong> &rarr; <strong>Boolean</strong>, <strong>char</strong> &rarr; <strong>Character</strong>.</span></li>
      <li><span class="num">2</span><span>Autoboxing wraps a primitive into its object form; unboxing does the reverse.</span></li>
    </ul></div>''',
        "speak": "Every primitive type has a matching wrapper class, an object version of that value, and that's what makes it usable inside an array list at all. Int becomes Integer, double becomes Double, boolean becomes Boolean, char becomes Character. Wrapping a primitive up is autoboxing, unwrapping it back down is unboxing, and Java does both directions automatically.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> first = sensorReadings.get(<span class="n">0</span>); <span class="c">// unboxed back into a double automatically</span></code></pre>''',
        "speak": "Three things worth knowing before they bite. Unboxing a null throws a Null Pointer Exception, a wrapper variable, or an array list of Integer slot, can hold null, and the instant Java tries to unbox that into a primitive, it crashes, exactly the shape of the missing-key bug you'll see in lesson 9.3. Double equals on Integer is unreliable too, it checks identity, not value, except Java happens to cache small values, so it can look like it works for small numbers and quietly fail for larger ones, use dot equals instead. And turning text into a number needs parse Int or parse Double, not autoboxing, that's a separate conversion for when you're starting from a String, like a field split out of a CSV line.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt; logs = <span class="k">new</span> <span class="t">ArrayList</span>&lt;&gt;();
logs.size();             <span class="c">// number of elements (like length, but a method — () required)</span>
logs.add(<span class="s">"started"</span>);     <span class="c">// appends to the end</span>
logs.add(<span class="n">0</span>, <span class="s">"boot"</span>);     <span class="c">// inserts at index 0, shifting everything else right</span>
logs.get(<span class="n">0</span>);              <span class="c">// reads the element at index 0</span>
logs.set(<span class="n">0</span>, <span class="s">"ready"</span>);     <span class="c">// replaces the element at index 0</span>
logs.remove(<span class="n">0</span>);           <span class="c">// removes BY INDEX — the element at index 0</span>
logs.remove(<span class="s">"ready"</span>);     <span class="c">// removes BY VALUE — the first element .equals("ready")</span>
logs.contains(<span class="s">"ready"</span>);   <span class="c">// true if any element .equals("ready")</span>
logs.indexOf(<span class="s">"ready"</span>);    <span class="c">// index of the first match, or -1 if not present</span>
logs.isEmpty();           <span class="c">// true if size() == 0</span></code></pre>''',
        "speak": "Here are the core methods, all together. Size tells you the element count, like length, but it's a method now, parentheses required. Add appends to the end, or takes an index to insert somewhere in the middle, shifting everything after it to the right. Get reads an element by index, set replaces one. Remove has two faces, an int argument removes by index, but any other object removes by value, the first match. Contains and index of both search by value, and is empty checks whether size is zero. Notice array list uses methods, get and set, instead of square brackets, it's a real class, not a built-in language feature the way an array is.",
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
      <li><span class="check">!</span>remove(30) on an ArrayList&lt;Integer&gt; removes BY INDEX, not the value 30.</li>
    </ul></div>''',
        "speak": "Four pitfalls. Square brackets on an array list simply don't compile, it's always get and set. Don't mix up length and size, arrays use the field length, array list uses the method size. Watch for an uninitialized array list, declaring one without actually calling new leaves it null, and calling any method on that throws a Null Pointer Exception. And remove of 30 on an array list of Integer does not remove the value 30, an int argument always picks the remove by index overload, so it removes whatever's sitting at position 30 instead, wrap the value first if that's really what you want removed.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>ArrayList is resizable &mdash; use it when the size isn't known up front or will change.</li>
      <li><span class="check">&#10003;</span>new ArrayList&lt;&gt;() (the diamond) infers the type parameter from the left side.</li>
      <li><span class="check">&#10003;</span>Primitives need their wrapper type; unboxing null throws, and == on wrappers is unreliable.</li>
      <li><span class="check">&#10003;</span>Core methods: size(), add(), get(index), set(index, obj), remove(index/Object), contains(), indexOf(), isEmpty().</li>
      <li><span class="check">&#10003;</span>Arrays use length and brackets; ArrayList uses size() and get/set.</li>
    </ul></div>''',
        "speak": "So, to recap. Array list is resizable, reach for it whenever the size isn't known up front or will change while the program runs. New ArrayList with the empty diamond infers the type parameter from the left side, no need to repeat it. Primitives need their wrapper type to go inside one, and two things to remember there, unboxing a null throws, and double equals on a wrapper is unreliable, use dot equals instead. The core methods are size, add, get, set, remove by either index or value, contains, index of, and is empty. And where arrays use length and square brackets, array list uses size, and get and set instead. Next up, lesson 9.3, hash map, for when position isn't how you want to look something up at all.",
    },
]
