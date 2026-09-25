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
      <li><span class="num">3</span><span>So how do those inherited private fields get initialized?</span></li>
    </ul></div>''',
        "speak": "Yet those inherited private fields still need to be properly set up before anything uses them. So how does a subclass initialize state that belongs to its superclass?",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">private</span> <span class="t">String</span> name;

    <span class="k">public</span> Subsystem(<span class="t">String</span> name) { this.name = name; }
    <span class="k">public</span> <span class="t">String</span> getName() { <span class="k">return</span> name; }
}</code></pre>''',
        "speak": "Here's our Subsystem superclass again, with its private name field, set by its own constructor.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">Subsystem</span>
{
    <span class="k">private boolean</span> hasGamePiece;

    <span class="k">public</span> Intake(<span class="t">String</span> name)
    {
        super(name);          <span class="c">// runs Subsystem's constructor, setting the private name field</span>
        hasGamePiece = <span class="k">false</span>;  <span class="c">// Intake's own field</span>
    }
}</code></pre>''',
        "speak": "The answer is the keyword super, used like a method call. Inside Intake's constructor, super, passing name, runs Subsystem's constructor code, in the context of the object already being built. That sets the private name field. Then Intake sets its own field, has game piece, to false.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What super(name) Is, and Isn't</h2><ul>
      <li><span class="num">1</span><span>It does <em>not</em> create a second object.</span></li>
      <li><span class="num">2</span><span>It's the one and only way to run Subsystem's own initialization for the object under construction.</span></li>
    </ul></div>''',
        "speak": "Super, name, isn't creating a second object. It's the one and only way to run Subsystem's own initialization logic for the object currently under construction. Without it, name would never get set, since Intake has no direct access to that private field to assign it itself.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Implicit super() Call</h2><ul>
      <li><span class="num">1</span><span>No explicit <strong>super(...)</strong> first? Java inserts a no-argument <strong>super()</strong> for you.</span></li>
      <li><span class="num">2</span><span>That only works if the superclass <em>has</em> a no-argument constructor.</span></li>
    </ul></div>''',
        "speak": "If a constructor doesn't start with an explicit super call, Java automatically inserts a no-argument super call for you. But that only works if the superclass actually has a no-argument constructor. If it doesn't, every subclass constructor must explicitly call super, with arguments matching a constructor that does exist, or the code won't compile.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">Object()</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox">Subsystem(String)</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox active">Intake(String)</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Construction unwinds from the top: Object's constructor runs first, the instantiated class's runs last.</p>''',
        "speak": "Explicit or implicit, every chain of super calls eventually reaches Object's own no-argument constructor, the one class with no superclass of its own. From there, construction unwinds. Object's constructor logic runs first, then each class going back down the hierarchy, ending with whichever class was actually instantiated.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Intake</span> intake = <span class="k">new</span> <span class="t">Intake</span>(<span class="s">"Front Intake"</span>);
<span class="c">// Order of execution: Object() -&gt; Subsystem(String) -&gt; Intake(String)</span></code></pre>''',
        "speak": "So creating a new Intake called Front Intake runs Object's constructor, then Subsystem's, then Intake's. By the time your own constructor's body runs, every inherited field further up the chain has already been properly initialized.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assigning a superclass's private field directly &mdash; this.name = name; won't compile in Intake.</li>
      <li><span class="check">!</span>Putting super(...) anywhere but the very first statement.</li>
      <li><span class="check">!</span>Assuming a no-argument super() always works.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Don't try to assign a superclass's private field directly. This dot name equals name, inside Intake's constructor, won't compile if name is private in Subsystem. Only super can reach it. Super must be the very first statement, since the superclass has to finish initializing before the subclass's own code can safely run. And don't assume a no-argument super always works. If the superclass only has constructors that take parameters, Java can't insert an implicit call, so you have to call super yourself, with matching arguments.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Constructors are never inherited &mdash; super(...) runs the superclass's constructor logic.</li>
      <li><span class="check">&#10003;</span>No explicit super(...)? Java inserts super() &mdash; only if a no-argument constructor exists.</li>
      <li><span class="check">&#10003;</span>Every chain reaches Object's constructor, which runs first; your own code runs last.</li>
    </ul></div>''',
        "speak": "So, to recap. Constructors are never inherited. Only a super call can run the superclass's constructor logic to initialize its own fields, even the private ones. If a subclass constructor doesn't call super explicitly, Java inserts a no-argument super call automatically, which only works if the superclass has one. And every construction chain eventually reaches Object's constructor, which runs first. Your subclass's own code only runs after every class above it has finished. Next up, lesson 17.3: inheritance hierarchies.",
    },
]
