BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 2 &middot; Variables &amp; Types</div>
      <h1>Variables &amp; Data Types</h1>
      <p class="scr-sub">Java&rsquo;s 8 primitive types &mdash; the building blocks everything else is made from.</p>
    </div>''',
        "speak": "Welcome to Chapter 2. Every value your robot code ever touches, a motor speed, a sensor reading, a true-or-false flag, has to live in a variable of some type. So before anything else, let's meet Java's types.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Primitives You'll Use Constantly</h2><ul></ul></div>''',
        "speak": "Java has exactly 8 primitive types, full stop, nothing else is built into the language directly. A primitive variable holds its value straight, with nothing underneath it. Five of the eight show up constantly in FRC code.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Primitives You'll Use Constantly</h2><ul>
      <li><span class="num">1</span><span><strong>int</strong> &mdash; a whole number, like 5 or negative 12. CAN IDs, ports, loop counters.</span></li>
    </ul></div>''',
        "speak": "int holds a whole number, five, negative twelve, whatever. This is what you'll use for CAN IDs, port numbers, loop counters, anything counted rather than measured.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Primitives You'll Use Constantly</h2><ul>
      <li><span class="num">1</span><span><strong>int</strong> &mdash; a whole number, like 5 or negative 12. CAN IDs, ports, loop counters.</span></li>
      <li><span class="num">2</span><span><strong>long</strong> &mdash; a bigger whole number, for values too large for int, like a timestamp. Written with an L.</span></li>
    </ul></div>''',
        "speak": "long is a bigger whole number, for values too large to fit in an int, a timestamp is the classic example. You write one with a trailing L, like one hundred L.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Primitives You'll Use Constantly</h2><ul>
      <li><span class="num">1</span><span><strong>int</strong> &mdash; a whole number, like 5 or negative 12. CAN IDs, ports, loop counters.</span></li>
      <li><span class="num">2</span><span><strong>long</strong> &mdash; a bigger whole number, for values too large for int, like a timestamp. Written with an L.</span></li>
      <li><span class="num">3</span><span><strong>double</strong> &mdash; a decimal number, like 0.85. Almost anything measured.</span></li>
    </ul></div>''',
        "speak": "double is a decimal number, zero point eight five, and so on. Almost anything you'd actually measure on a robot, speed, distance, voltage, is a double.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Primitives You'll Use Constantly</h2><ul>
      <li><span class="num">1</span><span><strong>int</strong> &mdash; a whole number, like 5 or negative 12. CAN IDs, ports, loop counters.</span></li>
      <li><span class="num">2</span><span><strong>long</strong> &mdash; a bigger whole number, for values too large for int, like a timestamp. Written with an L.</span></li>
      <li><span class="num">3</span><span><strong>double</strong> &mdash; a decimal number, like 0.85. Almost anything measured.</span></li>
      <li><span class="num">4</span><span><strong>float</strong> &mdash; a smaller, less precise decimal. Written with an f. WPILib itself prefers double.</span></li>
    </ul></div>''',
        "speak": "float is also a decimal, but smaller and less precise, written with a trailing f. You'll see it out in the wild, but WPILib itself prefers double, and so will we, almost everywhere.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Primitives You'll Use Constantly</h2><ul>
      <li><span class="num">1</span><span><strong>int</strong> &mdash; a whole number, like 5 or negative 12. CAN IDs, ports, loop counters.</span></li>
      <li><span class="num">2</span><span><strong>long</strong> &mdash; a bigger whole number, for values too large for int, like a timestamp. Written with an L.</span></li>
      <li><span class="num">3</span><span><strong>double</strong> &mdash; a decimal number, like 0.85. Almost anything measured.</span></li>
      <li><span class="num">4</span><span><strong>float</strong> &mdash; a smaller, less precise decimal. Written with an f. WPILib itself prefers double.</span></li>
      <li><span class="num">5</span><span><strong>boolean</strong> &mdash; only ever true or false.</span></li>
    </ul></div>''',
        "speak": "And boolean, only ever true or false. Nothing in between, nothing else allowed.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">byte</div><div class="dbox">short</div><div class="dbox">char</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox active">String</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">byte and short are rarely reached for directly; char holds one character &mdash; and String is really a chain of chars underneath.</p>''',
        "speak": "The remaining three primitives, byte, short, and char, round out the full list of eight. You'll rarely reach for byte or short directly. char is worth knowing though, it holds exactly one character, because String, which you already use constantly, is really just a sequence of chars glued together underneath. That's the whole list, nothing else in Java is a primitive. Everything else, String included, and every class you'll eventually write starting in Chapter 7, is built by combining these eight.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> motorSpeed;</code></pre>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">motorSpeed now exists &mdash; but doesn't hold a value yet.</p>''',
        "speak": "To create a variable, write its type, then its name, then a semicolon. int motor speed, semicolon. At this point motor speed exists, but it doesn't hold a value yet.",
    },
    {
        "screen": '''<pre class="code"><code>motorSpeed = <span class="n">5</span>;</code></pre>''',
        "speak": "Give it one with an equals sign. motor speed equals 5. Read that as motor speed gets assigned the value 5, not motor speed equals 5 the way you'd read it in math class. It's an instruction: take what's on the right, and store it in the box on the left.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> motorSpeed = <span class="n">5</span>;</code></pre>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Usually you do both steps at once &mdash; a local variable, since it lives only inside its method.</p>''',
        "speak": "Usually you'd do both steps at once, like this: int motor speed equals 5. Same reading: motor speed, of type int, is assigned the value 5. Since this lives inside a method body, it's called a local variable, it only exists inside that method. Java has other kinds of variables too, but those wait until classes and methods are properly on the table, starting in Chapter 7.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>maxSpeed</code><span class="nlabel">start lowercase, capitalize each new word</span></div>
      <div class="namerow"><code>isReady</code><span class="nlabel">say what the value IS &mdash; not just "x"</span></div>
    </div>''',
        "speak": "Naming matters. A name has to start with a letter and can't contain spaces, and Java's own style, which you'll see in every piece of code from here forward, is camelCase: start lowercase, then capitalize the first letter of every new word after that. And pick a name that actually says what the value is, speed tells you something useful, x tells you nothing.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> maxSpeed = <span class="n">0.85</span>;   <span class="c">// not max_speed, not MaxSpeed</span>
<span class="k">boolean</span> isReady = <span class="k">false</span>;</code></pre>''',
        "speak": "Here's camelCase in practice. double max speed, not max underscore speed, not Max Speed with a capital M. boolean is ready, same rule, lowercase start.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> motorSpeed = <span class="n">5</span>;         <span class="c">// a whole number &mdash; no decimal needed here</span>
<span class="k">double</span> maxOutput = <span class="n">0.85</span>;    <span class="c">// a percentage like 85% &mdash; needs a decimal</span>
<span class="k">boolean</span> isReady = <span class="k">false</span>;    <span class="c">// only ever true or false</span></code></pre>''',
        "speak": "Let's put this all together in a worked example. A whole-number motor speed, a decimal max output for something like an eighty five percent power cap, and a boolean flag for whether the robot's ready. Notice each type matches what the value actually needs.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> motorSpeed = <span class="n">5</span>;         <span class="c">// a whole number &mdash; no decimal needed here</span>
<span class="k">double</span> maxOutput = <span class="n">0.85</span>;    <span class="c">// a percentage like 85% &mdash; needs a decimal</span>
<span class="k">boolean</span> isReady = <span class="k">false</span>;    <span class="c">// only ever true or false</span>
<span class="t">String</span> robotName = <span class="s">"Titan"</span>; <span class="c">// text, built out of primitives under the hood</span></code></pre>''',
        "speak": "And a String for the robot's name, Titan, in quotes. Remember, under the hood that's really just a chain of chars, built out of the same eight primitives, wearing a more convenient wrapper.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> motorSpeed = <span class="n">5</span>;         <span class="c">// a whole number &mdash; no decimal needed here</span>
<span class="k">double</span> maxOutput = <span class="n">0.85</span>;    <span class="c">// a percentage like 85% &mdash; needs a decimal</span>
<span class="k">boolean</span> isReady = <span class="k">false</span>;    <span class="c">// only ever true or false</span>
<span class="t">String</span> robotName = <span class="s">"Titan"</span>; <span class="c">// text, built out of primitives under the hood</span>

System.out.<span class="me">println</span>(<span class="s">"Robot "</span> + robotName + <span class="s">" is set to speed "</span> + motorSpeed);</code></pre>''',
        "speak": "And finally, System dot out dot print line stitches it into one sentence with plus signs, robot name and motor speed get pulled in as their actual values, not as the literal words robot name or motor speed. That distinction is exactly where our first pitfall comes from.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Putting a variable's name inside quotes prints the literal word, not the value stored in it.</li>
      <li><span class="check">!</span>Case matters &mdash; motorSpeed and motorspeed are two different variables, silently.</li>
      <li><span class="check">!</span>Mismatching type and value &mdash; a decimal value stuffed into an int just throws away everything past the decimal point.</li>
    </ul></div>''',
        "speak": "A few pitfalls worth flagging. Never put a variable's name inside quotes, that prints the literal word, not the number stored inside it. Case matters, motor speed with a lowercase s and motor speed with an uppercase S are two completely different variables to Java, and that mistake won't throw an error, it'll just quietly break something. And match the type to the value, a decimal value needs a double, an int just throws away everything after the decimal point.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Java has exactly 8 primitive types &mdash; everything else is built from them.</li>
      <li><span class="check">&#10003;</span>A variable is type, then name, then semicolon &mdash; and equals means "gets assigned."</li>
      <li><span class="check">&#10003;</span>Local variables live only inside the method that declares them.</li>
      <li><span class="check">&#10003;</span>Names use camelCase and should describe what the value is.</li>
    </ul></div>''',
        "speak": "So, to recap. Java has exactly 8 primitive types, and everything else, String included, is built out of them. Declaring a variable is type, then name, then semicolon, and the equals sign means gets assigned, not equals. A local variable lives only inside the method that declares it. And names use camelCase and should actually describe what the value is. Next up, lesson 2.2, we'll start doing things with these variables, printing them and building expressions out of them.",
    },
]
