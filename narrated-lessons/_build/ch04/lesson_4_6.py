BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 4 &middot; Using Objects &amp; Calling Methods</div>
      <h1>Calling Instance Methods</h1>
      <p class="scr-sub">The other half of methods: the kind that only make sense on one specific object.</p>
    </div>''',
        "speak": "Lesson 4.2 covered static methods, called through the class name. Now let's cover their opposite, instance methods, which is honestly what you'll write and call the most on a real robot.",
    },
    {
        "screen": '''<pre class="code"><code>leftMotor.<span class="me">set</span>(<span class="n">0.5</span>); <span class="c">// instance method &mdash; acts on leftMotor specifically, not TalonFX in general</span></code></pre>''',
        "speak": "An instance method is always called on a specific object, and it reads or changes that object's own attributes. left motor dot set, 0 point 5, acts on left motor specifically, not on Talon F X in general. Math dot square root of 9 doesn't care which object called it, there is no object, it's pure computation. left motor dot set only makes sense applied to one specific motor.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">NullPointerException</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">One of the most common real bugs in object-oriented code.</p>''',
        "speak": "We named it last lesson, now let's see it happen. Calling a method on a reference that's null, declared but never actually built with new, throws a Null Pointer Exception at runtime.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span> intakeMotor = <span class="k">null</span>;
intakeMotor.<span class="me">set</span>(<span class="n">0.5</span>); <span class="c">// crashes: intakeMotor doesn't refer to a real object yet</span></code></pre>''',
        "speak": "intake motor is null, and calling set on it crashes immediately, because intake motor doesn't refer to a real object yet. This is one of the single most common real bugs you'll run into in object-oriented code, and it's exactly why last lesson's warning matters.",
    },
    {
        "screen": '''<pre class="code"><code>leftMotor.<span class="me">set</span>(<span class="n">0.5</span>);          <span class="c">// no extra behavior beyond the speed itself</span></code></pre>''',
        "speak": "Instance methods, just like the constructors from last lesson, can take arguments. left motor dot set, 0 point 5, is a simple case, just the speed itself.",
    },
    {
        "screen": '''<pre class="code"><code>leftMotor.<span class="me">set</span>(<span class="n">0.5</span>);          <span class="c">// no extra behavior beyond the speed itself</span>
elevator.<span class="me">moveToPosition</span>(<span class="n">24.0</span>); <span class="c">// 24.0 is the argument, saved into the method's parameter</span></code></pre>''',
        "speak": "elevator dot move to position, 24 point 0, works the same way, 24 point 0 is the argument, saved right into that method's parameter, wherever this specific elevator's code decides to use it.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Getters (Accessors)</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Reports one of an object's attributes &mdash; no side effects, just returns a value. Name starts with "get."</p>''',
        "speak": "A method that just reports one of an object's attributes, no side effects, purely returns a value, is called a getter, or formally, an accessor. By convention its name starts with get, and just like any other non-void method, its return value has to actually be used.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> speed = leftMotor.<span class="me">getVelocity</span>(); <span class="c">// a getter &mdash; must use the returned value</span></code></pre>''',
        "speak": "double speed equals left motor dot get velocity, stores the getter's return value properly.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> speed = leftMotor.<span class="me">getVelocity</span>(); <span class="c">// a getter &mdash; must use the returned value</span>
System.out.<span class="me">println</span>(<span class="s">"Current speed: "</span> + leftMotor.<span class="me">getVelocity</span>());</code></pre>''',
        "speak": "Or use it directly, print lining Current speed, followed by left motor dot get velocity, called right inline. Either way is fine, calling it and then throwing the result away is the one that isn't.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Calling an instance method without an object &mdash; set needs a specific motor to act on.</li>
      <li><span class="check">!</span>Calling a method on a null reference &mdash; the single most common source of NullPointerException.</li>
      <li><span class="check">!</span>Ignoring a getter's return value &mdash; a getter exists specifically to report a value you then use.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Calling an instance method without an object, Talon F X dot set doesn't make sense on its own, set needs one specific motor to act on. Calling a method on a null reference, the single most common source of Null Pointer Exception, make sure every object is actually constructed with new before you call anything on it. And ignoring a getter's return value, left motor dot get velocity on its own line does nothing useful, a getter exists specifically to report a value you're then meant to use.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An instance method is called on a specific object, and reads/changes its own attributes.</li>
      <li><span class="check">&#10003;</span>Calling a method on a null reference throws a NullPointerException.</li>
      <li><span class="check">&#10003;</span>A getter reports an attribute; its return value must be used, not ignored.</li>
    </ul></div>''',
        "speak": "So: an instance method is called on a specific object, and it reads or changes that object's own attributes, unlike a static method, which belongs to the class itself. Calling a method on a null reference throws a Null Pointer Exception, one of the most common real bugs out there. And a getter reports one of an object's attributes, its return value has to be used, not ignored. That closes out Chapter 4. Next, Chapter 5, control structures, where our code finally starts making its own decisions.",
    },
]
