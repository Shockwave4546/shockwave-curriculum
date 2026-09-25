BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 17 &middot; Inheritance &amp; Abstractions</div>
      <h1>Object Superclass</h1>
      <p class="scr-sub">Every class's ultimate parent &mdash; and the methods worth overriding almost everywhere.</p>
    </div>''',
        "speak": "We've said a few times now that every class ultimately inherits from Object. This lesson, we look at Object itself, and the methods it gives every class that you'll want to override almost everywhere.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Every Class's Ultimate Parent</h2><ul>
      <li><span class="num">1</span><span><strong>Object</strong>, from <strong>java.lang</strong>, is the superclass of every class in Java.</span></li>
      <li><span class="num">2</span><span>No explicit <strong>extends</strong>? You inherit from Object automatically.</span></li>
      <li><span class="num">3</span><span>Worth overriding: <strong>toString()</strong>, <strong>equals(Object other)</strong> &mdash; and, always with equals, <strong>hashCode()</strong>.</span></li>
    </ul></div>''',
        "speak": "Object, from java dot lang, is the superclass of every class in Java. Any class without an explicit extends inherits from it automatically. Three of Object's methods matter enough to override in almost every class you write: to string, equals, and, always together with equals, hash Code.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">A Preview: Overriding and @Override</h2><ul>
      <li><span class="num">1</span><span>Replacing an inherited method with a new version is called <strong>overriding</strong> (full story: Lesson 18.1).</span></li>
      <li><span class="num">2</span><span><strong>@Override</strong> tells the compiler &ldquo;this replaces a method I inherited&rdquo; &mdash; and it double-checks.</span></li>
    </ul></div>''',
        "speak": "This lesson replaces inherited methods with new versions, which is called overriding, and marks each one with at Override. Lesson 18.1 covers overriding in full. For now, at Override just tells the compiler, this method replaces one I inherited, and the compiler double-checks that it really does.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">RobotPart</span>
{
    <span class="c">// ...name field, constructor, getName(), log(), and stop() as in Lesson 17.1</span>

    <span class="k">@Override</span>
    <span class="k">public</span> <span class="t">String</span> toString() { <span class="k">return</span> name; }
}</code></pre>''',
        "speak": "Object's default to string produces something unhelpful, like Robot Part, an at sign, then a jumble of characters. That jumble is the object's hash code, written in hexadecimal. Overriding to string to describe the object's real state is good practice in nearly every class. Here's what Robot Part adds: marked with at Override, its to string just returns its name.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">RobotPart</span>
{
    <span class="k">private boolean</span> hasGamePiece;

    <span class="k">public</span> <span class="t">Intake</span>(<span class="t">String</span> name) { <span class="k">super</span>(name); }

    <span class="k">@Override</span>
    <span class="k">public</span> <span class="t">String</span> toString()
    {
        <span class="k">return super</span>.toString() + <span class="s">" (hasGamePiece="</span> + hasGamePiece + <span class="s">")"</span>;
    }
}</code></pre>''',
        "speak": "A subclass's own to string can call super dot to string, meaning the superclass's version of this method, and build on it, rather than starting from scratch. Lesson 18.2 covers super dot method in full. Intake takes whatever Robot Part's version returns, the name, and adds whether it currently has a game piece.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Default equals()</h2><ul>
      <li><span class="num">1</span><span>Inherited from Object: do two references point to the <em>exact same</em> object?</span></li>
      <li><span class="num">2</span><span>Same result as <strong>==</strong>.</span></li>
      <li><span class="num">3</span><span>Classes like <strong>String</strong> override it with something more useful.</span></li>
    </ul></div>''',
        "speak": "Now equals. The version inherited from Object tests whether two references point to the exact same object, the same result as double equals. Remember the double equals versus dot equals gotcha from lesson 6.1 and Chapter 13? That exists precisely because many classes, like String, override this default with something more useful.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Checking and Casting Object Types</h2><ul>
      <li><span class="num">1</span><span><strong>x instanceof RobotPart</strong> &mdash; true if x refers to a RobotPart or any subclass (false for null).</span></li>
      <li><span class="num">2</span><span><strong>(RobotPart) other</strong> &mdash; a cast: treat an Object reference as a RobotPart. The object doesn't change.</span></li>
      <li><span class="num">3</span><span>Wrong type? The cast throws <strong>ClassCastException</strong> &mdash; so check with instanceof first.</span></li>
    </ul></div>''',
        "speak": "Overriding equals needs two tools for working with a parameter typed Object. X instance of Robot Part is true when the object x refers to is a Robot Part or any subclass of one, and false when x is null. A cast, Robot Part in parentheses, tells the compiler to treat an Object reference as a Robot Part reference, so Robot Part's fields and methods can be used through it. It doesn't change the object at all. If the object isn't really a Robot Part, the cast throws a Class Cast Exception, which is why the instance of check comes first. Lesson 18.3 covers casting between class types in full.",
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
        "screen": '''<pre class="code"><code><span class="k">@Override</span>
<span class="k">public boolean</span> equals(<span class="t">Object</span> other)
{
    <span class="k">if</span> (<span class="k">this</span> == other) <span class="k">return true</span>;                   <span class="c">// 1. quick check: same object</span>
    <span class="k">if</span> (!(other <span class="k">instanceof</span> <span class="t">RobotPart</span>)) <span class="k">return false</span>;  <span class="c">// 2. must be the same type</span>
    <span class="t">RobotPart</span> o = (<span class="t">RobotPart</span>) other;                  <span class="c">// 3. safe to cast now</span>
    <span class="k">return this</span>.name.equals(o.name);                  <span class="c">// 4. compare the relevant fields</span>
}</code></pre>''',
        "speak": "Here's a standard recipe, added to Robot Part, that satisfies all five. Step one, a quick check: if this and other are the very same object, return true. Step two, if other isn't an instance of Robot Part, return false. Step three, now it's safe to cast other to Robot Part. And step four, compare the fields that matter, here, the name. Since Java 16, steps two and three can also be combined into one line, with a pattern: other instance of Robot Part o. When the check passes, o is already the cast variable.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>equals(Object other)</code><span class="nlabel">overrides Object's equals &mdash; what collections call</span></div>
      <div class="namerow"><code>equals(RobotPart other)</code><span class="nlabel">a different method &mdash; overloading</span></div>
    </div>''',
        "speak": "Notice the parameter type is always Object, never the class itself. Equals taking a Robot Part would be a completely different method, overloading, not overriding. It only runs when the argument's declared type is Robot Part. Library code, like Array List's contains, or a Hash Map, always calls the version that takes an Object, which would still be Object's identity check. So the bug stays silent until a collection gives a wrong answer. At Override is what catches it: on the Robot Part version, it's a compile error.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">equals() and hashCode() Go Together</div>
    <pre class="code"><code><span class="t">HashSet</span>&lt;<span class="t">RobotPart</span>&gt; parts = <span class="k">new</span> <span class="t">HashSet</span>&lt;<span class="t">RobotPart</span>&gt;();
parts.add(<span class="k">new</span> <span class="t">RobotPart</span>(<span class="s">"Front Intake"</span>));
<span class="c">// false without a hashCode() override, even though equals() says they match</span>
<span class="t">System</span>.out.println(parts.contains(<span class="k">new</span> <span class="t">RobotPart</span>(<span class="s">"Front Intake"</span>)));</code></pre>''',
        "speak": "Object has a third method tied to equals: hash Code, which returns an int that Hash Map and Hash Set use to decide where to store and look for an object. The rule: two objects that are equal must return the same hash code. Object's default gives every separate object its own value, so a class that overrides only equals breaks hash-based collections. Here, contains prints false, even though equals says the two parts match.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">@Override</span>
<span class="k">public int</span> hashCode()
{
    <span class="k">return</span> name.hashCode();  <span class="c">// same name -&gt; same hash code</span>
}</code></pre>''',
        "speak": "The fix is to override hash Code whenever you override equals, built from the same fields equals compares. Here, Robot Part just returns its name's hash code. With that added, the contains call prints true. For a class that compares several fields, Objects dot hash combines them.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Subclass equals() Trap</h2><ul>
      <li><span class="num">1</span><span>Suppose <strong>Intake</strong> overrode equals to <em>also</em> compare hasGamePiece.</span></li>
      <li><span class="num">2</span><span>genericPart.equals(intakeObj) &rarr; RobotPart's equals, compares only name.</span></li>
    </ul></div>''',
        "speak": "Overriding equals again, in a subclass of a class that's already overridden it, is genuinely hard to get right. Suppose Intake overrode equals to also compare has game piece. Then asking a generic Robot Part whether it equals an Intake calls Robot Part's equals, which compares only the name.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Subclass equals() Trap</h2><ul>
      <li><span class="num">1</span><span>Suppose <strong>Intake</strong> overrode equals to <em>also</em> compare hasGamePiece.</span></li>
      <li><span class="num">2</span><span>genericPart.equals(intakeObj) &rarr; RobotPart's equals, compares only name.</span></li>
      <li><span class="num">3</span><span>intakeObj.equals(genericPart) &rarr; Intake's equals: not an Intake, so <strong>false</strong>.</span></li>
    </ul></div>''',
        "speak": "But asking the Intake whether it equals the generic Robot Part calls Intake's equals, which checks whether other is an instance of Intake, and returns false, since a plain Robot Part isn't an Intake. The two calls disagree, and symmetry is broken. The general guideline: only one class in a hierarchy should provide a real equals override.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Writing equals(RobotPart other) instead of equals(Object other) &mdash; overloading, not overriding.</li>
      <li><span class="check">!</span>Overriding equals without hashCode &mdash; HashSet and HashMap stop finding equal objects.</li>
      <li><span class="check">!</span>Casting without an instanceof check first &mdash; ClassCastException.</li>
      <li><span class="check">!</span>Overriding equals again further down the hierarchy &mdash; tends to break symmetry.</li>
    </ul></div>''',
        "speak": "Four pitfalls. Writing equals with a Robot Part parameter, instead of Object, overloads a new method rather than overriding Object's, so collections still use Object's identity check. At Override turns that mistake into a compile error. Overriding equals without hash Code means two equal objects usually get different hash codes, so Hash Set and Hash Map quietly fail to find them. Override both, from the same fields. Casting other to your class without an instance of check first throws a Class Cast Exception, if other turns out to be some unrelated type. And overriding equals again further down a hierarchy tends to break symmetry, so let only one class own it.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Object is every class's superclass; override toString(), equals(Object other), and hashCode().</li>
      <li><span class="check">&#10003;</span>A subclass's toString() can build on super.toString().</li>
      <li><span class="check">&#10003;</span>Default equals is identity (==); a real override meets all five requirements.</li>
      <li><span class="check">&#10003;</span>Recipe: this == other, instanceof, cast (or the pattern), compare fields &mdash; parameter type Object.</li>
      <li><span class="check">&#10003;</span>Override hashCode whenever you override equals, from the same fields.</li>
      <li><span class="check">&#10003;</span>Override equals only once in a hierarchy.</li>
    </ul></div>''',
        "speak": "So, to recap. Object is the superclass of every class in Java, and to string, equals, and hash Code are its methods worth overriding almost everywhere. A subclass's to string can call super dot to string and extend it. Object's default equals is identity comparison, the same as double equals, and a correct override must be reflexive, symmetric, transitive, consistent, and never true against null. The standard recipe: check this against other, check instance of, cast, or use the pattern, then compare the relevant fields, always with a parameter of type Object. Whenever you override equals, override hash Code from the same fields. And avoid overriding equals more than once down a hierarchy. Next up, lesson 17.5: abstract classes and methods.",
    },
]
