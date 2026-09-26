BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 23 &middot; Encapsulation &amp; final</div>
      <h1>Access, <code>final</code>, and Immutability</h1>
      <p class="scr-sub">Who's allowed to touch a class's data, and what can never change once it's set.</p>
    </div>''',
        "speak": "Welcome to Chapter 23. Lesson 7.2 already covered where a variable lives, scope. Today is about two different questions: who, outside a class, is allowed to touch its data, and what can be guaranteed to never change once it's set.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span>
{
    <span class="k">public</span> <span class="t">String</span> status;        <span class="c">// reachable from anywhere</span>
    <span class="k">protected double</span> maxSpeed;   <span class="c">// reachable from the same package, or any subclass</span>
    <span class="k">double</span> gearRatio;            <span class="c">// no modifier — reachable only from the same package</span>
    <span class="k">private boolean</span> calibrated;  <span class="c">// reachable only from inside Intake itself</span>
}</code></pre>''',
        "speak": "Java actually has four access levels, not two. Public and private are the ones you've used everywhere so far; here they are together with the other two, protected, and package-private, which is what a field gets when it has no modifier at all.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Four Access Levels</h2><ul>
      <li><span class="num">1</span><span><code>public</code> &mdash; reachable everywhere</span></li>
      <li><span class="num">2</span><span><code>protected</code> &mdash; same package, or any subclass</span></li>
      <li><span class="num">3</span><span>package-private (no modifier) &mdash; same package only</span></li>
      <li><span class="num">4</span><span><code>private</code> &mdash; the declaring class only</span></li>
    </ul></div>''',
        "speak": "Public reaches everywhere. Protected reaches the same package, or any subclass, even in a different package. Package-private, no keyword at all, only reaches the same package. And private only reaches the declaring class itself. Protected came up briefly in Lesson 17.2, for reaching a superclass's member directly from a subclass — this is the full comparison.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2"><code>final</code>: Not Just for Fields</h2><ul>
      <li><span class="num">1</span><span>Can mark a local, a parameter, a field, a method, or a class</span></li>
      <li><span class="num">2</span><span>Means something related, but slightly different, in each place</span></li>
    </ul></div>''',
        "speak": "Now, final. Final can mark a local variable, a parameter, a field, a method, or a whole class, and it means something related, but slightly different, in each place.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public double</span> <span class="me">clamp</span>(<span class="k">final double</span> target, <span class="k">double</span> limit)
{
    <span class="c">// target = -target; would be a compile error here — target is final</span>
    <span class="k">return</span> Math.<span class="me">min</span>(target, limit);
}</code></pre>''',
        "speak": "Start with locals and parameters. A final local variable or parameter can be assigned exactly once, same as a field. Here, target is a final parameter — reassigning it inside the method would be a compile error.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">class</span> <span class="t">BatteryMonitor</span>
{
    <span class="k">private final</span> <span class="t">String</span> label;   <span class="c">// no initializer here — that's legal</span>

    <span class="k">public</span> <span class="me">BatteryMonitor</span>(<span class="t">String</span> label)
    {
        <span class="k">this</span>.label = label;       <span class="c">// as long as every constructor assigns it exactly once</span>
    }
}</code></pre>''',
        "speak": "Fields work a little differently. A final field doesn't need a value in its declaration — it can stay blank there, as long as every constructor assigns it exactly once, on every path through that constructor. Here, label gets its one assignment inside the constructor.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Blank Final Rule</h2><ul>
      <li><span class="num">1</span><span>Unassigned on some constructor path &mdash; compile error, not a runtime <code>null</code></span></li>
    </ul></div>''',
        "speak": "Leave a blank final field unassigned in some constructor, and it's a compile error, variable label might not have been initialized, not a null waiting to happen at runtime.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">class</span> <span class="t">RobotPart</span>
{
    <span class="k">public final</span> <span class="t">String</span> <span class="me">getName</span>() { <span class="k">return</span> name; }
    <span class="c">// ...</span>
}

<span class="k">class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">RobotPart</span>
{
    @Override
    <span class="k">public</span> <span class="t">String</span> <span class="me">getName</span>() { <span class="k">return</span> <span class="s">"Intake"</span>; }
    <span class="c">// COMPILE ERROR — getName() is final in RobotPart</span>
}</code></pre>''',
        "speak": "Methods: a final method can't be overridden by a subclass, full stop. Here, RobotPart's getName is final. Intake trying to override it fails to compile, right there.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2"><code>final</code> Classes</h2><ul>
      <li><span class="num">1</span><span>Can't be extended by anything, anywhere &mdash; <code>String</code> is one</span></li>
      <li><span class="num">2</span><span>Records (coming up) are implicitly <code>final</code> too</span></li>
    </ul></div>''',
        "speak": "A final class can't be extended by anything, anywhere. String is one, which is why a class extending String never compiles. Records, coming up, are implicitly final too.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> baseSpeed = <span class="n">0.5</span>;
baseSpeed = <span class="n">0.6</span>;
<span class="t">Runnable</span> r = () -&gt; System.out.<span class="me">println</span>(baseSpeed);
<span class="c">// COMPILE ERROR — baseSpeed isn't effectively final</span></code></pre>''',
        "speak": "One more form: effectively final. A local variable captured by a lambda doesn't have to be declared final, but it does have to behave like one, never reassigned anywhere after its first assignment. Here, reassigning base speed before the lambda disqualifies it — the lambda's capture is what fails to compile.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Reference vs. the Object</h2><ul>
      <li><span class="num">1</span><span>A <code>final Encoder</code> reference can never be repointed</span></li>
      <li><span class="num">2</span><span>But the <code>Encoder</code>'s own internal state can still change</span></li>
    </ul></div>''',
        "speak": "On an object reference, all of this only ever locks the reference itself. A final Encoder, WPILib's real rotation Encoder class, can never be pointed at a different Encoder. But nothing about final stops that Encoder's own internal state from changing as it spins. That gap, between the reference can't change, and nothing about the object can change, is exactly what the rest of this lesson is about.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">class</span> <span class="t">PitNotes</span>
{
    <span class="k">private final</span> <span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt; notes = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt;();

    <span class="k">public</span> <span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt; <span class="me">getNotes</span>()
    {
        <span class="k">return</span> notes; <span class="c">// leak — the caller now holds the SAME list object</span>
    }
}</code></pre>''',
        "speak": "Encapsulation leaks. Marking a field private isn't automatically enough to protect it. Here, PitNotes's notes list is private and final, but getNotes hands back a direct reference to that same list. Anything the caller does to the returned list changes PitNotes's own data, with none of PitNotes's own methods ever running.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="me">getNotes</span>()
{
    <span class="c">// a defensive copy — an unmodifiable snapshot, not the real list</span>
    <span class="k">return</span> <span class="t">List</span>.<span class="me">copyOf</span>(notes);
}</code></pre>''',
        "speak": "The fix is a defensive copy: hand back a new object with the same contents, instead of the original. List dot copy of notes gives the caller its own unmodifiable snapshot. Mutating it can't touch PitNotes's real data at all.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public record</span> <span class="t">Reading</span>(<span class="k">double</span> volts, <span class="k">double</span> timestampSeconds)
{
    <span class="k">public</span> <span class="me">Reading</span>
    {
        <span class="k">if</span> (volts &lt; <span class="n">0</span>)
        {
            <span class="k">throw new</span> <span class="t">IllegalArgumentException</span>(<span class="s">"volts can't be negative"</span>);
        }
    }
}</code></pre>''',
        "speak": "Records. When a class is really just a bundle of values, Java's record writes the immutable version of it for you. One line generates private final fields, a constructor, and here, a compact constructor validating that volts isn't negative, which runs before the fields are even assigned.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Reading</span> r = <span class="k">new</span> <span class="t">Reading</span>(<span class="n">12.6</span>, <span class="n">41.2</span>);
System.out.<span class="me">println</span>(r.<span class="me">volts</span>());   <span class="c">// an accessor named after the field, not getVolts()</span>
System.out.<span class="me">println</span>(r);           <span class="c">// Reading[volts=12.6, timestampSeconds=41.2]</span></code></pre>''',
        "speak": "Using it: an accessor named after the field, volts, not get volts, and printing the record itself for free, in the form Reading, volts equals, timestamp seconds equals. Record also generates working equals, hash code, and to string for free, and it's implicitly final, so nothing can extend it.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">An Immutability Checklist</h2><ul>
      <li><span class="num">1</span><span>Every field <code>private final</code></span></li>
      <li><span class="num">2</span><span>No setters &mdash; only a constructor ever assigns a field</span></li>
      <li><span class="num">3</span><span>Mutable fields (arrays, collections) copied going in and out</span></li>
      <li><span class="num">4</span><span>Reach for a <code>record</code> first, when the class is just a bundle of values</span></li>
    </ul></div>''',
        "speak": "Pulling it together: an immutability checklist. Every field private final. Nothing but a constructor ever assigns a field, no setters. Any mutable field, like an array or a collection, gets defensively copied going in, and going out. And when the class is really just a bundle of values, reach for a record first — it satisfies every one of those by construction.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Returning a mutable field directly from a getter &mdash; return a defensive copy instead.</li>
      <li><span class="check">!</span>Leaving a blank <code>final</code> field unassigned on some constructor path.</li>
      <li><span class="check">!</span>Reassigning a variable after using it in a lambda.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Returning a mutable field directly from a getter — private doesn't protect it once a reference escapes, so return a defensive copy instead. Leaving a blank final field unassigned on some constructor path — every constructor must assign it exactly once. And reassigning a variable after using it in a lambda — that breaks effectively final, and the lambda's capture is what fails to compile.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Four access levels: public, protected, package-private, private.</li>
      <li><span class="check">&#10003;</span>final: one assignment for locals/fields; blocks overriding on methods, extending on classes.</li>
      <li><span class="check">&#10003;</span>A lambda can only capture a final or effectively final local.</li>
      <li><span class="check">&#10003;</span>private isn't automatic protection &mdash; return defensive copies of mutable fields.</li>
      <li><span class="check">&#10003;</span>record gives you an immutable, final class in one line.</li>
    </ul></div>''',
        "speak": "So, to recap. Java has four access levels, public, protected, package-private, and private, differing in whether same-package code and subclasses elsewhere can reach a member. Final means assign exactly once for locals, parameters, and fields, with the blank-final rule for constructors; on a method it blocks overriding, and on a class it blocks extending entirely. A lambda can only capture a local variable that's final or effectively final. A private field isn't automatically safe from outside mutation — a getter that hands back the same mutable object leaks it, so return a defensive copy instead. And a record generates an immutable, implicitly final class, fields, accessors, equals, hash code, and to string, from one line. Scope and shadowing were covered back in Lesson 7.2. Next up, Chapter 24: Optional, and avoiding null pointer exceptions.",
    },
]
