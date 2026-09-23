BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 4 &middot; Using Objects &amp; Calling Methods</div>
      <h1>Objects &mdash; Instances of Classes</h1>
      <p class="scr-sub">A class is a blueprint; an object is one specific thing built from it.</p>
    </div>''',
        "speak": "We've been using objects since Chapter 3 without ever fully unpacking what one actually is. Let's fix that now, it's one of the most important ideas in the rest of this course.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">TalonFX <span style="color:var(--ink-faint)">(class)</span></div>
      <div class="darrow">&rarr;</div>
      <div class="dbox active">leftMotor</div>
      <div class="dbox active">rightMotor</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Like a cookie cutter stamping out cookies &mdash; same shape, each its own cookie.</p>''',
        "speak": "A class is a blueprint, an object is one specific thing built from it. Think of a cookie cutter stamping out cookies, same shape every time, but each one is its own separate cookie. Talon F X is a class, left motor and right motor are two separate objects built from it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span> leftMotor;
<span class="t">TalonFX</span> rightMotor;</code></pre>''',
        "speak": "A class also defines a brand new type, exactly the way int or double do. Talon F X left motor, semicolon, declares a variable exactly like int score would, it just holds a Talon F X instead of a whole number.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Attributes &amp; Behaviors, Revisited</h2><ul>
      <li><span class="num">1</span><span><strong>Attributes</strong> &mdash; the data it holds (its CAN ID, its current speed).</span></li>
    </ul></div>''',
        "speak": "Every object has attributes, the data it holds, its CAN ID, its current speed.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Attributes &amp; Behaviors, Revisited</h2><ul>
      <li><span class="num">1</span><span><strong>Attributes</strong> &mdash; the data it holds (its CAN ID, its current speed).</span></li>
      <li><span class="num">2</span><span><strong>Behaviors</strong> &mdash; what it can do, defined as methods (set, getVelocity).</span></li>
    </ul></div>''',
        "speak": "And behaviors, what it can do, defined as methods, set, get velocity. The class defines what attributes and behaviors exist, but each individual object has its own values for them. left motor and right motor are both Talon F X objects, but each has its own CAN ID and its own current speed, completely independent of the other.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Reference Variables</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">leftMotor holds a reference to the object &mdash; like a tracking number, not the object itself.</p>''',
        "speak": "Here's a subtlety worth catching early. A variable like left motor doesn't hold the motor object directly, it holds a reference to it, like a tracking number pointing at where the real object actually lives in memory. That's genuinely different from a primitive variable, an int or a double holds its value directly, with nothing in between.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">TalonFX</span> leftMotor = <span class="k">new</span> <span class="t">TalonFX</span>(<span class="n">1</span>);
<span class="t">TalonFX</span> rightMotor = <span class="k">new</span> <span class="t">TalonFX</span>(<span class="n">2</span>);
<span class="t">TalonFX</span> intakeMotor = <span class="k">new</span> <span class="t">TalonFX</span>(<span class="n">3</span>);</code></pre>''',
        "speak": "And you can create as many objects from one class as you actually need. Three separate Talon F X objects here, one class, three completely independent motors.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Confusing the class name with an object's name &mdash; TalonFX (Pascal case) is always the class; leftMotor (camelCase) is a specific object.</li>
      <li><span class="check">!</span>Assuming two objects of the same class share state &mdash; changing one's speed has zero effect on the other.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Confusing the class name with an object's name, Talon F X, written in Pascal case, capitalized, is always the class, left motor, in camelCase, is a specific object, mixing those two up is a genuinely common early error. And assuming two objects of the same class share state, left motor and right motor are both Talon F X objects, but changing one's speed has exactly zero effect on the other, each object's attributes are entirely its own.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A class is a blueprint; an object is one specific instance built from it.</li>
      <li><span class="check">&#10003;</span>A class defines a new type, just like int or double.</li>
      <li><span class="check">&#10003;</span>Attributes are an object's data; behaviors are what it can do.</li>
      <li><span class="check">&#10003;</span>A reference variable holds a pointer to an object, not the data directly.</li>
    </ul></div>''',
        "speak": "So: a class is a blueprint, an object is one specific instance built from it. A class defines a new type, just like int or double do. Attributes are an object's data, behaviors are what it can do. And a reference variable holds a pointer to an object, not the object's data directly. Next up, lesson 4.5, actually building objects with constructors, and what it means for a reference to point at nothing at all.",
    },
]
