BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>Array Creation and Access</h1>
      <p class="scr-sub">A fixed-size block of same-type values, accessed by position.</p>
    </div>''',
        "speak": "Welcome to Chapter 9. So far, every piece of data you've stored has needed its own separate variable. That falls apart fast the moment you have a dozen related values, imagine writing motor 1, motor 2, motor 3, all the way up. An array is the fix.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span>[] canBusIds = {<span class="n">1</span>, <span class="n">2</span>, <span class="n">3</span>, <span class="n">4</span>}; <span class="c">// an initializer list — size inferred, values set immediately</span></code></pre>''',
        "speak": "An array is a fixed-size block of memory holding several values of the same type, accessed by position, called an index, instead of by a pile of separate variable names. This is an initializer list, the size gets inferred from how many values you list, and they're all set immediately.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span>[] canBusIds;              <span class="c">// declares the variable — no array exists yet (it's null)</span>
canBusIds = <span class="k">new int</span>[<span class="n">4</span>];       <span class="c">// creates a 4-element array — all elements start at 0</span>

<span class="k">int</span>[] canBusIds2 = {<span class="n">1</span>, <span class="n">2</span>, <span class="n">3</span>, <span class="n">4</span>}; <span class="c">// initializer list: create + fill in one step</span></code></pre>''',
        "speak": "There are really two ways to create one. Declare the variable alone, and it's null, no array exists yet, exactly like any other object reference. Or use new with a size, which creates the array with every element already set to that type's default, 0 here since it's an int array. The initializer list from a moment ago does both steps in one, create and fill at once.",
    },
    {
        "screen": '''<pre class="code"><code>System.out.println(canBusIds.length); <span class="c">// 4</span>
canBusIds[<span class="n">0</span>] = <span class="n">5</span>;                     <span class="c">// assign</span>
System.out.println(canBusIds[<span class="n">0</span>]);     <span class="c">// read — prints 5</span></code></pre>''',
        "speak": "Indices start at 0, and the last valid index is always length minus 1. Notice length here has no parentheses, it's a field, not a method, unlike a string's length. Square brackets both read and write, index 0 on the left assigns, index 0 on the right reads back.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox err">index -1</div>
      <div class="dbox active">0</div><div class="dbox active">1</div><div class="dbox active">2</div><div class="dbox active">3</div>
      <div class="dbox err">index 4</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Anything outside 0 through length minus 1 throws an Array Index Out Of Bounds Exception.</p>''',
        "speak": "Step outside 0 through length minus 1 in either direction, and you get an Array Index Out Of Bounds Exception, one of the single most common runtime errors you'll run into, in any Java program, ever.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span>[] autoNames = {<span class="s">"3-Piece-Left"</span>, <span class="s">"1-Piece-Safe"</span>, <span class="s">"Mobility-Only"</span>};
<span class="k">double</span>[] autoTimes = {<span class="n">14.2</span>, <span class="n">8.5</span>, <span class="n">3.1</span>}; <span class="c">// autoTimes[i] is the recorded time for autoNames[i]</span></code></pre>''',
        "speak": "A really common pattern is parallel arrays, two or more arrays kept in the same order, where a given index means the same thing in both. Here, index i in auto times is the recorded run time for the auto routine named at index i in auto names.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span>[] driveMotors = <span class="k">new</span> <span class="t">TalonFX</span>[<span class="n">4</span>]; <span class="c">// 4 slots, all currently null</span>
driveMotors[<span class="n">0</span>] = <span class="k">new</span> <span class="t">TalonFX</span>(<span class="n">1</span>);        <span class="c">// must construct each element separately</span>
driveMotors[<span class="n">0</span>].set(<span class="n">0.5</span>);                <span class="c">// then call methods through the index</span></code></pre>''',
        "speak": "An array can hold any type at all, including your own classes, but there's a catch. New TalonFX bracket 4 gives you 4 slots, and every single one of them is null, not 4 ready-to-use motor objects. Each element still has to be constructed individually, on its own line, before you can call a method through it.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting an array must be constructed, not just declared.</li>
      <li><span class="check">!</span>Off-by-one on the last index &mdash; it's length minus 1, not length.</li>
      <li><span class="check">!</span>Forgetting to construct each element of an object array &mdash; new gives null slots, not ready-to-use objects.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Don't forget an array has to be constructed, not just declared, a bare declaration is null until you give it new with a size, or an initializer list. Watch the off-by-one on the last index, it's always length minus 1, never length itself. And don't forget to construct each element of an object array, new gives you empty slots, not ready-to-use objects, each one still needs its own new.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An array is a fixed-size, same-type collection, accessed by a 0-based index.</li>
      <li><span class="check">&#10003;</span>new type bracket size creates every element at its default; an initializer list fills it in one step.</li>
      <li><span class="check">&#10003;</span>length is a field, no parentheses; the last valid index is length minus 1.</li>
      <li><span class="check">&#10003;</span>Parallel arrays keep related data in sync by index.</li>
      <li><span class="check">&#10003;</span>An array of objects still requires constructing each element individually.</li>
    </ul></div>''',
        "speak": "So, to recap. An array is a fixed-size, same-type collection, accessed by a 0-based index. New, a type, and a size in brackets creates every element at its default; an initializer list creates and fills it in one step. Length is a field, no parentheses, and the last valid index is always length minus 1. Parallel arrays keep related data in sync by index. And an array of objects still needs each element constructed individually, the array itself doesn't build them for you. Next up, lesson 9.2, where we meet array list, the resizable alternative.",
    },
]
