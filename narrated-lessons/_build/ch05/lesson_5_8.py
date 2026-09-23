BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>While Loops</h1>
      <p class="scr-sub">Repetition when you're waiting for a condition, not counting to a known number.</p>
    </div>''',
        "speak": "for loops are great when you already know how many times to run. But sometimes you don't, you're just waiting for something to become true. That's exactly what while loops are for.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> attempts = <span class="n">0</span>;             <span class="c">// 1. initialize</span></code></pre>''',
        "speak": "Every loop, no matter its shape, needs the same three steps. First, initialize. attempts starts at 0.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> attempts = <span class="n">0</span>;             <span class="c">// 1. initialize</span>
<span class="k">while</span> (attempts &lt; <span class="n">3</span> &amp;&amp; !connected) { <span class="c">// 2. test</span></code></pre>''',
        "speak": "Second, test. This while loop keeps going as long as attempts is under 3, and we're still not connected. And critically, that test runs before every single pass, including the very first one.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> attempts = <span class="n">0</span>;             <span class="c">// 1. initialize</span>
<span class="k">while</span> (attempts &lt; <span class="n">3</span> &amp;&amp; !connected) { <span class="c">// 2. test</span>
    connected = tryConnect();
    attempts++;                <span class="c">// 3. update</span>
}</code></pre>''',
        "speak": "And third, update, right inside the body. attempts plus-plus, after every attempt. A for loop, from lesson 5.1, just packs all three of these steps into one header line, a while loop spreads them out, which feels far more natural when the update isn't a simple counter, here it's really connected changing based on whether try connect succeeded.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Infinite Loops</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Forget step 3, and the condition never changes.</p>''',
        "speak": "Forget step 3, and the condition never changes, so the loop just runs forever.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> i = <span class="n">0</span>;
<span class="k">while</span> (i &lt; <span class="n">10</span>)
{
    System.out.<span class="me">println</span>(i); <span class="c">// i never changes &mdash; this never stops</span>
}</code></pre>''',
        "speak": "Here, i starts at 0, and the loop keeps printing it forever, because nothing inside the body ever touches i. On a robot, an infinite loop like this doesn't just print forever, it can freeze the robot's entire control loop, since nothing written after it ever gets a chance to run.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">while vs. for</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">for fits a known count; while fits waiting for a condition.</p>''',
        "speak": "for fits naturally when you already know the number of iterations. while fits better when you're waiting for a condition, not counting to a fixed number, waiting for a sensor to settle, or retrying a connection a limited number of times.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">while</span> (!gyro.isConnected() &amp;&amp; attempts &lt; <span class="n">5</span>)
{
    attempts++;
}</code></pre>''',
        "speak": "Not gyro dot is connected, and attempts under 5. Keep trying, but only up to 5 attempts, this is exactly the retry-a-limited-number-of-times shape while loops are built for.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting to update the loop variable &mdash; the single most common cause of an infinite loop.</li>
      <li><span class="check">!</span>A condition that's false from the very first check &mdash; the loop body never runs at all, not even once.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Forgetting to update the loop variable, the single most common cause of an infinite loop, every while loop needs something inside it that eventually makes the condition false. And a condition that's false from the very first check, if it never holds, the loop body never runs, not even once, double-check the loop variable's starting value against the condition before you rely on it.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Every loop needs three steps: initialize, test, update.</li>
      <li><span class="check">&#10003;</span>while checks its condition before every pass, including the first.</li>
      <li><span class="check">&#10003;</span>Forgetting to update the loop variable is the classic cause of an infinite loop.</li>
      <li><span class="check">&#10003;</span>while fits waiting for a condition; for fits a known iteration count.</li>
    </ul></div>''',
        "speak": "So: every loop needs three steps, initialize, test, update, while loops just spell them out separately instead of packing them into one header. while checks its condition before every pass, including the very first. Forgetting to update the loop variable is the classic cause of an infinite loop, which can genuinely freeze a robot's control code. And while fits waiting for a condition, for fits a known iteration count. Next up, lesson 5.9, real patterns built from loops and selection working together.",
    },
]
