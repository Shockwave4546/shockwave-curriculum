BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 14 &middot; Why Design Patterns?</div>
      <h1>Why Design Patterns?</h1>
      <p class="scr-sub">The start of Java II &mdash; how multiple classes work together.</p>
    </div>''',
        "speak": "Chapter 14 kicks off Java Two. Before we learn any specific pattern, this chapter answers one question: why does any of this matter?",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Changes Now</h2><ul>
      <li><span class="num">1</span><span>Through Ch.13: mostly one class at a time, with a few helper classes along the way</span></li>
    </ul></div>''',
        "speak": "Everything up through Chapter 13 was mostly one class at a time, with a few helper classes along the way. Variables, control flow, arrays, a class with a few methods.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Changes Now</h2><ul>
      <li><span class="num">1</span><span>Through Ch.13: mostly one class at a time, with a few helper classes along the way</span></li>
      <li><span class="num">2</span><span>From here on: how <strong>multiple</strong> classes work together as a codebase grows &mdash; organization, reuse, and change over time</span></li>
    </ul></div>''',
        "speak": "From here on, the focus shifts to how multiple classes work together as a codebase grows. The concerns become organization, reuse, and change over time, not just, does this one method work.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What a Design Pattern Is</h2><ul>
      <li><span class="num">1</span><span>A <strong>named, reusable solution</strong> to a problem that keeps showing up across different programs</span></li>
    </ul></div>''',
        "speak": "A design pattern is a named, reusable solution to a problem that keeps showing up across different programs.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What a Design Pattern Is</h2><ul>
      <li><span class="num">1</span><span>A <strong>named, reusable solution</strong> to a problem that keeps showing up across different programs</span></li>
      <li><span class="num">2</span><span>Not code to copy-paste &mdash; a <strong>shape</strong> of solution: which classes exist, and how they relate</span></li>
    </ul></div>''',
        "speak": "It's not a specific piece of code to copy and paste. It's a shape of solution, which classes exist, and how they relate, that's been proven to work well for that kind of problem.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">IO-Layer Pattern</div>
      <div class="dbox">Static Factories</div>
      <div class="dbox">Builder Pattern</div>
      <div class="dbox active">Command-Based Programming</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Real patterns actually used in FRC codebases &mdash; one per chapter, after the language-tool chapters build up to them.</p>''',
        "speak": "The chapters that follow first build the language tools patterns depend on: collections, generics, inheritance, polymorphism, and interfaces. Then, in chapter order, come the real patterns actually used in FRC codebases. The IO Layer Pattern, Static Factories, the Builder Pattern, and eventually the biggest one of all, Command-Based Programming itself.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">The Real Motivation</div>
      <h1>&ldquo;Code is read much more often than it is written.&rdquo;</h1>
      <p class="scr-sub">&mdash; Guido van Rossum (adapted)</p>
    </div>''',
        "speak": "Here's the real motivation for this whole unit, a quote adapted from Guido van Rossum: code is read much more often than it is written.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Who Reads Robot Code?</h2><ul>
      <li><span class="num">1</span><span>Every teammate who touches it</span></li>
      <li><span class="num">2</span><span>Every mentor reviewing it</span></li>
      <li><span class="num">3</span><span><strong>You</strong>, again, in six months</span></li>
    </ul></div>''',
        "speak": "A robot's codebase gets read by every teammate who touches it, every mentor reviewing it, and by you, again, six months from now. That's far more often than it gets freshly written. Patterns exist because they make code easier to read and change later, not just easier to write once.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 14 &middot; Why Design Patterns?</div>
      <h1>Why Bother</h1>
      <p class="scr-sub">Three concrete reasons.</p>
    </div>''',
        "speak": "So why bother? There are three concrete reasons.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Bother</h2><ul>
      <li><span class="num">1</span><span><strong>Scalability</strong> &mdash; one crammed <code>Robot.java</code> works for blinking an LED, not for a full robot</span></li>
    </ul></div>''',
        "speak": "First, scalability. A single Robot dot java file with everything crammed inside works fine for a blink-an-LED program. It stops working once a robot has a drive train, an intake, a shooter, vision processing, and autonomous routines all interacting. Patterns are how experienced teams keep that complexity organized, instead of it collapsing into an unmaintainable mess.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Bother</h2><ul>
      <li><span class="num">1</span><span><strong>Scalability</strong> &mdash; one crammed <code>Robot.java</code> works for blinking an LED, not for a full robot</span></li>
      <li><span class="num">2</span><span><strong>A common language</strong> &mdash; &ldquo;this is a Builder&rdquo; communicates a whole design in a few words</span></li>
    </ul></div>''',
        "speak": "Second, a common language. Telling another mentor, I'm using a Factory here, or, this is a Builder, communicates an entire shape of design in a few words. They immediately know how the pieces relate, without you walking through every class. Patterns are shared vocabulary across the whole FRC community, and the broader software world, not something invented per team.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Bother</h2><ul>
      <li><span class="num">1</span><span><strong>Scalability</strong> &mdash; one crammed <code>Robot.java</code> works for blinking an LED, not for a full robot</span></li>
      <li><span class="num">2</span><span><strong>A common language</strong> &mdash; &ldquo;this is a Builder&rdquo; communicates a whole design in a few words</span></li>
      <li><span class="num">3</span><span><strong>Testability</strong> &mdash; decoupled pieces can be swapped, simulated, or tested independently</span></li>
    </ul></div>''',
        "speak": "Third, testability. Code built around patterns tends to be more decoupled. Pieces don't reach directly into each other's internals, so they can be swapped, simulated, or tested independently. A drive train built with a clean pattern can be tested in simulation, with no real motors or robot required. One where every class directly depends on every other class often can't be tested at all without the physical hardware present.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What This Chapter Is Not</h2><ul>
      <li><span class="num">1</span><span>It doesn&rsquo;t teach a specific pattern &mdash; the chapters right after it do, one at a time</span></li>
      <li><span class="num">2</span><span>Next up: language tools (Collections, Generics, Inheritance, Polymorphism, Interfaces) &mdash; then the named patterns</span></li>
    </ul></div>''',
        "speak": "This chapter doesn't teach a specific pattern. The chapters immediately following it do that, one at a time. Its only job is to answer why any of this matters, before two kinds of chapters begin: language tools, like Advanced Collections, Generics, Inheritance, Polymorphism, and Interfaces, and the named patterns themselves.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Reaching for a pattern before there&rsquo;s a real problem it solves &mdash; forcing one onto a two-class program usually adds complexity.</li>
      <li><span class="check">!</span>Treating pattern names as a vocabulary test &mdash; the value is communicating real structure, not sounding impressive.</li>
    </ul></div>''',
        "speak": "Two common pitfalls. Don't reach for a pattern before there's a real problem it solves. Patterns exist to manage genuine complexity, and forcing one onto a two-class program, just because patterns are good practice, usually adds complexity instead of removing it. And don't treat pattern names as a vocabulary test. The value of saying, this is a Factory, is that it communicates real structure to a teammate, not that it sounds impressive.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A design pattern is a reusable <em>shape</em> of solution to a recurring design problem, not a snippet to copy.</li>
      <li><span class="check">&#10003;</span>Three reasons they matter: scalability, a common language, and testability through decoupling.</li>
      <li><span class="check">&#10003;</span>The chapters that follow each teach one specific, real pattern used in actual FRC codebases.</li>
    </ul></div>''',
        "speak": "So, to recap Chapter 14. A design pattern is a reusable shape of solution to a recurring design problem, not a snippet of code to copy. Patterns matter for three concrete reasons: keeping a growing codebase organized, which is scalability, giving the team a shared vocabulary, which is a common language, and making code easier to test in isolation, through decoupling. And the chapters that follow each teach one specific, real pattern used in actual FRC codebases. Next up, Chapter 15: Advanced Collections.",
    },
]
