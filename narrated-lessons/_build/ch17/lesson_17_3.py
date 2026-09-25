BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 17 &middot; Inheritance &amp; Abstractions</div>
      <h1>Inheritance Hierarchies</h1>
      <p class="scr-sub">Many subclasses, one superclass &mdash; and one variable type that holds them all.</p>
    </div>''',
        "speak": "So far we've looked at one subclass at a time. Real robots have lots of subsystems, all sharing one parent. That family tree is called an inheritance hierarchy, and it's where inheritance really starts paying off.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Multiple Subclasses, One Superclass</h2><ul>
      <li><span class="num">1</span><span><strong>Intake</strong>, <strong>Shooter</strong>, and <strong>Climber</strong> all extending <strong>Subsystem</strong> is a small hierarchy.</span></li>
      <li><span class="num">2</span><span><strong>Object</strong> sits at the very top of <em>every</em> hierarchy in Java.</span></li>
    </ul></div>''',
        "speak": "An inheritance hierarchy forms when several subclasses inherit, directly, or through another subclass, from a common superclass. Intake, Shooter, and Climber all extending Subsystem is a small hierarchy. And Object sits at the very top of every hierarchy in Java, since every class ultimately inherits from it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Subsystem</span> s1 = <span class="k">new</span> <span class="t">Subsystem</span>(<span class="s">"Generic"</span>);
<span class="t">Subsystem</span> s2 = <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front Intake"</span>);   <span class="c">// legal — an Intake IS-A Subsystem</span>
<span class="t">Subsystem</span> s3 = <span class="k">new</span> <span class="t">Climber</span>(<span class="s">"Left Climber"</span>);  <span class="c">// legal — a Climber IS-A Subsystem</span></code></pre>''',
        "speak": "A variable typed as the superclass can refer to an object of that class, or any of its subclasses. A Subsystem variable can hold a plain Subsystem, an Intake, or a Climber. Both of those are legal, because an Intake is a Subsystem, and so is a Climber.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Intake</span> i = <span class="k">new</span> <span class="t">Subsystem</span>(<span class="s">"Generic"</span>); <span class="c">// ERROR — a Subsystem isn't necessarily an Intake</span></code></pre>''',
        "speak": "The reverse doesn't work. A subclass-typed variable can't hold a plain superclass object, since not every Subsystem is specifically an Intake. This line is a compile error.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public void</span> stopAll(<span class="t">Subsystem</span>[] subsystems)
{
    <span class="k">for</span> (<span class="t">Subsystem</span> s : subsystems)
    {
        s.stop(); <span class="c">// works for an Intake, a Climber, a Shooter — anything extending Subsystem</span>
    }
}</code></pre>''',
        "speak": "Here's why this matters. A method, array, or collection typed against the superclass automatically accepts every subclass too. This stop all method takes an array of Subsystem, loops over it, and calls stop on each one. That works for an Intake, a Climber, a Shooter, anything extending Subsystem.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Subsystem</span>[] robotSubsystems = { <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front"</span>), <span class="k">new</span> <span class="t">Climber</span>(<span class="s">"Left"</span>), <span class="k">new</span> <span class="t">Shooter</span>(<span class="s">"Main"</span>) };
stopAll(robotSubsystems);</code></pre>''',
        "speak": "So one array can hold an Intake, a Climber, and a Shooter side by side, and a single call to stop all stops every one of them. That's what makes managing a whole robot's subsystems from one place possible.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">Subsystem</span>&gt; allSubsystems = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">Subsystem</span>&gt;();
allSubsystems.add(<span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front"</span>));
allSubsystems.add(<span class="k">new</span> <span class="t">Climber</span>(<span class="s">"Left"</span>));</code></pre>''',
        "speak": "The same holds for collections. An Array List of Subsystem happily holds Intake and Climber objects side by side.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Which Method Actually Runs?</h2><ul>
      <li><span class="num">1</span><span>Java runs the object's <em>own</em> version of the method.</span></li>
      <li><span class="num">2</span><span>Decided by its real <strong>runtime type</strong>, not the variable's declared type.</span></li>
      <li><span class="num">3</span><span>The foundation of <strong>polymorphism</strong> &mdash; full story in Lesson 18.3.</span></li>
    </ul></div>''',
        "speak": "One more question. When you call a method through a superclass-typed variable, and the object is really a subclass instance, which version runs? Java runs that object's actual version, decided by its real runtime type, not the variable's declared type. That's the foundation of polymorphism, covered in full in lesson 18.3. For now, the key idea is that a Subsystem variable holding an Intake still calls Intake's own overridden methods, if it has any.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assigning a superclass object to a subclass-typed variable &mdash; compile error.</li>
      <li><span class="check">!</span>Thinking a Subsystem[] array can only hold plain Subsystem objects.</li>
      <li><span class="check">!</span>Forgetting the object's real class decides which method version runs.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Intake i equals new Subsystem is a compile error, not every Subsystem is an Intake, it only works the other direction. A Subsystem array isn't limited to plain Subsystem objects, it can hold any mix of Subsystem and its subclasses, and that flexibility is the entire point. And even when a variable is declared Subsystem, calling a method on it runs the object's real class's version, not necessarily Subsystem's own.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Subclasses sharing one superclass form a hierarchy, with Object at the top of every one.</li>
      <li><span class="check">&#10003;</span>A superclass-typed variable, array, or collection holds any subclass object &mdash; never the reverse.</li>
      <li><span class="check">&#10003;</span>One method signature or collection type can work across a whole family of subsystems.</li>
      <li><span class="check">&#10003;</span>The object's runtime type decides which method runs &mdash; the basis of polymorphism.</li>
    </ul></div>''',
        "speak": "So, to recap. Several subclasses inheriting from one common superclass form an inheritance hierarchy, with Object at the top of every hierarchy in Java. A superclass-typed variable, array, or collection can hold objects of that class or any of its subclasses, never the reverse. That lets one method signature, one array type, or one collection type work across a whole family of subsystem classes. And which method actually runs depends on the object's real runtime type, the basis of polymorphism. Next up, lesson 17.4: the Object superclass itself.",
    },
]
