BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 21 &middot; Static Factories</div>
      <h1>Static Factories</h1>
      <p class="scr-sub">A named method that hands you an object, instead of calling <code>new</code> yourself.</p>
    </div>''',
        "speak": "Welcome to Chapter 21, static factories. So far, whenever we've wanted an object, we've called new on a constructor directly. Today we look at an alternative, and at what it actually buys you.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What a Static Factory Method Is</h2><ul>
      <li><span class="num">1</span><span>A <code>public static</code> method that returns an object</span></li>
      <li><span class="num">2</span><span>Used <strong>instead of</strong> calling a constructor directly</span></li>
    </ul></div>''',
        "speak": "A static factory method is a public static method that returns an object, used instead of calling a constructor directly. At first glance, that looks like extra ceremony for no reason. But it buys a few concrete things a plain constructor can't.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Not Just <code>new</code>?</h2><ul>
      <li><span class="num">1</span><span><strong>A descriptive name</strong> &mdash; <code>MyCommands.print("Ready")</code> says exactly what you're getting</span></li>
    </ul></div>''',
        "speak": "First, a descriptive name. My Commands dot print, Ready, says exactly what you're getting. A constructor overload chosen by argument types alone doesn't communicate intent nearly as clearly.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Not Just <code>new</code>?</h2><ul>
      <li><span class="num">1</span><span><strong>A descriptive name</strong> &mdash; <code>MyCommands.print("Ready")</code> says exactly what you're getting</span></li>
      <li><span class="num">2</span><span><strong>Freedom not to construct anything new</strong> &mdash; it can return a cached, existing instance</span></li>
    </ul></div>''',
        "speak": "Second, the freedom to not construct a new object at all. A factory method can return a cached, already existing instance instead of a fresh one. A constructor, by contrast, always creates something new.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Not Just <code>new</code>?</h2><ul>
      <li><span class="num">1</span><span><strong>A descriptive name</strong> &mdash; <code>MyCommands.print("Ready")</code> says exactly what you're getting</span></li>
      <li><span class="num">2</span><span><strong>Freedom not to construct anything new</strong> &mdash; it can return a cached, existing instance</span></li>
      <li><span class="num">3</span><span><strong>Freedom to return a different concrete type</strong> &mdash; the caller only sees the return type</span></li>
    </ul></div>''',
        "speak": "And third, the freedom to return a completely different concrete type, chosen by logic inside the method. The caller only ever sees the return type, often an interface, never which concrete class was actually picked.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">MyCommands</span>
{
    <span class="k">public static</span> <span class="t">Command</span> <span class="me">print</span>(<span class="t">String</span> msg)
    {
        <span class="k">return</span> <span class="t">Command</span>.<span class="me">noRequirements</span>(coroutine -&gt; System.out.println(msg))
            .<span class="me">named</span>(<span class="s">"Print "</span> + msg);
    }
}</code></pre>''',
        "speak": "Here's one. My Commands dot print, Ready, reads clearly as: give me a command that prints this message. The caller never needs to know, or care, that it's built from Command dot no Requirements, from Lesson 25.2, underneath.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">SensorLog</span>
{
    <span class="k">private static final</span> <span class="t">SensorLog</span> INSTANCE = <span class="k">new</span> SensorLog();

    <span class="k">public static</span> <span class="t">SensorLog</span> <span class="me">getInstance</span>()
    {
        <span class="k">return</span> INSTANCE; <span class="c">// the same object every call — never a fresh one</span>
    }
}</code></pre>''',
        "speak": "That cached-instance freedom isn't just theoretical, here it is in practice. Sensor Log dot get Instance always hands back the exact same object, the one built once, when the class first loads. A constructor could never do this, new Sensor Log always builds a fresh one.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 21 &middot; Static Factories</div>
      <h1>Choosing an Implementation by Condition</h1>
      <p class="scr-sub">Real or simulated hardware, decided in exactly one place.</p>
    </div>''',
        "speak": "The pattern's biggest use in FRC code is picking between real and simulated hardware, deciding which concrete class to construct, in exactly one place, based on a condition.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public interface</span> <span class="t">Drivetrain</span>
{
    <span class="k">void</span> <span class="me">drive</span>(<span class="k">double</span> speed, <span class="k">double</span> turn);
}

<span class="k">public class</span> <span class="t">RealDrivetrain</span> <span class="k">implements</span> <span class="t">Drivetrain</span>
{
    <span class="me">@Override</span>
    <span class="k">public void</span> <span class="me">drive</span>(<span class="k">double</span> speed, <span class="k">double</span> turn)
    {
        <span class="c">// control the real motor controllers</span>
    }
}

<span class="k">public class</span> <span class="t">SimDrivetrain</span> <span class="k">implements</span> <span class="t">Drivetrain</span>
{
    <span class="me">@Override</span>
    <span class="k">public void</span> <span class="me">drive</span>(<span class="k">double</span> speed, <span class="k">double</span> turn)
    {
        <span class="c">// simulate motion via WPILib sim</span>
    }
}</code></pre>''',
        "speak": "Start with one interface, Drive Train, with a single drive method. Then two implementations of it, each in its own file. Real Drive Train controls the real motor controllers. Sim Drive Train simulates the motion, using WPILib's simulation support.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">DrivetrainFactory</span>
{
    <span class="k">private</span> DrivetrainFactory() {} <span class="c">// never instantiated — only static members</span>

    <span class="k">public static</span> <span class="t">Drivetrain</span> <span class="me">createDrivetrain</span>()
    {
        <span class="k">if</span> (RobotBase.isReal())
        {
            <span class="k">return new</span> RealDrivetrain();
        }
        <span class="k">else</span>
        {
            <span class="k">return new</span> SimDrivetrain();
        }
    }
}</code></pre>''',
        "speak": "And then the factory. It gets a private constructor, since it exists purely to hold static members, nothing should ever build one with new. Create Drive Train checks Robot Base dot is real. On the real robot, it returns a Real Drive Train, otherwise, a Sim Drive Train. Notice the return type is just Drive Train, the interface, either way.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// caller never picks the concrete class itself</span>
<span class="t">Drivetrain</span> drivetrain = DrivetrainFactory.createDrivetrain();</code></pre>''',
        "speak": "From the caller's side, it's one line. Ask the factory for a drive train, and get back whichever one fits. The caller never picks the concrete class itself.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">An Alternative to Constructor Injection</h2><ul>
      <li><span class="num">1</span><span>Ch.20: the <strong>caller</strong> decided which <code>IntakeIO</code> to pass in</span></li>
      <li><span class="num">2</span><span>A factory makes that decision <strong>itself</strong> &mdash; the real-vs-sim logic lives in one place</span></li>
    </ul></div>''',
        "speak": "This is a genuine alternative to constructor injection, the style from the IO-Layer Pattern, back in Chapter 20, where the caller decides which implementation to use and passes it in through a constructor parameter, the way Chapter 20's Robot constructor builds its own Intake IO Real. Here, the factory itself makes that decision, centralizing the real versus sim check in one place, instead of repeating it at every construction site. WPILib's own API uses this pattern too. Rotation2d dot from Degrees, from Lesson 4.5, is a real static factory.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">AutoFactory</span>
{
    <span class="k">public static</span> <span class="t">Command</span> <span class="me">createAuto</span>(<span class="t">String</span> mode)
    {
        <span class="k">return switch</span> (mode)
        {
            <span class="k">case</span> <span class="s">"Taxi"</span> -&gt; MyCommands.driveForward(<span class="n">3.0</span>);
            <span class="k">case</span> <span class="s">"2 Ball"</span> -&gt; MyCommands.twoBallAuto();
            <span class="k">case</span> <span class="s">"Nothing"</span> -&gt; Command.waitFor(Seconds.of(<span class="n">0.1</span>)).named(<span class="s">"Do Nothing"</span>);
            <span class="k">case</span> <span class="k">null</span>, <span class="k">default</span> -&gt; MyCommands.print(<span class="s">"Unknown Auto Mode"</span>);
        };
    }
}</code></pre>''',
        "speak": "Factories work for more than hardware, too. This is a switch expression, from Lesson 5.12, over a String. Create auto takes a mode name and switches on it. Taxi drives forward, two ball runs a two ball auto, nothing just waits, and case null comma default catches both an unrecognized mode and a null one, printing a warning instead.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// org.wpilib.tunable — the 2027 driver-station chooser</span>
Selectable&lt;String&gt; chooser = <span class="k">new</span> Selectable&lt;&gt;();
chooser.addDefault(<span class="s">"Taxi"</span>, <span class="s">"Taxi"</span>);

<span class="c">// built from whatever the driver station selected</span>
<span class="t">Command</span> auto = AutoFactory.createAuto(chooser.getSelected());</code></pre>''',
        "speak": "Selectable, from org dot wpilib dot tunable, is the 2027 driver-station chooser. Its get Selected can return null, if nothing was ever picked and no default was set with add Default, which is exactly why that null case matters: switching on a null String without it throws a Null Pointer Exception.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Returning a concrete class instead of an interface &mdash; return <code>Drivetrain</code>, not <code>RealDrivetrain</code>.</li>
      <li><span class="check">!</span>Duplicating the same real-vs-sim check in multiple places.</li>
      <li><span class="check">!</span>Confusing a factory with a constructor &mdash; a factory is just a regular static method.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Returning a concrete class instead of an interface, a factory declared to return Real Drive Train locks every caller into that one implementation, so return the interface type, Drive Train, and keep the real choice hidden inside the factory. Duplicating the same real versus sim check in multiple places, the whole point of a factory is centralizing that decision in one method, and scattering is real checks throughout the codebase defeats the purpose. And confusing a factory with a constructor. A factory method is just a regular static method, it can return a cached instance or pick any subtype, neither of which a constructor is free to do, since a constructor always returns a new instance of its own exact class. A factory method can validate its arguments, but so can a constructor, from Lesson 12, that part isn't a difference between them.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A static factory returns an object instead of a direct constructor call &mdash; with a name, caching, and type freedom.</li>
      <li><span class="check">&#10003;</span>Its most common FRC use: centralizing real-vs-sim selection in one place, an alternative to constructor injection.</li>
      <li><span class="check">&#10003;</span>It generalizes to anything chosen by a condition, like an autonomous mode &mdash; watch for <code>null</code>.</li>
      <li><span class="check">&#10003;</span>Always return the interface type; a factory-only class gets a <strong>private</strong> constructor.</li>
    </ul></div>''',
        "speak": "So, to recap. A static factory method returns an object in place of a direct constructor call, with a descriptive name, the option to return a cached instance, and the freedom to choose the actual concrete type internally. Its most common FRC use is centralizing real versus simulated selection, or comp bot versus practice bot, in one place, an alternative to constructor injection, so callers only ever depend on an interface. Factories generalize beyond hardware, anything selected by a condition, an autonomous mode, a config option, is a natural fit, and a switch expression choosing between commands needs case null comma default if the input could be null. Always return the interface type from a factory, not a specific concrete class, and give a factory-only class a private constructor, since nothing should ever build one with new. Next up, Chapter 22: the Builder Pattern.",
    },
]
