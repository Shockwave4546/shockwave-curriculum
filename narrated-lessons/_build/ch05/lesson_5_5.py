BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Nested if Statements</h1>
      <p class="scr-sub">Chaining more than two possible paths together &mdash; and a subtle trap when braces go missing.</p>
    </div>''',
        "speak": "A plain if-else only ever gives you two paths. Most real robot logic needs more than that, close range, mid range, far range, not just near or far. Let's chain more branches together.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (distance &lt; <span class="n">1.0</span>)
{
    state = IntakeState.CLOSE;
}
<span class="k">else</span> <span class="k">if</span> (distance &lt; <span class="n">3.0</span>)
{
    state = IntakeState.MID;
}
<span class="k">else</span>
{
    state = IntakeState.FAR;
}</code></pre>''',
        "speak": "else-if chains let you pick between three or more paths, and only the first true branch ever runs. Distance under 1, close. Otherwise, under 3, mid. Otherwise, far. A trailing plain else, no condition attached, catches everything not already matched, and it's optional, but leaving it off means doing nothing at all is a real, possible outcome.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Chained vs. Separate ifs</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">else if connects branches so only one runs. Separate ifs are checked independently.</p>''',
        "speak": "else-if connects the branches together, only one of them ever runs. Writing separate, unconnected if statements instead is a genuinely different, and often wrong, thing entirely, because all of them get checked independently.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// Connected &mdash; only one branch runs</span>
<span class="k">if</span> (score &gt;= <span class="n">90</span>) { grade = <span class="s">"A"</span>; }
<span class="k">else</span> <span class="k">if</span> (score &gt;= <span class="n">80</span>) { grade = <span class="s">"B"</span>; }
<span class="k">else</span> { grade = <span class="s">"C"</span>; }</code></pre>''',
        "speak": "Connected, with else-if, only one branch runs, ever. A score of 95 hits the first condition, gets graded A, and every branch after it is skipped entirely.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// Connected &mdash; only one branch runs</span>
<span class="k">if</span> (score &gt;= <span class="n">90</span>) { grade = <span class="s">"A"</span>; }
<span class="k">else</span> <span class="k">if</span> (score &gt;= <span class="n">80</span>) { grade = <span class="s">"B"</span>; }
<span class="k">else</span> { grade = <span class="s">"C"</span>; }

<span class="c">// NOT connected &mdash; multiple could run, overwriting each other</span>
<span class="k">if</span> (score &gt;= <span class="n">90</span>) { grade = <span class="s">"A"</span>; }
<span class="k">if</span> (score &gt;= <span class="n">80</span>) { grade = <span class="s">"B"</span>; } <span class="c">// a 95 would hit this too, overwriting "A" with "B"!</span></code></pre>''',
        "speak": "Now the unconnected version, two completely separate if statements. A 95 hits the first one, sets grade to A, but then hits this second, independent if too, since 95 is also greater than or equal to 80, and silently overwrites A with B. Same score, wrong final grade, purely because the ifs weren't chained together.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Dangling Else</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">An else always attaches to the closest unmatched if &mdash; regardless of indentation.</p>''',
        "speak": "When ifs are nested without braces, an else always attaches to the closest unmatched if, regardless of how you've indented it. If that's not what you meant, braces are the fix.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (sunny)
{
    <span class="k">if</span> (hot)
    {
        goToBeach();
    }
}
<span class="k">else</span> <span class="c">// now belongs to the OUTER if, thanks to the braces</span>
{
    bringUmbrella();
}</code></pre>''',
        "speak": "Here the braces around the inner if fence it off completely, so this else can only belong to the outer if, sunny. Without those braces, Java would attach the else to the nearest if instead, hot, and you'd bring an umbrella exactly backwards from what you meant.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> tier; <span class="c">// local variable, no initial value</span>

<span class="k">if</span> (score &gt;= <span class="n">8</span>)
{
    tier = <span class="s">"ELITE"</span>;
}
<span class="c">// no else &mdash; if score &lt; 8, tier is never assigned</span></code></pre>''',
        "speak": "One more trap. Here, tier is declared but not yet given a value. If score is at least 8, it gets set to elite. But there's no else, so if score is under 8, tier just never gets assigned at all.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> tier; <span class="c">// local variable, no initial value</span>

<span class="k">if</span> (score &gt;= <span class="n">8</span>)
{
    tier = <span class="s">"ELITE"</span>;
}
<span class="c">// no else &mdash; if score &lt; 8, tier is never assigned</span>

System.out.<span class="me">println</span>(tier); <span class="c">// won't compile: tier might not be assigned</span></code></pre>''',
        "speak": "And this line won't even compile. Java requires a local variable to be definitely assigned before it's read, and since no branch here is guaranteed to run, the compiler refuses to let you print tier at all. This only applies to local variables, an instance variable like state from a couple of beats ago already has a default value, so it doesn't need every branch to cover it.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using separate ifs instead of else if &mdash; each is checked independently; a later one can silently overwrite what an earlier one just set.</li>
      <li><span class="check">!</span>Relying on indentation instead of braces &mdash; Java ignores indentation entirely; only braces determine which if an else belongs to.</li>
      <li><span class="check">!</span>Skipping the trailing else when a local variable is only assigned inside branches &mdash; the compiler won't let you read a possibly-unassigned variable.</li>
    </ul></div>''',
        "speak": "Three pitfalls, all of which we just walked through directly. Using separate ifs instead of else-if, each is checked independently, and a later one can silently overwrite what an earlier one just set. Relying on indentation instead of braces, Java ignores indentation entirely, only actual braces determine which if an else belongs to. And skipping the trailing else when a local variable is only assigned inside branches, the compiler simply won't let you read a variable that isn't guaranteed to be assigned.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>else if chains pick exactly one branch &mdash; the first condition that's true.</li>
      <li><span class="check">&#10003;</span>Unconnected, separate if statements are checked independently and can overwrite each other.</li>
      <li><span class="check">&#10003;</span>An else attaches to the nearest unmatched if &mdash; braces are the only reliable control.</li>
    </ul></div>''',
        "speak": "So: else-if chains pick exactly one branch, the first condition that comes up true, and nothing after it. Unconnected, separate if statements are checked independently, and can overwrite each other's results. And an else always attaches to the nearest unmatched if, braces are the only reliable way to control that. Next up, lesson 5.6, combining multiple conditions together with and, or, and not.",
    },
]
