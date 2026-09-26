BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 27 &middot; Program Design &amp; Abstraction</div>
      <h1>Abstraction and Program Design</h1>
      <p class="scr-sub">Deciding which classes a program needs &mdash; before writing any of them.</p>
    </div>''',
        "speak": "This is an optional chapter. It's the general, from-scratch program design thinking that applies to any object-oriented code, not just FRC robot code. It's informational, not a required gateway, since real FRC teams build on top of WPILib's already-imposed architecture, command-based, from chapter 25, regardless.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Designing Before Writing: Find the Nouns</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">&ldquo;The robot has a <span class="hl">drivetrain</span>, an <span class="hl">intake</span> that picks up game pieces, and a <span class="hl">shooter</span> that scores them.&rdquo;</p>''',
        "speak": "Before writing a single class, it helps to first decide which classes a program actually needs, and what data and behavior each one owns. A reliable trick: read the problem description, and look for the nouns. They're usually your classes. Take this one: the robot has a drive train, an intake that picks up game pieces, and a shooter that scores them.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Designing Before Writing: Find the Nouns</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">&ldquo;The robot has a <span class="hl">drivetrain</span>, an <span class="hl">intake</span> that picks up game pieces, and a <span class="hl">shooter</span> that scores them.&rdquo;</p>
    <div style="margin-top:18px;"><div class="scr-diagram">
      <div class="dbox active">Drivetrain</div>
      <div class="dbox active">Intake</div>
      <div class="dbox active">Shooter</div>
    </div></div>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;max-width:52ch;margin:14px auto 0;">&rarr; the RobotPart subclasses (Ch.17/20) a real codebase ends up with</p>''',
        "speak": "Those three nouns, drive train, intake, and shooter, are exactly the RobotPart subclasses, from chapters 17 and 20, that a real codebase would end up with.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">UML Class Diagrams</h2><ul>
      <li><span class="num">1</span><span>A simple box-based sketch of a class &mdash; its attributes (instance variables) and its methods</span></li>
    </ul></div>''',
        "speak": "Once you know your classes, a U M L class diagram is a simple way to sketch one out: a box listing the class's attributes, meaning its instance variables, and its methods.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">UML Class Diagrams</div>
    <div class="scr-naming">
      <div class="namerow"><code>-</code><span class="nlabel">marks a private member</span></div>
      <div class="namerow"><code>+</code><span class="nlabel">marks a public member</span></div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;max-width:52ch;margin:14px auto 0;">Informal is fine &mdash; a whiteboard sketch before writing code is often enough.</p>''',
        "speak": "A minus sign marks a private member, and a plus sign marks a public one. These diagrams don't need to be formal. A quick whiteboard sketch before writing code is often enough to catch a design problem before it's baked into actual Java.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Data Abstraction</h2><ul>
      <li><span class="num">1</span><span>Separates what data represents from how it&rsquo;s stored &mdash; use an Intake without knowing its internals</span></li>
    </ul></div>''',
        "speak": "Next, data abstraction. It separates a data type's abstract properties from the concrete details of how it's represented. You can use an Intake object without knowing exactly how its internal state is stored.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Data Abstraction</h2><ul>
      <li><span class="num">1</span><span>Separates what data represents from how it&rsquo;s stored &mdash; use an Intake without knowing its internals</span></li>
      <li><span class="num">2</span><span><strong>Instance variables</strong> &mdash; unique per object, like each Intake&rsquo;s own hasGamePiece flag</span></li>
      <li><span class="num">3</span><span><strong>Class/static variables</strong> &mdash; shared by every instance, like a count of Intake objects</span></li>
    </ul></div>''',
        "speak": "Chapter 7 already introduced the vocabulary this curriculum uses for this. Instance variables are unique per object, like each Intake's own has game piece flag. And class, or static, variables are shared across every instance, like a running count of how many Intake objects exist.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Procedural Abstraction</div>
    <div class="scr-naming">
      <div class="namerow"><code>intake.retract()</code><span class="nlabel">use it by knowing <em>what</em> it does, not <em>how</em></span></div>
    </div>''',
        "speak": "Procedural abstraction does the same thing for a process. It gives a process a name, so it can be used by knowing what it does, without needing to know how. Calling intake dot retract doesn't require knowing exactly how the retraction is implemented underneath. That's exactly the value of a well-named method, from chapters 4 and 7.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Real Benefits</h2><ul>
      <li><span class="num">1</span><span><strong>Organization</strong> &mdash; smaller, named methods keep any one piece manageable</span></li>
    </ul></div>''',
        "speak": "Three real benefits fall out of it. First, organization. Breaking a large behavior into smaller, named methods keeps any one piece of code manageable.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Real Benefits</h2><ul>
      <li><span class="num">1</span><span><strong>Organization</strong> &mdash; smaller, named methods keep any one piece manageable</span></li>
      <li><span class="num">2</span><span><strong>Reuse</strong> &mdash; written once, called from many places (Ch.26&rsquo;s DRY, in disguise)</span></li>
    </ul></div>''',
        "speak": "Second, reuse. A method written once can be called from many places, instead of duplicating the same logic. That's chapter 26's Dry principle, in disguise.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Real Benefits</h2><ul>
      <li><span class="num">1</span><span><strong>Organization</strong> &mdash; smaller, named methods keep any one piece manageable</span></li>
      <li><span class="num">2</span><span><strong>Reuse</strong> &mdash; written once, called from many places (Ch.26&rsquo;s DRY, in disguise)</span></li>
      <li><span class="num">3</span><span><strong>Maintainability</strong> &mdash; easier to read, debug, and reason about</span></li>
    </ul></div>''',
        "speak": "And third, maintainability. Smaller, well-named methods are far easier to read, debug, and reason about than one sprawling method doing everything.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Change the Inside, Not the Outside</h2><ul>
      <li><span class="num">1</span><span>Internals can be rewritten freely &mdash; as long as the signature and observable behavior stay the same</span></li>
      <li><span class="num">2</span><span>Parameters let one method generalize across a whole range of inputs</span></li>
    </ul></div>''',
        "speak": "Procedural abstraction also means a method's internal implementation can change freely, made faster, refactored, rewritten, without breaking any code that calls it, as long as the method's signature and its observable behavior stay the same. And adding parameters extends this even further, letting one method generalize across a whole range of inputs, instead of needing a separate, near-duplicate method for each specific case.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Applying This to an FRC Robot</div>
    <div class="scr-diagram">
      <div class="dbox active">Drivetrain</div>
      <div class="dbox active">Intake</div>
      <div class="dbox active">Shooter</div>
      <div class="dbox active">Climber</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;max-width:52ch;margin:14px auto 0;">Sketch the nouns, and what each one needs, before writing Robot.java.</p>''',
        "speak": "Before writing Robot dot java, sketch out the nouns for an actual robot: drive train, intake, shooter, climber, and roughly what data and behavior each one needs. That's the same thinking that led to the RobotPart abstraction in chapters 17 and 20 in the first place. Those weren't arbitrary class boundaries. They came from identifying the real, distinct nouns in a robot's actual hardware.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Skipping design entirely &mdash; even a rough five-minute sketch catches structural mistakes cheaply.</li>
      <li><span class="check">!</span>Confusing data abstraction with encapsulation &mdash; encapsulation (Ch.7/23) is the mechanism that enforces it.</li>
      <li><span class="check">!</span>Assuming procedural abstraction only matters for long methods &mdash; naming even a two-line calculation documents intent.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Skipping design entirely, and writing code directly. Even a rough five-minute sketch of what classes you need, and what each one owns, catches structural mistakes far more cheaply than discovering them after a class already has fifteen unrelated responsibilities. Confusing data abstraction with encapsulation. They're related, but distinct. Data abstraction is about naming data without exposing its representation. Encapsulation, from chapters 7 and 23, is the specific mechanism, private fields and public accessors, that enforces it. And assuming procedural abstraction only matters for long methods. Even a short method benefits. Naming a two-line calculation calculate shooter RPM, of distance, documents intent in a way the raw calculation alone never does.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Object-oriented design starts with the nouns in a problem description &mdash; they&rsquo;re usually your classes.</li>
      <li><span class="check">&#10003;</span>A UML class diagram is a simple, informal sketch of a class&rsquo;s attributes and methods.</li>
      <li><span class="check">&#10003;</span>Data abstraction: what data represents, not how it&rsquo;s stored. Procedural abstraction: what a method does, not how.</li>
      <li><span class="check">&#10003;</span>The payoff: organization, reuse, and freedom to change a method&rsquo;s internals without breaking callers.</li>
    </ul></div>''',
        "speak": "So, to recap. Object-oriented design starts by identifying the nouns in a problem description, they're usually the classes a program needs. A U M L class diagram is a simple, informal way to sketch a class's attributes and methods before writing real code. Data abstraction separates what data represents from how it's stored, and procedural abstraction separates what a method does from how it's implemented. And procedural abstraction's real payoff is organization, code reuse, and the freedom to change a method's internals without breaking its callers. Next up, lesson 27.2, the impact of program design.",
    },
]
