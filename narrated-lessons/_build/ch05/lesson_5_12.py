BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>switch Statements and Expressions</h1>
      <p class="scr-sub">One value, many fixed choices &mdash; and a way to turn the choice straight into a value.</p>
    </div>''',
        "speak": "Last lesson in Chapter 5. When one value decides between many fixed choices, an else-if chain ends up comparing the same variable over and over. A switch says it directly, look at one value, then jump to the case that matches it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> autoMode = <span class="n">2</span>;

<span class="k">switch</span> (autoMode)
{
    <span class="k">case</span> <span class="n">1</span>:
        System.out.<span class="me">println</span>(<span class="s">"Drive forward"</span>);
        <span class="k">break</span>;
    <span class="k">case</span> <span class="n">2</span>:
        System.out.<span class="me">println</span>(<span class="s">"Score one piece"</span>);
        <span class="k">break</span>;
    <span class="k">case</span> <span class="n">3</span>:
        System.out.<span class="me">println</span>(<span class="s">"Score two pieces"</span>);
        <span class="k">break</span>;
    <span class="k">default</span>:
        System.out.<span class="me">println</span>(<span class="s">"Do nothing"</span>);
        <span class="k">break</span>;
}</code></pre>''',
        "speak": "Here auto mode is 2. Java evaluates the value in parentheses once, jumps to the case whose label matches, case 2, and runs the statements from there, printing score one piece. Then break ends the whole switch, the same break that leaves a loop early, from lesson 5.8. And default runs when no label matches, like the trailing else of an else-if chain. It's optional in a switch statement, but leaving it off makes doing nothing a real outcome.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Case Labels Are Fixed Values</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Switch on an int, a char, a String, or an enum &mdash; not a long, double, or boolean.</p>''',
        "speak": "Case labels must be fixed values, like 2, or the text red, never a condition, like auto mode greater than 2. For ranges, use an if-else chain. And you can switch on an int, a char, a String, or an enum, which is Chapter 11, but not on a long, a double, or a boolean.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Fall-Through</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Without a break, execution keeps running into the next case.</p>''',
        "speak": "Now the part that trips people up. Leave out a break, and execution doesn't stop at the next label. It falls through, and keeps running the following case's statements, ignoring that case's label, until it reaches a break, or the end of the switch.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">switch</span> (autoMode)
{
    <span class="k">case</span> <span class="n">1</span>:
        System.out.<span class="me">println</span>(<span class="s">"Drive forward"</span>);
        <span class="c">// no break: falls through into case 2</span>
    <span class="k">case</span> <span class="n">2</span>:
        System.out.<span class="me">println</span>(<span class="s">"Score one piece"</span>);
        <span class="k">break</span>;
    <span class="k">default</span>:
        System.out.<span class="me">println</span>(<span class="s">"Do nothing"</span>);
        <span class="k">break</span>;
}</code></pre>''',
        "speak": "With auto mode set to 1, this prints drive forward, and then, because there's no break, it falls straight into case 2 and prints score one piece as well. Fall-through is occasionally what you want, but far more often, it's a forgotten break.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">switch</span> (buttonNumber)
{
    <span class="k">case</span> <span class="n">1</span>, <span class="n">2</span>:
        System.out.<span class="me">println</span>(<span class="s">"Intake"</span>);
        <span class="k">break</span>;
    <span class="k">case</span> <span class="n">3</span>:
        System.out.<span class="me">println</span>(<span class="s">"Shoot"</span>);
        <span class="k">break</span>;
    <span class="k">default</span>:
        System.out.<span class="me">println</span>(<span class="s">"Unmapped button"</span>);
        <span class="k">break</span>;
}</code></pre>''',
        "speak": "When several values should do the same thing, list them in one case, separated by commas. Buttons 1 and 2 both run the intake. Older code gets the same effect with fall-through, stacking case 1 and case 2 on separate lines with nothing between them, but the comma form says it more clearly.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> alliance = <span class="s">"RED"</span>;

<span class="k">switch</span> (alliance)
{
    <span class="k">case</span> <span class="s">"RED"</span>:
        System.out.<span class="me">println</span>(<span class="s">"Start on the left"</span>);
        <span class="k">break</span>;
    <span class="k">case</span> <span class="s">"BLUE"</span>:
        System.out.<span class="me">println</span>(<span class="s">"Start on the right"</span>);
        <span class="k">break</span>;
    <span class="k">default</span>:
        System.out.<span class="me">println</span>(<span class="s">"Unknown alliance"</span>);
        <span class="k">break</span>;
}</code></pre>''',
        "speak": "You can switch on a String, too. A String case matches only the exact same text, capital letters included, so lowercase red would land in default. Chapter 6 explains how Java compares Strings.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Arrow Form: No Fall-Through</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">case ... -&gt; gives each case its own body, with no break to forget.</p>''',
        "speak": "There's a second way to write cases. Put an arrow after the label instead of a colon, and each case gets its own separate body. It never falls through, so there's no break to forget.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">switch</span> (autoMode)
{
    <span class="k">case</span> <span class="n">1</span> -&gt; System.out.<span class="me">println</span>(<span class="s">"Drive forward"</span>);
    <span class="k">case</span> <span class="n">2</span> -&gt;
    {
        System.out.<span class="me">println</span>(<span class="s">"Score one piece"</span>);
        System.out.<span class="me">println</span>(<span class="s">"Then back up"</span>);
    }
    <span class="k">case</span> <span class="n">3</span>, <span class="n">4</span> -&gt; System.out.<span class="me">println</span>(<span class="s">"Score two pieces"</span>);
    <span class="k">default</span> -&gt; System.out.<span class="me">println</span>(<span class="s">"Do nothing"</span>);
}</code></pre>''',
        "speak": "A case with one statement puts it right after the arrow. A case with several, like case 2 here, wraps them in braces. Case 3 comma 4 lists two labels again. One switch has to use one form throughout, you can't mix colon cases and arrow cases. And for new code, the arrow form is usually the better choice.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">switch Expressions</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">A switch can produce a value &mdash; like ?:, but for any number of choices.</p>''',
        "speak": "A switch can also produce a value, the way the question-mark-colon operator does in lesson 5.5, but for any number of choices.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> autoMode = <span class="n">3</span>;

<span class="t">String</span> plan = <span class="k">switch</span> (autoMode)
{
    <span class="k">case</span> <span class="n">1</span> -&gt; <span class="s">"Drive forward"</span>;
    <span class="k">case</span> <span class="n">2</span> -&gt; <span class="s">"Score one piece"</span>;
    <span class="k">case</span> <span class="n">3</span>, <span class="n">4</span> -&gt; <span class="s">"Score two pieces"</span>;
    <span class="k">default</span> -&gt; <span class="s">"Do nothing"</span>;
};

System.out.<span class="me">println</span>(plan); <span class="c">// Score two pieces</span></code></pre>''',
        "speak": "String plan equals switch, auto mode. Each case's value becomes the value of the whole switch, so with auto mode 3, plan is score two pieces. Two rules come with that. The semicolon after the closing brace is required, because the switch is part of an assignment statement. And a switch expression must be exhaustive, every possible value has to produce a result, so a switch expression on an int or a String needs a default.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> speed = <span class="k">switch</span> (gear)
{
    <span class="k">case</span> <span class="n">1</span> -&gt; <span class="n">0.3</span>;
    <span class="k">case</span> <span class="n">2</span> -&gt; <span class="n">0.6</span>;
    <span class="k">case</span> <span class="n">3</span> -&gt;
    {
        System.out.<span class="me">println</span>(<span class="s">"Top gear: watch the corners"</span>);
        <span class="k">yield</span> <span class="n">1.0</span>;
    }
    <span class="k">default</span> -&gt; <span class="n">0.0</span>;
};</code></pre>''',
        "speak": "If a case needs to do some work before producing its value, give it a block, and hand the value back with yield. In gear 3, we print a warning, then yield 1 point 0 as the switch's value. yield means, this is the switch's value, while return would try to leave the whole method instead. yield also replaces break if you ever write a switch expression in the colon form.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">switch and Enums &mdash; Ch.11</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Java 21+: case INTAKE or case ArmPosition.INTAKE. Java 17: bare name only.</p>''',
        "speak": "switch is at its best with enums, the named sets of choices Chapter 11 introduces, and that chapter picks up right where this lesson leaves off. One version note to carry there. On Java 21 and later, including Java 25, this course's target, an enum case label can be written either bare, just intake, or qualified with the enum's name, arm position dot intake. On Java 17, only the bare name compiles. Everything else in this lesson has been standard since Java 14, so it works the same on Java 17 and 25.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting break in the colon form &mdash; execution falls through into the next case. The arrow form can't fall through.</li>
      <li><span class="check">!</span>Writing a condition as a case label &mdash; case autoMode &gt; 2: won't compile. Use if/else for ranges.</li>
      <li><span class="check">!</span>Leaving out default in a switch expression on an int or String &mdash; it won't compile.</li>
      <li><span class="check">!</span>Forgetting the semicolon after a switch expression's closing brace.</li>
      <li><span class="check">!</span>Switching on a String that might be null &mdash; it throws a NullPointerException, even with a default.</li>
    </ul></div>''',
        "speak": "Five pitfalls. Forgetting break in the colon form, execution falls through and runs the next case too, the arrow form can't fall through, which is a good reason to prefer it. Writing a condition as a case label, that won't compile, labels are fixed values, so use an if-else chain for ranges. Leaving out default in a switch expression on an int or a String, it won't compile, because some values would have no result. Forgetting the semicolon after a switch expression, it ends an assignment, like any other. And switching on a String that might be null, the switch throws a Null Pointer Exception before it checks any case, even default.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A switch matches one value against fixed case labels: int, char, String, or enum.</li>
      <li><span class="check">&#10003;</span>Colon form: each case needs a break, or it falls through. default catches the rest.</li>
      <li><span class="check">&#10003;</span>Arrow form never falls through; case 1, 2 lists several labels.</li>
      <li><span class="check">&#10003;</span>A switch expression produces a value and must cover every input.</li>
      <li><span class="check">&#10003;</span>yield hands back a value from a multi-line case block.</li>
      <li><span class="check">&#10003;</span>Java 21+ allows qualified enum labels; Java 17 needs the bare name.</li>
    </ul></div>''',
        "speak": "So: a switch matches one value against fixed case labels, and works on ints, chars, Strings, and enums. In the colon form, each case needs a break, or it falls through into the next one, and default catches every value no label matched. The arrow form never falls through, and case 1 comma 2 lists several labels for one action. A switch expression produces a value, and must cover every possible input, so int and String switch expressions need a default. yield hands back the value from a multi-line block. And on Java 21 and later, an enum case label may be qualified, while Java 17 accepts only the bare name. That wraps up Chapter 5, control structures, if statements, loops, boolean logic, and now switch. Nice work getting through all of it.",
    },
]
