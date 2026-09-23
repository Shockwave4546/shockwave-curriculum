BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 6 &middot; Strings</div>
      <h1>Strings</h1>
      <p class="scr-sub">Text as an object &mdash; immutable, and indexed from 0.</p>
    </div>''',
        "speak": "Welcome to Chapter 6. You've been using String since your very first program, but we've never actually looked at what it is under the hood. Turns out it's a full class, with its own rules, and one big one: once you create a string, it can never change.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> autoName = <span class="k">new</span> <span class="t">String</span>(<span class="s">"BlueAlliance-Left"</span>); <span class="c">// rarely used</span>
<span class="t">String</span> autoName = <span class="s">"BlueAlliance-Left"</span>;              <span class="c">// the normal way</span></code></pre>''',
        "speak": "String is a class, part of Java's core library, no import needed. Like any class, you can build one with new, but there's also a shortcut, a string literal, just the text in quotes. Both lines here create a real string object. The literal form on the second line is what you'll use almost every time.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> name = <span class="s">"Titan"</span>;
name.toUpperCase(); <span class="c">// does nothing useful — the result is thrown away!</span>
name = name.toUpperCase(); <span class="c">// this is how you actually keep the change</span></code></pre>''',
        "speak": "Here's the big one: strings are immutable. Once a string exists, its characters can never change. Every method that looks like it modifies a string, like to upper case, actually builds a brand new string and returns it, leaving the original untouched. Call it and throw away the result, like the second line, and nothing useful happens. You have to capture the result, reassigning name to the new value, to actually keep the change.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> status = <span class="s">"Auto: "</span> + autoName + <span class="s">", step "</span> + <span class="n">3</span>; <span class="c">// the int 3 converts automatically</span></code></pre>''',
        "speak": "Plus, and plus equals, join strings together, and they automatically convert non-string values into text for you. Here, the int 3 gets converted into the text 3 automatically, no extra work needed.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">&quot;Score: &quot; + 1 + 2</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox err">&quot;Score: 12&quot;</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Plus reads left to right &mdash; parenthesize the numbers first if you actually want them added.</p>''',
        "speak": "Watch the order when you mix plus with numbers, because it's evaluated strictly left to right. Quote score colon quote plus 1 plus 2 does not give you three. It gives you score colon 1 2, because each number gets appended as text in turn, one after the other. If you actually want the addition to happen first, wrap it in parentheses.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Index and Length</h2><ul>
      <li><span class="num">1</span><span>Each character has a position, called an <strong>index</strong>, starting at 0.</span></li>
      <li><span class="num">2</span><span><strong>length()</strong> returns the total character count &mdash; the last valid index is always length() minus 1.</span></li>
      <li><span class="num">3</span><span>There's no bracket notation like an array's &mdash; getting one character means using substring.</span></li>
    </ul></div>''',
        "speak": "Every character in a string has a position, an index, and indexes always start at 0, not 1. The length method tells you the total character count, and that means the last valid index is always the length, minus 1. Unlike an array, there's no bracket shortcut to grab a single character directly, you can't write autoName followed by an index in square brackets, that's not valid Java for a string. Getting a single character means using substring instead, which is exactly what's up next. And a quick warning: reaching for an index outside 0 up through length minus 1 throws an Index Out Of Bounds Exception.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> autoName = <span class="s">"BlueAlliance-Left"</span>;
autoName.length();          <span class="c">// 17</span>
autoName.substring(<span class="n">0</span>, <span class="n">4</span>);   <span class="c">// "Blue" — from index 0 up to (not including) 4</span>
autoName.substring(<span class="n">13</span>);     <span class="c">// "Left" — from index 13 to the end</span>
autoName.indexOf(<span class="s">"Left"</span>);   <span class="c">// 13 — or -1 if not found</span>
autoName.equals(<span class="s">"BlueAlliance-Left"</span>); <span class="c">// true — compares actual characters</span></code></pre>''',
        "speak": "Those are the core string methods, all together. Length gives you the character count. Sub string with two numbers gives you the characters from the first index up to, but not including, the second, so sub string 0 to 4 gives you 4 characters, indices 0 through 3. Sub string with just one number gives you everything from that index to the end. Index of searches for some text and tells you where it starts, or gives you negative 1 if it's not there at all. And sub string of i, i plus 1 is the standard trick for pulling out just the single character at position i.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> a = <span class="k">new</span> <span class="t">String</span>(<span class="s">"Left"</span>);
<span class="t">String</span> b = <span class="k">new</span> <span class="t">String</span>(<span class="s">"Left"</span>);
System.out.println(a == b);       <span class="c">// false — two different objects</span>
System.out.println(a.equals(b));  <span class="c">// true — same characters</span></code></pre>''',
        "speak": "And the single most important rule in this whole lesson: use dot equals, not double equals, to compare string content. Double equals on a string checks whether two variables point at the exact same object in memory, not whether their text matches. Here, a and b hold the same characters, but they're two separate objects, so a double-equals b comes back false. a dot equals b compares the actual characters, and correctly comes back true.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using double equals to compare string content &mdash; it compiles and runs, but almost always gives the wrong answer.</li>
      <li><span class="check">!</span>Forgetting a string method's result has to be captured &mdash; strings are immutable, so a thrown-away result is a no-op.</li>
      <li><span class="check">!</span>Off-by-one in sub string &mdash; the second index is exclusive, so sub string 0 to 4 gives 4 characters, not 5.</li>
    </ul></div>''',
        "speak": "A few pitfalls worth flagging one more time. Never use double equals to compare what's actually inside a string, it compiles, it runs, and it's wrong far more often than it errors out, so always reach for dot equals instead. Don't forget a string method's result has to be used, since strings are immutable, calling to upper case and throwing away what it returns does absolutely nothing. And watch the off-by-one in sub string, the ending index is exclusive, so sub string 0 to 4 gives you 4 characters, not 5.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>String is a class &mdash; literals are the normal way to create one.</li>
      <li><span class="check">&#10003;</span>Strings are immutable &mdash; every "modifying" method returns a new string instead.</li>
      <li><span class="check">&#10003;</span>Plus and plus-equals concatenate, auto-converting non-string values.</li>
      <li><span class="check">&#10003;</span>length, sub string, and index of are the core methods, all indexed from 0.</li>
      <li><span class="check">&#10003;</span>Use dot equals to compare string content &mdash; double equals only checks if it's the same object.</li>
    </ul></div>''',
        "speak": "So, to recap. String is a class, and a string literal is the normal way to build one. Strings are immutable, every method that looks like it modifies one actually hands back a brand new string. Plus and plus-equals concatenate, converting non-string values automatically. Length, sub string, and index of are your core tools, all indexed starting from 0. And always use dot equals, never double equals, to compare what's actually inside two strings. Next up, lesson 6.2, we'll put strings to work in real loops, scanning them character by character.",
    },
]
