BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 22 &middot; The Builder Pattern</div>
      <h1>The Builder Pattern</h1>
      <p class="scr-sub">Constructing a complicated object step by step, with every setting named.</p>
    </div>''',
        "speak": "Welcome to Chapter 22, the Builder Pattern. It's the fix for a problem that shows up the moment a class needs a lot of settings to get built.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Shooter</span> shooter = <span class="k">new</span> Shooter(<span class="n">0.01</span>, <span class="n">0.3</span>, <span class="n">0.02</span>, <span class="k">true</span>, <span class="k">false</span>, <span class="n">12.0</span>, <span class="n">0.5</span>);</code></pre>''',
        "speak": "Here's that problem. A constructor with many parameters, especially several of the same type, or several optional ones, becomes genuinely hard to read, and easy to get wrong. Look at this call. What does each number actually mean?",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">&ldquo;Constructor Hell&rdquo;</h2><ul>
      <li><span class="num">1</span><span>Swap two same-typed arguments and the compiler won't catch it</span></li>
    </ul></div>''',
        "speak": "Swap two arguments of the same type by mistake, and the compiler won't catch it. It'll just silently misconfigure the shooter. This is sometimes called constructor hell.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">&ldquo;Constructor Hell&rdquo;</h2><ul>
      <li><span class="num">1</span><span>Swap two same-typed arguments and the compiler won't catch it</span></li>
      <li><span class="num">2</span><span>More optional settings means every caller specifies everything, or a pile of overloads</span></li>
    </ul></div>''',
        "speak": "And it gets worse the more optional settings a class has, since a constructor either forces every caller to specify every parameter, or multiplies into a pile of overloads trying to cover every combination.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Construct Step by Step</h2><ul>
      <li><span class="num">1</span><span>A separate <strong>Builder</strong> object collects settings one at a time</span></li>
      <li><span class="num">2</span><span>Through named, chainable methods</span></li>
      <li><span class="num">3</span><span>Then produces the final object once, via <code>build()</code></span></li>
    </ul></div>''',
        "speak": "The Builder Pattern separates building an object from using it. A separate Builder object collects settings one at a time, through named, chainable methods, and then produces the final object only once, with a call to build.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Shooter</span> shooter = <span class="k">new</span> Shooter.Builder()
    .setKP(<span class="n">0.01</span>)
    .setKI(<span class="n">0.3</span>)
    .setKD(<span class="n">0.02</span>)
    .enableFeedforward(<span class="k">true</span>)
    .setMaxRPM(<span class="n">12.0</span>)
    .setMinRPM(<span class="n">0.5</span>)
    .build();</code></pre>''',
        "speak": "Here's the same shooter, built with a builder. Every call is now self-documenting. Set K P, zero point zero one, says exactly what that zero point zero one means, in a way a bare constructor argument never could.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Implementing a Builder</h2><ul>
      <li><span class="num">1</span><span>The target class gets a <code>private</code> constructor &mdash; no direct construction</span></li>
      <li><span class="num">2</span><span>Plus a <code>public static</code> nested <code>Builder</code> class that collects the settings</span></li>
    </ul></div>''',
        "speak": "So how do you build one? The target class, Shooter, gets a private constructor, so callers can no longer construct it directly, only through the builder. Plus, a public static nested Builder class that collects the settings.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Shooter</span>
{
    <span class="k">private final double</span> kP, kI, kD;
    <span class="k">private final boolean</span> feedforward;
    <span class="k">private final double</span> maxRPM, minRPM;

    <span class="k">private</span> <span class="me">Shooter</span>(<span class="t">Builder</span> builder)
    {
        <span class="k">this</span>.kP = builder.kP;
        <span class="k">this</span>.kI = builder.kI;
        <span class="k">this</span>.kD = builder.kD;
        <span class="k">this</span>.feedforward = builder.feedforward;
        <span class="k">this</span>.maxRPM = builder.maxRPM;
        <span class="k">this</span>.minRPM = builder.minRPM;
    }</code></pre>''',
        "speak": "First, the Shooter itself. Every field is private and final. And the only constructor is private, taking a finished Builder, and copying each of its values into the matching field, exactly once.",
    },
    {
        "screen": '''<pre class="code"><code>    <span class="k">public static class</span> <span class="t">Builder</span>
    {
        <span class="k">private double</span> kP = <span class="n">0</span>, kI = <span class="n">0</span>, kD = <span class="n">0</span>;
        <span class="k">private boolean</span> feedforward = <span class="k">false</span>;
        <span class="k">private double</span> maxRPM = <span class="n">0</span>, minRPM = <span class="n">0</span>;

        <span class="k">public</span> <span class="t">Builder</span> <span class="me">setKP</span>(<span class="k">double</span> kP) { <span class="k">this</span>.kP = kP; <span class="k">return this</span>; }
        <span class="k">public</span> <span class="t">Builder</span> <span class="me">setKI</span>(<span class="k">double</span> kI) { <span class="k">this</span>.kI = kI; <span class="k">return this</span>; }
        <span class="k">public</span> <span class="t">Builder</span> <span class="me">setKD</span>(<span class="k">double</span> kD) { <span class="k">this</span>.kD = kD; <span class="k">return this</span>; }
        <span class="k">public</span> <span class="t">Builder</span> <span class="me">enableFeedforward</span>(<span class="k">boolean</span> ff) { <span class="k">this</span>.feedforward = ff; <span class="k">return this</span>; }
        <span class="k">public</span> <span class="t">Builder</span> <span class="me">setMaxRPM</span>(<span class="k">double</span> max) { <span class="k">this</span>.maxRPM = max; <span class="k">return this</span>; }
        <span class="k">public</span> <span class="t">Builder</span> <span class="me">setMinRPM</span>(<span class="k">double</span> min) { <span class="k">this</span>.minRPM = min; <span class="k">return this</span>; }

        <span class="k">public</span> <span class="t">Shooter</span> <span class="me">build</span>() { <span class="k">return new</span> Shooter(<span class="k">this</span>); }
    }
}</code></pre>''',
        "speak": "Then, still inside Shooter, the nested Builder. It holds its own copy of every setting, each with a default. One short setter per setting. And finally, build, which hands the builder itself to that private Shooter constructor.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why <code>return this;</code> Matters</h2><ul>
      <li><span class="num">1</span><span>Each builder method returns the same builder it was called on</span></li>
      <li><span class="num">2</span><span>So each call's result is ready for the next call, until <code>.build()</code></span></li>
      <li><span class="num">3</span><span>This call-chaining style is called a <strong>fluent interface</strong></span></li>
    </ul></div>''',
        "speak": "Notice every Builder method ends with return this, returning the same builder object it was just called on. That's exactly what makes chaining possible. Each call's result is another Builder, ready for the next call in the chain, all the way until build finally produces the real Shooter. This style, a chain of method calls, each step returning the object it was called on, is called a fluent interface.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Safer, Not Just Prettier</h2><ul>
      <li><span class="num">1</span><span>Every setting has a readable name at the call site</span></li>
      <li><span class="num">2</span><span>Optional settings simply aren't called &mdash; no overload for every combination</span></li>
      <li><span class="num">3</span><span>The result is typically <strong>immutable</strong> &mdash; every field <code>final</code>, set exactly once</span></li>
    </ul></div>''',
        "speak": "And the result is safer, not just prettier. Every setting has a readable name at the call site, instead of an anonymous position in an argument list. Optional settings simply aren't called, rather than needing a separate constructor overload for every combination. And the final Shooter is typically built as immutable, every field final, and set exactly once, inside the private constructor, from the builder's already finished values.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TrajectoryConfig</span> config = <span class="k">new</span> TrajectoryConfig(maxSpeed, maxAccel)
    .setKinematics(driveKinematics)
    .addConstraint(voltageConstraint);</code></pre>''',
        "speak": "You've likely seen this style already. Several real WPILib classes use builder-like chaining, even without a nested Builder class. Trajectory Config is one, created with a max speed and acceleration, then chained with set kinematics and add constraint.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Same Idea in Command Groups</h2><ul>
      <li><span class="num">1</span><span><code>SequentialCommandGroup</code> and <code>ParallelCommandGroup</code> build a larger thing out of smaller declared pieces</span></li>
    </ul></div>''',
        "speak": "Sequential Command Group and Parallel Command Group follow the same underlying idea, building up a larger thing step by step, out of smaller declared pieces, rather than one giant constructor call.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">When Not to Reach for a Builder</h2><ul>
      <li><span class="num">1</span><span>A builder is a whole extra nested class &mdash; real overhead</span></li>
      <li><span class="num">2</span><span>For 2&ndash;3 simple, always-required parameters: a plain constructor or a static factory (Ch.21)</span></li>
    </ul></div>''',
        "speak": "But a builder is genuine overhead, a whole extra nested class, and it only pays for itself once a constructor's parameter list gets long, or has several optional pieces. For a class with two or three simple, always required parameters, a plain constructor, or, from Chapter 21, a static factory method, is simpler, and should be preferred.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting <code>return this;</code> in a builder method &mdash; chaining the next call won't compile.</li>
      <li><span class="check">!</span>Making the target class's constructor <code>public</code> alongside the builder.</li>
      <li><span class="check">!</span>Reaching for a builder on a simple, 2&ndash;3-parameter class.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Forgetting return this in a builder method, without it, the method returns void, and chaining the next call fails to compile. Making the target class's constructor public alongside the builder, that defeats the pattern's purpose, callers should only ever construct the object through the builder, which is why the real constructor stays private. And reaching for a builder on a simple, two or three parameter class, that's exactly the case the pattern isn't meant for, and the extra ceremony isn't worth it there.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A builder separates step-by-step construction from usage, avoiding constructor hell.</li>
      <li><span class="check">&#10003;</span>A nested static class with named, chainable methods (each returning this), finishing with build().</li>
      <li><span class="check">&#10003;</span>The real constructor is private, copying the builder's values into final fields.</li>
      <li><span class="check">&#10003;</span>WPILib's TrajectoryConfig and command groups use the same chaining idea.</li>
      <li><span class="check">&#10003;</span>Skip it for simple classes &mdash; a constructor or static factory is simpler there.</li>
    </ul></div>''',
        "speak": "So, to recap. The Builder Pattern separates step by step construction from a class's actual usage, avoiding constructor hell, many same-typed or optional parameters. A builder is a nested static class that collects settings through named, chainable methods, each returning this, a fluent interface, and finishes with build. The target class's real constructor is private, taking the finished builder and copying its values into final fields, producing an immutable, safely configured result. Real WPILib classes, Trajectory Config and the command groups, already use this same chaining idea. And skip the builder for simple classes with few, always required parameters, a constructor or static factory is simpler there. Next up, Chapter 23: encapsulation, and the final keyword.",
    },
]
