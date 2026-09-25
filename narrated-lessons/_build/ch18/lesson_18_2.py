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
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Climber</span> <span class="k">extends</span> <span class="t">RobotPart</span>
{
    <span class="k">public</span> <span class="t">Climber</span>(<span class="t">String</span> name) { <span class="k">super</span>(name); }

    <span class="k">@Override</span>
    <span class="k">public void</span> stop()
    {
        <span class="k">super</span>.stop();            <span class="c">// runs RobotPart's stop() first</span>
        log(<span class="s">"brake engaged"</span>);    <span class="c">// then adds Climber's own step</span>
    }
}</code></pre>''',
        "speak": "Here's Climber. It should still do everything Robot Part's stop does, and then engage its brake. So its stop override calls super dot stop first, which runs Robot Part's version and logs stopped. Then it logs brake engaged, its own extra step. Extended, not replaced. You've actually seen this once already: in lesson 17.4, Intake's to string called super dot to string, and added to its result.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Uses of super</h2><ul>
      <li><span class="num">1</span><span><strong>super(...)</strong> &mdash; calls a superclass <em>constructor</em>, from inside a constructor (Lesson 17.2).</span></li>
      <li><span class="num">2</span><span>Java 25: only statements that don&rsquo;t use the object may come before it. Java 17: it must be first.</span></li>
    </ul></div>''',
        "speak": "The super keyword actually has two distinct uses, and you've now seen both. First, super followed directly by parentheses. That calls a superclass constructor, from inside a constructor. You met that one back in lesson 17.2. On Java 25, only statements that don't use the object being built may come before it. On Java 17, it must be the constructor's very first statement.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Uses of super</h2><ul>
      <li><span class="num">1</span><span><strong>super(...)</strong> &mdash; calls a superclass <em>constructor</em>, from inside a constructor (Lesson 17.2).</span></li>
      <li><span class="num">2</span><span>Java 25: only statements that don&rsquo;t use the object may come before it. Java 17: it must be first.</span></li>
      <li><span class="num">3</span><span><strong>super.method()</strong> &mdash; calls a superclass <em>method</em>, from anywhere inside a subclass method body.</span></li>
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
        "screen": '''<pre class="code"><code><span class="t">RobotPart</span> part = <span class="k">new</span> <span class="t">Climber</span>(<span class="s">"Left Climber"</span>);
part.stop();
<span class="c">// prints:</span>
<span class="c">// [Left Climber] stopped</span>
<span class="c">// [Left Climber] brake engaged</span></code></pre>''',
        "speak": "Here, a Robot Part variable holds a Climber named Left Climber, and we call stop on it. It prints two lines: Left Climber stopped, then Left Climber brake engaged.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Tracing part.stop()</h2><ul>
      <li><span class="num">1</span><span>Starts in <strong>Climber.stop()</strong> &mdash; the object&rsquo;s actual class.</span></li>
      <li><span class="num">2</span><span>Reaches <strong>super.stop()</strong> &mdash; runs <strong>RobotPart.stop()</strong>, which logs <em>stopped</em>.</span></li>
      <li><span class="num">3</span><span>Returns to finish <strong>Climber.stop()</strong>, which logs <em>brake engaged</em>.</span></li>
    </ul></div>''',
        "speak": "Let's trace it. Calling stop starts in Climber's own stop, since the object is a Climber. When execution reaches super dot stop, it runs Robot Part's stop, which logs stopped. Then it returns, and finishes the rest of Climber's body, which logs brake engaged.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">super Only Affects One Call</h2><ul>
      <li><span class="num">1</span><span><strong>super.someMethod()</strong> only changes which version of <em>that one call</em> runs.</span></li>
      <li><span class="num">2</span><span>Every other call (unqualified, or through <strong>this</strong>) still dispatches on the object&rsquo;s actual runtime type.</span></li>
      <li><span class="num">3</span><span>If Climber overrode <strong>log()</strong>, the log call inside RobotPart&rsquo;s stop() would run <em>Climber&rsquo;s</em> log().</span></li>
    </ul></div>''',
        "speak": "One subtlety. Calling super dot some method only changes which version of that one specific call runs. It doesn't change how any other call inside the same method resolves. Any call made without super, a plain unqualified call, or one through this, still dispatches based on the object's actual runtime type, even from inside inherited code. Robot Part's stop calls log. If Climber also overrode log, then that log call inside Robot Part's stop, reached through super dot stop, would run Climber's log, not Robot Part's. The override wins everywhere, except the one spot super explicitly marks.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Expecting <strong>super.method()</strong> to run automatically &mdash; it never does; you must call it yourself.</li>
      <li><span class="check">!</span>Confusing the two forms &mdash; <strong>super(...)</strong> is constructors only.</li>
      <li><span class="check">!</span>Assuming <strong>super</strong> switches <em>every</em> call in that method to the superclass&rsquo;s versions.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Unlike super for constructors, super dot method never happens automatically. Overriding a method completely discards the superclass's version, unless your override calls super dot method itself. Don't confuse the two forms, either. Super with just parentheses only ever calls a constructor, and only from inside a constructor, first on Java 17, and after only object-free statements on Java 25. Super dot method calls a named method, anywhere in a method body. And don't assume super switches every call inside that method over to the superclass's versions. It only affects the one call it's written on.",
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
