BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>While Loops</h1>
      <p class="scr-sub">Repetition when you're waiting for a condition, not counting to a known number.</p>
    </div>''',
        "speak": "for loops are great when you already know how many times to run. But sometimes you don't, you're just waiting for something to become true. That's exactly what while loops are for. And along the way, a loop that always runs at least once, and two ways to leave a loop early.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> attempts = <span class="n">0</span>;             <span class="c">// 1. initialize</span></code></pre>''',
        "speak": "Every loop, no matter its shape, needs the same three steps. First, initialize. attempts starts at 0.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> attempts = <span class="n">0</span>;             <span class="c">// 1. initialize</span>
<span class="k">while</span> (attempts &lt; <span class="n">3</span> &amp;&amp; !connected) <span class="c">// 2. test</span></code></pre>''',
        "speak": "Second, test. This while loop keeps going as long as attempts is under 3, and we're still not connected. And critically, that test runs before every single pass, including the very first one.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> attempts = <span class="n">0</span>;             <span class="c">// 1. initialize</span>
<span class="k">while</span> (attempts &lt; <span class="n">3</span> &amp;&amp; !connected) <span class="c">// 2. test</span>
{
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
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">for fits a known count; while fits repeating until a condition changes.</p>''',
        "speak": "for fits naturally when you already know the number of iterations. while fits better when you're repeating until a condition changes, not counting to a fixed number, like retrying a connection a limited number of times.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> attempts = <span class="n">0</span>;
<span class="k">while</span> (!gyro.isConnected() &amp;&amp; attempts &lt; <span class="n">5</span>)
{
    gyro.reconnect(); <span class="c">// assume our gyro class has this retry method</span>
    attempts++;
}</code></pre>''',
        "speak": "Not gyro dot is connected, and attempts under 5. Each pass calls reconnect, a retry method we're assuming our gyro class has, then counts the attempt. This tries at most 5 times, then moves on, whether or not the gyro came back.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Retry, Don&rsquo;t Wait</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Robot code runs in short, repeating cycles &mdash; check once per cycle.</p>''',
        "speak": "What a loop like this must never do is wait. Robot code runs in short, repeating cycles, many times per second, and a loop that sits spinning until a sensor finally responds holds up everything else, the same freeze as an infinite loop. In robot code, check a condition once per cycle, instead of looping until it changes.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">do-while: Run the Body at Least Once</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">The condition is checked after each pass, not before.</p>''',
        "speak": "A do-while loop flips when the check happens. It tests its condition after each pass instead of before, so the body always runs at least once.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> attempts = <span class="n">0</span>;
<span class="k">do</span>
{
    connected = tryConnect();
    attempts++;
} <span class="k">while</span> (!connected &amp;&amp; attempts &lt; <span class="n">3</span>); <span class="c">// this semicolon is required</span></code></pre>''',
        "speak": "This is the very first loop from this lesson, reshaped. The first connection attempt happens unconditionally, and the test at the bottom only decides whether to try again. Notice the semicolon after the closing while, it's required. Use do-while when there's nothing to test until the body has run once, otherwise, a plain while is the usual choice.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Leaving a Loop Early</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">break ends the loop; continue skips to the next pass.</p>''',
        "speak": "Two statements change a loop's flow from inside its body. break ends the loop immediately. continue skips the rest of the current pass, and moves on to the next one.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> port = <span class="n">0</span>; port &lt; <span class="n">10</span>; port++)
{
    <span class="k">if</span> (port == <span class="n">3</span>)
    {
        <span class="k">continue</span>; <span class="c">// port 3 is reserved: skip to the next pass</span>
    }
    <span class="k">if</span> (isFree(port))
    {
        System.out.<span class="me">println</span>(<span class="s">"First free port: "</span> + port);
        <span class="k">break</span>;    <span class="c">// found one: stop the whole loop now</span>
    }
}</code></pre>''',
        "speak": "This loop looks for the first free port. Port 3 is reserved, so continue skips it, jumping straight to the next pass. As soon as a free port turns up, we print it, and break stops the whole loop, there's no point checking the rest. In a for loop, continue still runs the update, port plus-plus, before the next test. In a while loop, it jumps straight to the test. Inside nested loops, both only affect the innermost loop they're in. And break has one more job, ending a case in a switch statement, that's lesson 5.12.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting to update the loop variable &mdash; the single most common cause of an infinite loop.</li>
      <li><span class="check">!</span>A condition that's false from the very first check &mdash; the loop body never runs at all, not even once.</li>
      <li><span class="check">!</span>Leaving off the semicolon after a do-while's condition &mdash; it won't compile. A stray ; after a plain while (...) header empties the loop body.</li>
      <li><span class="check">!</span>A continue in a while loop that skips the update &mdash; the loop repeats the same value forever.</li>
    </ul></div>''',
        "speak": "Four pitfalls. Forgetting to update the loop variable, the single most common cause of an infinite loop, every while loop needs something inside it that eventually makes the condition false. A condition that's false from the very first check, then the loop body never runs, not even once, so double-check the starting value against the condition. Leaving off the semicolon after a do-while's condition, that won't compile, and the opposite mistake, a stray semicolon right after a plain while header, gives the loop an empty body, and an infinite loop if the condition starts true. And a continue in a while loop that jumps past the update, the skipped pass never reaches i plus-plus, so the loop repeats the same value forever.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Every loop needs three steps: initialize, test, update.</li>
      <li><span class="check">&#10003;</span>while checks its condition before every pass, including the first.</li>
      <li><span class="check">&#10003;</span>Forgetting to update the loop variable is the classic cause of an infinite loop.</li>
      <li><span class="check">&#10003;</span>while fits repeating until a condition changes; for fits a known iteration count.</li>
      <li><span class="check">&#10003;</span>do-while checks after each pass, so its body always runs at least once.</li>
      <li><span class="check">&#10003;</span>break ends the innermost loop; continue skips to its next pass.</li>
    </ul></div>''',
        "speak": "So: every loop needs three steps, initialize, test, update, while loops just spell them out separately instead of packing them into one header. while checks its condition before every pass, including the very first. Forgetting to update the loop variable is the classic cause of an infinite loop, which can genuinely freeze a robot's control code. while fits repeating until a condition changes, for fits a known iteration count. A do-while checks after each pass, so its body always runs at least once, and its closing while needs a semicolon. And break ends the innermost loop right away, while continue skips to that loop's next pass. Next up, lesson 5.9, real patterns built from loops and selection working together.",
    },
]
