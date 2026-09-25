BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 17 &middot; Inheritance &amp; Abstractions</div>
      <h1>Object Superclass</h1>
      <p class="scr-sub">Every class's ultimate parent &mdash; and the two methods worth overriding almost everywhere.</p>
    </div>''',
        "speak": "We've said a few times now that every class ultimately inherits from Object. This lesson, we look at Object itself, and the two methods it gives every class that you'll want to override almost everywhere.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Every Class's Ultimate Parent</h2><ul>
      <li><span class="num">1</span><span><strong>Object</strong>, from <strong>java.lang</strong>, is the superclass of every class in Java.</span></li>
      <li><span class="num">2</span><span>No explicit <strong>extends</strong>? You inherit from Object automatically.</span></li>
      <li><span class="num">3</span><span>Two methods worth overriding: <strong>toString()</strong> and <strong>equals(Object other)</strong>.</span></li>
    </ul></div>''',
        "speak": "Object, from java dot lang, is the superclass of every class in Java. Any class without an explicit extends inherits from it automatically. Two of Object's methods matter enough to override in almost every class you write: to string, and equals.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">private</span> <span class="t">String</span> name;

    <span class="k">public</span> Subsystem(<span class="t">String</span> name) { this.name = name; }

    @Override
    <span class="k">public</span> <span class="t">String</span> toString() { <span class="k">return</span> name; }
}</code></pre>''',
        "speak": "Object's default to string produces something unhelpful, like Subsystem, at sign, then a jumble of characters, the class name plus a hash derived from its memory address. Overriding it to describe the object's real state is good practice in nearly every class. Here, marked with at Override, Subsystem's to string just returns its name.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">Subsystem</span>
{
    <span class="k">private boolean</span> hasGamePiece;

    <span class="k">public</span> Intake(<span class="t">String</span> name) { super(name); }

    @Override
    <span class="k">public</span> <span class="t">String</span> toString()
    {
        <span class="k">return</span> super.toString() + <span class="s">" (hasGamePiece="</span> + hasGamePiece + <span class="s">")"</span>;
    }
}</code></pre>''',
        "speak": "A subclass's own to string can call super dot to string, and build on it, rather than starting from scratch. Intake takes whatever Subsystem's version returns, the name, and adds whether it currently has a game piece.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Default equals()</h2><ul>
      <li><span class="num">1</span><span>Inherited from Object: do two references point to the <em>exact same</em> object?</span></li>
      <li><span class="num">2</span><span>Same result as <strong>==</strong>.</span></li>
      <li><span class="num">3</span><span>Classes like <strong>String</strong> override it with something more useful.</span></li>
    </ul></div>''',
        "speak": "Now equals. The version inherited from Object tests whether two references point to the exact same object, the same result as double equals. Remember Chapter 13's double equals versus dot equals gotcha? That exists precisely because many classes, like String, override this default with something more useful.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Five Requirements for equals()</h2><ul>
      <li><span class="num">1</span><span><strong>Reflexive</strong> &mdash; o.equals(o) is always true</span></li>
      <li><span class="num">2</span><span><strong>Symmetric</strong> &mdash; a.equals(b) matches b.equals(a)</span></li>
      <li><span class="num">3</span><span><strong>Transitive</strong> &mdash; a equals b and b equals c implies a equals c</span></li>
      <li><span class="num">4</span><span><strong>Consistent</strong> &mdash; repeated calls agree, if nothing changed</span></li>
      <li><span class="num">5</span><span><strong>Never equal to null</strong></span></li>
    </ul></div>''',
        "speak": "Overriding equals is more involved than to string, because it has to satisfy five formal requirements to stay safe to use anywhere. Reflexive: any object equals itself. Symmetric: a equals b gives the same answer as b equals a. Transitive: if a equals b, and b equals c, then a equals c. Consistent: repeated calls give the same answer, if nothing changed. And never equal to null.",
    },
    {
        "screen": '''<pre class="code"><code>@Override
<span class="k">public boolean</span> equals(<span class="t">Object</span> other)
{
    <span class="k">if</span> (this == other) <span class="k">return true</span>;               <span class="c">// 1. quick check: same object</span>
    <span class="k">if</span> (!(other <span class="k">instanceof</span> <span class="t">Subsystem</span>)) <span class="k">return false</span>; <span class="c">// 2. must be the same type</span>
    <span class="t">Subsystem</span> o = (<span class="t">Subsystem</span>) other;               <span class="c">// 3. safe to cast now</span>
    <span class="k">return</span> this.name.equals(o.name);               <span class="c">// 4. compare the relevant fields</span>
}</code></pre>''',
        "speak": "Here's a standard recipe that satisfies all five. Step one, a quick check: if this and other are the very same object, return true. Step two, if other isn't an instance of Subsystem, return false. Step three, now it's safe to cast other to Subsystem. And step four, compare the fields that matter, here, the name.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>equals(Object other)</code><span class="nlabel">overrides Object's equals</span></div>
      <div class="namerow"><code>equals(Subsystem other)</code><span class="nlabel">a different method &mdash; overloading</span></div>
    </div>''',
        "speak": "Notice the parameter type is always Object, never the class itself. Equals taking a Subsystem would be a completely different method, overloading, not overriding. It's not the one Object actually declares.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Subclass equals() Trap</h2><ul>
      <li><span class="num">1</span><span>Suppose <strong>Intake</strong> overrode equals to <em>also</em> compare hasGamePiece.</span></li>
      <li><span class="num">2</span><span>genericSubsystem.equals(intakeObj) &rarr; Subsystem's equals, compares only name.</span></li>
    </ul></div>''',
        "speak": "Overriding equals again, in a subclass of a class that's already overridden it, is genuinely hard to get right. Suppose Intake overrode equals to also compare has game piece. Then asking a generic Subsystem whether it equals an Intake calls Subsystem's equals, which compares only the name.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Subclass equals() Trap</h2><ul>
      <li><span class="num">1</span><span>Suppose <strong>Intake</strong> overrode equals to <em>also</em> compare hasGamePiece.</span></li>
      <li><span class="num">2</span><span>genericSubsystem.equals(intakeObj) &rarr; Subsystem's equals, compares only name.</span></li>
      <li><span class="num">3</span><span>intakeObj.equals(genericSubsystem) &rarr; Intake's equals: not an Intake, so <strong>false</strong>.</span></li>
    </ul></div>''',
        "speak": "But asking the Intake whether it equals the generic Subsystem calls Intake's equals, which checks whether other is an instance of Intake, and returns false, since a plain Subsystem isn't an Intake. The two calls disagree, and symmetry is broken. The general guideline: only one class in a hierarchy should provide a real equals override.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Writing equals(Subsystem other) instead of equals(Object other) &mdash; overloading, not overriding.</li>
      <li><span class="check">!</span>Casting without an instanceof check first &mdash; ClassCastException.</li>
      <li><span class="check">!</span>Overriding equals again further down the hierarchy &mdash; tends to break symmetry.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Writing equals with a Subsystem parameter, instead of Object, overloads a new method rather than overriding Object's, so code calling equals on a Subsystem variable still uses Object's original version. Casting other to your class without an instance of check first throws a Class Cast Exception, if other turns out to be some unrelated type. And overriding equals again further down a hierarchy tends to break symmetry, so let only one class own it.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Object is every class's superclass; override toString() and equals(Object other).</li>
      <li><span class="check">&#10003;</span>A subclass's toString() can build on super.toString().</li>
      <li><span class="check">&#10003;</span>Default equals is identity (==); a real override meets all five requirements.</li>
      <li><span class="check">&#10003;</span>Recipe: this == other, instanceof, cast, compare fields &mdash; parameter type Object.</li>
      <li><span class="check">&#10003;</span>Override equals only once in a hierarchy.</li>
    </ul></div>''',
        "speak": "So, to recap. Object is the superclass of every class in Java, and to string and equals are its two methods worth overriding almost everywhere. A subclass's to string can call super dot to string and extend it. Object's default equals is identity comparison, the same as double equals, and a correct override must be reflexive, symmetric, transitive, consistent, and never true against null. The standard recipe: check this against other, check instance of, cast, then compare the relevant fields, always with a parameter of type Object. And avoid overriding equals more than once down a hierarchy. That wraps up Chapter 17. Next up, Chapter 18: polymorphism.",
    },
]
