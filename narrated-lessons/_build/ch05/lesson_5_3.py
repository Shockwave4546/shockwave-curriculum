BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Algorithms with Selection &amp; Repetition</h1>
      <p class="scr-sub">Every algorithm you'll ever write is built from exactly three ingredients.</p>
    </div>''',
        "speak": "We just met if statements and for loops. Let's zoom out for a second, because those two, plus one more idea you've already been using since Chapter 1, are genuinely all you need to build any algorithm at all.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Three Building Blocks</h2><ul>
      <li><span class="num">1</span><span><strong>Sequence</strong> &mdash; steps run in order, one after another.</span></li>
    </ul></div>''',
        "speak": "Sequence, steps run in order, one after another. This is what every program has done from lesson 1.2 onward.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Three Building Blocks</h2><ul>
      <li><span class="num">1</span><span><strong>Sequence</strong> &mdash; steps run in order, one after another.</span></li>
      <li><span class="num">2</span><span><strong>Selection</strong> &mdash; branch based on a true/false decision (if/else).</span></li>
    </ul></div>''',
        "speak": "Selection, branch based on a true or false decision, exactly what if and else give us.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Three Building Blocks</h2><ul>
      <li><span class="num">1</span><span><strong>Sequence</strong> &mdash; steps run in order, one after another.</span></li>
      <li><span class="num">2</span><span><strong>Selection</strong> &mdash; branch based on a true/false decision (if/else).</span></li>
      <li><span class="num">3</span><span><strong>Repetition</strong> &mdash; repeat a block until some condition is met (loops).</span></li>
    </ul></div>''',
        "speak": "And repetition, repeat a block until some condition is met, exactly what a for loop gives us. That's genuinely it, every autonomous routine, every teleop control loop, every piece of robot code you will ever write is some combination of just these three.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Planning Before Coding</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Plain English, a diagram, or pseudocode &mdash; before a single line of real Java.</p>''',
        "speak": "For anything beyond a couple of lines, it genuinely pays to plan the steps before writing real Java, in plain English, a diagram, or pseudocode, informal step-by-step notes that aren't real code, but capture the sequence, selection, and repetition structure. This is the same planning idea from lesson 1.2, just applied to a bigger problem now.",
    },
    {
        "screen": '''<pre class="code"><code>Drive forward until the distance sensor reads &lt; 12 inches</code></pre>''',
        "speak": "Here's pseudocode for a simple autonomous routine. Drive forward until the distance sensor reads less than 12 inches, that's a repetition, keep driving while a condition holds.",
    },
    {
        "screen": '''<pre class="code"><code>Drive forward until the distance sensor reads &lt; 12 inches
If a game piece is detected, run the intake</code></pre>''',
        "speak": "If a game piece is detected, run the intake, that's a selection, a true-or-false branch.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>Drive forward until the distance sensor reads &lt; 12 inches
If a game piece is detected, run the intake
Otherwise, back up and try a different path</code></pre>''',
        "speak": "Otherwise, back up and try a different path, the other side of that same selection. Three lines of plain English, and you can already see sequence, selection, and repetition all showing up. Only after the steps are clear like this does it actually make sense to translate each line into real Java.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Skipping the planning step for a multi-branch routine &mdash; exactly how logic errors sneak in, a wrong branch order, a missed case.</li>
      <li><span class="check">!</span>Assuming "selection" only means if &mdash; any true/false branching decision counts, including the conditions inside loops.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Skipping the planning step for a multi-branch routine, jumping straight to code for anything with several conditions or a loop is exactly how logic errors sneak in, a wrong branch order, a missed case you never wrote pseudocode for. And assuming selection only means if, any true-or-false branching decision counts, including the conditions tucked inside loops themselves.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Every algorithm is built from sequence, selection, and repetition &mdash; nothing else is needed.</li>
      <li><span class="check">&#10003;</span>Pseudocode is a real planning tool &mdash; use it before writing real code for anything with multiple branches or a loop.</li>
    </ul></div>''',
        "speak": "So: every algorithm is built from sequence, selection, and repetition, nothing else is needed, ever. And pseudocode is a real planning tool, not busywork, use it before writing real code for anything with multiple branches or a loop. Next up, lesson 5.4, boolean expressions, the actual conditions that drive every selection and repetition we just talked about.",
    },
]
