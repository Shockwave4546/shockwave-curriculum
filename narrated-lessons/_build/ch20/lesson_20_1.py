BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 20 &middot; The IO-Layer Pattern</div>
      <h1>The IO-Layer Pattern</h1>
      <p class="scr-sub">Keeping hardware access completely separate from the logic that uses it.</p>
    </div>''',
        "speak": "Welcome to Chapter 20. Everything from the last three chapters, inheritance, polymorphism, and especially interfaces as contracts, comes together here, in a real, widely used FRC architecture pattern: keeping hardware access completely separate from the logic that uses it.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Problem: Hardware Everywhere</h2><ul>
      <li><span class="num">1</span><span>A subsystem that talks straight to motors and sensors can't run without the physical robot</span></li>
    </ul></div>''',
        "speak": "Start with the problem. A subsystem that talks directly to real motor controllers and sensors is genuinely hard to reason about. It can't run at all without the physical robot present, and there's no clean seam anywhere you could intercept its data.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Problem: Hardware Everywhere</h2><ul>
      <li><span class="num">1</span><span>A subsystem that talks straight to motors and sensors can't run without the physical robot</span></li>
      <li><span class="num">2</span><span>A stronger idea logs <strong>every</strong> input flowing into the robot code, every loop cycle</span></li>
    </ul></div>''',
        "speak": "A stronger idea than typical FRC logging solves this. Instead of logging just a handful of chosen values, log every single input flowing into the robot code, every loop cycle.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Problem: Hardware Everywhere</h2><ul>
      <li><span class="num">1</span><span>A subsystem that talks straight to motors and sensors can't run without the physical robot</span></li>
      <li><span class="num">2</span><span>A stronger idea logs <strong>every</strong> input flowing into the robot code, every loop cycle</span></li>
      <li><span class="num">3</span><span>So a match can be <strong>replayed</strong> off the robot, same inputs, same logic</span></li>
    </ul></div>''',
        "speak": "Since every input is captured, a match can later be replayed off the robot, with the exact same inputs, running the exact same logic. That turns logging from a tool for checking specific values into a real safety net, for verifying how any part of the code actually behaved. A logging framework, Chapter 33, can record and replay data structured this way. But it only works if all input data flows through one well-defined seam. That seam is what the IO layer is for.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Layers of a Subsystem</h2><ul>
      <li><span class="num">1</span><span><strong>Public interface</strong> &mdash; the methods the rest of the robot calls</span></li>
      <li><span class="num">2</span><span><strong>Control logic</strong> &mdash; deciding what to do with sensor data</span></li>
      <li><span class="num">3</span><span><strong>Hardware interface</strong> &mdash; actually reading sensors, actually commanding motors</span></li>
    </ul></div>''',
        "speak": "Traditionally, an FRC subsystem mixes three concerns in one class. Its public interface, the methods the rest of the robot calls. Its control logic, deciding what to do with sensor data. And its hardware interface, actually reading sensors and actually commanding motors. The IO-Layer Pattern pulls that third piece out into its own object. Commands v3, Chapter 25, calls this kind of class a Mechanism; this chapter keeps calling it a subsystem, the term used across the pattern's whole history.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public interface</span> <span class="t">IntakeIO</span>
{
    <span class="k">void</span> <span class="me">updateInputs</span>(<span class="t">IntakeInputs</span> inputs);
    <span class="k">void</span> <span class="me">setVoltage</span>(<span class="k">double</span> volts);
}</code></pre>''',
        "speak": "Here it is. Intake IO is exactly the kind of contract from Chapter 19. It says what an intake can do, report its inputs, and accept a voltage command, without saying anything about how. Both methods are abstract, since neither one has a sensible default.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">IntakeIOReal</span> <span class="k">implements</span> <span class="t">IntakeIO</span>
{
    <span class="c">// uses real hardware APIs to move physical rollers</span>
}

<span class="k">public class</span> <span class="t">IntakeIOSim</span> <span class="k">implements</span> <span class="t">IntakeIO</span>
{
    <span class="c">// uses physics math (moment of inertia) to "fake" the robot in code</span>
}</code></pre>''',
        "speak": "Two real implementations honor that same contract, each in its own file. Intake IO Real uses real hardware APIs to move physical rollers. Intake IO Sim uses physics math, moment of inertia, to fake the robot entirely in code.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Subsystem Only Knows the Interface</h2><ul>
      <li><span class="num">1</span><span>The subsystem class only ever talks to <code>IntakeIO</code></span></li>
      <li><span class="num">2</span><span>It never knows which concrete implementation is running underneath</span></li>
    </ul></div>''',
        "speak": "The subsystem class itself only ever talks to the Intake IO interface. It never knows, and never needs to know, which concrete implementation is actually running underneath it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="me">Robot</span>()
{
    <span class="k">if</span> (<span class="t">RobotBase</span>.<span class="me">isReal</span>())
    {
        intake = <span class="k">new</span> Intake(<span class="k">new</span> IntakeIOReal());
    }
    <span class="k">else</span>
    {
        intake = <span class="k">new</span> Intake(<span class="k">new</span> IntakeIOSim());
    }
}</code></pre>''',
        "speak": "So which one runs? That's decided in exactly one place, typically the Robot constructor, at startup. Robot Base dot is Real, from org dot wpilib dot framework, is the actual check that's true only on real SystemCore hardware. If it's real, the subsystem gets built with the real implementation. Otherwise, in simulation, it gets the sim implementation. That's the whole choice, made once.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Chosen Once, at Construction</h2><ul>
      <li><span class="num">1</span><span><code>Intake</code> accepts an <code>IntakeIO</code> in its constructor and stores it</span></li>
      <li><span class="num">2</span><span>Every call after that dispatches polymorphically to whichever implementation was supplied</span></li>
    </ul></div>''',
        "speak": "Intake, the subsystem, accepts an Intake IO in its constructor and stores it. Every call from then on goes through that one reference, polymorphically, just like Lesson 18.3, dispatching to whichever implementation was actually supplied.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Outputs vs. Inputs</h2><ul>
      <li><span class="num">1</span><span><strong>Outputs</strong> (like <code>setVoltage</code>) are simple, one-way method calls</span></li>
      <li><span class="num">2</span><span><strong>Inputs</strong> go into a shared object: public fields for every hardware value</span></li>
    </ul></div>''',
        "speak": "Outputs, commands like set voltage, are simple, one-way method calls. Inputs get handled more carefully, since they need to be read consistently, and stay replayable later. Each IO interface has an accompanying inputs class, holding public fields for every value that comes off the hardware. That's a plain data holder with no logic of its own, so it's an intentional exception to the private-field style Chapter 7 taught.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// pull fresh data from the IO layer into inputs, once per cycle</span>
io.updateInputs(inputs);</code></pre>''',
        "speak": "Each cycle, one line does the work. IO dot update inputs pulls fresh data from the IO layer into the inputs object.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Always Read From <code>inputs</code></h2><ul>
      <li><span class="num">1</span><span>The rest of the subsystem reads the <code>inputs</code> object &mdash; never the IO layer directly</span></li>
      <li><span class="num">2</span><span>Every piece of code in one loop cycle sees the exact same cached values</span></li>
    </ul></div>''',
        "speak": "The rest of the subsystem then reads from that inputs object, never straight from the IO layer, and for a critical reason. Every piece of code within one loop cycle sees the exact same cached values, so the logic feeds off exactly the same numbers a replay later would see, instead of whatever the hardware happens to report at the exact instant each line runs.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 20 &middot; The IO-Layer Pattern</div>
      <h1>Ports and Adapters</h1>
      <p class="scr-sub">The general architecture idea behind the IO layer.</p>
    </div>''',
        "speak": "This isn't an FRC-specific trick. It's a specific application of a broader, well-known software architecture idea, called Hexagonal Architecture, or Ports and Adapters.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">Intake (core logic)</div><div class="darrow">&rarr;</div>
      <div class="dbox active">IntakeIO (port)</div>
    </div>
    <div class="scr-diagram" style="margin-top:14px;">
      <div class="dbox">IntakeIOReal (adapter)</div>
      <div class="dbox">IntakeIOSim (adapter)</div>
    </div>''',
        "speak": "The idea is to keep core logic decoupled from whatever external system it happens to talk to, a database, a user interface, or real hardware. You define a port, the interface, here Intake IO, that any number of adapters can plug into, here the real and sim implementations. The core logic only ever depends on the port, never on any specific adapter, exactly mirroring Intake only ever depending on Intake IO.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Tradeoff Is Real</h2><ul>
      <li><span class="num">1</span><span>More abstraction and more files than talking to hardware directly</span></li>
      <li><span class="num">2</span><span>Pays for itself once testability, simulation, or swappable hardware matter</span></li>
    </ul></div>''',
        "speak": "The tradeoff is real. It's more abstraction and more files than just talking to hardware directly, which is overkill for a one-off script. But it pays for itself the moment testability, simulation, or swappable hardware actually matter, and for a competition robot, they do.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Letting the subsystem read hardware directly, bypassing the IO layer &mdash; no sim support, no clean replay.</li>
      <li><span class="check">!</span>Adding getters to the IO interface and reading them directly, instead of reading the cached inputs object.</li>
      <li><span class="check">!</span>Treating the IO layer as optional overhead on a small subsystem.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Letting the subsystem read hardware directly, bypassing the IO layer, brings back exactly the coupling the pattern exists to remove, no sim support, no clean replay. Adding getters to the IO interface and calling them from the subsystem's logic instead of reading the cached inputs object is the second. Intake IO itself has nothing to read, but as soon as an implementation grows a getter, reaching for it directly reintroduces values that can change mid-cycle in ways a replayed log never could, so always read from inputs. And third, treating the IO layer as optional overhead on a small subsystem. Yes, it's more files and more ceremony, but that payoff, simulation, replay, and decoupled testing, is exactly why competitive FRC codebases use it anyway.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>The IO layer moves a subsystem's hardware access into its own interface.</li>
      <li><span class="check">&#10003;</span>One interface, real and sim implementations, chosen once at construction.</li>
      <li><span class="check">&#10003;</span>Inputs flow through a shared object, so every piece of logic in a cycle reads the same snapshot.</li>
      <li><span class="check">&#10003;</span>It's Ports and Adapters: core logic depends only on the port, never a specific adapter.</li>
    </ul></div>''',
        "speak": "So, to recap. The IO-Layer Pattern separates a subsystem's hardware access into its own interface, so the subsystem's logic never touches real hardware APIs directly. One interface, multiple implementations, real hardware or simulated, chosen once at construction, with everything else dispatching polymorphically through that shared interface. Inputs flow through a dedicated, shared object, update inputs, called once per cycle, so every piece of logic in that cycle reads the exact same snapshot, the structure a logging framework needs to record and replay a match later. And it's FRC's own application of Hexagonal Architecture, Ports and Adapters: core logic depends only on a port, the interface, never on a specific adapter. Next up, Chapter 21: static factories.",
    },
]
