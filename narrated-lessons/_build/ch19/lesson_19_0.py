BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 19 &middot; Interfaces as Contracts</div>
      <h1>Interfaces as Contracts</h1>
      <p class="scr-sub">What an object can do, without saying how it does it.</p>
    </div>''',
        "speak": "Welcome to Chapter 19. An interface defines what an object can do, without specifying how it does it. It's a contract, a set of method signatures any implementing class agrees to provide, with no implementation of its own. That lets two groups write code against a shared agreement without either needing to know the other's internals.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public interface</span> <span class="t">IntakeIO</span>
{
    <span class="k">void</span> <span class="me">updateInputs</span>(<span class="t">IntakeInputs</span> inputs);
    <span class="k">void</span> <span class="me">setVoltage</span>(<span class="k">double</span> volts);
}</code></pre>''',
        "speak": "Here's Intake IO. Method signatures inside an interface have no body, just a semicolon, no braces. Every one of those methods is abstract, Lesson 17.5's term for a signature with no body. Interface is the keyword.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">RealIntakeIO</span> <span class="k">implements</span> <span class="t">IntakeIO</span>
{
    <span class="me">@Override</span>
    <span class="k">public void</span> <span class="me">updateInputs</span>(<span class="t">IntakeInputs</span> inputs) { <span class="c">/* real sensor reads */</span> }

    <span class="me">@Override</span>
    <span class="k">public void</span> <span class="me">setVoltage</span>(<span class="k">double</span> volts) { <span class="c">/* real motor.setVoltage(volts) */</span> }
}</code></pre>''',
        "speak": "A class agrees to the contract with implements. Real Intake I O must provide a real method body for every method the interface declares, or the class fails to compile. And every one of those methods is implicitly public, even though Intake IO never writes the word. Write the implementing method as anything weaker than public, and it won't compile.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Multiple Interfaces, One Superclass</h2><ul>
      <li><span class="num">1</span><span><strong>extends</strong> &mdash; exactly one superclass (Lesson 17.1)</span></li>
      <li><span class="num">2</span><span><strong>implements</strong> &mdash; any number of interfaces at once</span></li>
    </ul></div>''',
        "speak": "Unlike extends, which is limited to exactly one superclass, a class can implement as many interfaces as it needs. A class has one parent, but can honor any number of separate contracts at once.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">implements</span> <span class="t">Stowable</span>, <span class="t">Diagnosable</span>
{
    <span class="c">// must provide every method declared by BOTH Stowable and Diagnosable</span>
}</code></pre>''',
        "speak": "Here, Intake implements both Stowable and Diagnosable at once, comma-separated, and must provide every method both of them declare.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public void</span> <span class="me">configureIntake</span>(<span class="t">IntakeIO</span> io)
{
    <span class="c">// works for RealIntakeIO, SimIntakeIO, or any other IntakeIO implementation</span>
    io.<span class="me">setVoltage</span>(<span class="n">0.0</span>);
}</code></pre>''',
        "speak": "Just like a superclass, an interface is a real reference type. A variable, parameter, array, or collection can be declared against it, and hold any object whose class implements it. Code written against Intake IO never needs to know or care which concrete implementation it's actually working with, real hardware or a simulated stand-in. This exact pattern is the foundation of the IO-Layer Pattern, next chapter.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public interface</span> <span class="t">IntakeIO</span>
{
    <span class="c">// implicitly public static final — same as Lesson 7.4's constants</span>
    <span class="k">double</span> <span class="t">MAX_VOLTS</span> = <span class="n">12.0</span>;

    <span class="k">void</span> <span class="me">setVoltage</span>(<span class="k">double</span> volts);
}</code></pre>''',
        "speak": "A field declared inside an interface is implicitly public static final, a shared constant, not per-object state. Intake I O dot Max underscore Volts reads it directly off the interface name, exactly like any other static final constant from Lesson 7.4.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public interface</span> <span class="t">Diagnosable</span>
{
    <span class="t">String</span> <span class="me">getStatus</span>();
}

<span class="k">public interface</span> <span class="t">LoggingDiagnosable</span> <span class="k">extends</span> <span class="t">Diagnosable</span>
{
    <span class="k">void</span> <span class="me">logStatus</span>(); <span class="c">// LoggingDiagnosable now requires BOTH getStatus() and logStatus()</span>
}</code></pre>''',
        "speak": "An interface can extend another interface, not a class, to build a bigger contract out of a smaller one. Unlike a class, an interface can extend more than one interface at once, since there's no object state to conflict. A class that implements Logging Diagnosable must provide both methods, the inherited one and the new one.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Default Methods</h2><ul>
      <li><span class="num">1</span><span>A <strong>default</strong> method has a real body, right inside the interface</span></li>
      <li><span class="num">2</span><span>Implementing classes inherit it automatically</span></li>
    </ul></div>''',
        "speak": "Normally every method in an interface is abstract. Default and static methods are the exceptions. A default method provides a real implementation directly inside the interface, marked with the default keyword, which implementing classes inherit automatically without being forced to write it themselves.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public interface</span> <span class="t">IntakeIO</span>
{
    <span class="k">void</span> <span class="me">updateInputs</span>(<span class="t">IntakeInputs</span> inputs);
    <span class="k">void</span> <span class="me">setVoltage</span>(<span class="k">double</span> volts);

    <span class="k">default void</span> <span class="me">stop</span>()
    {
        <span class="c">// built on top of the abstract method every implementer must provide</span>
        <span class="me">setVoltage</span>(<span class="n">0.0</span>);
    }
}</code></pre>''',
        "speak": "Update Inputs and set Voltage are still required, every implementing class must provide them. Stop comes for free: written once, here, every Intake I O implementation inherits it automatically, calling that implementation's own set Voltage. That's how default methods let an interface grow new methods later without breaking every class that already implements it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public interface</span> <span class="t">IntakeIO</span>
{
    <span class="k">static double</span> <span class="me">clampVolts</span>(<span class="k">double</span> v)
    {
        <span class="k">return</span> <span class="t">Math</span>.<span class="me">max</span>(-<span class="n">12.0</span>, <span class="t">Math</span>.<span class="me">min</span>(<span class="n">12.0</span>, v));
    }
}</code></pre>''',
        "speak": "An interface can also declare static methods, utility methods associated with the interface itself, not with any implementing object, called directly on the interface name rather than through an instance. Intake I O dot clamp Volts of fourteen calls it directly on the interface name, no Intake I O object needed, the same way Math dot max needs no Math object.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">When Two Defaults Collide</h2><ul>
      <li><span class="num">1</span><span>Two interfaces, same default signature &mdash; Java can't pick one for you</span></li>
      <li><span class="num">2</span><span>The implementing class must override it and resolve the conflict itself</span></li>
    </ul></div>''',
        "speak": "One wrinkle. If a class implements two interfaces that both supply a default method with the same signature, Java can't pick one for you. The class must override that method itself, calling one of them explicitly if that's what's wanted, or it's a compile error. This only comes up with defaults; two abstract methods with the same signature just merge into one requirement.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Interface or Abstract Class?</h2><ul>
      <li><span class="num">1</span><span><strong>Abstract class</strong> &mdash; shared state and code (fields, constructors, helper methods)</span></li>
      <li><span class="num">2</span><span><strong>Interface</strong> &mdash; shared methods only, or honoring several contracts at once</span></li>
    </ul></div>''',
        "speak": "Lesson 17.5 promised this comparison. Reach for an abstract class when the related classes share real state and code, like Robot Part's name and log method. Reach for an interface when classes only need to share a set of methods, with no shared state, and especially when a class needs to honor more than one contract at once, since a class can implement many interfaces but extend only one class.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Leaving even one required method unimplemented &mdash; fails to compile.</li>
      <li><span class="check">!</span>Writing an implementing method weaker than <strong>public</strong> &mdash; every interface method is implicitly public.</li>
      <li><span class="check">!</span>Making every method an empty default &mdash; silently removes the compiler's guarantee of real behavior.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Forgetting to implement every abstract method an interface declares fails to compile, every non-default, non-static method is a firm requirement. Writing an implementing method with weaker access than public, say package-private, fails to compile too. And making every interface method an empty default, quote unquote for convenience, silently removes the compiler's guarantee that an implementation provides real behavior, a class that forgets to override an empty default set Voltage compiles fine and simply never moves the motor.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An interface is a contract: method signatures with no body, implicitly public, implicitly public static final for fields.</li>
      <li><span class="check">&#10003;</span>A class <strong>implements</strong> any number of interfaces; an interface can <strong>extend</strong> one or more other interfaces.</li>
      <li><span class="check">&#10003;</span>An interface is a real type &mdash; variables, parameters, collections can all be declared against it.</li>
      <li><span class="check">&#10003;</span><strong>default</strong> methods add real behavior implementers inherit for free; <strong>static</strong> methods belong to the interface itself.</li>
      <li><span class="check">&#10003;</span>Abstract class: shared state and code. Interface: shared behavior only, or multiple contracts at once.</li>
    </ul></div>''',
        "speak": "So, to recap. An interface is a contract, method signatures with no implementation, default and static methods aside, specifying what a class can do, not how. Every abstract method is implicitly public, every field implicitly public static final. A class agrees with implements, any number at once, unlike the single-superclass limit of extends, and an interface can itself extend one or more other interfaces. An interface is a real type. A default method provides real behavior implementers inherit for free; a static method belongs to the interface itself. And the short version of abstract class versus interface: shared state and code means abstract class, shared behavior only, or multiple contracts at once, means interface. Next up, Lesson 19.1: lambdas and method references.",
    },
]
