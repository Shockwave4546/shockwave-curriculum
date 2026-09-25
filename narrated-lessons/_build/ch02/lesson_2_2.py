BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 2 &middot; Variables &amp; Types</div>
      <h1>Expressions &amp; Output</h1>
      <p class="scr-sub">Printing values, and the math trap that catches almost everyone once.</p>
    </div>''',
        "speak": "Now that we can hold values in variables, let's actually do something with them, print them out, and combine them with math. There's one gotcha in here that trips up almost every new Java programmer exactly once.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Ways to Print</h2><ul>
      <li><span class="num">1</span><span><strong>System.out.println</strong> &mdash; prints, then moves to a new line.</span></li>
    </ul></div>''',
        "speak": "There are two ways to print in Java. System dot out dot print line prints its value, then moves to a new line.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Ways to Print</h2><ul>
      <li><span class="num">1</span><span><strong>System.out.println</strong> &mdash; prints, then moves to a new line.</span></li>
      <li><span class="num">2</span><span><strong>System.out.print</strong> &mdash; prints, and stays on the same line.</span></li>
    </ul></div>''',
        "speak": "And System dot out dot print, no ln on the end, prints its value but stays right where it is, on the same line.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">print</span>(<span class="s">"Score: "</span>);
System.out.<span class="me">println</span>(<span class="n">24</span>);
<span class="c">// Output: Score: 24</span></code></pre>''',
        "speak": "Watch what happens combining them. Print writes Score, colon, space, and holds the cursor right there. Print line then writes 24 immediately after it, on that same line, before finally moving down. The result is one clean line, Score: 24.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> score = <span class="n">24</span>;
System.out.<span class="me">println</span>(<span class="s">"Score: "</span> + score); <span class="c">// Score: 24</span></code></pre>''',
        "speak": "Plus doesn't just add numbers. Between a String and anything else, it joins them into one longer piece of text instead. int score equals 24, print line of quote Score colon quote plus score, prints Score: 24. You've already been doing this in every worked example so far.",
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">println</span>(<span class="s">"a"</span> + <span class="n">1</span> + <span class="n">2</span>); <span class="c">// a12 — "a"+1 makes "a1" (text), then +2 makes "a12" (text)</span>
System.out.<span class="me">println</span>(<span class="n">1</span> + <span class="n">2</span> + <span class="s">"a"</span>); <span class="c">// 3a  — 1+2 makes 3 (math) first, then +"a" makes "3a" (text)</span></code></pre>''',
        "speak": "Here's the catch: plus still runs left to right, so where the text shows up changes the result. Quote a quote plus 1 plus 2 prints a12, because quote a quote plus 1 makes the text a1 first, then plus 2 tacks on a 2 as more text. But 1 plus 2 plus quote a quote prints 3a, because 1 plus 2 does the math first, giving 3, and only then does plus quote a quote turn it into text. Once a plus touches a String, everything after it becomes text-joining, left to right, there's no going back to math mode later in the same line.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">println</span>(<span class="s">"Line one\\\\nLine two"</span>); <span class="c">// prints on two separate lines</span>
System.out.<span class="me">println</span>(<span class="s">"She said \\\\"go\\\\""</span>); <span class="c">// She said "go"</span></code></pre>''',
        "speak": "Text inside quotes can also hold escape sequences, a backslash followed by a letter, meaning something other than a literal character. Backslash n is a new line, backslash t is a tab, backslash quote is a literal quote mark inside the text, and double backslash is a literal backslash. Line one, backslash n, Line two prints on two separate lines, and She said backslash-quote go backslash-quote prints She said, in quotes, go, in quotes.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Math Works Like You'd Expect&hellip;</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:44ch;margin:0 auto;">Plus, minus, times, divide &mdash; with one big exception.</p>''',
        "speak": "Plus, minus, times, divide all work the way you'd expect, with one big exception, and it's the single most common source of wrong-answer, no-error-message bugs you will personally run into.",
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">println</span>(<span class="n">7</span> / <span class="n">2</span>); <span class="c">// prints 3, not 3.5</span></code></pre>''',
        "speak": "7 divided by 2 prints 3. Not 3 point 5. Dividing two whole numbers throws away the decimal part entirely, it doesn't round, it just chops it off. This is called truncating division.",
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">println</span>(<span class="n">7.0</span> / <span class="n">2</span>); <span class="c">// prints 3.5</span></code></pre>''',
        "speak": "The fix is simple, if you want the decimal part, at least one of the two numbers needs to be a double. 7 point 0 divided by 2 prints 3 point 5, exactly what you'd hope for.",
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">println</span>(<span class="n">2</span> + <span class="n">3</span> * <span class="n">2</span>);   <span class="c">// 8</span>
System.out.<span class="me">println</span>((<span class="n">2</span> + <span class="n">3</span>) * <span class="n">2</span>); <span class="c">// 10</span></code></pre>''',
        "speak": "Order of operations is exactly the same as math class, times and divide happen before plus and minus. 2 plus 3 times 2 is 8, because the multiplication happens first. Wrap it in parentheses, 2 plus 3, times 2, and now it's 10, parentheses override everything else.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Remainder Operator: %</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:44ch;margin:0 auto;">5 percent 2 is 1 &mdash; 2 fits into 5 twice, with 1 left over.</p>''',
        "speak": "One more operator worth knowing, the percent sign, which gives you the remainder, whatever's left over after dividing. 5 percent 2 is 1, because 2 fits into 5 twice, with 1 left over.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> totalSeconds = <span class="n">150</span>;
System.out.<span class="me">println</span>(totalSeconds / <span class="n">60</span>); <span class="c">// 2 &mdash; whole minutes</span></code></pre>''',
        "speak": "Here's a real use for it. 150 total seconds. Dividing by 60 gives 2, that's the whole minutes.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> totalSeconds = <span class="n">150</span>;
System.out.<span class="me">println</span>(totalSeconds / <span class="n">60</span>); <span class="c">// 2 &mdash; whole minutes</span>
System.out.<span class="me">println</span>(totalSeconds % <span class="n">60</span>); <span class="c">// 30 &mdash; leftover seconds</span>
<span class="c">// 150 seconds = 2 minutes, 30 seconds</span></code></pre>''',
        "speak": "And 150 percent 60 gives 30, the leftover seconds that didn't make a full minute. Put together, 150 seconds is 2 minutes and 30 seconds, and that division-plus-remainder pair is exactly how you'd split any total into two units like that. One more wrinkle: percent binds just as tightly as times and divide, so the same order-of-operations rule applies, and it behaves a little differently with negative numbers than you might expect. Negative 7 divided by 2 is negative 3, still truncated toward zero, not rounded down, and negative 7 percent 2 is negative 1, the remainder keeps the sign of the number being divided.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Dividing two whole numbers and expecting a decimal &mdash; it truncates instead. Check whether at least one side is a double.</li>
      <li><span class="check">!</span>Dividing by zero &mdash; whole-number division by 0 crashes the program; decimal division by 0.0 gives a nonsense result instead.</li>
    </ul></div>''',
        "speak": "Two pitfalls to watch for. Dividing two whole numbers and expecting a decimal, it'll truncate instead, so check whether at least one side is a double. And dividing by zero, whole-number division by zero crashes your program outright, decimal division by zero point zero doesn't crash, but it hands you back a nonsense result, infinity or not-a-number, which is really a sign something upstream already went wrong.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>print stays on the line; println moves to a new one.</li>
      <li><span class="check">&#10003;</span>Dividing two whole numbers truncates instead of rounding.</li>
      <li><span class="check">&#10003;</span>Times and divide happen before plus and minus, unless parentheses say otherwise.</li>
      <li><span class="check">&#10003;</span>% gives the remainder &mdash; useful for splitting a total into two units.</li>
    </ul></div>''',
        "speak": "To recap: print stays on the line, print line moves to a new one. Dividing two whole numbers truncates instead of rounding, use a double if you need the decimal. Joining text and values with plus runs left to right, so where the text shows up changes the result. Times and divide happen before plus and minus, unless parentheses say otherwise. And the remainder operator gives you what's left over after division, which is exactly how you split a total into two units. Next time, lesson 2.3, we'll look at assignment more closely, and where input actually comes from.",
    },
]
