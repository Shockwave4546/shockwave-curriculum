BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 18 &middot; Polymorphism: Many Forms</div>
      <h1>super Keyword</h1>
      <p class="scr-sub">Extending inherited behavior, not just replacing it.</p>
    </div>''',
        "speak": "Last lesson, overriding a method completely replaced the superclass's version. But often a subclass wants to keep the original logic, and add something on top, rather than throwing it away. That's what the super keyword is for, and that's lesson 18.2.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Extending, Not Just Replacing</h2><ul>
      <li><span class="num">1</span><span>An override normally <em>replaces</em> the superclass&rsquo;s version entirely.</span></li>
      <li><span class="num">2</span><span><strong>super.method()</strong> explicitly calls the superclass&rsquo;s version, from inside the override.</span></li>
    </ul></div>''',
        "speak": "An override normally replaces the superclass's version entirely. Writing super dot, then the method name, explicitly calls the superclass's version of that method, from right inside your override. So you get the original behavior, plus whatever you add.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">@Override</span>
    <span class="k">public</span> <span class="t">String</span> toString() { <span class="k">return</span> <span class="s">"Subsystem"</span>; }
}</code></pre>''',
        "speak": "Here, Subsystem's to string method returns just the word Subsystem.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">Subsystem</span>
{
    <span class="k">@Override</span>
    <span class="k">public</span> <span class="t">String</span> toString()
    {
        <span class="k">return super</span>.toString() + <span class="s">" (Intake)"</span>; <span class="c">// runs Subsystem's version first, then extends it</span>
    }
}</code></pre>''',
        "speak": "Intake overrides to string, but instead of starting from scratch, it calls super dot to string first, which runs Subsystem's version, and then tacks Intake in parentheses onto the end. The result is Subsystem, followed by Intake in parentheses. Extended, not replaced.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Uses of super</h2><ul>
      <li><span class="num">1</span><span><strong>super(...)</strong> &mdash; calls a superclass <em>constructor</em>; must be a constructor&rsquo;s first line (Lesson 17.2).</span></li>
    </ul></div>''',
        "speak": "The super keyword actually has two distinct uses, and you've now seen both. First, super followed directly by parentheses. That calls a superclass constructor, and it must be the very first line of a constructor. You met that one back in lesson 17.2.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Uses of super</h2><ul>
      <li><span class="num">1</span><span><strong>super(...)</strong> &mdash; calls a superclass <em>constructor</em>; must be a constructor&rsquo;s first line (Lesson 17.2).</span></li>
      <li><span class="num">2</span><span><strong>super.method()</strong> &mdash; calls a superclass <em>method</em>, from anywhere inside a subclass method body.</span></li>
    </ul></div>''',
        "speak": "Second, super dot a method name. That calls a superclass method, and it can appear anywhere inside a subclass method body, not just on the first line.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">How Method Lookup Works</h2><ul>
      <li><span class="num">1</span><span>Every object remembers the <strong>actual class</strong> it was created with.</span></li>
      <li><span class="num">2</span><span>A method call starts looking <em>there</em> first.</span></li>
      <li><span class="num">3</span><span>Not found? Java searches up the chain &mdash; parent, grandparent, and so on.</span></li>
    </ul></div>''',
        "speak": "To see exactly what super is doing, it helps to know how Java finds a method in the first place. Every object remembers the actual class it was created with. A method call on that object starts looking in that exact class first. If the method isn't there, Java searches up the chain, parent, grandparent, and so on, until it finds a match. And it always will, or the code wouldn't have compiled in the first place.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">public void</span> periodic() { System.out.println(<span class="s">"Subsystem periodic"</span>); }
}</code></pre>''',
        "speak": "Here's a Subsystem with a periodic method that prints Subsystem periodic.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Climber</span> <span class="k">extends</span> <span class="t">Subsystem</span>
{
    <span class="k">@Override</span>
    <span class="k">public void</span> periodic()
    {
        <span class="k">super</span>.periodic();                    <span class="c">// explicitly runs Subsystem's version first</span>
        System.out.println(<span class="s">"Climber periodic"</span>); <span class="c">// then adds Climber's own behavior</span>
    }
}</code></pre>''',
        "speak": "And here's Climber, which overrides periodic. Its first line calls super dot periodic, explicitly running Subsystem's version, and then it prints Climber periodic, adding its own behavior on top.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Tracing climberInstance.periodic()</h2><ul>
      <li><span class="num">1</span><span>Starts in <strong>Climber.periodic()</strong> &mdash; the object&rsquo;s actual class.</span></li>
      <li><span class="num">2</span><span>Reaches <strong>super.periodic()</strong> &mdash; runs <strong>Subsystem.periodic()</strong>.</span></li>
      <li><span class="num">3</span><span>Returns to finish the rest of <strong>Climber.periodic()</strong>&rsquo;s body.</span></li>
    </ul></div>''',
        "speak": "Let's trace it. Calling periodic on a Climber object starts in Climber's own periodic, since that's the object's actual class. When execution reaches super dot periodic, it runs Subsystem's periodic, which prints Subsystem periodic. Then it returns, and finishes the rest of Climber's body, printing Climber periodic.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">super Only Affects One Call</h2><ul>
      <li><span class="num">1</span><span><strong>super.someMethod()</strong> only changes which version of <em>that one call</em> runs.</span></li>
      <li><span class="num">2</span><span>Every other call (unqualified, or through <strong>this</strong>) still dispatches on the object&rsquo;s actual runtime type.</span></li>
      <li><span class="num">3</span><span>So the subclass&rsquo;s override &ldquo;wins&rdquo; everywhere except the one spot marked <strong>super</strong>.</span></li>
    </ul></div>''',
        "speak": "One subtlety. Calling super dot some method only changes which version of that one specific call runs. It doesn't change how any other call inside the same method resolves. Any call made without super, a plain unqualified call, or one through this, still dispatches based on the object's actual runtime type, even from inside inherited code. So if a super dot method one call internally calls some other method, it still ends up running the subclass's override of that other method. The override wins everywhere, except the one spot super explicitly marks.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Expecting <strong>super.method()</strong> to run automatically &mdash; it never does; you must call it yourself.</li>
      <li><span class="check">!</span>Confusing the two forms &mdash; <strong>super(...)</strong> is constructors only, first line only.</li>
      <li><span class="check">!</span>Assuming <strong>super</strong> switches <em>every</em> call in that method to the superclass&rsquo;s versions.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Unlike super for constructors, super dot method never happens automatically. Overriding a method completely discards the superclass's version, unless your override calls super dot method itself. Don't confuse the two forms, either. Super with just parentheses only ever calls a constructor, and only as a constructor's first line, while super dot method calls a named method, anywhere in a method body. And don't assume super switches every call inside that method over to the superclass's versions. It only affects the one call it's written on.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span><strong>super.method()</strong> lets a subclass extend, not fully replace, inherited behavior.</li>
      <li><span class="check">&#10003;</span>Method lookup starts at the object&rsquo;s actual class and searches upward.</li>
      <li><span class="check">&#10003;</span><strong>super(...)</strong> and <strong>super.method()</strong> are two distinct uses of one keyword.</li>
      <li><span class="check">&#10003;</span><strong>super</strong> affects only its one call &mdash; everything else uses the real runtime type.</li>
    </ul></div>''',
        "speak": "So, to recap. Super dot method explicitly calls the superclass's version, letting a subclass extend inherited behavior rather than fully replace it. Method lookup starts at the object's actual class, and searches upward through its ancestors until it finds a match. Super with parentheses, for constructors, and super dot method, for methods, are two distinct uses of the same keyword. And a super dot method call only affects that one call, every other call inside still dispatches to the object's real runtime type. Next up, lesson 18.3, polymorphism itself.",
    },
]
