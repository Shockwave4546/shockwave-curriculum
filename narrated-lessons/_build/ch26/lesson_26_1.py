BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 26 &middot; Architecture Takeaways</div>
      <h1>Architecture Takeaways</h1>
      <p class="scr-sub">DRY, YAGNI, and SOLID &mdash; naming the principles Java II has been demonstrating all along.</p>
    </div>''',
        "speak": "Java two opened, back in chapter 14, with why design patterns matter at all. This closing chapter names the general software engineering principles that everything since, inheritance, interfaces, the I O layer pattern, factories, builders, even command-based itself, has really been demonstrating in FRC form. None of these ideas are FRC-specific, or even Java-specific. They're widely known across the whole software industry, which is exactly why they're worth naming.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">DRY: Don&rsquo;t Repeat Yourself</h2><ul>
      <li><span class="num">1</span><span>The same logic or value in more than one place &mdash; every copy has to be updated on a change</span></li>
    </ul></div>''',
        "speak": "First up, Dry: don't repeat yourself. If the same logic, or even the same literal value, shows up in more than one place, any future change has to remember to update every single copy. And it's easy to miss one.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">DRY: Don&rsquo;t Repeat Yourself</h2><ul>
      <li><span class="num">1</span><span>The same logic or value in more than one place &mdash; every copy has to be updated on a change</span></li>
      <li><span class="num">2</span><span>The fix: a common superclass (Ch.17), a shared utility method, or one Constants class (Ch.25.7)</span></li>
    </ul></div>''',
        "speak": "The fix is almost always a tool this curriculum already covered. Pull shared behavior into a common superclass, from chapter 17, or a shared utility method, or a single Constants class, from lesson 25.7, instead of copy-pasting a magic number into five different files.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// NOT DRY &mdash; the same speed value is hardcoded in three places</span>
intakeMotor.<span class="me">set</span>(<span class="n">0.8</span>);
indexerMotor.<span class="me">set</span>(<span class="n">0.8</span>);
feederMotor.<span class="me">set</span>(<span class="n">0.8</span>);

<span class="c">// DRY &mdash; one named constant, one place to change it</span>
intakeMotor.<span class="me">set</span>(IntakeConstants.kRollerSpeed);
indexerMotor.<span class="me">set</span>(IntakeConstants.kRollerSpeed);
feederMotor.<span class="me">set</span>(IntakeConstants.kRollerSpeed);</code></pre>''',
        "speak": "Here's what that looks like. On top, the version that isn't dry: the same speed value, point eight, hard-coded in three places. Change the roller speed later, and you have to find and fix all three. Underneath, the dry version: all three motors read one named constant, Intake Constants dot k Roller Speed. One place to change it.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">YAGNI: You Ain&rsquo;t Gonna Need It</h2><ul>
      <li><span class="num">1</span><span>Don&rsquo;t build flexibility or abstraction for a requirement that doesn&rsquo;t exist yet</span></li>
    </ul></div>''',
        "speak": "Next, Yagni: you ain't gonna need it. Don't build flexibility or abstraction for a requirement that doesn't exist yet.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">YAGNI: You Ain&rsquo;t Gonna Need It</h2><ul>
      <li><span class="num">1</span><span>Don&rsquo;t build flexibility or abstraction for a requirement that doesn&rsquo;t exist yet</span></li>
      <li><span class="num">2</span><span>Every layer costs complexity &mdash; a Builder (Ch.22), a generic type (Ch.16), an extra interface</span></li>
    </ul></div>''',
        "speak": "Every layer of abstraction has a real cost in complexity. A builder, from chapter 22. A generic type, from chapter 16. An extra interface. That cost is only worth paying once the actual need shows up.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">YAGNI: You Ain&rsquo;t Gonna Need It</h2><ul>
      <li><span class="num">1</span><span>Don&rsquo;t build flexibility or abstraction for a requirement that doesn&rsquo;t exist yet</span></li>
      <li><span class="num">2</span><span>Every layer costs complexity &mdash; a Builder (Ch.22), a generic type (Ch.16), an extra interface</span></li>
      <li><span class="num">3</span><span>In practice: a Builder for a 2-parameter class, or a factory (Ch.21) that only ever returns one implementation</span></li>
    </ul></div>''',
        "speak": "Yagni in practice looks like a builder for a class with just two parameters, or a factory, from chapter 21, that only ever returns one concrete implementation. That's solving a problem the code doesn't actually have yet, and paying for it with a codebase that's harder to read today, for a payoff that may never arrive.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">SOLID: Five Principles, One Letter Each</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">Not a single idea &mdash; an acronym for five distinct principles, each one already somewhere in this curriculum.</p>''',
        "speak": "Now, Solid. Solid isn't a single idea. It's an acronym for five distinct principles, each one addressing a different way a class or module's design can go wrong. All five already show up somewhere in this curriculum, even though they haven't been named until now.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">SOLID</h2><ul>
      <li><span class="num">S</span><span><strong>Single Responsibility</strong> &mdash; one, and only one, reason to change</span></li>
    </ul></div>''',
        "speak": "S is for single responsibility. A class should have one, and only one, reason to change. A subsystem that only manages one piece of hardware, from chapters 20 and 25, is a direct application of this. Its only job is that hardware, not also handling button bindings or autonomous logic.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">SOLID</h2><ul>
      <li><span class="num">S</span><span><strong>Single Responsibility</strong> &mdash; one, and only one, reason to change</span></li>
      <li><span class="num">O</span><span><strong>Open/Closed</strong> &mdash; open for extension, closed for modification</span></li>
    </ul></div>''',
        "speak": "O is for open closed. A module should be open for extension, but closed for modification. You should be able to add new behavior without editing code that already works. The I O layer pattern, from chapter 20, is a textbook example: adding a brand new Intake I O Sim implementation never requires touching Intake's own logic, since both implementations honor the same Intake I O contract.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">SOLID</h2><ul>
      <li><span class="num">S</span><span><strong>Single Responsibility</strong> &mdash; one, and only one, reason to change</span></li>
      <li><span class="num">O</span><span><strong>Open/Closed</strong> &mdash; open for extension, closed for modification</span></li>
      <li><span class="num">L</span><span><strong>Liskov Substitution</strong> &mdash; a subclass works anywhere its superclass is expected</span></li>
    </ul></div>''',
        "speak": "L is for Liskov substitution. A subclass should be usable anywhere its superclass is expected, without breaking anything. That's exactly the is a substitution test from lesson 17.1. If swapping in a subclass object somewhere a superclass is expected changes whether the code is correct, the inheritance relationship was wrong to begin with.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">SOLID</h2><ul>
      <li><span class="num">S</span><span><strong>Single Responsibility</strong> &mdash; one, and only one, reason to change</span></li>
      <li><span class="num">O</span><span><strong>Open/Closed</strong> &mdash; open for extension, closed for modification</span></li>
      <li><span class="num">L</span><span><strong>Liskov Substitution</strong> &mdash; a subclass works anywhere its superclass is expected</span></li>
      <li><span class="num">I</span><span><strong>Interface Segregation</strong> &mdash; several small interfaces, not one bloated one</span></li>
    </ul></div>''',
        "speak": "I is for interface segregation. Don't force a class to implement methods it doesn't actually need, just because they're bundled into one large interface. Several small, focused interfaces, each describing one real capability, are better than one bloated interface everything is forced to implement in full.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">SOLID</h2><ul>
      <li><span class="num">S</span><span><strong>Single Responsibility</strong> &mdash; one, and only one, reason to change</span></li>
      <li><span class="num">O</span><span><strong>Open/Closed</strong> &mdash; open for extension, closed for modification</span></li>
      <li><span class="num">L</span><span><strong>Liskov Substitution</strong> &mdash; a subclass works anywhere its superclass is expected</span></li>
      <li><span class="num">I</span><span><strong>Interface Segregation</strong> &mdash; several small interfaces, not one bloated one</span></li>
      <li><span class="num">D</span><span><strong>Dependency Inversion</strong> &mdash; depend on abstractions, not concrete implementations</span></li>
    </ul></div>''',
        "speak": "And D is for dependency inversion. Code should depend on abstractions, meaning interfaces, not on concrete implementations. Every constructor that accepts an Intake I O, instead of hard-coding new Intake I O Spark Max directly, and every static factory that returns an interface type rather than a specific class, from chapters 20 and 21, is dependency inversion in action.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Name These at All</h2><ul>
      <li><span class="num">1</span><span>Industry-wide vocabulary &mdash; not FRC- or Java-specific</span></li>
      <li><span class="num">2</span><span>&ldquo;This violates single responsibility.&rdquo; &ldquo;That&rsquo;s YAGNI.&rdquo; &mdash; a precise critique in a few words</span></li>
    </ul></div>''',
        "speak": "So why name these at all? Because none of them are FRC-specific, or even Java-specific. They're shared vocabulary across the whole software industry, the same common language benefit chapter 14 opened with. Saying this violates single responsibility, or that's Yagni, communicates a specific, well-understood critique in just a few words, to any programmer who knows these terms, not just people who've read this particular curriculum.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Applying DRY so aggressively that unrelated code gets forced together &mdash; looking similar isn&rsquo;t the same as belonging together.</li>
      <li><span class="check">!</span>Treating YAGNI as an excuse to never plan ahead &mdash; the IO-Layer Pattern earns its overhead because sim and hardware swaps are real needs.</li>
      <li><span class="check">!</span>Only remembering the &ldquo;S&rdquo; of SOLID &mdash; &ldquo;one class, one responsibility&rdquo; is just one of five principles.</li>
    </ul></div>''',
        "speak": "Three pitfalls. First, applying Dry so aggressively that unrelated code gets forced together. Two pieces of code that just happen to look similar today, for unrelated reasons, don't necessarily belong in one shared abstraction. Applying Dry too early can create awkward, tangled dependencies between things that should stay separate. Second, treating Yagni as an excuse to never plan ahead. Yagni argues against building unneeded flexibility now, not against architecture altogether. The I O layer pattern is worth its overhead in FRC precisely because simulation and hardware swapping are real, common needs, not speculative ones. And third, only remembering the S of Solid. The deck's own shorthand, one class, one responsibility, is really just single responsibility. Solid names four more distinct principles beyond that one.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>DRY: one source of truth &mdash; a constant, a shared method, a superclass &mdash; means one place to change something.</li>
      <li><span class="check">&#10003;</span>YAGNI: don&rsquo;t build abstraction for a need that doesn&rsquo;t exist yet &mdash; every layer has a real cost.</li>
      <li><span class="check">&#10003;</span>SOLID: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.</li>
      <li><span class="check">&#10003;</span>Industry-standard vocabulary &mdash; naming it precisely is the &ldquo;common language&rdquo; benefit from Ch.14.</li>
    </ul></div>''',
        "speak": "So, to recap. Dry: don't duplicate logic or values. A single source of truth, a constant, a shared method, a superclass, means one place to fix or change something. Yagni: don't build abstraction or flexibility for a need that doesn't exist yet. Every layer of indirection has a real cost, worth paying only once it's actually needed. Solid is five separate principles: single responsibility, open closed, Liskov substitution, interface segregation, and dependency inversion, each one already demonstrated somewhere in this curriculum's FRC examples. And all of it is industry-standard vocabulary, so naming it precisely is itself the common language benefit from chapter 14. Next up, chapter 27, an optional chapter on program design and abstraction.",
    },
]
