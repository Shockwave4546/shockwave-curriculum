BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Nested if Statements</h1>
      <p class="scr-sub">Chaining more than two paths together, a subtle trap when braces go missing, and a one-line way to pick a value.</p>
    </div>''',
        "speak": "A plain if-else only ever gives you two paths. Most real robot logic needs more than that, close range, mid range, far range, not just near or far. Let's chain more branches together. And at the end, a compact operator for when all an if-else does is pick a value.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (distance &lt; <span class="n">1.0</span>)
{
    zone = <span class="s">"CLOSE"</span>;
}
<span class="k">else</span> <span class="k">if</span> (distance &lt; <span class="n">3.0</span>)
{
    zone = <span class="s">"MID"</span>;
}
<span class="k">else</span>
{
    zone = <span class="s">"FAR"</span>;
}</code></pre>''',
        "speak": "else-if chains let you pick between three or more paths, and only the first true branch ever runs. Distance under 1, the zone is close. Otherwise, under 3, mid. Otherwise, far. A trailing plain else, no condition attached, catches everything not already matched, and it's optional, but leaving it off means doing nothing at all is a real, possible outcome.",
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
        "speak": "When ifs are nested without braces, an else always attaches to the closest unmatched if, regardless of how you've indented it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (sunny)
    <span class="k">if</span> (hot)
        goToBeach();
<span class="k">else</span> <span class="c">// looks like it belongs to sunny, but it belongs to hot</span>
    bringUmbrella();</code></pre>''',
        "speak": "Look at this one. The else is lined up under if sunny, so it looks like it belongs there. But Java ignores indentation, and attaches it to the closest unmatched if, which is hot. So this brings an umbrella when it's sunny but not hot, and when it isn't sunny at all, nothing happens.",
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
        "speak": "Braces are the fix. The braces around the inner if fence it off completely, so this else can only belong to the outer if, sunny. Now, not sunny means bring an umbrella, exactly what we meant.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">A Missing else Can Leave a Variable Unassigned</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">A local variable must be definitely assigned before it&rsquo;s read.</p>''',
        "speak": "One more trap. Java requires a local variable, one declared inside a method, to be definitely assigned before it's read.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> tier; <span class="c">// local variable, no initial value</span>

<span class="k">if</span> (score &gt;= <span class="n">8</span>)
{
    tier = <span class="s">"ELITE"</span>;
}
<span class="c">// no else &mdash; if score &lt; 8, tier is never assigned</span></code></pre>''',
        "speak": "Here, tier is declared but not yet given a value. If score is at least 8, it gets set to elite. But there's no else, so if score is under 8, tier just never gets assigned at all.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">String</span> tier; <span class="c">// local variable, no initial value</span>

<span class="k">if</span> (score &gt;= <span class="n">8</span>)
{
    tier = <span class="s">"ELITE"</span>;
}
<span class="c">// no else &mdash; if score &lt; 8, tier is never assigned</span>

System.out.<span class="me">println</span>(tier); <span class="c">// won't compile: tier might not be assigned</span></code></pre>''',
        "speak": "And this line won't even compile. Since no branch here is guaranteed to run, the compiler refuses to let you print tier at all. Adding a trailing else that assigns tier, or giving tier a starting value, fixes it.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Choosing Between Two Values with ?:</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">condition ? valueIfTrue : valueIfFalse</p>''',
        "speak": "Last idea. Sometimes an if-else exists only to pick one of two values for the same variable. For that, Java has the conditional operator, question mark, colon, often called the ternary operator, because it has three parts.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> speed;
<span class="k">if</span> (boosted)
{
    speed = <span class="n">1.0</span>;
}
<span class="k">else</span>
{
    speed = <span class="n">0.5</span>;
}</code></pre>''',
        "speak": "Here's the long way. If boosted, speed is 1 point 0, otherwise, 0 point 5. Nine lines, just to choose a number.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> speed;
<span class="k">if</span> (boosted)
{
    speed = <span class="n">1.0</span>;
}
<span class="k">else</span>
{
    speed = <span class="n">0.5</span>;
}</code></pre>
<pre class="code"><code><span class="k">double</span> speed = boosted ? <span class="n">1.0</span> : <span class="n">0.5</span>;</code></pre>''',
        "speak": "And here's the same thing in one line. double speed equals, boosted, question mark, 1 point 0, colon, 0 point 5. Read it as condition, question mark, value if true, colon, value if false. Java checks the condition, then produces exactly one of the two values. Use it for short value choices, and keep a regular if-else when a branch needs to actually do things, not just produce a value.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using separate ifs instead of else if &mdash; each is checked independently; a later one can silently overwrite what an earlier one just set.</li>
      <li><span class="check">!</span>Relying on indentation instead of braces &mdash; Java ignores indentation entirely; only braces determine which if an else belongs to.</li>
      <li><span class="check">!</span>Skipping the trailing else when a local variable is only assigned inside branches &mdash; the compiler won't let you read a possibly-unassigned variable.</li>
      <li><span class="check">!</span>Stacking ternaries &mdash; a ? x : b ? y : z is legal but hard to read; use an else if chain for three or more choices.</li>
    </ul></div>''',
        "speak": "Four pitfalls, all of which we just walked through. Using separate ifs instead of else-if, each is checked independently, and a later one can silently overwrite what an earlier one just set. Relying on indentation instead of braces, Java ignores indentation entirely, only actual braces determine which if an else belongs to. Skipping the trailing else when a local variable is only assigned inside branches, the compiler won't let you read a variable that isn't guaranteed to be assigned, so add an else, or give it a starting value. And stacking ternaries, one inside another, is legal, but hard to read, for three or more choices, use an else-if chain.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>else if chains pick exactly one branch &mdash; the first condition that's true.</li>
      <li><span class="check">&#10003;</span>Unconnected, separate if statements are checked independently and can overwrite each other.</li>
      <li><span class="check">&#10003;</span>An else attaches to the nearest unmatched if &mdash; braces are the only reliable control.</li>
      <li><span class="check">&#10003;</span>condition ? a : b picks one of two values in a single expression.</li>
    </ul></div>''',
        "speak": "So: else-if chains pick exactly one branch, the first condition that comes up true, and nothing after it. Unconnected, separate if statements are checked independently, and can overwrite each other's results. And an else always attaches to the nearest unmatched if, braces are the only reliable way to control that. And condition, question mark, a, colon, b, picks one of two values in a single expression, a compact stand-in for an if-else that only assigns. Next up, lesson 5.6, combining multiple conditions together with and, or, and not.",
    },
]
