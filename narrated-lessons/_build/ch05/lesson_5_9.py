BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 5 &middot; Control Structures</div>
      <h1>Implementing Selection &amp; Iteration Algorithms</h1>
      <p class="scr-sub">A handful of loop shapes that come up constantly &mdash; once you recognize them, you'll see them everywhere.</p>
    </div>''',
        "speak": "We now have everything we need, loops and selection, to actually build something. A handful of shapes come up over and over, let's meet each one. These examples loop over an existing collection with an enhanced for, building your own collections is Chapter 9, for now, focus purely on the shape of each pattern.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Accumulator Pattern</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Initialize before the loop, update inside it, use the result after.</p>''',
        "speak": "First, the accumulator pattern, building up a running total across a loop. Initialize before the loop starts, update inside it, use the result only after it's done.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> sum = <span class="n">0</span>;
<span class="k">for</span> (<span class="k">double</span> sample : visionLatencies)
{
    sum += sample; <span class="c">// accumulate</span>
}</code></pre>''',
        "speak": "sum starts at 0, outside the loop. For each sample in vision latencies, sum plus-equals sample, accumulating a running total.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> sum = <span class="n">0</span>;
<span class="k">for</span> (<span class="k">double</span> sample : visionLatencies)
{
    sum += sample; <span class="c">// accumulate</span>
}
<span class="k">double</span> average = sum / visionLatencies.size();</code></pre>''',
        "speak": "And only after the loop finishes do we actually use that total, dividing by how many samples there were to get the average.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Min/Max with an if Inside a Loop</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Pair an accumulator with an if, comparing each new value to the best one seen so far.</p>''',
        "speak": "Second, tracking a minimum or a maximum, by pairing that same accumulator idea with an if inside the loop.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> max = Double.MIN_VALUE;
<span class="k">for</span> (<span class="k">double</span> sample : visionLatencies)
{
    <span class="k">if</span> (sample &gt; max)
    {
        max = sample; <span class="c">// running max</span>
    }
}</code></pre>''',
        "speak": "max starts at Double dot Min underscore Value, the smallest possible double, guaranteeing the very first real sample will always beat it. Then for each sample, if it's bigger than the current max, it becomes the new max. By the end, max holds the true largest value seen across the whole loop.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Frequency Counting</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">A counter incremented inside a conditional, once per matching item.</p>''',
        "speak": "Third, frequency counting, counting how many values in a sequence meet some criterion, with a counter incremented inside a conditional.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> faultyCount = <span class="n">0</span>;
<span class="k">for</span> (<span class="t">Sensor</span> sensor : sensors)
{
    <span class="k">if</span> (sensor.isFaulty())
    {
        faultyCount++;
    }
}</code></pre>''',
        "speak": "faulty count starts at 0. For each sensor, if it's faulty, faulty count plus-plus. By the end, it holds exactly how many sensors were flagged, out of the whole set.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Simulating Probability</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Math.random() &lt; p is true with probability p.</p>''',
        "speak": "And fourth, simulating a probability. Math dot random, less than p, is true with probability p, a real way to simulate an event that happens some percentage of the time, useful for testing your code against randomized, simulated sensor noise.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (Math.<span class="me">random</span>() &lt; <span class="n">0.1</span>) <span class="c">// roughly 10% of the time</span>
{
    simulateSensorGlitch();
}</code></pre>''',
        "speak": "Math dot random, less than zero point one, fires roughly 10 percent of the time, exactly enough to simulate an occasional sensor glitch during testing.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Initializing an accumulator with the wrong starting value &mdash; a sum starts at 0; a max should start at the smallest possible value.</li>
      <li><span class="check">!</span>Putting the accumulator update outside the loop &mdash; it has to be inside the body to accumulate across every iteration.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Initializing an accumulator with the wrong starting value, a sum starts at 0, but a max should start at the smallest possible value, so the very first real value always replaces it. And putting the accumulator update outside the loop, it has to be inside the loop body, or it only ever runs once instead of accumulating across every iteration.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Accumulator: initialize before the loop, update inside, use the result after.</li>
      <li><span class="check">&#10003;</span>Min/max tracking pairs an accumulator with an if, comparing each value to the best seen so far.</li>
      <li><span class="check">&#10003;</span>Frequency counting increments a counter inside a conditional.</li>
      <li><span class="check">&#10003;</span>Math.random() &lt; p simulates an event with probability p.</li>
    </ul></div>''',
        "speak": "So: the accumulator pattern, initialize before the loop, update inside, use the result after. Min-max tracking pairs an accumulator with an if, comparing each new value to the best one seen so far. Frequency counting increments a counter inside a conditional. And Math dot random, less than p, simulates an event with probability p. Next up, lesson 5.10, nesting one of these loops inside another.",
    },
]
