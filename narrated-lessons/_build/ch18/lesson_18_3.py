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
    <span class="c">// works the same whichever motor controller class is passed in</span>
    controller.setThrottle(<span class="n">0.5</span>);
}</code></pre>''',
        "speak": "Real WPILib code relies on this constantly. WPILib's Motor Controller type describes what every motor controller can do, and code written against it calls the same method on any motor controller, without caring which class it actually is. This drive forward method takes any Motor Controller, and calls set Throttle with zero point five. It works the same whichever motor controller class gets passed in. Motor Controller is actually an interface, a kind of type Chapter 19 covers in full. For now, treat it like a superclass shared by every WPILib motor controller class.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Declared Type vs. Actual Type</div>
    <pre class="code"><code><span class="t">RobotPart</span> part = <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front Intake"</span>);
<span class="c">// declared type: RobotPart</span>
<span class="c">// actual type:   Intake</span></code></pre>''',
        "speak": "Every variable has two types that matter. Its declared type, also called its compile-time type, is what it's written as in the code. Its actual type, the runtime type, is the real class that was constructed with new. Here, part is declared as a Robot Part, but the object it actually holds is an Intake.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Compiler Only Checks the Declared Type</div>
    <pre class="code"><code><span class="t">Object</span> message = <span class="k">new</span> <span class="t">String</span>(<span class="s">"hi"</span>);
<span class="c">// COMPILE ERROR — Object has no indexOf method, even though String does</span>
message.indexOf(<span class="s">"h"</span>);</code></pre>''',
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
    <pre class="code"><code><span class="t">RobotPart</span> part = <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front Intake"</span>);  <span class="c">// declared RobotPart, actually an Intake</span>
<span class="c">// the compiler only confirms RobotPart HAS a stop() method —</span>
<span class="c">// but Intake's own override (Lesson 18.1) is what actually runs</span>
part.stop();</code></pre>''',
        "speak": "Once code does compile, the other half kicks in. The JVM decides which overridden version of a method actually runs by looking at the object's real, actual type, starting there and searching upward through its superclasses if needed. Same lookup process as the super lesson. So here, the compiler only confirms that Robot Part has a stop method. But the version that actually runs is Intake's own override, from lesson 18.1.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="t">RobotPart</span> p : allParts)
{
    <span class="c">// Intake's stop(), Climber's stop(), Shooter's stop() — whichever fits each object</span>
    p.stop();
}</code></pre>''',
        "speak": "This is exactly what made the Robot Part arrays and array lists from lesson 17.3 genuinely useful. One loop calls stop on each element, and each object automatically runs whichever subclass's own stop actually applies, Intake's, Climber's, Shooter's. No if, else chain checking each object's specific type.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Casting Back Down</h2><ul>
      <li><span class="num">1</span><span><strong>Upcast</strong> (subclass &rarr; superclass type): automatic &mdash; every Intake is a RobotPart.</span></li>
      <li><span class="num">2</span><span><strong>Downcast</strong> (superclass &rarr; subclass type): needs an explicit cast &mdash; not every RobotPart is an Intake.</span></li>
    </ul></div>''',
        "speak": "Now the other direction. Storing an Intake in a Robot Part variable is an upcast, from a subclass type up to a superclass type, and it happens automatically, because every Intake is a Robot Part. Going the other way, a downcast, needs an explicit cast, because not every Robot Part is an Intake.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">RobotPart</span>
{
    <span class="c">// ...hasGamePiece field, constructor, and stop() as in Lessons 17.2 and 18.1</span>
    <span class="k">public boolean</span> hasGamePiece() { <span class="k">return</span> hasGamePiece; }
}</code></pre>''',
        "speak": "Suppose Intake adds a method of its own: has Game Piece, a getter for the field from lesson 17.2. Calling it through part doesn't compile, since part is declared Robot Part.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">RobotPart</span> part = <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front Intake"</span>);  <span class="c">// upcast: automatic</span>
<span class="t">Intake</span> intake = (<span class="t">Intake</span>) part;                <span class="c">// downcast: needs a cast</span>
<span class="t">System</span>.out.println(intake.hasGamePiece());</code></pre>''',
        "speak": "A cast tells the compiler to treat the reference as an Intake. The upcast on the first line is automatic. The downcast on the second line needs Intake in parentheses. After that, has Game Piece is available.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">RobotPart</span> other = <span class="k">new</span> <span class="t">Climber</span>(<span class="s">"Left Climber"</span>);
<span class="c">// compiles, but throws ClassCastException when it runs: a Climber isn't an Intake</span>
<span class="t">Intake</span> wrong = (<span class="t">Intake</span>) other;</code></pre>''',
        "speak": "The cast is checked when the program runs. Here, other really holds a Climber. The cast compiles, but when it runs, it throws a Class Cast Exception, because a Climber isn't an Intake.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">if</span> (part <span class="k">instanceof</span> <span class="t">Intake</span> i)
{
    <span class="t">System</span>.out.println(<span class="s">"Holding a piece: "</span> + i.hasGamePiece());
}</code></pre>''',
        "speak": "So check with instance of first. Since Java 16, the check and the cast combine into one step, with a pattern. If part refers to an Intake, the new variable i is that same object, already typed as Intake, inside the if. Needing lots of downcasts, though, is usually a sign the method belongs in the superclass as an override. Polymorphism exists so most code never has to ask which kind this is.",
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
      <li><span class="check">!</span>Downcasting without checking &mdash; ClassCastException; guard with <strong>instanceof</strong>.</li>
      <li><span class="check">!</span>Expecting polymorphism for static methods &mdash; they&rsquo;re resolved by declared type alone.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Don't assume the compiler checks the actual type. It never does, which is why message dot index of fails to compile even though the real object has that method. Don't forget that runtime dispatch is what decides which override runs. The declared type only gates whether the code compiles. Don't downcast without checking. The cast compiles whenever part could be an Intake, but throws a Class Cast Exception at runtime if it isn't, so guard it with instance of, or use the pattern. And don't expect polymorphism to apply to static methods. They're resolved by declared type alone, and don't participate in overriding the way instance methods do.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>The method that runs depends on the object&rsquo;s actual type, not its declared type.</li>
      <li><span class="check">&#10003;</span>The compiler checks the declared type; the JVM picks the override by the actual type.</li>
      <li><span class="check">&#10003;</span>One <strong>RobotPart</strong>-typed loop or parameter works with every subclass.</li>
      <li><span class="check">&#10003;</span>Upcasts are automatic; downcasts need a cast &mdash; safest as <strong>if (x instanceof Intake i)</strong>.</li>
      <li><span class="check">&#10003;</span>Static methods don&rsquo;t participate &mdash; declared type only, at compile time.</li>
    </ul></div>''',
        "speak": "So, to recap. Polymorphism means the method that runs depends on an object's actual runtime type, not its variable's declared type. The compiler only checks the declared type to decide whether a call is legal, and the JVM decides which overridden version actually runs based on the real type. That's why a Robot Part-typed array or method parameter can work transparently with Intake, Climber, Shooter, or any other subclass. One piece of code, many possible real behaviors. Upcasts are automatic, while downcasts need an explicit cast, can throw a Class Cast Exception, and are safest with the instance of pattern. And static methods don't participate, they're resolved entirely by declared type, at compile time. That wraps up Chapter 18.",
    },
]
