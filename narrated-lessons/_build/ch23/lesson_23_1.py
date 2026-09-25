BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 23 &middot; Encapsulation &amp; final</div>
      <h1>Scope and Access</h1>
      <p class="scr-sub">Where a variable exists at all, who's allowed to touch it, and what <code>final</code> locks down.</p>
    </div>''',
        "speak": "Welcome to Chapter 23. Today is about scope, where a variable actually exists, how that connects to encapsulation, and what the final keyword does, and doesn't, lock down.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Scope Means</h2><ul>
      <li><span class="num">1</span><span>A variable's <strong>scope</strong> is where it's accessible &mdash; where it lives and exists</span></li>
      <li><span class="num">2</span><span>Set by the nearest enclosing pair of curly braces around its declaration</span></li>
    </ul></div>''',
        "speak": "A variable's scope is where it's accessible, where it lives and exists. It's determined by the nearest enclosing pair of curly braces around wherever the variable was declared. And using a variable outside its scope isn't just bad practice. The variable genuinely doesn't exist there, and the code won't compile.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span>
{
    <span class="k">private boolean</span> hasGamePiece;             <span class="c">// CLASS scope — visible to every method in Intake</span>

    <span class="k">public void</span> <span class="me">setState</span>(<span class="k">boolean</span> detected)    <span class="c">// detected is a parameter — METHOD scope</span>
    {
        <span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; <span class="n">3</span>; i++)           <span class="c">// i is a loop variable — BLOCK scope</span>
        {
            <span class="k">boolean</span> sample = detected;        <span class="c">// BLOCK scope — only exists inside this loop's braces</span>
        }
        hasGamePiece = detected;              <span class="c">// fine: class-scope field, reachable anywhere in the class</span>
    }
}</code></pre>''',
        "speak": "This one small class shows all three levels of scope at once. The field, has game piece. The parameter, detected. And inside the loop, the loop variable i, and a local variable called sample. Let's take each level in turn.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Levels of Scope</h2><ul>
      <li><span class="num">1</span><span><strong>Class scope</strong> &mdash; fields, visible to every method in the class, public or private</span></li>
    </ul></div>''',
        "speak": "Class scope is for instance variables, fields, like has game piece. They're visible to every method in the class, regardless of whether they're public or private.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Levels of Scope</h2><ul>
      <li><span class="num">1</span><span><strong>Class scope</strong> &mdash; fields, visible to every method in the class, public or private</span></li>
      <li><span class="num">2</span><span><strong>Method scope</strong> &mdash; local variables and parameters, alive only for that one call</span></li>
    </ul></div>''',
        "speak": "Method scope is for local variables and parameters, like detected, declared inside a method or constructor. They exist only for that one method call, and they can never be declared public or private themselves.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Levels of Scope</h2><ul>
      <li><span class="num">1</span><span><strong>Class scope</strong> &mdash; fields, visible to every method in the class, public or private</span></li>
      <li><span class="num">2</span><span><strong>Method scope</strong> &mdash; local variables and parameters, alive only for that one call</span></li>
      <li><span class="num">3</span><span><strong>Block scope</strong> &mdash; declared inside a narrower block, gone the instant it ends</span></li>
    </ul></div>''',
        "speak": "And block scope is for variables declared inside any block narrower than a whole method, a loop, an if, and so on, like i and sample. They stop existing the instant that block ends.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="t">String</span> <span class="me">getStatus</span>()
{
    <span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; <span class="n">3</span>; i++)
    {
        <span class="k">int</span> sample = i;
    }
    System.out.println(sample); <span class="c">// COMPILE ERROR — sample only existed inside the loop's braces</span>
    <span class="k">return</span> <span class="s">"done"</span>;
}</code></pre>''',
        "speak": "Here's what happens when you forget that. Sample is declared inside the loop's braces, so the moment the loop ends, it's gone. Trying to print it afterward is a compile error, sample simply doesn't exist on that line.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Parameters Follow the Same Rule</h2><ul>
      <li><span class="num">1</span><span>A constructor's parameter only exists for that constructor call</span></li>
      <li><span class="num">2</span><span>It isn't reachable from any other method &mdash; not even <code>toString()</code></span></li>
    </ul></div>''',
        "speak": "Parameters follow the same rule. A constructor's parameter only exists for that one constructor call, and it isn't reachable from any other method in the class, including to string, or any other method that seems related.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span>
{
    <span class="k">private</span> <span class="t">String</span> name;

    @Override
    <span class="k">public</span> <span class="t">String</span> <span class="me">toString</span>()
    {
        <span class="t">String</span> name = <span class="s">"unknown"</span>;  <span class="c">// this local variable shadows the instance variable name</span>
        <span class="k">return</span> name;              <span class="c">// returns "unknown", NOT the instance variable's real value</span>
    }
}</code></pre>''',
        "speak": "What if a local variable, or a parameter, shares a name with an instance variable? Then the local one wins, inside that method. That's called shadowing. Here, to string declares its own local name, set to unknown, so it returns unknown, not the instance variable's real value.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Fix, From Ch.8</h2><ul>
      <li><span class="num">1</span><span><code>this.name</code> explicitly reaches the instance variable, even while it's shadowed</span></li>
    </ul></div>''',
        "speak": "Chapter 8 already introduced the fix for this exact situation inside constructors. This dot name explicitly reaches the instance variable, even when a same-named local variable or parameter is shadowing it.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Scope vs. Access Modifiers</h2><ul>
      <li><span class="num">1</span><span><strong>Scope</strong>: where a variable exists at all</span></li>
      <li><span class="num">2</span><span><strong>Access modifiers</strong>: who outside the class is allowed to touch it</span></li>
      <li><span class="num">3</span><span>A <code>private</code> field keeps its class scope &mdash; it just blocks outside code</span></li>
    </ul></div>''',
        "speak": "Encapsulation, back from Chapter 7, is really scope applied deliberately. Marking a field private doesn't change its class scope, every method in the class can still see it. What it does is restrict outside code from reaching it directly, forcing access through public getters and setters instead. So scope and access modifiers are two separate, but related, ideas. Scope is about where a variable exists at all. Access modifiers are about who outside the class is allowed to touch it.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 23 &middot; Encapsulation &amp; final</div>
      <h1>The <code>final</code> Keyword</h1>
      <p class="scr-sub">Assigned exactly once, never reassigned.</p>
    </div>''',
        "speak": "Now, final. A field, parameter, or local variable marked final can be assigned exactly once. Any attempt to reassign it afterward is a compile error. That matters for anything that genuinely should never change after it's set.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">private final</span> <span class="t">TalonFX</span> motor = <span class="k">new</span> TalonFX(<span class="n">1</span>); <span class="c">// this reference can never be reassigned to a different motor</span>

<span class="k">public double</span> <span class="me">getVelocity</span>()
{
    <span class="k">return</span> motor.getVelocity().getValue();
}</code></pre>''',
        "speak": "Here, motor is a final Talon FX. That reference can never be reassigned to point at a different motor. But get velocity can still read from it, and use it, as much as it likes.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2"><code>final</code> Locks the Reference</h2><ul>
      <li><span class="num">1</span><span><code>motor</code> can't be pointed at a different <code>TalonFX</code></span></li>
      <li><span class="num">2</span><span>But the <code>TalonFX</code> object itself can still change its own state</span></li>
    </ul></div>''',
        "speak": "That's the key detail. Final on an object reference only locks the reference itself. It doesn't make the object's own internal state unchangeable. Motor can't be pointed at a different Talon FX, but the real Talon FX object it points to can still have its own state change, through its own methods.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">True Immutability Is Stronger</h2><ul>
      <li><span class="num">1</span><span>An <strong>immutable</strong> object's internal state can never change once constructed</span></li>
      <li><span class="num">2</span><span>That's why WPILib's <code>Pose2d</code> is thread-safe and predictable</span></li>
    </ul></div>''',
        "speak": "True immutability, an object whose internal state can never change at all once it's constructed, is a stronger guarantee. And it's exactly why immutable classes, like WPILib's Pose2d, are thread-safe and predictable. Nothing can ever be halfway through changing one, because nothing can change it at all.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Using a loop or block-scoped variable after its block ends &mdash; declare it at method scope instead.</li>
      <li><span class="check">!</span>Assuming a shadowed local variable is the instance variable &mdash; use <code>this.fieldName</code>.</li>
      <li><span class="check">!</span>Confusing <code>final</code> with true immutability.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Trying to use a loop or block-scoped variable after its block ends, it stops existing the instant the enclosing braces close, so declare it at method scope instead if it needs to survive past the block. Assuming a shadowed local variable is the instance variable, inside a method with a same-named local variable or parameter, the local one always wins, so use this dot field name to reach the instance variable explicitly. And confusing final with true immutability. Final only prevents reassigning a reference, the object it refers to can still have its own internal state changed, unless that object's class was specifically designed to be immutable.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Scope &mdash; class, method, or block &mdash; is set by the nearest enclosing braces.</li>
      <li><span class="check">&#10003;</span>Locals and parameters live for one call; fields live for the whole object.</li>
      <li><span class="check">&#10003;</span>A same-named local shadows a field &mdash; this.fieldName reaches the real one.</li>
      <li><span class="check">&#10003;</span>final allows exactly one assignment &mdash; for references, it locks the reference.</li>
      <li><span class="check">&#10003;</span>True immutability is a stronger, separate guarantee &mdash; like Pose2d.</li>
    </ul></div>''',
        "speak": "So, to recap. A variable's scope, class, method, or block, is set by the nearest enclosing curly braces around its declaration, and using it outside that scope doesn't compile. Local variables and parameters exist only for their method or constructor call, while instance variables exist for the whole object, reachable from every method regardless of access modifier. A local variable or parameter sharing a name with an instance variable shadows it inside that method, and this dot field name is how to reach the real instance variable. Final allows exactly one assignment, and for object references, it locks the reference, not necessarily the object's internal state. And true immutability is a stronger, separate guarantee, it's what makes classes like Pose2d safe to share and reason about. Next up, Chapter 24: Optional, and avoiding null pointer exceptions.",
    },
]
