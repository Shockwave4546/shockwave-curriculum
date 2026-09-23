BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 2 &middot; Variables &amp; Types</div>
      <h1>Compound Assignment Operators</h1>
      <p class="scr-sub">Shortcuts for the "update a variable using its own value" pattern we've already been writing.</p>
    </div>''',
        "speak": "Back in lesson 2.3 we wrote step equals step plus 1, updating a variable using its own current value. That pattern is so common Java gives it a shortcut, several, actually, and we'll use them constantly from here on.",
    },
    {
        "screen": '''<pre class="code"><code>score += <span class="n">10</span>;   <span class="c">// same as: score = score + 10;</span></code></pre>''',
        "speak": "score plus-equals 10 means exactly the same thing as score equals score plus 10, just shorter to write and, honestly, easier to read once it's familiar.",
    },
    {
        "screen": '''<pre class="code"><code>score += <span class="n">10</span>;   <span class="c">// same as: score = score + 10;</span>
power *= <span class="n">0.5</span>;  <span class="c">// same as: power = power * 0.5;</span></code></pre>''',
        "speak": "The same shortcut works for every operator, plus-equals, minus-equals, times-equals, divide-equals, and remainder-equals. power times-equals zero point five means power equals power times zero point five.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>step++;   <span class="c">// same as step += 1, same as step = step + 1</span></code></pre>''',
        "speak": "Adding or subtracting exactly 1 is common enough to earn its own even shorter shortcut. step plus-plus means the same thing as step plus-equals 1, which means the same thing as step equals step plus 1.",
    },
    {
        "screen": '''<pre class="code"><code>step++;   <span class="c">// same as step += 1, same as step = step + 1</span>
timer--;</code></pre>''',
        "speak": "And timer minus-minus subtracts exactly 1 the same way.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">A Real Example: Ramping Up Power</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:48ch;margin:0 auto;">Increase power a little at a time, instead of jumping straight to full.</p>''',
        "speak": "Here's where this earns its keep on an actual robot. Instead of slamming straight to full power, you increase it gradually, a small amount each time through the loop.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> power = <span class="n">0.0</span>;
<span class="k">double</span> rampRate = <span class="n">0.02</span>; <span class="c">// add 2% each time this runs</span>

power += rampRate;</code></pre>''',
        "speak": "power starts at zero, ramp rate is two percent. Each time through, power plus-equals ramp rate, so it climbs by two percent every pass.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> power = <span class="n">0.0</span>;
<span class="k">double</span> rampRate = <span class="n">0.02</span>; <span class="c">// add 2% each time this runs</span>

power += rampRate;
<span class="k">if</span> (power &gt; targetPower) {
    power = targetPower; <span class="c">// stop it from going past the target</span>
}</code></pre>''',
        "speak": "But without a limit, that climb never stops on its own, so there's an if check right after, if power ever climbs past the target, snap it back down to exactly the target. That check matters, without it, power just keeps climbing straight past where you actually wanted it to stop.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Tracing Code by Hand</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:48ch;margin:0 auto;">Walk through it line by line, updating each variable as you go &mdash; a real debugging skill.</p>''',
        "speak": "One more skill while we're here: tracing. That means walking through code line by line, by hand, updating each variable's value as you go. It's a genuinely useful way to find bugs when just reading the code isn't cutting it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> step = <span class="n">0</span>;
<span class="k">int</span> delta = <span class="n">5</span>;
<span class="k">int</span> total = <span class="n">1</span>;

step++;              <span class="c">// step: 1</span>
delta -= <span class="n">3</span>;          <span class="c">// delta: 2</span></code></pre>''',
        "speak": "Let's trace one together. step starts at 0, delta at 5, total at 1. step plus-plus makes step 1. delta minus-equals 3 makes delta 2.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> step = <span class="n">0</span>;
<span class="k">int</span> delta = <span class="n">5</span>;
<span class="k">int</span> total = <span class="n">1</span>;

step++;              <span class="c">// step: 1</span>
delta -= <span class="n">3</span>;          <span class="c">// delta: 2</span>
total = step + delta; <span class="c">// total: 1 + 2 = 3</span>
step = total * <span class="n">2</span>;    <span class="c">// step: 3 * 2 = 6</span></code></pre>''',
        "speak": "total gets reassigned to step plus delta, that's 1 plus 2, so total becomes 3. Then step gets reassigned to total times 2, that's 3 times 2, so step becomes 6. Notice step's old value, 1, is already gone by this point, we're using its brand new value from two lines up.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> step = <span class="n">0</span>;
<span class="k">int</span> delta = <span class="n">5</span>;
<span class="k">int</span> total = <span class="n">1</span>;

step++;              <span class="c">// step: 1</span>
delta -= <span class="n">3</span>;          <span class="c">// delta: 2</span>
total = step + delta; <span class="c">// total: 1 + 2 = 3</span>
step = total * <span class="n">2</span>;    <span class="c">// step: 3 * 2 = 6</span>
delta %= <span class="n">2</span>;          <span class="c">// delta: 2 % 2 = 0</span>
total--;             <span class="c">// total: 2</span></code></pre>''',
        "speak": "delta percent-equals 2, that's 2 percent 2, which is 0, so delta becomes 0. And total minus-minus drops total from 3 down to 2. Final values: step is 6, delta is 0, total is 2. That's the whole discipline, one line, one updated value, in order, never skipping ahead.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting the clamp when ramping &mdash; power += rampRate with no limit check just keeps climbing past your target.</li>
      <li><span class="check">!</span>Skipping ahead while tracing &mdash; go one line at a time, in order; skipping ahead is how you miss the actual bug.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Forgetting the clamp when ramping, power plus-equals ramp rate with no limit check just sails right past your target and keeps going. And skipping ahead while tracing, go one line at a time, in order, skipping ahead is exactly how you miss the actual bug you were trying to find.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>+= -= *= /= %= update a variable using its current value, then store the result back.</li>
      <li><span class="check">&#10003;</span>++ and -- are shortcuts for adding or subtracting exactly 1.</li>
      <li><span class="check">&#10003;</span>Ramping power up gradually is a real use of +=, checked against a limit each time.</li>
      <li><span class="check">&#10003;</span>Tracing code by hand, one line and one value at a time, is a real debugging skill.</li>
    </ul></div>''',
        "speak": "So: plus-equals, minus-equals, times-equals, divide-equals, and remainder-equals all update a variable using its current value, then store the result right back into it. Plus-plus and minus-minus are shortcuts for adding or subtracting exactly 1. Ramping power up gradually is a real use of plus-equals, always checked against a limit. And tracing code by hand, one line, one value, in order, is a real skill you'll lean on constantly. That wraps up Chapter 2 on variables and types, next we move into Chapter 3 and start using code other people already wrote for us.",
    },
]
