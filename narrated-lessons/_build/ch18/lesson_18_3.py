BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 18 &middot; Polymorphism: Many Forms</div>
      <h1>Polymorphism</h1>
      <p class="scr-sub">Many forms, one piece of code.</p>
    </div>''',
        "speak": "Everything in Chapter 17, and the last two lessons, has been building toward this one idea. Polymorphism, which literally means many forms. This is lesson 18.3.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Polymorphism Means</h2><ul>
      <li><span class="num">1</span><span>The method that actually runs depends on the object&rsquo;s <strong>actual</strong> type &mdash; not the type its variable was declared with.</span></li>
    </ul></div>''',
        "speak": "Polymorphism means the method that actually runs, at runtime, depends on the object's actual type, not the type its variable was declared with.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public void</span> driveForward(<span class="t">MotorController</span> controller)
{
    controller.set(<span class="n">0.5</span>); <span class="c">// works identically whether controller is a TalonFX or a SparkMax</span>
}</code></pre>''',
        "speak": "Real WPILib code does this all the time. It treats a Talon F X or a Spark Max as just a Motor Controller, and calls the same method on either one without caring which it actually is. This drive forward method takes any Motor Controller, and calls set with zero point five. It works identically whichever kind of controller gets passed in.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Declared Type vs. Actual Type</div>
    <pre class="code"><code><span class="t">Subsystem</span> s = <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front Intake"</span>);
<span class="c">// declared type: Subsystem</span>
<span class="c">// actual type:   Intake</span></code></pre>''',
        "speak": "Every variable has two types that matter. Its declared type, also called its compile-time type, is what it's written as in the code. Its actual type, the runtime type, is the real class that was constructed with new. Here, s is declared as a Subsystem, but the object it actually holds is an Intake.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Compiler Only Checks the Declared Type</div>
    <pre class="code"><code><span class="t">Object</span> message = <span class="k">new</span> <span class="t">String</span>(<span class="s">"hi"</span>);
message.indexOf(<span class="s">"h"</span>); <span class="c">// COMPILE ERROR — Object has no indexOf method, even though String does</span></code></pre>''',
        "speak": "When deciding whether code compiles, the compiler only ever checks the declared type. It verifies that the method you're calling actually exists on that declared type, or one of its ancestors. So here, message is declared as an Object, but really holds a String. Calling index of on it is a compile error.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why That Fails</h2><ul>
      <li><span class="num">1</span><span>The real object is a <strong>String</strong> &mdash; which does have <strong>indexOf</strong>.</span></li>
      <li><span class="num">2</span><span>But the compiler only looks at the declared type, <strong>Object</strong>.</span></li>
      <li><span class="num">3</span><span><strong>Object</strong> never promises an <strong>indexOf</strong> method &mdash; so it won&rsquo;t compile.</span></li>
    </ul></div>''',
        "speak": "Why does that fail? The real object is a String, which absolutely does have index of. But the compiler only looks at message's declared type, Object, and Object never promises an index of method. So it refuses to compile.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Actual Type Decides Which Version Runs</div>
    <pre class="code"><code><span class="t">Subsystem</span> s = <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front Intake"</span>); <span class="c">// declared Subsystem, actually an Intake</span>
s.stop(); <span class="c">// the compiler only confirms Subsystem HAS a stop() method — but Intake's own override is what actually runs</span></code></pre>''',
        "speak": "Once code does compile, the other half kicks in. The JVM decides which overridden version of a method actually runs by looking at the object's real, actual type, starting there and searching upward through its superclasses if needed. Same lookup process as the super lesson. So here, the compiler only confirms that Subsystem has a stop method. But the version that actually runs is Intake's own override.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="t">Subsystem</span> s : allSubsystems)
{
    s.stop(); <span class="c">// Intake's stop(), Climber's stop(), Shooter's stop() — whichever is actually correct for each object</span>
}</code></pre>''',
        "speak": "This is exactly what made the Subsystem arrays and array lists from lesson 17.3 genuinely useful. One loop calls stop on each element, and each object automatically runs whichever subclass's own stop actually applies, Intake's, Climber's, Shooter's. No if, else chain checking each object's specific type.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Static Methods Don&rsquo;t Get This</h2><ul>
      <li><span class="check">!</span>Polymorphic dispatch only applies to regular <strong>instance</strong> methods.</li>
      <li><span class="check">!</span>A <strong>static</strong> call is resolved by the declared type, at compile time &mdash; no runtime lookup.</li>
    </ul></div>''',
        "speak": "One exception. Polymorphic dispatch only applies to regular instance methods. A static method call is resolved entirely by the declared type, at compile time, with no runtime lookup at all, since static methods belong to the class itself, not to any particular object.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assuming the compiler checks the actual type &mdash; it only ever consults the declared type.</li>
      <li><span class="check">!</span>Forgetting runtime dispatch decides which override runs &mdash; the declared type only gates whether it compiles.</li>
      <li><span class="check">!</span>Expecting polymorphism for static methods &mdash; they&rsquo;re resolved by declared type alone.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Don't assume the compiler checks the actual type. It never does, which is why message dot index of fails to compile even though the real object has that method. Don't forget that runtime dispatch is what decides which override runs. The declared type only gates whether the code compiles. And don't expect polymorphism to apply to static methods. They're resolved by declared type alone, and don't participate in overriding the way instance methods do.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>The method that runs depends on the object&rsquo;s actual type, not its declared type.</li>
      <li><span class="check">&#10003;</span>The compiler checks the declared type; the JVM picks the override by the actual type.</li>
      <li><span class="check">&#10003;</span>One <strong>Subsystem</strong>-typed loop or parameter works with every subclass.</li>
      <li><span class="check">&#10003;</span>Static methods don&rsquo;t participate &mdash; declared type only, at compile time.</li>
    </ul></div>''',
        "speak": "So, to recap. Polymorphism means the method that runs depends on an object's actual runtime type, not its variable's declared type. The compiler only checks the declared type to decide whether a call is legal, and the JVM decides which overridden version actually runs based on the real type. That's why a Subsystem-typed array or method parameter can work transparently with Intake, Climber, Shooter, or any other subclass. One piece of code, many possible real behaviors. And static methods don't participate, they're resolved entirely by declared type, at compile time. That wraps up Chapter 18.",
    },
]
