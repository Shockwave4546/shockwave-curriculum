BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 4 &middot; Using Objects &amp; Calling Methods</div>
      <h1>Creating &amp; Initializing Objects: Constructors</h1>
      <p class="scr-sub">What "new" actually does &mdash; and what happens when a reference points at nothing.</p>
    </div>''',
        "speak": "Every time we've written new followed by a class name, we've actually been calling something specific, a constructor. Let's look at what that word really means.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span> leftMotor = <span class="k">new</span> <span class="t">TalonFX</span>(<span class="n">5</span>); <span class="c">// 5 is the CAN ID &mdash; argument order matters</span></code></pre>''',
        "speak": "A constructor initializes a new object's attributes the moment it's created. new followed by the class name is actually a call to that constructor. Here, 5 is the CAN ID, and argument order matters, we'll see exactly why that matters in a second.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Constructors Can Be Overloaded</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Different ways to set up an object, distinguished by their parameter lists &mdash; same idea as method overloading.</p>''',
        "speak": "A class can offer more than one constructor, different ways to set up an object, distinguished by their parameter lists. This is the exact same overloading idea from lesson 4.1, just applied to constructors instead of regular methods.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Pose2d</span> start1 = <span class="k">new</span> <span class="t">Pose2d</span>();                       <span class="c">// no-argument constructor: defaults to (0, 0, facing 0°)</span></code></pre>''',
        "speak": "Pose 2 D, a class representing a position and heading on the field, has a no-argument constructor. Call it with empty parentheses, and it defaults to zero, zero, facing zero degrees.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Pose2d</span> start1 = <span class="k">new</span> <span class="t">Pose2d</span>();                       <span class="c">// no-argument constructor: defaults to (0, 0, facing 0°)</span>
<span class="t">Pose2d</span> start2 = <span class="k">new</span> <span class="t">Pose2d</span>(<span class="n">1.0</span>, <span class="n">2.0</span>, <span class="k">new</span> <span class="t">Rotation2d</span>()); <span class="c">// x, y, and heading, explicitly</span></code></pre>''',
        "speak": "Or call the other constructor, passing x, y, and a heading explicitly. Same class, two completely different constructors, chosen based on what you pass in. And here's why argument order matters so much, mixing up which number means x and which means y produces a real, silent bug, the code compiles perfectly fine, but the object quietly ends up in the wrong place.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Object References and null</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">A reference can be declared without pointing at any object yet.</p>''',
        "speak": "A reference variable can actually be declared without pointing at any object yet, that state is called null, meaning it doesn't refer to anything at all.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span> intakeMotor = <span class="k">null</span>; <span class="c">// no object yet</span></code></pre>''',
        "speak": "intake motor equals null, no object exists behind this variable yet.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span> intakeMotor = <span class="k">null</span>; <span class="c">// no object yet</span>
intakeMotor = <span class="k">new</span> <span class="t">TalonFX</span>(<span class="n">7</span>); <span class="c">// now it does</span></code></pre>''',
        "speak": "Assign it a real constructed object later, and now it does. Calling a method on a reference that's still null, one that was declared but never actually constructed, throws a Null Pointer Exception at runtime, more on that in the very next lesson, since it's one of the most common real bugs you'll hit.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="k">class</span> <span class="t">Pose2d</span> {
    <span class="k">public</span> <span class="t">Pose2d</span>() { <span class="c">/* implementation not shown */</span> }
    <span class="k">public</span> <span class="t">Pose2d</span>(<span class="k">double</span> x, <span class="k">double</span> y, <span class="t">Rotation2d</span> rotation) { <span class="c">/* implementation not shown */</span> }
}</code></pre>''',
        "speak": "Just like a regular method, a constructor has a signature too, its name, always the same as the class, plus its parameter types. Pose 2 D here really does offer both constructors we just used. When you're working with a library class, its documentation is exactly where you look up which constructors exist and what order their arguments expect.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting new &mdash; creating an object always requires it; skipping it doesn't compile.</li>
      <li><span class="check">!</span>Mixing up argument order &mdash; a constructor called with arguments in the wrong order can silently compile with the wrong values swapped.</li>
      <li><span class="check">!</span>Calling a method on an unconstructed reference &mdash; leaves it null, and calling anything on it crashes with a NullPointerException.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Forgetting new, creating an object always requires it, skip it and the line simply won't compile. Mixing up argument order, a constructor taking x, y, rotation, called with those arguments swapped around, either won't compile because the types don't match, or worse, compiles fine with the wrong values silently swapped. And calling a method on an unconstructed reference, that leaves it null, and calling anything on a null reference crashes with a Null Pointer Exception.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>new ClassName(arguments) calls a constructor to build and initialize an object.</li>
      <li><span class="check">&#10003;</span>A class can have multiple overloaded constructors.</li>
      <li><span class="check">&#10003;</span>A reference can be null &mdash; pointing at no object &mdash; until assigned a real one.</li>
      <li><span class="check">&#10003;</span>Calling a method on a null reference throws a NullPointerException.</li>
    </ul></div>''',
        "speak": "So: new, followed by a class name and arguments, calls a constructor to build and initialize an object. A class can have multiple overloaded constructors. A reference can be null, pointing at no object at all, until it's assigned a real one. And calling a method on a null reference throws a Null Pointer Exception. Next up, lesson 4.6, calling methods on the specific objects we've built, and getting values back out of them.",
    },
]
