# Covers both 5.1 (if Statements) and 5.2 (For Loops) — combined lesson item, per the outline.

BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>if Statements &amp; For Loops</h1>
      <p class="scr-sub">Where robot code stops running top-to-bottom and starts making decisions.</p>
    </div>''',
        "speak": "Everything up through Chapter 4 ran top to bottom, one line after another, no exceptions. Chapter 5 changes that. First up, two of the most important tools you'll ever write, if statements and for loops.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">if: One-Way Selection</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Runs its body only when a boolean condition is true.</p>''',
        "speak": "An if statement runs its body only when a boolean condition is true. That's the whole idea.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (joystick.getRawButton(<span class="n">1</span>))
{
    intake.spin(<span class="n">0.5</span>);
}</code></pre>''',
        "speak": "If the joystick's first button is being held down, spin the intake at half power. If that button isn't pressed, this whole block just gets skipped, and execution carries on right past it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (joystick.getRawButton(<span class="n">1</span>))
{
    intake.spin(<span class="n">0.5</span>);
}
<span class="k">else</span>
{
    intake.stop();
}</code></pre>''',
        "speak": "Add an else, and now there's a second branch, one that runs specifically when the condition is false. Button held, spin the intake, button not held, stop it. Exactly one of these two blocks runs, never both, never neither.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Always Use Curly Braces</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Java doesn't require them for a single statement &mdash; but skipping them is how bugs happen.</p>''',
        "speak": "Always wrap the body in curly braces, even for a single statement. Java technically doesn't require them, but skipping them is exactly how the classic which-statement-is-actually-inside-the-if bug happens, someone adds a second line later, assumes it's still inside the if, and it silently isn't.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (isCold = <span class="k">true</span>)</code></pre>''',
        "speak": "Here's a real, sneaky mistake. One equals sign assigns a value, two equals signs test whether a value equals something. Writing if, is cold, single equals, true, actually compiles, it's a legal assignment expression, but it silently does the wrong thing, it assigns true to is cold, and the condition itself is always true, no matter what is cold used to be. Double-check your equals signs inside every condition you write.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">For Loops: Three Parts, One Line</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Initialize, test, update &mdash; bundled into one header.</p>''',
        "speak": "Now, for loops. A for loop bundles the three steps of a loop, initialize, test, update, into a single header line.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; sensors.length; i++)
{
    <span class="k">if</span> (sensors[i].isFaulty())
    {
        report(sensors[i]);
    }
}</code></pre>''',
        "speak": "int i equals 0 initializes the loop variable. i less than sensors dot length is the test, run again as long as this is true. i plus-plus updates it after every pass. Inside, we check each sensor in turn, and report it if it's faulty. The three parts are always separated by semicolons, and always in this order, initialize, test, update.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Starting at 0 vs. Starting at 1</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">0 pairs naturally with &lt; &mdash; 1 pairs naturally with &lt;=.</p>''',
        "speak": "One detail worth internalizing, starting at 0 pairs naturally with less-than, starting at 1 pairs naturally with less-than-or-equal. Pick whichever combination actually matches how many times you want the loop to run.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Missing curly braces &mdash; only the very next line is part of the body; everything after runs unconditionally, every time.</li>
      <li><span class="check">!</span>= instead of == in a condition &mdash; compiles fine, and the condition is silently always true.</li>
      <li><span class="check">!</span>Off-by-one in a for loop's bound &mdash; i &lt;= sensors.length runs one iteration too many and reads past the end.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Missing curly braces, without them, only the very next line is actually part of the if or the loop, everything written after it runs unconditionally, every single time. A single equals instead of a double equals inside a condition, it compiles fine, and the condition is silently, permanently true. And an off-by-one in a for loop's bound, i less-than-or-equal sensors dot length runs one iteration too many, and reads straight past the end of the array.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>if runs its body only when its condition is true; else gives it a second branch.</li>
      <li><span class="check">&#10003;</span>Always use curly braces around a conditional or loop body.</li>
      <li><span class="check">&#10003;</span>== tests equality; = assigns. Confusing them compiles but silently breaks the logic.</li>
      <li><span class="check">&#10003;</span>A for loop's header is initialize, test, update, always in that order.</li>
    </ul></div>''',
        "speak": "So: if runs its body only when its condition is true, else gives it a second branch for when it's false. Always use curly braces around any conditional or loop body. Double equals tests equality, single equals assigns, confusing them compiles but silently breaks your logic. And a for loop's header is always initialize, test, update, in that order. Next up, lesson 5.3, the three building blocks every algorithm is actually made of.",
    },
]
