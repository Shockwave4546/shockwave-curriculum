BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 13 &middot; Common Gotchas</div>
      <h1>Common Gotchas</h1>
      <p class="scr-sub">A quick-reference checklist &mdash; not new material.</p>
    </div>''',
        "speak": "Chapter 13 isn't teaching anything brand new. Every single item here was already covered somewhere earlier in the curriculum. This is a quick-reference checklist, the handful of real mistakes that tend to resurface long after the lesson that first covered them, all in one place.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Gotcha 1</div>
      <h1>== vs. .equals()</h1>
      <p class="scr-sub">Comparing primitives is not comparing objects.</p>
    </div>''',
        "speak": "First up: double-equals versus dot-equals. Double-equals compares primitives, ints, doubles, booleans, by value, and that's correct and sufficient for them.",
    },
    {
        "screen": '''<pre class="code"><code>String a = <span class="k">new</span> String("BlueAlliance-Left");
String b = <span class="k">new</span> String("BlueAlliance-Left");
a == b;        <span class="c">// false — two different objects, even with identical text</span>
a.equals(b);   <span class="c">// true — compares the actual characters</span></code></pre>''',
        "speak": "But for objects, including String, double-equals checks something totally different: whether two variables point at the exact same object in memory. Here, a and b hold identical text, but they're two separate String objects, so double-equals says false. Dot-equals actually compares the characters, and correctly says true.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Fix</h2><ul>
      <li><span class="num">1</span><span>Use <code>.equals()</code> for any object type, including boxed numbers like <code>Integer</code> and <code>Double</code></span></li>
    </ul></div>''',
        "speak": "The rule of thumb: use dot-equals for any object type at all, and that includes boxed numbers like Integer and Double, not just String. See lesson 6.1 if you want the full explanation of why this happens.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Gotcha 2</div>
      <h1>Integer Division</h1>
      <p class="scr-sub">Truncated, not rounded.</p>
    </div>''',
        "speak": "Second: integer division. Dividing two ints produces an int, and the fractional part just gets silently thrown away, not rounded to the nearest whole number.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">int</span> result = 5 / 2;       <span class="c">// 2, not 2.5 — the .5 is thrown away, not rounded</span>
<span class="t">double</span> result2 = 5.0 / 2.0; <span class="c">// 2.5 — at least one operand must be a floating-point type</span></code></pre>''',
        "speak": "Five divided by two as ints gives you two, not two-point-five, the point-five is simply discarded. Make at least one of the two operands a floating-point type, like five point zero divided by two point zero, and you get the real answer, two point five.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Where This Bites</h2><ul>
      <li><span class="num">1</span><span>Averaging &mdash; <code>total / count</code> where both are <code>int</code> &mdash; cast at least one operand to <code>double</code> first</span></li>
    </ul></div>''',
        "speak": "This bites most often when averaging, total divided by count, where both happen to be ints. Cast at least one of them to double before dividing. Lesson 2.4 has the full casting rules if you need a refresher.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Gotcha 3</div>
      <h1>NullPointerException</h1>
      <p class="scr-sub">Calling a method on nothing.</p>
    </div>''',
        "speak": "Third: the null pointer exception, one of the single most common runtime crashes in any Java program, robot code very much included. It happens when you call a method or access a field on a variable that's null, declared, but never actually assigned a real object.",
    },
    {
        "screen": '''<pre class="code"><code>Drivetrain drivetrain; <span class="c">// declared, but never assigned — currently null</span>
drivetrain.stop();      <span class="c">// NullPointerException — nothing to call stop() on</span></code></pre>''',
        "speak": "A Drive Train variable that's only ever been declared, never constructed with new, is null. Call stop on it, and there's nothing there to actually call stop on, so you get a null pointer exception.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Fix Is Always the Same Shape</h2><ul>
      <li><span class="num">1</span><span>Make sure every object is actually constructed with <code>new</code> before anything calls a method on it</span></li>
    </ul></div>''',
        "speak": "The fix is always the same shape: make sure every object is genuinely constructed with new before anything ever calls a method on it.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Fix Is Always the Same Shape</h2><ul>
      <li><span class="num">1</span><span>Make sure every object is actually constructed with <code>new</code> before anything calls a method on it</span></li>
      <li><span class="num">2</span><span>Check for null explicitly anywhere a value might legitimately be missing</span></li>
    </ul></div>''',
        "speak": "And check for null explicitly anywhere a value might legitimately be missing, like a HashMap get call that found no match at all. Lesson 9.3 covers that case directly.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Gotcha 4</div>
      <h1>Off-by-One</h1>
      <p class="scr-sub">The last valid index is length minus one.</p>
    </div>''',
        "speak": "Fourth and last: off-by-one. Arrays, and ArrayList, are indexed starting at zero, so the last valid index is always length minus one, or size minus one, never length itself.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">int</span>[] canBusIds = <span class="k">new</span> <span class="t">int</span>[10]; <span class="c">// valid indices: 0 through 9</span>
canBusIds[10]; <span class="c">// ArrayIndexOutOfBoundsException — 10 is one past the end</span></code></pre>''',
        "speak": "Ten CAN bus IDs means valid indices zero through nine. Reach for index ten, one past the end, and you'll get an ArrayIndexOutOfBoundsException. This is the single most common loop-bound mistake there is, writing i less-than-or-equal-to array dot length instead of i less-than array dot length. Lessons 9.1 and 9.2 have the full indexing rules for arrays and ArrayList.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Treating this chapter as the complete list of Java mistakes &mdash; it isn't, it's just what the original deck happened to flag, and it's expected to grow.</li>
      <li><span class="check">!</span>Fixing the symptom instead of the cause &mdash; e.g. wrapping a NullPointerException in try/catch instead of fixing why the object was never constructed.</li>
    </ul></div>''',
        "speak": "Two meta-pitfalls to close with. Don't treat this chapter as the complete list of Java mistakes, it isn't, it's just the handful the original deck happened to flag, and real practice will surface plenty more over time. And don't fix the symptom instead of the cause, wrapping a null pointer exception in a try-catch, from last chapter, instead of fixing why the object was never constructed in the first place, just buries the real bug.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Use == for primitives, .equals() for objects.</li>
      <li><span class="check">&#10003;</span>int / int truncates; make at least one operand a floating-point type to keep the fraction.</li>
      <li><span class="check">&#10003;</span>NullPointerException means something was used before it was constructed &mdash; always initialize before use.</li>
      <li><span class="check">&#10003;</span>Valid indices run 0 to length - 1 &mdash; never length itself.</li>
    </ul></div>''',
        "speak": "So, to recap this whole checklist. Use double-equals for primitives, dot-equals for objects. Int divided by int truncates, so make at least one operand a floating-point type if you want to keep the fraction. A null pointer exception means something got used before it was ever actually constructed, always initialize before use. And valid indices run from zero to length minus one, never length itself. And remember, this list is expected to grow, it's a living checklist, not a finished one, as real code review and practice surface more of the mistakes people actually make. That's the end of this run of chapters, nice work getting through all of it.",
    },
]
