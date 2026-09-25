BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 17 &middot; Inheritance &amp; Abstractions</div>
      <h1>Inheritance and Constructors</h1>
      <p class="scr-sub">How a subclass gets its superclass's fields properly set up.</p>
    </div>''',
        "speak": "Last lesson, a subclass inherited fields and methods from its superclass. But constructors work differently, and that raises a real question about how an object's inherited state ever gets set up. That's this lesson.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Constructors Are Never Inherited</h2><ul>
      <li><span class="num">1</span><span>A subclass inherits <strong>public</strong> methods and fields &mdash; but <em>not</em> constructors.</span></li>
      <li><span class="num">2</span><span>It can't directly touch the superclass's <strong>private</strong> fields either.</span></li>
    </ul></div>''',
        "speak": "A subclass inherits its superclass's public methods and fields, but it does not inherit constructors. And it can't directly touch the superclass's private fields, either.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Constructors Are Never Inherited</h2><ul>
      <li><span class="num">1</span><span>A subclass inherits <strong>public</strong> methods and fields &mdash; but <em>not</em> constructors.</span></li>
      <li><span class="num">2</span><span>It can't directly touch the superclass's <strong>private</strong> fields either.</span></li>
      <li><span class="num">3</span><span>Yet every Intake still <em>contains</em> RobotPart's private name &mdash; so how does it get set?</span></li>
    </ul></div>''',
        "speak": "Yet every Intake object still contains Robot Part's private name field, and that field needs to be properly set up before anything uses it. So how does a subclass initialize state that belongs to its superclass?",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">RobotPart</span>
{
    <span class="k">private</span> <span class="t">String</span> name;

    <span class="k">public</span> <span class="t">RobotPart</span>(<span class="t">String</span> name) { <span class="k">this</span>.name = name; }
    <span class="c">// ...getName(), log(), and stop() as in Lesson 17.1</span>
}</code></pre>''',
        "speak": "Here's the part of Robot Part that matters for construction: its private name field, and the one constructor that sets it. The rest of the class is the same as in lesson 17.1.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">RobotPart</span>
{
    <span class="k">private boolean</span> hasGamePiece;

    <span class="k">public</span> <span class="t">Intake</span>(<span class="t">String</span> name)
    {
        <span class="c">// runs RobotPart's constructor, setting the private name field</span>
        <span class="k">super</span>(name);
        hasGamePiece = <span class="k">false</span>;  <span class="c">// Intake's own field</span>
    }
}</code></pre>''',
        "speak": "The answer is the keyword super, used like a method call. Inside Intake's constructor, super, passing name, runs Robot Part's constructor code, in the context of the object already being built. That sets the private name field. Then Intake sets its own field, has game piece, to false.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What super(name) Is, and Isn't</h2><ul>
      <li><span class="num">1</span><span>It does <em>not</em> create a second object.</span></li>
      <li><span class="num">2</span><span>It's the one and only way to run RobotPart's own initialization for the object under construction.</span></li>
    </ul></div>''',
        "speak": "Super, name, isn't creating a second object. It's the one and only way to run Robot Part's own initialization logic for the object currently under construction. Without it, name would never get set, since Intake has no direct access to that private field to assign it itself.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Implicit super() Call</h2><ul>
      <li><span class="num">1</span><span>No explicit <strong>super(...)</strong>? Java inserts a no-argument <strong>super()</strong> at the start for you.</span></li>
      <li><span class="num">2</span><span>That only works if the superclass <em>has</em> a no-argument constructor.</span></li>
      <li><span class="num">3</span><span>RobotPart doesn't &mdash; so every subclass constructor must call <strong>super(...)</strong> itself.</span></li>
    </ul></div>''',
        "speak": "If a constructor doesn't contain an explicit super call, Java automatically inserts a no-argument super call at its start. But that only works if the superclass actually has a no-argument constructor. If it doesn't, every subclass constructor must explicitly call super, with arguments matching a constructor that does exist, or the code won't compile. Robot Part only has a constructor that takes a name, so every subclass has to call super itself.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Where super(...) Goes</div>
    <pre class="code"><code><span class="k">public</span> <span class="t">Intake</span>(<span class="t">String</span> name)
{
    <span class="k">if</span> (name.isBlank()) <span class="k">throw new</span> <span class="t">IllegalArgumentException</span>(<span class="s">"Intake needs a name"</span>);
    <span class="k">super</span>(name.trim());
    hasGamePiece = <span class="k">false</span>;
}</code></pre>''',
        "speak": "Where can super go? On Java 25, a constructor may run a few statements before super, as long as they don't use the object being built. Here, Intake checks that the name isn't blank, and trims it, before handing it up.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Before super(...): Only What Doesn't Use the Object</h2><ul>
      <li><span class="num">1</span><span>Java 25: checking or preparing arguments before <strong>super(...)</strong> is fine.</span></li>
      <li><span class="num">2</span><span>Calling the object's methods (even <strong>getName()</strong>) or reading its fields there: compile error.</span></li>
      <li><span class="num">3</span><span><strong>Java 17: super(...) must be the very first statement.</strong> Putting it first works everywhere.</span></li>
    </ul></div>''',
        "speak": "What those early statements can't do is use the object itself. Calling one of its methods, even an inherited one like get Name, or reading its fields before super, is a compile error, because the Robot Part part of the object doesn't exist yet. And on Java 17, super must be the very first statement of the constructor, with nothing at all before it. Putting super first works on every version.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">Object()</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox">RobotPart(String)</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox active">Intake(String)</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Construction unwinds from the top: Object's constructor runs first, the instantiated class's runs last.</p>''',
        "speak": "Explicit or implicit, every chain of super calls eventually reaches Object's own no-argument constructor, the one class with no superclass of its own. From there, construction unwinds. Object's constructor logic runs first, then each class going back down the hierarchy, ending with whichever class was actually instantiated.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Intake</span> intake = <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front Intake"</span>);
<span class="c">// Order of execution: Object() -&gt; RobotPart(String) -&gt; Intake(String)</span></code></pre>''',
        "speak": "So creating a new Intake called Front Intake runs Object's constructor, then Robot Part's, then Intake's. By the time the rest of your own constructor's body runs, every inherited field further up the chain has already been properly initialized.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">A Middle Ground: protected</h2><ul>
      <li><span class="num">1</span><span><strong>private</strong> hides a field even from subclasses.</span></li>
      <li><span class="num">2</span><span><strong>protected</strong> lets subclasses (and classes in the same package) use it directly.</span></li>
      <li><span class="num">3</span><span>This course keeps fields private &mdash; Lesson 23.1 compares all four access levels.</span></li>
    </ul></div>''',
        "speak": "Private fields are hidden even from subclasses. Java has one access level in between. A field or method marked protected can be used directly by subclasses, and by other classes in the same package. If Robot Part had declared its name protected, Intake could read and assign it itself. This course keeps fields private, and goes through super and getters instead, so the superclass stays in control of its own data. Lesson 23.1 compares all four access levels side by side.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Writing Your Own Exception</div>
    <pre class="code"><code><span class="k">public class</span> <span class="t">ArmLimitException</span> <span class="k">extends</span> <span class="t">RuntimeException</span>
{
    <span class="k">public</span> <span class="t">ArmLimitException</span>(<span class="t">String</span> message)
    {
        <span class="k">super</span>(message);  <span class="c">// RuntimeException stores it for getMessage()</span>
    }
}</code></pre>''',
        "speak": "Now that you can write a subclass, you can create your own exception type. Extend Runtime Exception, and pass the message up with super, so the inherited get Message method returns it. Then throwing a new Arm Limit Exception works like any built-in exception, and a catch block for Arm Limit Exception handles exactly this problem and nothing else. Because it extends Runtime Exception, it's unchecked.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assigning a superclass's private field directly &mdash; this.name = name; won't compile in Intake.</li>
      <li><span class="check">!</span>Using the object before super(...) has run &mdash; and on Java 17, putting anything before super(...).</li>
      <li><span class="check">!</span>Assuming a no-argument super() always works.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Don't try to assign a superclass's private field directly. This dot name equals name, inside Intake's constructor, won't compile if name is private in Robot Part. Only super can reach it. Don't use the object before super has run. On Java 25, statements that don't touch the object may come first, but calling its methods or reading its fields there doesn't compile. On Java 17, super must be the very first statement. And don't assume a no-argument super always works. If the superclass only has constructors that take parameters, Java can't insert an implicit call, so you have to call super yourself, with matching arguments.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Constructors are never inherited &mdash; super(...) runs the superclass's constructor logic.</li>
      <li><span class="check">&#10003;</span>No explicit super(...)? Java inserts super() &mdash; only if a no-argument constructor exists.</li>
      <li><span class="check">&#10003;</span>Java 25: only object-free statements before super(...); Java 17: super(...) first.</li>
      <li><span class="check">&#10003;</span>Every chain reaches Object's constructor, which runs first; your own code runs last.</li>
      <li><span class="check">&#10003;</span>protected lets subclasses use a member directly; a custom exception extends RuntimeException.</li>
    </ul></div>''',
        "speak": "So, to recap. Constructors are never inherited. Only a super call can run the superclass's constructor logic to initialize its own fields, even the private ones. If a subclass constructor doesn't call super explicitly, Java inserts a no-argument super call automatically, which only works if the superclass has one. On Java 25, only statements that don't use the object may come before super. On Java 17, super must come first. Every construction chain eventually reaches Object's constructor, which runs first. And protected lets subclasses use a member directly, while a custom exception is just a subclass of Runtime Exception that calls super with its message. Next up, lesson 17.3: inheritance hierarchies.",
    },
]
