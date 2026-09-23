BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 7 &middot; The Class Blueprint</div>
      <h1>Anatomy of a Java Class</h1>
      <p class="scr-sub">Every class you write has the same three parts, in the same order.</p>
    </div>''',
        "speak": "Welcome to Chapter 7. Up to now you've been using classes other people wrote, String, Scanner, Math. Starting today, you're writing your own. And every single class you'll ever write, no matter what it represents, breaks down into the same three parts.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Three Anatomical Parts</h2><ul>
      <li><span class="num">1</span><span><strong>Instance variables</strong> &mdash; the data each object owns.</span></li>
    </ul></div>''',
        "speak": "First, instance variables. This is the data, and each object you create gets its own separate copy. Two different Intake objects can each track their own current speed, completely independently.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Three Anatomical Parts</h2><ul>
      <li><span class="num">1</span><span><strong>Instance variables</strong> &mdash; the data each object owns.</span></li>
      <li><span class="num">2</span><span><strong>Constructors</strong> &mdash; initialize those instance variables when an object is built.</span></li>
    </ul></div>''',
        "speak": "Second, constructors. Their job is to initialize the instance variables the moment an object gets built with new.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Three Anatomical Parts</h2><ul>
      <li><span class="num">1</span><span><strong>Instance variables</strong> &mdash; the data each object owns.</span></li>
      <li><span class="num">2</span><span><strong>Constructors</strong> &mdash; initialize those instance variables when an object is built.</span></li>
      <li><span class="num">3</span><span><strong>Methods</strong> &mdash; the behaviors, which can read and change those instance variables.</span></li>
    </ul></div>''',
        "speak": "And third, methods, the behaviors, the things an object can actually do, which read and change its own instance variables along the way.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span>
{
    <span class="c">// 1. instance variables — the data each object owns</span>

    <span class="c">// 2. constructors — initialize the instance variables</span>

    <span class="c">// 3. methods — the behaviors</span>
}</code></pre>''',
        "speak": "Here's that skeleton in real Java, for a subsystem called Intake, always in this order: instance variables first, constructors second, methods third.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span>
{
    <span class="k">private boolean</span> isDeployed;
    <span class="k">private double</span> currentSpeed;
    <span class="k">private boolean</span> hasGamePiece;
}</code></pre>''',
        "speak": "Before writing any code, design the class by asking one question: what does this thing need to know about itself? For an Intake subsystem, is it currently deployed, what's its current motor speed, and does it have a sensor reading a game piece. Answer that question first, and the instance variables practically write themselves.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span>
{
    <span class="k">private double</span> currentSpeed; <span class="c">// only Intake's own code can touch this directly</span>
}</code></pre>''',
        "speak": "Notice every one of those is private, not public. Public means any other class can reach it directly; private restricts access to code inside that same class only. This is encapsulation, the class's internal data stays hidden, and outside code can only interact with it through whatever methods the class chooses to expose. It matters in practice, if current speed were public, any other piece of code could set it directly, bypassing whatever safety logic Intake's own methods enforce, like a ramp limit or a max-speed clamp. Keeping it private means the only way in is through Intake's own methods, which can enforce those rules every single time.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span>
{
    <span class="c">// 1. instance variables</span>
    <span class="k">private boolean</span> isDeployed;
    <span class="k">private double</span> currentSpeed;

    <span class="c">// 2. constructor</span>
    <span class="k">public</span> Intake()
    {
        isDeployed = <span class="k">false</span>;
        currentSpeed = <span class="n">0.0</span>;
    }

    <span class="c">// 3. methods</span>
    <span class="k">public void</span> deploy()
    {
        isDeployed = <span class="k">true</span>;
    }
}</code></pre>''',
        "speak": "Put all three parts together and here's a complete, working class. Instance variables at the top, a constructor that sets them to a sensible starting state, and a method, deploy, that changes one of them. Nothing fancy yet, constructors and methods each get their own full lesson soon, but this is genuinely the whole shape of every class you'll write.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">One More Thing</h2><ul>
      <li><span class="num">1</span><span>Any class can also have a <strong>main</strong> method &mdash; usually just to test that one class by itself.</span></li>
    </ul></div>''',
        "speak": "One more small thing worth knowing: any class can also have a main method. It's usually not there for the class's normal job, it's a quick, convenient way to test that one class in isolation, separate from the rest of your program.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Making instance variables public "to keep things simple" &mdash; this defeats encapsulation entirely.</li>
      <li><span class="check">!</span>Skipping the design step &mdash; jumping straight to code tends to produce classes with the wrong data.</li>
    </ul></div>''',
        "speak": "Two pitfalls worth calling out. Don't make instance variables public just to keep things simple, that defeats encapsulation completely, letting any other class set them to anything, with none of your class's own safety logic enforced. And don't skip the design step, jumping straight to code without first asking what this class needs to know about itself tends to produce classes with the wrong data, and you usually don't find out until you're several methods in.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Every class has the same three parts, in order: instance variables, constructors, methods.</li>
      <li><span class="check">&#10003;</span>Instance variables are per-object &mdash; each object gets its own independent copies.</li>
      <li><span class="check">&#10003;</span>Instance variables should be private; that's encapsulation.</li>
      <li><span class="check">&#10003;</span>Design a class by first asking what data it needs to represent.</li>
    </ul></div>''',
        "speak": "So, to recap. Every class has the same three parts, always in the same order, instance variables, constructors, methods. Instance variables are per-object, each object keeps its own independent copies. Instance variables should be private, and that's what encapsulation actually means. And design a class by first asking what data it needs to represent, before writing a single line of code. Next up, lesson 7.2, where we actually write those methods.",
    },
]
