BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 28 &middot; Algorithms: Searching, Sorting &amp; Recursion</div>
      <h1>Recursion</h1>
      <p class="scr-sub">A method that calls itself &mdash; and how to make it stop.</p>
    </div>''',
        "speak": "One more optional lesson, and a big idea: recursion. Recursion is when a method calls itself. It's another form of repetition, right alongside the loops from chapter 5.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">A Method That Calls Itself</div>
    <pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="k">void</span> <span class="me">neverEnd</span>()
{
    System.out.<span class="me">println</span>(<span class="s">"This never stops!"</span>);
    <span class="me">neverEnd</span>(); <span class="c">// calls itself again, forever</span>
}</code></pre>''',
        "speak": "Without care, it goes wrong immediately. Never end prints a line, and then calls itself again. Which prints a line, and calls itself again. Forever.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Infinite Recursion</h2><ul>
      <li><span class="num">1</span><span>Every in-progress call takes up space to be tracked</span></li>
      <li><span class="num">2</span><span>Recurse too deep, and it crashes with <strong>StackOverflowError</strong></span></li>
    </ul></div>''',
        "speak": "That's infinite recursion. It eventually crashes with a Stack Overflow Error, because a program can only recurse so deep before it runs out of space to track all those in-progress calls.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Required Ingredients</h2><ul>
      <li><span class="num">1</span><span><strong>A base case</strong> &mdash; a condition that stops the recursion and returns directly</span></li>
    </ul></div>''',
        "speak": "So every well-behaved recursive method needs two ingredients. First, at least one base case: a condition that stops the recursion and returns directly, with no further self-call.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Required Ingredients</h2><ul>
      <li><span class="num">1</span><span><strong>A base case</strong> &mdash; a condition that stops the recursion and returns directly</span></li>
      <li><span class="num">2</span><span><strong>A recursive call</strong> &mdash; one that moves the problem closer to the base case</span></li>
    </ul></div>''',
        "speak": "And second, at least one recursive call, one that moves the problem closer to that base case.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">static</span> <span class="t">int</span> <span class="me">factorial</span>(<span class="t">int</span> n)
{
    <span class="k">if</span> (n == <span class="n">0</span>)         <span class="c">// base case &mdash; the smallest input this method answers directly</span>
    {
        <span class="k">return</span> <span class="n">1</span>;
    }
    <span class="k">else</span>
    {
        <span class="k">return</span> n * <span class="me">factorial</span>(n - <span class="n">1</span>); <span class="c">// recursive call &mdash; moves toward the base case</span>
    }
}</code></pre>''',
        "speak": "The classic example is factorial. When n is zero, that's the base case, the smallest input this method answers directly, so it just returns one. Otherwise, it returns n times factorial of n minus one. That's the recursive call.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Every Call Should Shrink the Problem</div>
    <div class="scr-naming">
      <div class="namerow"><code>factorial(n - 1)</code><span class="nlabel">one step closer&hellip;</span></div>
      <div class="namerow"><code>n == 0</code><span class="nlabel">&hellip;to the base case that stops it</span></div>
    </div>''',
        "speak": "Every recursive call should shrink the problem. Factorial's call passes n minus one, one step closer to the n equals zero base case that eventually stops the recursion.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Tracing: The Call Stack</h2><ul>
      <li><span class="num">1</span><span>Each recursive call is pushed onto the <strong>call stack</strong></span></li>
      <li><span class="num">2</span><span>Each one gets its own independent copy of local variables and parameters</span></li>
    </ul></div>''',
        "speak": "Every method call, recursive or not, gets pushed onto the call stack, from chapter 12, with its own independent copy of local variables and parameters. Recursion just applies the same mechanics to a method calling itself repeatedly, so the stack ends up holding several frames for the same method at once, each with its own copy of n.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Tracing factorial(3)</div>
    <pre class="code"><code>factorial(3) returns 3 * factorial(2)
factorial(2) returns 2 * factorial(1)
factorial(1) returns 1 * factorial(0)
factorial(0) returns 1</code></pre>''',
        "speak": "Let's trace factorial of three. Factorial of three returns three times factorial of two. Factorial of two returns two times factorial of one. Factorial of one returns one times factorial of zero. And factorial of zero is the base case. It just returns one.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Substituting Back Up</div>
    <pre class="code"><code>factorial(1) returns 1 * factorial(0) = 1 * 1 = 1
factorial(2) returns 2 * factorial(1) = 2 * 1 = 2
factorial(3) returns 3 * factorial(2) = 3 * 2 = 6</code></pre>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;max-width:52ch;margin:14px auto 0;">factorial(3) returns 6.</p>''',
        "speak": "Then substitute the values back upward, starting from the base case. Factorial of one is one times one, which is one. Factorial of two is two times one, which is two. And factorial of three is three times two, so factorial of three returns six.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Bother? Recursion for Trees</h2><ul>
      <li><span class="num">1</span><span>Any loop can be rewritten recursively, and vice versa</span></li>
      <li><span class="num">2</span><span>Recursion shines on <strong>branching</strong> structures &mdash; &ldquo;trees&rdquo;</span></li>
    </ul></div>''',
        "speak": "Any loop can, in principle, be rewritten recursively, and vice versa. So why use recursion at all? Because it shines on branching structures, which computer scientists call trees, rather than simple linear ones.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">A Useful Mental Model</div>
    <div class="scr-naming">
      <div class="namerow"><code>for loop</code><span class="nlabel">a linear structure, like an array (Ch.9)</span></div>
      <div class="namerow"><code>nested loops</code><span class="nlabel">a 2D array (Ch.10)</span></div>
      <div class="namerow"><code>recursion</code><span class="nlabel">something that branches</span></div>
    </div>''',
        "speak": "Here's a useful mental model. A for loop, for a linear structure like an array, from chapter 9. Nested loops, for a two-D array, from chapter 10. And recursion, for something that branches.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Something That Branches</h2><ul>
      <li><span class="num">1</span><span>Count the subsystems in an equipment group &mdash; which can contain further nested groups</span></li>
      <li><span class="num">2</span><span>Each nested group is <em>the same problem</em>, just smaller</span></li>
    </ul></div>''',
        "speak": "Like calculating the total number of subsystems nested inside an equipment group, where that group can itself contain further nested groups. Each nested group is the same problem, just smaller. A for loop naturally handles walk through this flat list. It struggles to express walk through this, and every branch inside it, and every branch inside those.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting the base case &mdash; the method is really just neverEnd() in disguise.</li>
      <li><span class="check">!</span>A base case that can be skipped right over &mdash; a negative n sails past n == 0 and never stops.</li>
      <li><span class="check">!</span>A recursive call that doesn&rsquo;t shrink the problem &mdash; it never terminates, even with a base case.</li>
      <li><span class="check">!</span>Confusing &ldquo;elegant here&rdquo; with &ldquo;required here&rdquo; &mdash; flat, linear data is usually clearer as a loop.</li>
    </ul></div>''',
        "speak": "Four pitfalls. Forgetting the base case entirely. Without one, every recursive method is really just never end in disguise: infinite recursion, and a crash. A base case that can be skipped right over. Factorial's base case only checks n equals zero. Call it with a negative n, and the recursive call sails past zero without ever matching it, recursing until Stack Overflow Error. A safer check is often a range, like n less than or equal to zero, rather than an exact match. A recursive call that doesn't actually shrink the problem. If the argument passed to the next call doesn't move closer to the base case, the recursion never terminates, even with a base case defined. And confusing recursion is elegant here with recursion is required here. Simple linear traversal, an array, a String, is usually clearer and more efficient as a loop. Recursion earns its keep on genuinely branching structures.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Recursion is a method calling itself &mdash; repetition, structured around self-calls.</li>
      <li><span class="check">&#10003;</span>Every correct recursive method needs a base case, and a recursive call that moves toward it.</li>
      <li><span class="check">&#10003;</span>Each call gets its own locals on the call stack &mdash; trace down, then substitute back up.</li>
      <li><span class="check">&#10003;</span>Recursion is most valuable for branching &ldquo;tree&rdquo; structures; loops stay better for flat ones.</li>
    </ul></div>''',
        "speak": "So, to recap. Recursion is a method calling itself, repetition like a loop, but structured around self-calls instead of a loop construct. Every correct recursive method needs a base case, which stops the recursion, and a recursive call that moves toward it. Each recursive call gets its own independent local variables and parameters, tracked on the call stack, so tracing means writing out each call, then substituting values back up from the base case. And recursion is most valuable for branching, tree structures. A simple for loop is still the better tool for flat, linear ones. Next up, lesson 28.4: recursive searching and sorting.",
    },
]
