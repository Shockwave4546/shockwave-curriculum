BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 2 &middot; Variables &amp; Types</div>
      <h1>Assignment &amp; Input</h1>
      <p class="scr-sub">What "gets assigned" really means &mdash; and where a value from outside your code lands.</p>
    </div>''',
        "speak": "We've used equals signs constantly already, so let's slow down and make sure the mental model is exactly right, because it's easy to accidentally think about it the wrong way.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> score = <span class="n">10</span> * <span class="n">2</span> + <span class="n">5</span>; <span class="c">// score is assigned the value 25</span></code></pre>''',
        "speak": "Equals always has one variable on the left, and a value or a math expression on the right. int score equals 10 times 2 plus 5, read as score gets assigned the value 25, not score equals 25. Java works out the right side completely first, then stores the result.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> x = <span class="n">3</span>;
<span class="k">int</span> y = <span class="n">2</span>;
x = y;   <span class="c">// x is now assigned a copy of y's value: 2</span></code></pre>''',
        "speak": "Here's the part that catches people off guard. x starts at 3, y starts at 2. x equals y copies y's value into x, so x becomes 2. But it's a copy, not a link.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> x = <span class="n">3</span>;
<span class="k">int</span> y = <span class="n">2</span>;
x = y;   <span class="c">// x is now assigned a copy of y's value: 2</span>
y = <span class="n">5</span>;   <span class="c">// y changes &mdash; x is still 2, unaffected</span></code></pre>''',
        "speak": "Change y afterward, set it to 5, and x doesn't move, it's still 2. The moment that copy happened, x and y went their separate ways. This trips people up because in everyday language, linking two things together feels natural, but assignment in code is a one-time snapshot, not a standing relationship.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> x = <span class="n">1</span>;
<span class="k">double</span> y = <span class="n">2.2</span>;
x = <span class="n">2</span> * y;   <span class="c">// won't compile &mdash; 2 * y is a double, and x is an int</span></code></pre>''',
        "speak": "Java also refuses to use a variable before it's been given a value, and it insists the value's type actually matches. Here, 2 times y works out to a double, but x was declared as an int, so this line simply won't compile. The fix isn't to force it through some trick, it's to recognize x should have been a double in the first place, since that's genuinely what it's meant to hold.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> step = <span class="n">0</span>;
step = step + <span class="n">1</span>; <span class="c">// uses the OLD value of step, then stores the new result back into it</span></code></pre>''',
        "speak": "One pattern comes up constantly, updating a variable based on its own current value. step equals step plus 1. Java reads the old value of step first, adds 1 to it, and only then stores that new result back into step. Lesson 2.5 shows a shorthand for exactly this, step plus plus.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Where "Input" Comes From</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:48ch;margin:0 auto;">On a robot, it's a joystick or a sensor, not typed text &mdash; but the idea is identical.</p>''',
        "speak": "Now, input. Some value arrives from outside your code, lands in a variable, and the rest of your code reacts to it. On a laptop that might be typed text, but on a robot, it's a joystick reading or a sensor value. The mechanism is exactly the same either way, a variable holds whatever value showed up, and the rest of the code doesn't have to change no matter what that value turns out to be.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> throttle = <span class="n">0.6</span>; <span class="c">// stands in for "whatever value the controller sends"</span>
<span class="k">double</span> output = throttle * maxSpeed;</code></pre>''',
        "speak": "Here, throttle stands in for whatever value the controller happens to send in at that instant, we're just hard-coding 0 point 6 to see the shape of it. Output then gets computed from throttle, and it works identically whether throttle came from a hard-coded number or a live joystick reading.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using a variable before it has a value &mdash; Java won't let this compile. That's a safety net, not an inconvenience.</li>
      <li><span class="check">!</span>Assuming a copy keeps two variables linked &mdash; it copies the value once, then they're independent.</li>
    </ul></div>''',
        "speak": "Two pitfalls to keep in mind. Using a variable before it has a value, Java simply won't compile that, and that's a safety net working as intended, not an annoyance to route around. And assuming y equals x keeps them linked going forward, it copies the value exactly once, and after that, changing one does absolutely nothing to the other.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Read = as "gets assigned," never as "equals."</li>
      <li><span class="check">&#10003;</span>Copying a value doesn't link two variables &mdash; each is independent afterward.</li>
      <li><span class="check">&#10003;</span>A variable needs a value, of a matching type, before it's used.</li>
      <li><span class="check">&#10003;</span>"Input" is any value from outside your code &mdash; a joystick, a sensor, or typed text.</li>
    </ul></div>''',
        "speak": "So, read equals as gets assigned, never as equals. Copying a value doesn't link two variables together, each one goes its own way afterward. A variable needs a value of a matching type before you can use it. And input is any value that shows up from outside your code, whether that's a joystick, a sensor, or typed text. Next up, lesson 2.4, we'll look at converting between types on purpose, and what happens when a value doesn't fit.",
    },
]
