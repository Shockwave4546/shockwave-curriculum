BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 17 &middot; Inheritance &amp; Abstractions</div>
      <h1>Inheritance, Superclass, Subclass</h1>
      <p class="scr-sub">One class inheriting fields and methods from another &mdash; and when that's the right call.</p>
    </div>''',
        "speak": "Welcome to Chapter 17. Every subsystem on a robot shares some real structure, and today we meet the tool Java gives us for sharing it properly: inheritance.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Inheritance Does</h2><ul>
      <li><span class="num">1</span><span>One class inherits fields and methods from another.</span></li>
      <li><span class="num">2</span><span>The class inherited <em>from</em> is the <strong>superclass</strong> (parent); the one doing the inheriting is the <strong>subclass</strong> (child).</span></li>
    </ul></div>''',
        "speak": "Inheritance lets one class inherit fields and methods from another. The class being inherited from is the superclass, sometimes called the parent class. The class doing the inheriting is the subclass, or child class.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Subsystems Share Real Structure</h2><ul>
      <li><span class="num">1</span><span>A name, for logging</span></li>
      <li><span class="num">2</span><span>A <strong>stop()</strong> method</span></li>
      <li><span class="num">3</span><span>A <strong>periodic()</strong> method WPILib calls every loop</span></li>
    </ul></div>''',
        "speak": "Think about every subsystem on an FRC robot. Each one has a name for logging, a stop method, and a periodic method that WPILib calls every loop. That shared structure makes them a natural fit for one common superclass.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public abstract class</span> <span class="t">Subsystem</span>
{
    <span class="k">private</span> <span class="t">String</span> name;

    <span class="k">public</span> Subsystem(<span class="t">String</span> name) { this.name = name; }
    <span class="k">public</span> <span class="t">String</span> getName() { <span class="k">return</span> name; }
    <span class="k">public void</span> log(<span class="t">String</span> msg) { System.out.println(<span class="s">"["</span> + name + <span class="s">"] "</span> + msg); }
}</code></pre>''',
        "speak": "Here's that superclass. Subsystem holds a private name, a constructor that sets it, a get name method, and a log method that prints any message tagged with the subsystem's name in square brackets.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">Subsystem</span>
{
    <span class="c">// inherits getName() and log() for free</span>
}</code></pre>''',
        "speak": "And here's a subclass. The keyword extends is what sets up inheritance. Intake extends Subsystem, so Intake gets get name and log for free, without writing either one again.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Exactly One Superclass</h2><ul>
      <li><span class="num">1</span><span>A Java class can only <strong>extends</strong> <em>one</em> superclass &mdash; no multiple inheritance of this kind.</span></li>
      <li><span class="num">2</span><span>No <strong>extends</strong> at all? The class implicitly inherits from Java's built-in <strong>Object</strong> class.</span></li>
    </ul></div>''',
        "speak": "A Java class can only extend one superclass. Unlike a person with two biological parents, Java has no multiple inheritance of this kind. And leaving extends off entirely doesn't mean no parent. It means the class implicitly inherits from Java's built-in Object class, which we'll look at in lesson 17.4.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The is-a Relationship</h2><ul>
      <li><span class="num">1</span><span>An <strong>Intake</strong> <em>is a</em> Subsystem. A <strong>Climber</strong> <em>is a</em> Subsystem.</span></li>
      <li><span class="num">2</span><span>The substitution test: could the subclass stand in anywhere the superclass is expected, and still make sense?</span></li>
    </ul></div>''',
        "speak": "Inheritance should only model a genuine is a relationship. An Intake is a Subsystem. A Climber is a Subsystem. Here's the test to apply: could you substitute the subclass anywhere the superclass is expected, and have it still make sense?",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The is-a Relationship</h2><ul>
      <li><span class="num">1</span><span>An <strong>Intake</strong> <em>is a</em> Subsystem. A <strong>Climber</strong> <em>is a</em> Subsystem.</span></li>
      <li><span class="num">2</span><span>The substitution test: could the subclass stand in anywhere the superclass is expected, and still make sense?</span></li>
      <li><span class="num">3</span><span><strong>Vision</strong> passes. A <strong>Robot</strong>, or a <strong>Controller</strong> wrapping a joystick, doesn't.</span></li>
    </ul></div>''',
        "speak": "A Vision processor being asked to stop, and getting logged, makes perfect sense as a Subsystem, so it passes. But a Robot class itself, or a Controller wrapping a joystick, isn't a kind of Subsystem, even if it happens to interact with one.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">has-a: Holding a Reference</div>
    <pre class="code"><code><span class="k">public class</span> <span class="t">Robot</span>
{
    <span class="k">private</span> <span class="t">Drivetrain</span> drivetrain;  <span class="c">// has-a: Robot holds a Drivetrain, isn't one</span>
    <span class="k">private</span> <span class="t">Intake</span> intake;          <span class="c">// has-a</span>
}</code></pre>''',
        "speak": "The has a relationship, also called association, is different. That's when one class simply holds a reference to another, without being a specialized kind of it. A Robot has a Drive Train and an Intake, as fields. It isn't a subclass of either one. Compare that to Intake extends Subsystem, which is is a: an Intake really is a specialized kind of Subsystem.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Bother</h2><ul>
      <li><span class="num">1</span><span><strong>Generalization</strong> &mdash; pull shared data and behavior up into one common parent.</span></li>
    </ul></div>''',
        "speak": "Two forces motivate reaching for a superclass. The first is generalization. Several classes already share data or behavior, so you pull the shared parts up into one common parent. Intake, Shooter, and Climber all need a name and a log method, and that's exactly what Subsystem is for.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Bother</h2><ul>
      <li><span class="num">1</span><span><strong>Generalization</strong> &mdash; pull shared data and behavior up into one common parent.</span></li>
      <li><span class="num">2</span><span><strong>Specialization</strong> &mdash; keep most of a parent's behavior, but add or change something of your own.</span></li>
    </ul></div>''',
        "speak": "The second is specialization. A class wants most of a parent's behavior, but needs to add something of its own, or do one thing differently. Intake inherits log unchanged, but it still needs its own stop method, specific to its own motor.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using inheritance purely to reuse code, with no real is-a relationship &mdash; use has-a (a field) instead.</li>
      <li><span class="check">!</span>Forgetting every class has exactly one superclass &mdash; no extends means Object.</li>
      <li><span class="check">!</span>Trying to extend more than one class &mdash; it doesn't compile.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Don't use inheritance purely to reuse code. If the substitution test fails, model it as has a, a field, instead of extends. Don't forget that a class always has exactly one superclass, leaving off extends means the parent is Object. And don't try to extend two classes at once, that doesn't compile. Java allows only one extends, though a class can implement multiple interfaces.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>extends declares inheritance: the subclass gains the superclass's fields and methods.</li>
      <li><span class="check">&#10003;</span>Only one superclass per class; no extends means extending Object.</li>
      <li><span class="check">&#10003;</span>Use inheritance only for a genuine is-a &mdash; check with the substitution test.</li>
      <li><span class="check">&#10003;</span>has-a (association) is the right model when is-a doesn't apply.</li>
    </ul></div>''',
        "speak": "So, to recap. Extends declares inheritance, and the subclass gains the superclass's fields and methods. A class can only extend one superclass, and leaving extends off means extending Object. Use inheritance only for a genuine is a relationship, verified with the substitution test. And when is a doesn't really apply, has a, one class holding a reference to another, is the right model. Next up, lesson 17.2: how constructors work with inheritance.",
    },
]
