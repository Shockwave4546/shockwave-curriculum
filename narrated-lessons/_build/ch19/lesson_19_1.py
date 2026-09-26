BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 19 &middot; Interfaces as Contracts</div>
      <h1>Lambdas &amp; Method References</h1>
      <p class="scr-sub">Implementing a one-method interface without writing a class.</p>
    </div>''',
        "speak": "Lesson 19.1. Lambdas and method references. Two shorthands for implementing an interface without all the ceremony of a full class.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">interface</span> <span class="t">SpeedSource</span>
{
    <span class="k">double</span> <span class="me">get</span>(); <span class="c">// exactly one abstract method (Lesson 19) — a method with no body</span>
}</code></pre>''',
        "speak": "Lesson 19's implements always names a class. Java also lets you implement an interface inline, right where an object is needed, with no separate class declaration at all, an anonymous class. Here's Speed Source, one abstract method.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">SpeedSource</span> speed = <span class="k">new</span> <span class="t">SpeedSource</span>()
{
    <span class="me">@Override</span>
    <span class="k">public double</span> <span class="me">get</span>() { <span class="k">return</span> joystick.<span class="me">getY</span>(); }
};</code></pre>''',
        "speak": "The syntax is new, the interface name, parentheses, then a class body right there in the expression. This creates one object of a brand-new, unnamed class that implements Speed Source, built and used in a single expression, with none of the ceremony of a separate file or a named top-level class. It's most useful for a one-off implementation that nothing else in the program needs to refer to by name.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// Anonymous class: still a full class body just to supply one value</span>
<span class="t">SpeedSource</span> speed = <span class="k">new</span> <span class="t">SpeedSource</span>()
{
    <span class="me">@Override</span>
    <span class="k">public double</span> <span class="me">get</span>() { <span class="k">return</span> joystick.<span class="me">getY</span>(); }
};

<span class="c">// With a lambda: the same thing, far more directly</span>
<span class="t">SpeedSource</span> speed = () -&gt; joystick.<span class="me">getY</span>();</code></pre>''',
        "speak": "When an interface declares exactly one abstract method, a functional interface, an anonymous class is still a lot of ceremony for something conceptually simple: here's the one bit of behavior you asked for. A lambda expression writes that one method's body directly, with no class declaration at all. Same interface, same value, one line. WPILib commands and suppliers are built almost entirely on this pattern, which is exactly what makes lambdas so central to command-based programming, in Chapter 25.",
    },
    {
        "screen": '''<pre class="code"><code>(parameters) -&gt; expression</code></pre>''',
        "speak": "A lambda expression has three parts: a parameter list in parentheses, an arrow, and a body.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Lambda Syntax</h2><ul>
      <li><span class="num">1</span><span>Parameter types are usually left out &mdash; the compiler infers them</span></li>
      <li><span class="num">2</span><span>Parentheses can be dropped around a single parameter</span></li>
      <li><span class="num">3</span><span>A single expression returns automatically &mdash; no <strong>return</strong> keyword</span></li>
    </ul></div>''',
        "speak": "Parameter types are usually left out, the compiler already knows them from the functional interface being implemented, though writing them is technically legal. Parentheses can be dropped around a single parameter. And a single-expression body is the return value automatically, no return keyword needed.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// single expression — auto-returned</span>
<span class="t">SpeedSource</span> speed = () -&gt; joystick.<span class="me">getY</span>();

<span class="c">// multi-statement body needs braces + return</span>
<span class="t">SpeedSource</span> clampedSpeed = () -&gt; {
    <span class="k">double</span> raw = joystick.<span class="me">getY</span>();
    <span class="k">return</span> <span class="t">Math</span>.<span class="me">max</span>(-<span class="n">1.0</span>, <span class="t">Math</span>.<span class="me">min</span>(<span class="n">1.0</span>, raw));
};</code></pre>''',
        "speak": "A single expression, like reading the joystick directly, auto-returns. A multi-statement body needs braces and an explicit return, exactly like a regular method. Clamped Speed reads the joystick, clamps it between negative one and one, and returns that.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public interface</span> <span class="t">IntBinaryOperation</span>
{
    <span class="k">int</span> <span class="me">apply</span>(<span class="k">int</span> a, <span class="k">int</span> b);
}

<span class="t">IntBinaryOperation</span> add = (a, b) -&gt; a + b;</code></pre>''',
        "speak": "A lambda with more than one parameter lists them comma-separated inside the parentheses. Int Binary Operation takes two ints; add is written as a, b, arrow, a plus b.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> base = <span class="n">1.0</span>;
base = <span class="n">2.0</span>; <span class="c">// reassigned — base is no longer effectively final</span>
<span class="c">// does NOT compile — base is no longer effectively final</span>
<span class="t">SpeedSource</span> s = () -&gt; base;</code></pre>''',
        "speak": "A lambda body can read local variables and parameters from the method around it, but only ones that are never reassigned after being given a value, effectively final, even without writing the final keyword. Reassign base before a lambda reads it, and the lambda fails to compile: local variables referenced from a lambda expression must be final or effectively final. If a value genuinely needs to change and be read from inside a lambda, it has to live in a field instead, Lesson 7.2's where variables live.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Functional Interfaces You&rsquo;ll Actually Use</h2><ul>
      <li><span class="num">1</span><span><strong>Supplier&lt;T&gt;</strong> &mdash; no input, returns a value</span></li>
      <li><span class="num">2</span><span><strong>Consumer&lt;T&gt;</strong> &mdash; takes a value, returns nothing</span></li>
      <li><span class="num">3</span><span><strong>Function&lt;T,R&gt;</strong> &mdash; takes a value, returns a value</span></li>
      <li><span class="num">4</span><span><strong>Predicate&lt;T&gt;</strong> &mdash; takes a value, returns true/false</span></li>
    </ul></div>''',
        "speak": "Java ships a whole family of ready-made functional interfaces in the java dot util dot function package, so you rarely need to declare your own. Supplier of T takes no input and returns a value. Consumer of T takes a value and returns nothing. Function of T, R takes a value and returns a, possibly different typed, value. And Predicate of T takes a value and returns true or false. Each is marked at Functional Interface, a compiler check confirming it has exactly one abstract method.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">import</span> java.util.function.DoubleSupplier;
<span class="k">import</span> java.util.function.BooleanSupplier;

<span class="t">Runnable</span> stopAll = () -&gt; intake.<span class="me">stop</span>();                 <span class="c">// java.lang — no import needed</span>
<span class="c">// java.util.function — needs the import above</span>
<span class="t">DoubleSupplier</span> speed = () -&gt; joystick.<span class="me">getY</span>();
<span class="t">BooleanSupplier</span> hasGamePiece = () -&gt; intake.<span class="me">hasPiece</span>();</code></pre>''',
        "speak": "Two more specialized ones show up constantly in robot code, Double Supplier, no arguments, returns a double, and Boolean Supplier, no arguments, returns a boolean. Both come from java dot util dot function and need an import. Runnable is the one exception, it lives in java dot lang, so it never needs an import.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Method References: Four Kinds</h2><ul>
      <li><span class="num">1</span><span><strong>Bound instance</strong> &mdash; <code>intake::stop</code></span></li>
      <li><span class="num">2</span><span><strong>Unbound instance</strong> &mdash; <code>String::isEmpty</code></span></li>
      <li><span class="num">3</span><span><strong>Static</strong> &mdash; <code>Math::abs</code></span></li>
      <li><span class="num">4</span><span><strong>Constructor</strong> &mdash; <code>IllegalStateException::new</code></span></li>
    </ul></div>''',
        "speak": "When a lambda's entire body is just calling one existing method, a method reference says the same thing even more directly. There are four kinds. A bound instance reference already has its object, intake, and Java calls stop on that exact object. An unbound instance reference names only a class, String, and the object to call the method on arrives as the functional interface's own argument. A static reference calls a static method directly, like Math's abs. And a constructor reference calls new on a class, forwarding whatever arguments the functional interface supplies, exactly how Chapter 24's Illegal State Exception reference works, as a Supplier of Illegal State Exception.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// a lambda...</span>
<span class="t">Runnable</span> stopAll = () -&gt; intake.<span class="me">stop</span>();
<span class="c">// ...is exactly equivalent to this bound method reference</span>
<span class="t">Runnable</span> stopAll2 = intake::stop;</code></pre>''',
        "speak": "Intake, then a bound reference to stop, reads as the stop method, called on intake. Java fills in the call automatically, with whatever arguments the functional interface's method expects. Method references exist purely as a shorthand for a lambda that does nothing but forward to an existing method, but they aren't quite identical in one respect.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Reassigning a local variable a lambda reads &mdash; must be final or effectively final.</li>
      <li><span class="check">!</span>Reaching for a method reference when the lambda does more than forward one call.</li>
      <li><span class="check">!</span>Assuming a bound reference and its lambda behave identically &mdash; the reference reads its object at creation, the lambda only when called.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Reassigning a local variable a lambda reads breaks the final-or-effectively-final rule, a compile error. Reaching for a method reference when the lambda does more than forward one call, that genuinely needs a lambda. And assuming a bound method reference and its equivalent lambda behave identically: the reference reads, and can throw on, its target object the moment it's created, while the lambda only reads that object when it's actually called. If the object could be null at the time the reference is written, that timing difference matters.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An anonymous class implements an interface inline; a lambda skips the class syntax entirely for a functional interface.</li>
      <li><span class="check">&#10003;</span>Parameter types inferred; parentheses droppable for one parameter; single expression auto-returns.</li>
      <li><span class="check">&#10003;</span>A lambda can only capture final or effectively final locals &mdash; a changing value belongs in a field.</li>
      <li><span class="check">&#10003;</span><strong>java.util.function</strong> ships Supplier, Consumer, Function, Predicate, DoubleSupplier, BooleanSupplier &mdash; Runnable doesn&rsquo;t need an import.</li>
      <li><span class="check">&#10003;</span>Four method-reference kinds: bound instance, unbound instance, static, constructor.</li>
    </ul></div>''',
        "speak": "So, to recap. An anonymous class implements an interface inline, with no separate named class; a lambda goes one step further for a functional interface, skipping the class syntax entirely. Parameter types are normally inferred, parentheses droppable for a single parameter, and a single expression returns automatically. A lambda can only read local variables that are final or effectively final, a value that needs to change belongs in a field. Java dot util dot function ships Supplier, Consumer, Function, and Predicate, plus Double Supplier and Boolean Supplier, all needing an import; Runnable doesn't. And a method reference comes in four kinds: bound instance, unbound instance, static, and constructor, shorthand for a lambda that does nothing but call one existing method or constructor. That wraps up Chapter 19. Next up, Chapter 20: the IO-layer pattern.",
    },
]
