BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 17 &middot; Inheritance &amp; Abstractions</div>
      <h1>Abstract Classes and Methods</h1>
      <p class="scr-sub">A superclass that can't be built on its own &mdash; and methods every subclass must write.</p>
    </div>''',
        "speak": "This is the last lesson of Chapter 17, and it's the one that puts the abstractions in inheritance and abstractions. Today: abstract classes, and abstract methods.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">A Class That Shouldn't Be Instantiated</h2><ul>
      <li><span class="num">1</span><span>Lesson 17.3 wrote <strong>new RobotPart(&quot;Generic&quot;)</strong> &mdash; but no real part is &ldquo;just a robot part.&rdquo;</span></li>
      <li><span class="num">2</span><span>RobotPart's <strong>stop()</strong> only logs; every real part must stop its own hardware its own way.</span></li>
      <li><span class="num">3</span><span>Wanted: &ldquo;every real part must be a subclass, and every subclass must write its own stop().&rdquo;</span></li>
    </ul></div>''',
        "speak": "Every example so far could build a plain Robot Part. Lesson 17.3 even wrote new Robot Part, called Generic. But on a real robot there's no such thing as just a robot part. Every part is an intake, a shooter, a climber. And Robot Part's stop only prints a message, while every real part has to stop its own hardware, in its own way. What the design really wants to say is: Robot Part is only a starting point. Every real part must be a subclass, and every subclass must write its own stop. Java says exactly that with the keyword abstract.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public abstract class</span> <span class="t">RobotPart</span>
{
    <span class="k">private</span> <span class="t">String</span> name;

    <span class="k">public</span> <span class="t">RobotPart</span>(<span class="t">String</span> name) { <span class="k">this</span>.name = name; }
    <span class="k">public</span> <span class="t">String</span> getName() { <span class="k">return</span> name; }
    <span class="k">public void</span> log(<span class="t">String</span> msg) { <span class="t">System</span>.out.println(<span class="s">"["</span> + name + <span class="s">"] "</span> + msg); }

    <span class="k">public abstract void</span> stop();  <span class="c">// no body: every subclass writes its own</span>
}</code></pre>''',
        "speak": "Writing abstract in the class declaration makes it an abstract class: a class that can be extended, but never instantiated with new. Here's Robot Part from lesson 17.1 as an abstract class. The name field, the constructor, get Name, and log are all still here, unchanged. But stop is now an abstract method: just a signature, ending in a semicolon, with no body at all.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// ERROR: RobotPart is abstract; cannot be instantiated</span>
<span class="t">RobotPart</span> generic = <span class="k">new</span> <span class="t">RobotPart</span>(<span class="s">"Generic"</span>);</code></pre>''',
        "speak": "Trying to build one directly is now a compile error. Robot Part is abstract, so it cannot be instantiated. A class that can be instantiated, which is every class you've written until now, is called a concrete class.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Abstract Methods</h2><ul>
      <li><span class="num">1</span><span>Declared with <strong>abstract</strong>, a signature, and a semicolon &mdash; <em>no body</em>.</span></li>
      <li><span class="num">2</span><span><strong>public abstract void stop();</strong> &mdash; &ldquo;every RobotPart has a stop()&rdquo;, without saying what it does.</span></li>
      <li><span class="num">3</span><span>A class that declares an abstract method must itself be <strong>abstract</strong>.</span></li>
    </ul></div>''',
        "speak": "An abstract method is declared with abstract, has a signature, and ends in a semicolon instead of a body. Public abstract void stop says, every Robot Part has a stop method, without saying what it does. And a class that declares an abstract method must itself be marked abstract, otherwise it doesn't compile.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Concrete Subclasses Fill In the Blanks</div>
    <pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">RobotPart</span>
{
    <span class="k">public</span> <span class="t">Intake</span>(<span class="t">String</span> name) { <span class="k">super</span>(name); }

    <span class="k">@Override</span>
    <span class="k">public void</span> stop() { log(<span class="s">"rollers off"</span>); }
}</code></pre>''',
        "speak": "A concrete subclass must provide a body for every abstract method it inherits. Writing that body is called implementing the method. It uses the same syntax as overriding, which is lesson 18.1, including at Override. Here, Intake calls super with its name, and implements stop by logging rollers off.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Forget One, and It Won't Compile</h2><ul>
      <li><span class="num">1</span><span>Leave out <strong>stop()</strong>: <em>Intake is not abstract and does not override abstract method stop() in RobotPart</em>.</span></li>
      <li><span class="num">2</span><span>The only other option: declare the subclass <strong>abstract</strong> too, passing the job down.</span></li>
    </ul></div>''',
        "speak": "If Intake left stop out, the compiler would reject it, with an error saying Intake is not abstract, and does not override the abstract method stop in Robot Part. The only other option is for the subclass to be declared abstract too, passing the job down to its own subclasses.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What an Abstract Class Can Still Have</h2><ul>
      <li><span class="num">1</span><span><strong>Fields</strong> &mdash; RobotPart still has its private name.</span></li>
      <li><span class="num">2</span><span><strong>Constructors</strong> &mdash; still run for every Intake, through <strong>super(name)</strong>.</span></li>
      <li><span class="num">3</span><span><strong>Concrete methods</strong> &mdash; getName() and log() are inherited unchanged.</span></li>
      <li><span class="num">4</span><span><strong>Use as a type</strong> &mdash; RobotPart variables, parameters, arrays, and lists still work.</span></li>
    </ul></div>''',
        "speak": "Abstract removes only the ability to call new on the class itself. Everything else still works. Robot Part still has its private name field. Its constructor still exists, and still runs for every Intake, through super. You just can't call it with new. Get Name and log still have bodies, and every subclass inherits them unchanged. And Robot Part is still a perfectly good type for a variable, a parameter, an array, or a collection. A Robot Part variable can hold a new Intake. Every object it holds is some concrete subclass, so every one of them really has a stop method.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Abstract Classes in WPILib</h2><ul>
      <li><span class="num">1</span><span><strong>MotorSafety</strong> (org.wpilib.hardware.motor) declares <strong>public abstract void stopMotor();</strong></span></li>
      <li><span class="num">2</span><span><strong>PWMMotorController</strong>, the parent of WPILib's PWM motor controller classes, is abstract too.</span></li>
      <li><span class="num">3</span><span>Robot code never writes <strong>new PWMMotorController(...)</strong> &mdash; it builds a specific subclass.</span></li>
    </ul></div>''',
        "speak": "WPILib uses the same tool. Motor Safety is an abstract class that declares an abstract stop Motor method. And PWM Motor Controller, the shared parent of WPILib's PWM motor controller classes, is abstract too. Robot code never writes new PWM Motor Controller. It constructs one of the specific controller classes that extend it, each of which inherits the shared code.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Looking Ahead: Interfaces (Ch.19)</h2><ul>
      <li><span class="num">1</span><span>An <strong>interface</strong> lists methods a class promises to have &mdash; no object state, no constructors.</span></li>
      <li><span class="num">2</span><span>A class can <strong>implements</strong> several interfaces at once.</span></li>
      <li><span class="num">3</span><span>Shared state and code? Abstract class. Only a shared set of methods? Interface.</span></li>
      <li><span class="num">4</span><span>Ch.18 goes back to the <em>concrete</em> RobotPart from 17.1, whose stop() has a body.</span></li>
    </ul></div>''',
        "speak": "Chapter 19 introduces interfaces, a related tool. An interface lists methods a class promises to have, but has no fields holding object state, and no constructors, and a class can implement several of them at once. Chapter 19 compares the two directly. The short version: reach for an abstract class when the related classes share real state and code, like Robot Part's name and log, and an interface when they only share a set of methods. One more note: starting in Chapter 18, the course's Robot Part examples go back to the concrete Robot Part from lesson 17.1, whose stop has a body, because Chapter 18's lessons override and extend that body.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Trying to instantiate an abstract class &mdash; build a concrete subclass instead.</li>
      <li><span class="check">!</span>Giving an abstract method a body, or leaving the semicolon off.</li>
      <li><span class="check">!</span>Forgetting to implement an abstract method in a concrete subclass.</li>
      <li><span class="check">!</span>Thinking an abstract class can't have constructors or fields.</li>
    </ul></div>''',
        "speak": "Four pitfalls. New Robot Part doesn't compile once Robot Part is abstract, so build a concrete subclass instead, and store it in a Robot Part variable if you like. An abstract method is a signature followed by a semicolon, with no braces at all, so giving it a body, even an empty one, doesn't compile. Every abstract method a concrete subclass inherits needs a body, or the subclass must itself be declared abstract. And an abstract class can have both constructors and fields. Its constructor runs through super, from each subclass.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An abstract class can be extended but never instantiated; a class you can instantiate is concrete.</li>
      <li><span class="check">&#10003;</span>An abstract method has a signature and a semicolon, no body; its class must be abstract.</li>
      <li><span class="check">&#10003;</span>A concrete subclass implements every inherited abstract method, or is abstract itself.</li>
      <li><span class="check">&#10003;</span>Abstract classes still have fields, constructors, concrete methods, and work as types.</li>
      <li><span class="check">&#10003;</span>WPILib uses them too; Ch.19's interfaces share methods without shared state.</li>
    </ul></div>''',
        "speak": "So, to recap. An abstract class can be extended, but never instantiated with new, and a class that can be instantiated is concrete. An abstract method has a signature and a semicolon but no body, and a class that declares one must itself be abstract. A concrete subclass must implement every inherited abstract method, with the same syntax as overriding, or be declared abstract itself. Abstract classes still have fields, constructors that run through super, concrete methods, and they still work as variable, parameter, and collection types. And WPILib uses abstract classes too, while Chapter 19's interfaces are the related tool for sharing methods without shared state. That wraps up Chapter 17. Next up, Chapter 18: polymorphism.",
    },
]
