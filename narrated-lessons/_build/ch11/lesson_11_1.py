BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 11 &middot; Enums</div>
      <h1>Enums: Named Choices</h1>
      <p class="scr-sub">A type with a fixed, predefined set of legal values.</p>
    </div>''',
        "speak": "Welcome to Chapter 11. Today's idea is the enum, short for enumerated type, and it solves a problem you've probably already run into without a name for it: a variable that's only supposed to hold one of a small handful of named states.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Old Way: Plain Integers</h2><ul>
      <li><span class="num">1</span><span><code>int armState = 2;</code> &mdash; but what does 2 even mean?</span></li>
    </ul></div>''',
        "speak": "Before enums, code often represented a fixed set of states with a plain integer, something like int armState equals 2. The problem is that lets any number in at all, including ones that mean absolutely nothing.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public enum</span> ArmPosition
{
    STOWED, INTAKE, SCORE
}</code></pre>''',
        "speak": "An enum fixes that at compile time. You declare it with the enum keyword, and list the legal named values inside curly braces. Arm Position here can only ever be stowed, intake, or score, nothing else.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public enum</span> ArmPosition
{
    STOWED, INTAKE, SCORE
}

ArmPosition target = ArmPosition.INTAKE; <span class="c">// legal</span>
ArmPosition target = ArmPosition.CLIMB;  <span class="c">// compile error — CLIMB was never defined</span></code></pre>''',
        "speak": "Assigning Arm Position dot Intake is completely legal. But try Arm Position dot Climb, a value that was never declared, and the code doesn't even compile. An invalid state isn't just wrong at runtime anymore, it's flat-out impossible to write.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Naming Convention</h2><ul>
      <li><span class="num">1</span><span>Enum constants use <code>SCREAMING SNAKE CASE</code>, same as other constants</span></li>
    </ul></div>''',
        "speak": "One naming convention to lock in early: enum constants are written in screaming snake case, all capitals with underscores between words, the exact same style as other constants, back from lesson 1.2.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">switch</span> (target)
{
    <span class="k">case</span> STOWED -&gt; arm.setAngle(0);
    <span class="k">case</span> INTAKE -&gt; arm.setAngle(35);
    <span class="k">case</span> SCORE  -&gt; arm.setAngle(110);
}</code></pre>''',
        "speak": "Enums pair beautifully with switch. Modern arrow-style case needs no break at all, and this reads close to plain English: if the target is stowed, set the angle to zero, and so on for each named state.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">No Type Prefix Inside a Switch</h2><ul>
      <li><span class="num">1</span><span>Just <code>STOWED</code>, not <code>ArmPosition.STOWED</code></span></li>
    </ul></div>''',
        "speak": "Notice each case label is just STOWED, not Arm Position dot STOWED. Inside a switch over an Arm Position, Java already knows the type, so writing the prefix would be redundant, and it actually won't compile if you include it.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 11 &middot; Enums</div>
      <h1>An Enum Is Really a Class</h1>
      <p class="scr-sub">Not just fancier named integers.</p>
    </div>''',
        "speak": "Here's the part that surprises a lot of people: an enum isn't just a dressed-up set of named integers, it's a genuine, full class. Its body can declare fields, a constructor, and methods, so every single constant can carry its own data.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public enum</span> ArmPosition
{
    STOWED(0), INTAKE(35), SCORE(110); <span class="c">// constants, WITH constructor arguments</span>

    <span class="k">private final</span> <span class="t">double</span> angleDegrees;</code></pre>''',
        "speak": "Here's that same Arm Position enum, upgraded. Each constant now takes a constructor argument, its own target angle in degrees, and there's a private final field to hold it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public enum</span> ArmPosition
{
    STOWED(0), INTAKE(35), SCORE(110); <span class="c">// constants, WITH constructor arguments</span>

    <span class="k">private final</span> <span class="t">double</span> angleDegrees;

    ArmPosition(<span class="t">double</span> angleDegrees)
    {
        <span class="k">this</span>.angleDegrees = angleDegrees;
    }

    <span class="k">public</span> <span class="t">double</span> <span class="me">getAngleDegrees</span>()
    {
        <span class="k">return</span> angleDegrees;
    }
}</code></pre>''',
        "speak": "Then a constructor that just stores whatever angle it's handed, and a plain getter to read it back out. Each constant listed up top, stowed zero, intake thirty-five, score one-ten, calls that constructor with its own arguments.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Rules This Depends On</h2><ul>
      <li><span class="num">1</span><span>The constant list must come <strong>first</strong> in the enum body</span></li>
    </ul></div>''',
        "speak": "Two rules make this work. First, the list of constants has to come first in the enum's body, before any fields or methods.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Two Rules This Depends On</h2><ul>
      <li><span class="num">1</span><span>The constant list must come <strong>first</strong> in the enum body</span></li>
      <li><span class="num">2</span><span>Once fields or methods follow, that list must end with a semicolon</span></li>
    </ul></div>''',
        "speak": "Second, once fields or methods follow the constant list, that list has to end with a semicolon. Skip that semicolon here and the enum simply won't compile.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">You Can Never <code>new</code> One Yourself</h2><ul>
      <li><span class="num">1</span><span>An enum's constructor is implicitly <code>private</code></span></li>
      <li><span class="num">2</span><span>The only instances that will ever exist are the ones listed in the enum body</span></li>
    </ul></div>''',
        "speak": "And here's the part that keeps the whole guarantee airtight: an enum's constructor is implicitly private. You're never allowed to write new Arm Position yourself, anywhere. The only Arm Position objects that will ever exist, for the entire life of the program, are exactly the ones listed right there in the enum body.",
    },
    {
        "screen": '''<pre class="code"><code>arm.setAngle(target.getAngleDegrees());</code></pre>''',
        "speak": "With that upgrade in place, the earlier switch actually gets simpler. Every position already carries its own target angle, so you can just call arm dot set angle, target dot get angle degrees, no switch needed at all anymore.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 11 &middot; Enums</div>
      <h1>Iterating Every Value</h1>
      <p class="scr-sub">Every enum gets a free <code>values()</code> method.</p>
    </div>''',
        "speak": "Every enum you write automatically gets a static values method for free. It returns an array of every one of its constants, in the exact order you declared them.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (ArmPosition position : ArmPosition.values())
{
    System.out.println(position + " -&gt; " + position.getAngleDegrees() + " degrees");
}</code></pre>''',
        "speak": "That makes it trivial to loop over every possibility, here, printing each position alongside the angle it carries, with no need to maintain some separate list of all the states yourself.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Enums Can&rsquo;t Do</h2><ul>
      <li><span class="num">1</span><span>Every enum implicitly extends <code>java.lang.Enum</code></span></li>
    </ul></div>''',
        "speak": "One real limitation. Behind the scenes, every enum you write implicitly extends java dot lang dot Enum.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Enums Can&rsquo;t Do</h2><ul>
      <li><span class="num">1</span><span>Every enum implicitly extends <code>java.lang.Enum</code></span></li>
      <li><span class="num">2</span><span>Java only allows extending one parent class, so an enum can never extend anything else</span></li>
    </ul></div>''',
        "speak": "And since Java only allows extending a single parent class, an enum can never extend anything of its own on top of that. It can still implement as many interfaces as you like, that part's unaffected, it's specifically extending another class that's off the table.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Looking Ahead</div>
      <h1>Enums &rarr; State Machines</h1>
      <p class="scr-sub">Java II builds directly on this idea.</p>
    </div>''',
        "speak": "Keep this chapter in the back of your mind going forward. A fixed set of named states, plus a switch that reacts to whichever one is currently active, is exactly the foundation the State Machine pattern builds on later, in Java Two, where a subsystem tracks which named state it's in right now and transitions between them over time.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Writing the enum type prefix inside a switch &mdash; case ArmPosition dot INTAKE doesn't compile, just case INTAKE.</li>
      <li><span class="check">!</span>Forgetting the semicolon after the constant list once fields or methods follow.</li>
      <li><span class="check">!</span>Trying to new an enum constant yourself &mdash; the only instances are the ones declared in the enum body.</li>
    </ul></div>''',
        "speak": "A few common pitfalls before we wrap up. Don't write the enum's type prefix inside a switch, case Arm Position dot Intake simply doesn't compile, it's just case Intake. Don't forget the semicolon after the constant list once fields or methods follow it. And don't try to new an enum constant yourself, the only instances that will ever exist are the ones declared right there in the enum body.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An enum defines a fixed, named set of legal values &mdash; the compiler rejects anything not in that list.</li>
      <li><span class="check">&#10003;</span>Constants use SCREAMING_SNAKE_CASE; a switch over an enum omits the type prefix on each case.</li>
      <li><span class="check">&#10003;</span>An enum is a real class &mdash; it can have fields, a constructor, and methods.</li>
      <li><span class="check">&#10003;</span>values() returns every constant, in order, for looping; an enum can't extend another class, only implement interfaces.</li>
    </ul></div>''',
        "speak": "So, to recap Chapter 11. An enum defines a fixed, named set of legal values, and the compiler rejects anything outside that list. Constants use screaming snake case, and a switch over an enum leaves off the type prefix on every case. An enum is a genuine class, it can carry its own fields, a constructor, and methods, so each constant can hold its own data. Values, called with parentheses, hands you every constant in order for looping. And an enum can never extend another class, only implement interfaces. Next up, Chapter 12: exceptions and try-catch, what happens when something goes wrong while your program is running.",
    },
]
