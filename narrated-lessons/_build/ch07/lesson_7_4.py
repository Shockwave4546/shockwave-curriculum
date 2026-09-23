BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 7 &middot; The Class Blueprint</div>
      <h1>Class (static) Variables &amp; Methods</h1>
      <p class="scr-sub">Data and behavior that belong to the class itself, not to any one object.</p>
    </div>''',
        "speak": "Everything so far in this chapter has belonged to individual objects. static flips that. A static method or variable belongs to the class itself, one single shared copy, no matter how many objects exist, or even if none do. You already know an example, Math dot random, you never make a new Math first.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">public static int</span> instanceCount = <span class="n">0</span>; <span class="c">// one shared copy for ALL Subsystem objects</span>

    <span class="k">public</span> Subsystem()
    {
        instanceCount++; <span class="c">// every constructor call increments the ONE shared counter</span>
    }
}</code></pre>''',
        "speak": "Here's static in action. instanceCount belongs to the Subsystem class itself, not to any particular Subsystem object. Every time any Subsystem gets constructed, anywhere in the program, that same one shared counter goes up.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">Subsystem A</div>
      <div class="dbox">Subsystem B</div>
      <div class="dbox">Subsystem C</div>
      <div class="darrow">&darr;</div>
      <div class="dbox active">one shared instanceCount</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Every object of the class points at the exact same static variable.</p>''',
        "speak": "No matter how many Subsystem objects you create, they all share that one single counter. That's the entire point of static, exactly one copy, visible to, and shared by, every object of the class.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">private double</span> currentSpeed; <span class="c">// instance variable — belongs to ONE object</span>

    <span class="k">public static void</span> printStatic()
    {
        System.out.println(currentSpeed); <span class="c">// compile error! no object to read this from</span>
    }
}</code></pre>''',
        "speak": "Here's the flip side, and it's important. A static method can freely use other static members, but it cannot reach an instance variable, or call an instance method, directly. Why? Static code runs without any particular object in hand, and instance data only exists per object. This exact line will not compile, current speed belongs to some specific Subsystem, and print Static has no idea which one.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static void</span> printSpeed(<span class="t">Subsystem</span> s)
{
    System.out.println(s.currentSpeed); <span class="c">// fine — reading a specific object's data</span>
}</code></pre>''',
        "speak": "The fix, if a static method genuinely needs instance data, is to pass in an actual object as a parameter. Now s is a specific Subsystem, and reading s dot current speed is perfectly fine, we finally have an object to read it from.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">public static double</span> maxObservedCurrent = <span class="n">0</span>;

    <span class="k">public</span> Subsystem(<span class="k">double</span> current)
    {
        <span class="k">if</span> (current &gt; maxObservedCurrent)
        {
            maxObservedCurrent = current; <span class="c">// updates the ONE shared value</span>
        }
    }
}</code></pre>''',
        "speak": "A static variable is genuinely useful for tracking things across every object a class has ever created, a running maximum here. Every time a new Subsystem gets built with some current draw, it checks that value against the single shared maxObservedCurrent, and updates it if this one's higher. Changing it from any one object's constructor updates what every other object sees too, since there's only ever the one copy.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static final double</span> MAX_SPEED = <span class="n">1.0</span>;</code></pre>''',
        "speak": "final makes a variable's value unchangeable once it's set, and that's what you reach for to declare a true constant, conventionally named in all caps with underscores between words, here, a public, static, final double, Max underscore Speed, set once to 1.0. Trying to reassign a final variable later on is a compile error, not a runtime surprise, Java catches it immediately.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Trying to read an instance variable from a static method &mdash; it doesn't compile.</li>
      <li><span class="check">!</span>Expecting a static variable to have a separate copy per object &mdash; it doesn't, that's exactly what makes it useful.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Don't try to read an instance variable straight from a static method, it simply doesn't compile, unless an actual object gets passed in as a parameter first. And don't expect a static variable to have a separate copy per object, it never does, there's exactly one, shared by everything, which is precisely what makes it useful for a running count or a running maximum.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>static members belong to the class itself &mdash; one shared copy.</li>
      <li><span class="check">&#10003;</span>Static code cannot access instance data directly &mdash; it needs an object passed in.</li>
      <li><span class="check">&#10003;</span>A static variable's value is shared across every object of the class.</li>
      <li><span class="check">&#10003;</span>final marks an unchangeable constant, conventionally named in ALL CAPS.</li>
    </ul></div>''',
        "speak": "So, to recap. static members belong to the class itself, one single shared copy, no matter how many objects exist. Static code cannot access instance variables or instance methods directly, it needs an actual object handed in first. A static variable's value is shared across every object of the class, useful for running totals, counts, or maximums. And final marks a variable as an unchangeable constant, conventionally named in all caps with underscores. That wraps up Chapter 7. Next up, Chapter 8, constructors and this, in much more depth.",
    },
]
