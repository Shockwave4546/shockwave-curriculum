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
      <li><span class="num">1</span><span>Codes of ethics (ACM: <em>Avoid harm</em>, <em>Respect privacy</em>) &mdash; effects on society, the economy, and culture can be beneficial, harmful, or both</span></li>
    </ul></div>''',
        "speak": "Software increasingly has direct impacts on people, not just abstract users. That's why computing professionals follow codes of ethics, like the ACM Code of Ethics, with principles such as avoid harm, and respect privacy. Programs affect society, the economy, and culture, and those effects can be beneficial, harmful, or both, sometimes in ways their authors never intended.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Code Has Real Consequences</h2><ul>
      <li><span class="num">1</span><span>Codes of ethics (ACM: <em>Avoid harm</em>, <em>Respect privacy</em>) &mdash; effects on society, the economy, and culture can be beneficial, harmful, or both</span></li>
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
      <li><span class="num">1</span><span><strong>All source code</strong> is licensed under its author&rsquo;s terms &mdash; free or not</span></li>
    </ul></div>''',
        "speak": "Programmers reuse other people's code constantly: libraries, examples, WPILib itself, and code other teams have published. And all of that code is licensed under its author's terms, whether or not it costs anything.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Legal and Licensing</h2><ul>
      <li><span class="num">1</span><span><strong>All source code</strong> is licensed under its author&rsquo;s terms &mdash; free or not</span></li>
      <li><span class="num">2</span><span><strong>Open source</strong> &mdash; free to use <em>under its license</em> (credit, notices, sometimes share-alike)</span></li>
      <li><span class="num">3</span><span><strong>Not open source</strong> &mdash; needs the owner&rsquo;s permission, often payment</span></li>
    </ul></div>''',
        "speak": "Open source code is free to use, but only under its license, and licenses differ. Many require you to keep the author's credit and license notice, and some require you to share your own changes under the same license. Code that isn't published as open source generally needs the owner's permission, and often payment, before you can use it.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Legal and Licensing</h2><ul>
      <li><span class="num">1</span><span><strong>All source code</strong> is licensed under its author&rsquo;s terms &mdash; free or not</span></li>
      <li><span class="num">2</span><span><strong>Open source</strong> &mdash; free to use <em>under its license</em> (credit, notices, sometimes share-alike)</span></li>
      <li><span class="num">3</span><span><strong>Not open source</strong> &mdash; needs the owner&rsquo;s permission, often payment</span></li>
      <li><span class="num">4</span><span>Follow the terms &mdash; for <strong>legal</strong> and <strong>ethical</strong> reasons</span></li>
    </ul></div>''',
        "speak": "Following those terms matters for two reasons. It's a legal obligation, since licenses are enforceable. And it's an ethical one: respecting the work, and the wishes, of the people who wrote the code. That's also why every lesson in this curriculum credits its sources. And code produced by AI tools can reproduce licensed code too, so where code came from still matters.",
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
      <li><span class="check">!</span>Reusing code without checking its license &mdash; open source included.</li>
      <li><span class="check">!</span>Assuming design choices are ethically neutral &mdash; defaults, broad permissions, and untested edge cases have consequences.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Treating it compiled as the same thing as it's reliable. Compiling successfully only means the code is syntactically valid. Reliability takes actually testing its behavior, under realistic, and edge case, conditions. Reusing code without checking its license. Every piece of code, open source included, comes with license terms. Easy to copy and paste doesn't mean free of obligations. And assuming design choices are ethically neutral. A default behavior, a permission granted too broadly, or an untested edge case can carry real consequences for whoever the software ultimately affects.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Reliability means performing correctly under real, tested conditions &mdash; not just &ldquo;it worked once.&rdquo;</li>
      <li><span class="check">&#10003;</span>Software&rsquo;s impact can be beneficial or harmful &mdash; especially concrete when code controls physical hardware.</li>
      <li><span class="check">&#10003;</span>All source code is licensed &mdash; follow its terms for legal and ethical reasons.</li>
      <li><span class="check">&#10003;</span>Increasingly autonomous software, AI included, raises real ethical questions worth being aware of.</li>
    </ul></div>''',
        "speak": "So, to recap. System reliability means performing correctly under real, tested conditions, not just it worked once. Software's real-world impact can be beneficial or harmful, often in ways beyond its original intended use, and that's especially concrete in FRC, where code directly controls physical hardware. All source code is licensed under its respective terms. Open source is free to use only under its license, other code needs permission, and following those terms is both a legal and an ethical obligation. And increasingly autonomous software, AI included, raises genuine ethical questions worth being aware of, even without a clean technical answer. Next up, chapter 28, algorithms, starting with lesson 28.1, searching.",
    },
]
