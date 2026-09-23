BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 3 &middot; APIs, Libraries &amp; Documentation</div>
      <h1>APIs and Libraries</h1>
      <p class="scr-sub">Why you'll never have to write your own motor controller code from scratch.</p>
    </div>''',
        "speak": "Starting today, we stop writing every single line ourselves. Real FRC code leans constantly on code other people already wrote, and this lesson is about exactly how that works.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Library vs. API</h2><ul>
      <li><span class="num">1</span><span><strong>Library</strong> &mdash; a collection of code someone else already wrote, that you reuse instead of writing it yourself.</span></li>
    </ul></div>''',
        "speak": "A library is a collection of code someone else already wrote, that you get to reuse instead of writing it yourself. WPILib, the library every FRC robot depends on, is exactly this, motor control, sensors, the whole command-based framework, written once and reused by thousands of teams.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Library vs. API</h2><ul>
      <li><span class="num">1</span><span><strong>Library</strong> &mdash; a collection of code someone else already wrote, that you reuse instead of writing it yourself.</span></li>
      <li><span class="num">2</span><span><strong>API</strong> &mdash; the instructions for how to actually use it: what classes it gives you, and what to pass in.</span></li>
    </ul></div>''',
        "speak": "The API, short for Application Programming Interface, is the instructions for how to actually use a library, what classes it gives you, what each one can do, what you need to pass in. You don't need to know how a library works internally, you just need its API.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">TalonFX <span style="color:var(--ink-faint)">(class)</span></div>
      <div class="darrow">&rarr;</div>
      <div class="dbox active">shooterMotor <span style="color:var(--accent)">(object)</span></div>
    </div>''',
        "speak": "A class is the building block a library hands you, it defines a brand new kind of value, the same way int or double do, except this time you, or a library author, decide what it means. An object is one specific thing built from a class.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Every Class Bundles Two Things</h2><ul>
      <li><span class="num">1</span><span><strong>Attributes</strong> &mdash; the data it holds. Stored in variables.</span></li>
    </ul></div>''',
        "speak": "Every class bundles two things together. Attributes, the data it holds, stored in variables.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Every Class Bundles Two Things</h2><ul>
      <li><span class="num">1</span><span><strong>Attributes</strong> &mdash; the data it holds. Stored in variables.</span></li>
      <li><span class="num">2</span><span><strong>Behaviors</strong> &mdash; what it can do. Defined as methods.</span></li>
    </ul></div>''',
        "speak": "And behaviors, what it can actually do, defined as methods.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span> shooterMotor = <span class="k">new</span> <span class="t">TalonFX</span>(<span class="n">5</span>); <span class="c">// shooterMotor is an object, built from the TalonFX class</span></code></pre>''',
        "speak": "Here's the object side of it. A new Talon F X, built for CAN ID 5, gets stored in shooterMotor. Talon F X is the class, the blueprint, shooterMotor is one specific object built from it, and a real robot might have several of these, one per motor.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span> shooterMotor = <span class="k">new</span> <span class="t">TalonFX</span>(<span class="n">5</span>); <span class="c">// shooterMotor is an object, built from the TalonFX class</span>

shooterMotor.<span class="me">set</span>(<span class="n">0.8</span>); <span class="c">// a behavior &mdash; call a method with the dot operator</span></code></pre>''',
        "speak": "And here's a behavior. shooterMotor dot set, 0 point 8. That dot is the dot operator, it's how you reach into an object and trigger one of its behaviors. This line means: find the set method defined on the Talon F X class, and run it on this specific motor object.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Why This Matters</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">You don't need to know CAN bus protocol or motor controller firmware to call shooterMotor dot set correctly.</p>''',
        "speak": "You don't need to know how Talon F X is implemented internally, the motor controller firmware, the CAN bus protocol, none of it, to use shooterMotor dot set correctly. That's the entire point of a library, someone else solved the hard problem once, documented how to use their solution, and you build on top of it instead of starting from zero.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Confusing a class with an object &mdash; TalonFX is the blueprint; shooterMotor is one specific object built from it.</li>
      <li><span class="check">!</span>Forgetting the dot operator &mdash; the dot is what connects an object to its behavior.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Confusing a class with an object, Talon F X is the blueprint, shooterMotor is one specific object built from it, and a robot can have several such objects, one per motor. And forgetting the dot operator, shooterMotor set 0 point 8 with no dot in between just isn't valid Java, the dot is what connects an object to its behavior.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A library is reusable code someone else wrote; its API documents how to use it.</li>
      <li><span class="check">&#10003;</span>A class bundles attributes (data) and behaviors (methods) together.</li>
      <li><span class="check">&#10003;</span>An object is one specific instance built from a class.</li>
      <li><span class="check">&#10003;</span>The dot operator accesses an object's attributes and behaviors.</li>
    </ul></div>''',
        "speak": "So: a library is reusable code someone else already wrote, and its API documents how to actually use it. A class bundles attributes and behaviors together. An object is one specific instance built from a class. And the dot operator is how you reach an object's attributes and behaviors. Next up, lesson 3.2, how to document the methods you write, so the next person calling them, quite possibly future you, knows exactly what's safe to pass in.",
    },
]
