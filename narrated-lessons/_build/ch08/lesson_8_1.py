# Combined lesson covering both 8.1 (Writing Constructors) and 8.2 (the "this" Keyword),
# matching the source lesson markdown's combined granularity (8.1-8.2-constructors-and-this.md).
BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 8 &middot; Constructors &amp; "this"</div>
      <h1>Constructors &amp; "this"</h1>
      <p class="scr-sub">Building an object into a valid state, and the keyword that means "this one, right here."</p>
    </div>''',
        "speak": "Welcome to Chapter 8. We've used constructors informally for a while now, today we go deep on exactly what a constructor's job is, and we meet this, a keyword that turns out to matter more than it first looks like it should.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Climber</span>
{
    <span class="k">private int</span> motorPort;

    <span class="k">public</span> Climber(<span class="k">int</span> motorPort) <span class="c">// same name as the class, no return type</span>
    {
        this.motorPort = motorPort;
    }
}</code></pre>''',
        "speak": "A constructor has exactly one job: put a brand new object into a valid state, every instance variable set to something usable. Its signature looks a lot like a method's, but with two real differences. There's no return type, not even void, and its name is always, exactly, the class's own name.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Climber</span>
{
    <span class="k">private int</span> motorPort; <span class="c">// if no constructor is written, this defaults to 0</span>
}</code></pre>''',
        "speak": "Every instance variable starts at its type's default the instant an object exists, 0 for int, 0.0 for double, false for boolean, null for any object reference, whether or not you ever write a constructor. If you don't write one at all, Java quietly adds an empty no-argument constructor for you, it doesn't do anything beyond that automatic default initialization. But the moment you write even one constructor yourself, that free one disappears completely, you're now responsible for covering every way you want objects of your class to get built.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Climber</span>
{
    <span class="k">private int</span> motorPort;
    <span class="k">private double</span> climbSpeed;

    <span class="k">public</span> Climber(<span class="k">int</span> motorPort)
    {
        this.motorPort = motorPort;
        this.climbSpeed = <span class="n">0.5</span>; <span class="c">// a sensible default</span>
    }

    <span class="k">public</span> Climber(<span class="k">int</span> motorPort, <span class="k">double</span> climbSpeed)
    {
        this.motorPort = motorPort;
        this.climbSpeed = climbSpeed;
    }
}</code></pre>''',
        "speak": "Just like methods back in Chapter 4, a class can have several constructors, distinguished by their parameter lists, the same overloading idea. Here, one constructor takes just a motor port and picks a sensible default climb speed, the other lets the caller specify both. Same class, two different ways to build one.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Climber</span>
{
    <span class="k">private int</span> motorPort;
    <span class="k">private double</span> climbSpeed;

    <span class="k">public</span> Climber(<span class="k">int</span> motorPort)
    {
        this(motorPort, <span class="n">0.5</span>); <span class="c">// delegates to the two-argument constructor below</span>
    }

    <span class="k">public</span> Climber(<span class="k">int</span> motorPort, <span class="k">double</span> climbSpeed)
    {
        this.motorPort = motorPort;
        this.climbSpeed = climbSpeed;
    }
}</code></pre>''',
        "speak": "One constructor can also call another constructor in the same class directly, using this followed by parentheses and the arguments to pass along, instead of repeating the same setup code. That's called constructor chaining. On Java 17, that call has to be the very first statement in the constructor, nothing before it. Java 25 loosens that a little, letting a simple check run first, as long as it doesn't touch the object's fields or methods yet. This lesson still puts it first, since that works the same on both versions.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">"this": the Current Object</h2><ul>
      <li><span class="num">1</span><span>Inside an instance method or constructor, <strong>this</strong> refers to the specific object it's currently running for.</span></li>
    </ul></div>''',
        "speak": "Now, this. Inside an instance method or a constructor, this refers to the one specific object the code is currently running for.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> Climber(<span class="k">int</span> motorPort)
{
    this.motorPort = motorPort; <span class="c">// left side: instance variable. right side: parameter.</span>
}</code></pre>''',
        "speak": "It's most useful exactly when a parameter shares a name with an instance variable, which happens constantly in constructors. this dot motor port unambiguously means this object's motor port, the instance variable, while bare motor port on its own means the parameter that just came in. Without this, motor port equals motor port would just assign the parameter to itself, and the instance variable would never actually get set at all, a genuinely sneaky bug because it compiles perfectly cleanly.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Where "this" Does, and Doesn't, Exist</h2><ul>
      <li><span class="num">1</span><span><strong>this</strong> only exists inside instance methods and constructors.</span></li>
      <li><span class="num">2</span><span>A static method has no current object to refer to, so it has no <strong>this</strong> at all.</span></li>
    </ul></div>''',
        "speak": "this only exists inside instance methods and constructors. Remember static from last lesson, a static method has no particular object running it, so it has no this to refer to, there's simply nothing for the word to mean in that context.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Climber</span>
{
    <span class="k">private double</span> currentHeight;

    <span class="k">public void</span> reportTo(<span class="t">ClimbLogger</span> logger)
    {
        logger.record(this); <span class="c">// pass the current Climber object itself</span>
    }
}</code></pre>''',
        "speak": "this is a real reference, usable anywhere an object reference is expected, including passing the current object into another method or constructor entirely. Here, report to hands the current Climber object itself off to a logger, so the logger can go read whatever it needs directly from this exact object.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting this when a parameter shadows an instance variable &mdash; assigns the parameter to itself, and does nothing.</li>
      <li><span class="check">!</span>Assuming a class always gets a free default constructor &mdash; only true if you write zero constructors yourself.</li>
      <li><span class="check">!</span>Writing void ClassName(...) instead of a constructor &mdash; that's just an ordinary method, and it never runs automatically.</li>
    </ul></div>''',
        "speak": "Three pitfalls to really lock in. Forgetting this when a parameter shadows an instance variable, motor port equals motor port with no this, assigns the parameter to itself and leaves the actual instance variable completely untouched, no error, just silently wrong, the same scope idea from lesson seven point two. Don't assume a class always gets a free default constructor, that's only true if you write exactly zero constructors yourself, write even one, and you own every constructor your class needs from then on. And watch for adding void in front of a constructor's name, that turns it into an ordinary method that just happens to share the class's name, it's not a constructor anymore, and it never runs automatically when you build a new object.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A constructor's signature has no return type and matches the class's name; its job is a valid starting state.</li>
      <li><span class="check">&#10003;</span>Every instance variable starts at its type's default regardless of any constructor; with none written, Java adds an empty one.</li>
      <li><span class="check">&#10003;</span>Constructors can be overloaded, just like methods &mdash; one overload can chain to another with this(...).</li>
      <li><span class="check">&#10003;</span>this refers to the current object &mdash; essential when a parameter shares a name with an instance variable.</li>
      <li><span class="check">&#10003;</span>this can be passed as an argument, like any other reference. Static methods have no this.</li>
    </ul></div>''',
        "speak": "So, to recap. A constructor's signature has no return type and always matches the class's name, and its whole job is leaving the object in a valid state. Every instance variable starts at its type's default the moment an object exists, no matter what, with no constructor written Java just adds an empty one. Constructors can be overloaded, just like methods, and one overload can chain to another with this and parentheses instead of repeating the same setup code. this refers to the current object, and it's essential for disambiguating a parameter from an instance variable that shares its name. And this can be passed around as an argument like any other object reference, though static methods never have one. Next up, Chapter 9, where we start storing more than one piece of data at a time, arrays, array lists, and hash maps.",
    },
]
