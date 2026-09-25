BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 2 &middot; Variables &amp; Types</div>
      <h1>Casting &amp; Ranges of Values</h1>
      <p class="scr-sub">Converting between types on purpose &mdash; and what happens when a value doesn't fit.</p>
    </div>''',
        "speak": "We saw truncating division back in lesson 2.2, whole numbers dividing and quietly losing their decimal part. Now let's fix that on purpose, and look at what other limits Java's number types actually have.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Widening vs. Narrowing</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:48ch;margin:0 auto;">Small into big happens automatically; big into small needs an explicit cast.</p>''',
        "speak": "Java moves values between numeric types two different ways. Widening is a smaller type flowing into a bigger one automatically, no cast needed, int into double is always safe since no information is lost. Narrowing is the other direction, a bigger type into a smaller one, which loses information, so Java requires an explicit cast to make sure you meant it, double into int needs a cast. That's exactly the rule behind the possible-lossy-conversion compile errors back in lessons 2.1 and 2.3.",
    },
    {
        "screen": '''<pre class="code"><code>(<span class="k">double</span>) <span class="n">1</span> / <span class="n">3</span>   <span class="c">// 0.333... &mdash; the 1 becomes a double first, then divides</span></code></pre>''',
        "speak": "Put double in parentheses right before a value to convert it to that type on the spot. Here, the 1 becomes a double first, and only then divides by 3, giving us zero point three repeating.",
    },
    {
        "screen": '''<pre class="code"><code>(<span class="k">int</span>) <span class="n">3.6</span>        <span class="c">// 3 &mdash; cuts off everything after the decimal point</span></code></pre>''',
        "speak": "The same trick works the other way. int in parentheses before 3 point 6 gives you 3. And that's the detail to really lock in, int always cuts off the decimal, it never rounds. int of 3 point 9 is 3, not 4.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> rounded = (<span class="k">int</span>)(<span class="n">5.7</span> + <span class="n">0.5</span>); <span class="c">// 6 &mdash; this is rounding, not truncating</span></code></pre>''',
        "speak": "So if you actually want rounding instead of truncating, add zero point five first, then cast. 5 point 7 plus zero point 5 is 6 point 2, and casting that to an int truncates it down to 6, which happens to be the correctly rounded answer. It's a trick, not a different kind of cast, but it works. One big catch, though: this only rounds correctly for non-negative numbers. For a negative value it rounds the wrong way, and FRC values like joystick input or encoder deltas are often negative. Java's own Math dot round, covered in Chapter 4, handles the sign correctly and is the better tool for real code.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Fixing Truncating Division</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:48ch;margin:0 auto;">The cast has to happen before the division &mdash; position matters.</p>''',
        "speak": "Now let's revisit that truncating-division bug from lesson 2.2 properly. Casting one of the two numbers fixes it, but only if the cast happens before the division, not after.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> total = <span class="n">17</span>;
<span class="k">int</span> games = <span class="n">5</span>;

<span class="k">double</span> average = (<span class="k">double</span>) total / games;   <span class="c">// correct: 3.4</span></code></pre>''',
        "speak": "17 total, across 5 games. Cast total to a double first, then divide by games, and you correctly get 3 point 4.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> total = <span class="n">17</span>;
<span class="k">int</span> games = <span class="n">5</span>;

<span class="k">double</span> average = (<span class="k">double</span>) total / games;   <span class="c">// correct: 3.4</span>
<span class="k">double</span> wrong    = (<span class="k">double</span>) (total / games); <span class="c">// wrong: int division first, then cast: 3.0</span></code></pre>''',
        "speak": "But wrap the parentheses around the whole division instead, cast open-paren total divide games close-paren, and Java divides total by games as whole numbers first, getting 3, and only afterward converts that 3 to a double. You end up with 3 point 0, not 3 point 4, the decimal precision was already gone before the cast ever got a chance to help.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Whole Numbers Have a Limit</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:48ch;margin:0 auto;">Roughly plus or minus 2.1 billion &mdash; go past it, and it silently wraps around.</p>''',
        "speak": "int values aren't unlimited. They can only hold values in a fixed range, roughly plus or minus 2 point 1 billion. Go past that limit, and the number doesn't throw an error, it silently wraps around to a completely wrong value.",
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">println</span>(Integer.MAX_VALUE + <span class="n">1</span>); <span class="c">// wraps to the smallest possible int</span></code></pre>''',
        "speak": "Integer dot Max underscore Value is Java's built-in name for that largest possible int. Integer here is a built-in helper class that travels alongside the int primitive, you'll meet it properly in Chapter 9.2. Add just 1 more to Max Value, and instead of getting a bigger number, it wraps all the way around to the smallest possible int. No error, no warning. It's unlikely to bite you mid-match, but it's a real risk for a counter that keeps climbing and is never reset.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Decimals Have a Precision Limit Too</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:48ch;margin:0 auto;">About 15-16 significant digits &mdash; and most decimals can't be stored exactly at all.</p>''',
        "speak": "double has its own limit, precision rather than range. It can only store about 15 to 16 significant digits, and beyond that, extra digits get quietly rounded off. But the everyday cause isn't running out of digits, it's that most decimals simply can't be stored exactly in binary at all, the same way one-third can't be written exactly in decimal.",
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">println</span>(<span class="n">0.1</span> + <span class="n">0.2</span>);        <span class="c">// 0.30000000000000004, not 0.3</span>
System.out.<span class="me">println</span>(<span class="n">0.1</span> + <span class="n">0.2</span> == <span class="n">0.3</span>); <span class="c">// false</span></code></pre>''',
        "speak": "Zero point 1 plus zero point 2 doesn't print zero point 3, it prints zero point 3 followed by a long string of extra digits. And zero point 1 plus zero point 2 double-equals zero point 3 comes back false. That's exactly why comparing two doubles with double-equals is risky, two values that should be mathematically equal can differ by a tiny rounding amount you never typed in yourself.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> target = <span class="n">45.0</span>;
<span class="k">double</span> current = <span class="n">44.98</span>;
<span class="k">double</span> tolerance = <span class="n">0.05</span>;

<span class="k">boolean</span> closeEnough = Math.<span class="me">abs</span>(current - target) &lt; tolerance; <span class="c">// true</span></code></pre>''',
        "speak": "The fix, needed constantly for things like checking whether a robot arm reached its target angle, is a tolerance comparison. Instead of asking are these exactly equal, ask are these close enough. Math dot abs of current minus target, less than tolerance. Math dot abs strips the sign, so it doesn't matter whether current is a bit above or a bit below target, only how far apart they are.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Casting after dividing instead of before &mdash; the division already happened as whole numbers by the time the cast runs.</li>
      <li><span class="check">!</span>Assuming a cast rounds &mdash; int always cuts off the decimal; rounding needs the add-0.5-then-cast trick, and even that only works for non-negative numbers.</li>
      <li><span class="check">!</span>Comparing doubles with == &mdash; use a tolerance comparison instead.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Casting after dividing instead of before, by the time the cast runs, the division already happened as whole numbers, and there's nothing left for the cast to save. Assuming a cast rounds, it doesn't, int always just cuts off the decimal, rounding needs that add-zero-point-five-then-cast trick from earlier, and even that only works for non-negative numbers. And comparing doubles with double-equals, two values that should be equal often aren't, bit for bit, use a tolerance comparison instead.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Widening (small into big) happens automatically; narrowing (big into small) needs an explicit cast.</li>
      <li><span class="check">&#10003;</span>(int) and (double) convert a value's type on the spot &mdash; (int) truncates, never rounds.</li>
      <li><span class="check">&#10003;</span>To fix truncating division, cast before dividing &mdash; position matters.</li>
      <li><span class="check">&#10003;</span>int values have a fixed range; going past it silently wraps to a wrong value.</li>
      <li><span class="check">&#10003;</span>double values have a precision limit &mdash; compare with a tolerance, not ==.</li>
    </ul></div>''',
        "speak": "To recap: widening, small type into big, happens automatically; narrowing, big into small, needs an explicit cast. int and double in parentheses convert a value's type right on the spot, and int always truncates, never rounds. To fix truncating division, cast before dividing, not after, position genuinely matters. int values have a fixed range, and going past it silently wraps to a wrong answer with no warning. And double values have a precision limit and can't store most decimals exactly, so compare them with a tolerance, not double-equals. Next time, lesson 2.5, shortcuts for updating a variable using its own current value.",
    },
]
