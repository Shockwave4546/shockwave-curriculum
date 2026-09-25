BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 27 &middot; Program Design &amp; Abstraction</div>
      <h1>Impact of Program Design</h1>
      <p class="scr-sub">Reliability, real-world consequences, licensing, and ethics.</p>
    </div>''',
        "speak": "Like lesson 27.1, this one's optional. It's general software engineering context, rather than FRC-specific mechanics, covering four ideas: reliability, real-world consequences, licensing, and ethics.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">System Reliability</h2><ul>
      <li><span class="num">1</span><span>Performs its intended task correctly, under stated conditions, without failure</span></li>
    </ul></div>''',
        "speak": "System reliability means a program performs its intended task correctly, under stated conditions, without failure.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">System Reliability</h2><ul>
      <li><span class="num">1</span><span>Performs its intended task correctly, under stated conditions, without failure</span></li>
      <li><span class="num">2</span><span>On a robot: code that only works &ldquo;most of the time&rdquo; costs matches</span></li>
    </ul></div>''',
        "speak": "On a competition robot, reliability isn't abstract. Code that only works most of the time is code that costs matches.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">System Reliability</h2><ul>
      <li><span class="num">1</span><span>Performs its intended task correctly, under stated conditions, without failure</span></li>
      <li><span class="num">2</span><span>On a robot: code that only works &ldquo;most of the time&rdquo; costs matches</span></li>
      <li><span class="num">3</span><span>Test real conditions &mdash; a dead battery, a jammed mechanism, a disconnected sensor</span></li>
    </ul></div>''',
        "speak": "What catches failures before they happen on the field, rather than during a match, is testing under a real range of conditions: a dead battery, a jammed mechanism, a sensor that's disconnected.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Code Has Real Consequences</h2><ul>
      <li><span class="num">1</span><span>Effects can be beneficial, harmful, or both &mdash; sometimes in ways the authors never intended</span></li>
    </ul></div>''',
        "speak": "Software increasingly has direct impacts on people, not just abstract users. And a program's effects can be beneficial, harmful, or both, sometimes in ways its authors never intended.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Code Has Real Consequences</h2><ul>
      <li><span class="num">1</span><span>Effects can be beneficial, harmful, or both &mdash; sometimes in ways the authors never intended</span></li>
      <li><span class="num">2</span><span>A motor-output bug isn&rsquo;t a wrong number on a screen &mdash; it&rsquo;s a real mechanism moving unexpectedly, or unsafely</span></li>
    </ul></div>''',
        "speak": "An FRC robot is a literal example of code controlling a real, physical machine. A bug in motor output code isn't just a wrong number on a screen. It's a real mechanism moving in an unexpected, or unsafe, way.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">WPILib&rsquo;s Safety Defaults</div>
    <div class="scr-naming">
      <div class="namerow"><code>motors disabled</code><span class="nlabel">unless explicitly commanded</span></div>
      <div class="namerow"><code>watchdog</code><span class="nlabel">stops the robot if code stops responding</span></div>
    </div>''',
        "speak": "That's exactly why WPILib's safety defaults exist. Motors stay disabled unless they're explicitly commanded, and a watchdog stops the robot if the code stops responding. Those are real design decisions, made because the code's failures have real, physical consequences.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Legal and Licensing</h2><ul>
      <li><span class="num">1</span><span>Attribute what you build on &mdash; every lesson&rsquo;s &ldquo;Derived from&rdquo; line exists for this</span></li>
    </ul></div>''',
        "speak": "Reusing other people's code is extremely common. And properly attributing what you build on matters, whether that's an open-source library, WPILib itself, or another team's published code. That's the whole reason every lesson in this curriculum carries a derived from line.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Legal and Licensing</h2><ul>
      <li><span class="num">1</span><span>Attribute what you build on &mdash; every lesson&rsquo;s &ldquo;Derived from&rdquo; line exists for this</span></li>
      <li><span class="num">2</span><span><strong>Open source</strong> &mdash; free to use, under its license terms</span></li>
      <li><span class="num">3</span><span><strong>Not open source</strong> &mdash; generally needs explicit permission, sometimes payment</span></li>
    </ul></div>''',
        "speak": "Open source code is free to use, often under specific license terms that are worth actually reading. Code that isn't published as open source generally requires explicit permission, sometimes payment, before it can legally be used in another program.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Legal and Licensing</h2><ul>
      <li><span class="num">1</span><span>Attribute what you build on &mdash; every lesson&rsquo;s &ldquo;Derived from&rdquo; line exists for this</span></li>
      <li><span class="num">2</span><span><strong>Open source</strong> &mdash; free to use, under its license terms</span></li>
      <li><span class="num">3</span><span><strong>Not open source</strong> &mdash; generally needs explicit permission, sometimes payment</span></li>
      <li><span class="num">4</span><span>In FRC: vendor libraries carry their own terms; most teams publish their code openly</span></li>
    </ul></div>''',
        "speak": "This matters directly in FRC. Vendor libraries, like motor controller and sensor libraries, each carry their own license terms. And most FRC teams publish their own robot code openly, for other teams to learn from. This curriculum is part of that same culture. The whole project builds on Mechanical Advantage's own published lesson deck.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Ethical Questions in AI and Automation</h2><ul>
      <li><span class="num">1</span><span>Autonomous decisions raise hard questions &mdash; who&rsquo;s responsible for a split-second call?</span></li>
    </ul></div>''',
        "speak": "Finally, ethics. As software takes on more autonomous decision-making, with self-driving cars the most commonly cited example, genuinely hard ethical questions come up. Who's responsible when an autonomous system has to make a split-second decision with real consequences?",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Ethical Questions in AI and Automation</h2><ul>
      <li><span class="num">1</span><span>Autonomous decisions raise hard questions &mdash; who&rsquo;s responsible for a split-second call?</span></li>
      <li><span class="num">2</span><span>No clean technical answer &mdash; but worth being aware of, AI-assisted coding included</span></li>
    </ul></div>''',
        "speak": "These aren't questions with a clean technical answer. But they're worth being aware of, as automation, including AI-assisted coding itself, becomes a bigger part of how software gets built.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Treating &ldquo;it compiled&rdquo; as &ldquo;it&rsquo;s reliable&rdquo; &mdash; compiling only proves the syntax is valid.</li>
      <li><span class="check">!</span>Reusing code without checking its license or attribution requirements.</li>
      <li><span class="check">!</span>Assuming design choices are ethically neutral &mdash; defaults, broad permissions, and untested edge cases have consequences.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Treating it compiled as the same thing as it's reliable. Compiling successfully only means the code is syntactically valid. Reliability takes actually testing its behavior, under realistic, and edge case, conditions. Reusing code without checking its license, or its attribution requirements. Even code that's easy to copy and paste can carry real legal obligations. And assuming design choices are ethically neutral. A default behavior, a permission granted too broadly, or an untested edge case can carry real consequences for whoever the software ultimately affects.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Reliability means performing correctly under real, tested conditions &mdash; not just &ldquo;it worked once.&rdquo;</li>
      <li><span class="check">&#10003;</span>Software&rsquo;s impact can be beneficial or harmful &mdash; especially concrete when code controls physical hardware.</li>
      <li><span class="check">&#10003;</span>Reusing code carries legal obligations &mdash; open source under its license, other code with explicit permission.</li>
      <li><span class="check">&#10003;</span>Increasingly autonomous software, AI included, raises real ethical questions worth being aware of.</li>
    </ul></div>''',
        "speak": "So, to recap. System reliability means performing correctly under real, tested conditions, not just it worked once. Software's real-world impact can be beneficial or harmful, often in ways beyond its original intended use, and that's especially concrete in FRC, where code directly controls physical hardware. Reusing code carries real legal and licensing obligations: open source code is free to use under its license terms, and other code generally requires explicit permission. And increasingly autonomous software, AI included, raises genuine ethical questions worth being aware of, even without a clean technical answer. Next up, chapter 28, algorithms, starting with lesson 28.1, searching.",
    },
]
