BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 4 &middot; Using Objects &amp; Calling Methods</div>
      <h1>Using the Math Class</h1>
      <p class="scr-sub">A built-in class made entirely of static methods &mdash; and the trick to getting a random number in a range.</p>
    </div>''',
        "speak": "Math is the class you'll reach for constantly, and it's a perfect example of everything we just covered, every single method on it is static.",
    },
    {
        "screen": '''<pre class="code"><code>Math.<span class="me">abs</span>(-<span class="n">4</span>);     <span class="c">// 4 &mdash; absolute value</span></code></pre>''',
        "speak": "No object, no new, just call it directly by the class name. Math dot abs of negative 4 gives you 4, the absolute value.",
    },
    {
        "screen": '''<pre class="code"><code>Math.<span class="me">abs</span>(-<span class="n">4</span>);     <span class="c">// 4 &mdash; absolute value</span>
Math.<span class="me">pow</span>(<span class="n">2</span>, <span class="n">3</span>);   <span class="c">// 8.0 &mdash; 2 to the power of 3</span></code></pre>''',
        "speak": "Math dot pow, 2, 3, gives you 2 to the power of 3, 8 point 0.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>Math.<span class="me">abs</span>(-<span class="n">4</span>);     <span class="c">// 4 &mdash; absolute value</span>
Math.<span class="me">pow</span>(<span class="n">2</span>, <span class="n">3</span>);   <span class="c">// 8.0 &mdash; 2 to the power of 3</span>
Math.<span class="me">sqrt</span>(<span class="n">9</span>);     <span class="c">// 3.0</span></code></pre>''',
        "speak": "Math dot square root of 9 gives you 3 point 0.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>Math.<span class="me">abs</span>(-<span class="n">4</span>);     <span class="c">// 4 &mdash; absolute value</span>
Math.<span class="me">pow</span>(<span class="n">2</span>, <span class="n">3</span>);   <span class="c">// 8.0 &mdash; 2 to the power of 3</span>
Math.<span class="me">sqrt</span>(<span class="n">9</span>);     <span class="c">// 3.0</span>
Math.<span class="me">random</span>();    <span class="c">// a double &gt;= 0.0 and &lt; 1.0</span></code></pre>''',
        "speak": "And Math dot random gives you a double that's greater than or equal to 0 point 0, and strictly less than 1 point 0. All four of these return a value, so, same rule as last lesson, you should actually use what comes back. And since Math lives in java dot lang, it never needs an import.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">More Math Methods Robot Code Uses</h2><ul>
      <li><span class="num">1</span><span><strong>Math.max(a, b) / Math.min(a, b)</strong> &mdash; larger / smaller of two values</span></li>
      <li><span class="num">2</span><span><strong>Math.round(x)</strong> &mdash; nearest whole number</span></li>
      <li><span class="num">3</span><span><strong>Math.floor(x) / Math.ceil(x)</strong> &mdash; round down / up, as a double</span></li>
    </ul></div>''',
        "speak": "Math has plenty more that robot code uses constantly. Math dot max and Math dot min give you the larger or smaller of two values, max of 3 and 7 is 7. Math dot round rounds to the nearest whole number, round of 2 point 6 is 3. And Math dot floor and Math dot ceil round down or up, giving back a double, floor of 2 point 6 is 2 point 0.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">More Math Methods Robot Code Uses</h2><ul>
      <li><span class="num">1</span><span><strong>Math.max(a, b) / Math.min(a, b)</strong> &mdash; larger / smaller of two values</span></li>
      <li><span class="num">2</span><span><strong>Math.round(x)</strong> &mdash; nearest whole number</span></li>
      <li><span class="num">3</span><span><strong>Math.floor(x) / Math.ceil(x)</strong> &mdash; round down / up, as a double</span></li>
      <li><span class="num">4</span><span><strong>Math.signum(x)</strong> &mdash; the sign: -1.0, 0.0, or 1.0</span></li>
      <li><span class="num">5</span><span><strong>Math.PI</strong> &mdash; the constant &pi; &mdash; no parentheses</span></li>
      <li><span class="num">6</span><span><strong>Math.toRadians(degrees)</strong> &mdash; degrees to radians</span></li>
    </ul></div>''',
        "speak": "Math dot signum gives you just the sign of a number, negative 1, 0, or positive 1. Math dot PI is the constant pie itself, a value, not a method, so no parentheses. And Math dot to radians converts an angle in degrees into radians, 180 degrees is pie radians.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">More Math Methods Robot Code Uses</h2><ul>
      <li><span class="num">1</span><span><strong>Math.max(a, b) / Math.min(a, b)</strong> &mdash; larger / smaller of two values</span></li>
      <li><span class="num">2</span><span><strong>Math.round(x)</strong> &mdash; nearest whole number</span></li>
      <li><span class="num">3</span><span><strong>Math.floor(x) / Math.ceil(x)</strong> &mdash; round down / up, as a double</span></li>
      <li><span class="num">4</span><span><strong>Math.signum(x)</strong> &mdash; the sign: -1.0, 0.0, or 1.0</span></li>
      <li><span class="num">5</span><span><strong>Math.PI</strong> &mdash; the constant &pi; &mdash; no parentheses</span></li>
      <li><span class="num">6</span><span><strong>Math.toRadians(degrees)</strong> &mdash; degrees to radians</span></li>
      <li><span class="num">7</span><span><strong>Math.hypot(x, y)</strong> &mdash; &radic;(x&sup2; + y&sup2;) &mdash; a distance</span></li>
      <li><span class="num">8</span><span><strong>Math.atan2(y, x)</strong> &mdash; angle (radians) toward (x, y) &mdash; y first</span></li>
      <li><span class="num">9</span><span><strong>Math.clamp(value, min, max)</strong> &mdash; value kept inside min to max</span></li>
    </ul></div>''',
        "speak": "Math dot hypot, short for hypotenuse, takes x and y and gives the straight-line distance, hypot of 3 and 4 is 5. Math dot a tan 2 gives the angle, in radians, pointing at x, y, and note that y comes first. And Math dot clamp keeps a value inside a range, clamp of 1 point 4, between negative 1 and 1, gives back 1 point 0.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// never lower than -1.0 or higher than 1.0</span>
<span class="k">double</span> throttle = <span class="t">Math</span>.<span class="me">clamp</span>(joystickValue * <span class="n">1.5</span>, -<span class="n">1.0</span>, <span class="n">1.0</span>);</code></pre>''',
        "speak": "Clamp is the one you'll use most for motors. It keeps a computed throttle from ever leaving the legal range, never lower than negative 1, never higher than 1, no matter how big joystick value times 1 point 5 gets.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Java 17 Note</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Math.clamp was added in Java 21. On Java 17, write Math.max(-1.0, Math.min(1.0, value)) instead.</p>''',
        "speak": "One version note. Math dot clamp was added in Java 21. On Java 17, write Math dot max of negative 1, and Math dot min of 1 and value, instead, it gives exactly the same result.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Random Numbers in a Range</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Math.random() alone is rarely useful on its own &mdash; you stretch and shift it to get the range you want.</p>''',
        "speak": "Math dot random by itself gives you a double between 0 and 1, including 0, never quite reaching 1. That's rarely the range you actually want, so you stretch it and shift it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> rnd = (<span class="k">int</span>)(Math.<span class="me">random</span>() * <span class="n">10</span>);      <span class="c">// an int from 0-9 (10 possible values)</span></code></pre>''',
        "speak": "Multiply Math dot random by 10, and you spread that zero-to-one range across zero-to-ten. Cast the whole thing to an int, and you get a whole number from 0 to 9, 10 possible values.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> rnd = (<span class="k">int</span>)(Math.<span class="me">random</span>() * <span class="n">10</span>);      <span class="c">// an int from 0-9 (10 possible values)</span>
<span class="k">int</span> rnd2 = (<span class="k">int</span>)(Math.<span class="me">random</span>() * <span class="n">10</span>) + <span class="n">1</span>; <span class="c">// an int from 1-10 (shifted up by 1)</span></code></pre>''',
        "speak": "Add 1 at the very end, outside the cast, and the whole range shifts up by one, giving you 1 through 10 instead. The general recipe: multiply by how many values you want, cast to int to drop the decimal, then add the minimum to shift the whole range up.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// A random autonomous delay between 1 and 4 seconds</span>
<span class="k">double</span> delay = Math.<span class="me">random</span>() * <span class="n">3.0</span> + <span class="n">1.0</span>; <span class="c">// [1.0, 4.0)</span></code></pre>''',
        "speak": "Here's a real FRC use, a random autonomous delay between 1 and 4 seconds. Multiply by 3, the size of the range, then add 1, the minimum, no cast needed here since we actually want a decimal, not a whole number.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// A random autonomous delay between 1 and 4 seconds</span>
<span class="k">double</span> delay = Math.<span class="me">random</span>() * <span class="n">3.0</span> + <span class="n">1.0</span>; <span class="c">// [1.0, 4.0)</span>

<span class="c">// A random starting position index, 0 through 2 (3 choices)</span>
<span class="k">int</span> startPos = (<span class="k">int</span>)(Math.<span class="me">random</span>() * <span class="n">3</span>);</code></pre>''',
        "speak": "And a random starting position index, 0 through 2, 3 total choices, this time cast to an int since a position index has to be whole.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>(<span class="k">int</span>)(Math.<span class="me">random</span>() * <span class="n">10</span>)   <span class="c">// casts the whole scaled expression &mdash; correct</span>
(<span class="k">int</span>)Math.<span class="me">random</span>() * <span class="n">10</span>     <span class="c">// casts Math.random() alone first &mdash; always 0</span></code></pre>''',
        "speak": "The parentheses matter enormously here. Cast open-paren, Math dot random times 10, close-paren, casts the whole scaled expression, that's correct. But drop those inner parentheses, and int only wraps Math dot random by itself, which truncates it down to 0 before the multiplication even happens. 0 times 10 is always 0, every single time.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting the parentheses around the scaled expression &mdash; the cast has to wrap the whole Math.random() times range expression.</li>
      <li><span class="check">!</span>Off-by-one on the range size &mdash; for an inclusive range like 1-10, the range size is 10, not 9.</li>
      <li><span class="check">!</span>Ignoring the return value &mdash; the result has to be stored or used.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Forgetting the parentheses around the scaled expression, we just saw exactly why that breaks everything. Off-by-one on the range size, for an inclusive range like 1 through 10, the range size is 10, not 9, count how many distinct values you actually want. And ignoring the return value, same rule as always, a static method's result has to actually be stored or used.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Math methods are static &mdash; call them as Math.methodName(...), no object needed.</li>
      <li><span class="check">&#10003;</span>Math.random() returns a double in [0.0, 1.0) &mdash; 0.0 possible, 1.0 never reached.</li>
      <li><span class="check">&#10003;</span>Random int in a range: (int)(Math.random() * range) + min.</li>
      <li><span class="check">&#10003;</span>The parentheses around Math.random() * range are required.</li>
      <li><span class="check">&#10003;</span>Math also has max/min, round, floor/ceil, signum, PI, toRadians, hypot, atan2, and (Java 21+) clamp.</li>
    </ul></div>''',
        "speak": "So: Math methods are static, call them as Math dot method name, no object ever needed. Math dot random returns a double between 0 and 1, 0 possible, 1 never reached. To get a random int in a range, cast, open-paren, Math dot random, times range, close-paren, plus the minimum. And those inner parentheses around Math dot random times range are not optional, skip them and the formula silently breaks. And Math also gives you max and min, round, floor and ceil, signum, pie, to radians, hypot, a tan 2, and, on Java 21 and later, clamp. Next up, lesson 4.4, what an object actually is, the difference between a class and the objects built from it.",
    },
]
