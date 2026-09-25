BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 7 &middot; The Class Blueprint</div>
      <h1>Passing &amp; Returning Object References</h1>
      <p class="scr-sub">What actually gets copied when an object crosses a method boundary.</p>
    </div>''',
        "speak": "So far our instance variables have all been primitives. But a class's instance variable can itself be another object, and once that happens, a new question shows up: what really gets copied when you hand that object to a method, or hand it back out?",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">class</span> <span class="t">MotorConfig</span>
{
    <span class="k">private double</span> rampRate;
    <span class="k">private int</span> currentLimit;
    <span class="c">// constructor, getters, setters not shown</span>
}

<span class="k">class</span> <span class="t">Subsystem</span>
{
    <span class="k">private</span> <span class="t">String</span> name;
    <span class="k">private</span> <span class="t">MotorConfig</span> config; <span class="c">// instance variable of type MotorConfig</span>
}</code></pre>''',
        "speak": "This is called a has-a relationship. Here, a Subsystem has a Motor Config, its own tuning settings, stored as an instance variable of another class entirely. That's completely normal, objects are built out of other objects all the time.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> Subsystem(<span class="t">String</span> initName, <span class="t">MotorConfig</span> initConfig)
{
    name = initName;
    config = initConfig; <span class="c">// stores the SAME reference the caller passed in</span>
}</code></pre>''',
        "speak": "Java always uses call by value, that part never changes. But for an object, the value being copied is the reference, the pointer to the object, not the object's actual contents. So passing a Motor Config into this constructor copies the reference, and now the parameter and the original argument both point at the exact same object.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">caller's initConfig</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox active">one Motor Config object</div>
      <div class="darrow">&larr;</div>
      <div class="dbox">Subsystem's config</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Same object, viewed from two places &mdash; not two separate copies.</p>''',
        "speak": "If Motor Config is mutable, has setters, this matters a lot. Whoever else is holding onto that same Motor Config object can change it, and the Subsystem sees that change too, immediately, because it isn't a separate copy. It's the exact same object, just viewed from two different places at once.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> Subsystem(<span class="t">String</span> initName, <span class="t">MotorConfig</span> initConfig)
{
    name = initName;
    <span class="c">// Defensive copy — a brand new MotorConfig with the same values,</span>
    <span class="c">// not the same object</span>
    config = <span class="k">new</span> <span class="t">MotorConfig</span>(initConfig.getRampRate(), initConfig.getCurrentLimit());
}</code></pre>''',
        "speak": "If you don't want outside code able to reach in and change your object's data after the fact, make a defensive copy instead of storing the reference you were handed. This builds a brand new Motor Config, with the same values, but it's a different object entirely. Now, changing the original initConfig later has zero effect on the Subsystem's own copy. Notice name, a String, needed no defensive copy at all, Strings are immutable, so there's nothing to defend against there, only a mutable object reference actually needs this. And watch for a null argument, calling a method on a null initConfig throws a Null Pointer Exception, a real defensive copy has to account for that too.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="t">MotorConfig</span> getConfig()
{
    <span class="k">return</span> config; <span class="c">// returns the SAME object — caller can mutate it!</span>
}</code></pre>''',
        "speak": "The exact same rule applies in reverse for a getter. A method that returns an object returns a reference to the real object, not a copy of it. If that object is mutable, whoever calls this getter now has a live handle on the Subsystem's actual internal state.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">MotorConfig</span> c = subsystem.getConfig();
c.setRampRate(<span class="n">0.5</span>); <span class="c">// this actually changes subsystem's real config!</span></code></pre>''',
        "speak": "And here's exactly that danger, playing out. Grab the config from the getter, call a setter on it, and you've just changed the Subsystem's real, actual configuration from completely outside the class, without ever calling one of Subsystem's own methods. If that's not what you want, return a defensive copy from the getter too, same trick as before, just on the way out instead of the way in.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Chaining Method Calls</h2><ul>
      <li><span class="num">1</span><span>Calling a method directly on another method's return value is called <strong>chaining</strong>.</span></li>
      <li><span class="num">2</span><span>It only compiles if each call's declared return type actually has the next method.</span></li>
    </ul></div>''',
        "speak": "One more useful idea while we're here: chaining. Calling a method directly on another method's return value, like grabbing a subsystem's config and immediately asking it for its ramp rate in one line, is called chaining. It only compiles if the first call's declared return type actually has the next method in the chain, get config returns Motor Config, and Motor Config has a get ramp rate, so this one's valid, the compiler checks this, not the programmer.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">One public Class Per File</h2><ul>
      <li><span class="num">1</span><span>A file can hold several classes, but at most one can be <strong>public</strong>.</span></li>
      <li><span class="num">2</span><span>Put the class with <strong>main</strong> first &mdash; java File.java runs the first class, on both Java 25 and Java 17.</span></li>
    </ul></div>''',
        "speak": "One more housekeeping rule, now that we're writing multiple classes in one file. A file can hold several classes, but only one of them can be public, and with a normal compile, that public class's name has to match the file name. When a file has a main method, put that class first in the file, running it directly with java File dot java runs the first class's main, not necessarily the one matching the file name, and that's true on both Java 25 and Java 17, so this one rule covers both versions.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assuming storing a passed-in object automatically makes an independent copy &mdash; it doesn't.</li>
      <li><span class="check">!</span>Returning a mutable instance variable directly from a getter &mdash; hands out a live reference to your real internal state.</li>
      <li><span class="check">!</span>Chaining calls without checking each return type.</li>
    </ul></div>''',
        "speak": "Three pitfalls to carry forward. Don't assume storing a passed-in object automatically makes an independent copy, it doesn't, only the reference gets copied, the stored object is the exact same one the caller still holds. Don't return a mutable instance variable directly from a getter unless you genuinely mean to hand out a live reference to your real internal state. And don't chain calls without checking each return type, a dot get x dot get y chain only compiles if get x's return type actually has a get y method on it.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An object can be another object's instance variable &mdash; a has-a relationship.</li>
      <li><span class="check">&#10003;</span>Passing or returning an object copies its reference, not the object itself.</li>
      <li><span class="check">&#10003;</span>A defensive copy protects a mutable object, on the way in and/or on the way out.</li>
      <li><span class="check">&#10003;</span>Chaining method calls compiles only if each call's declared return type has the next method.</li>
      <li><span class="check">&#10003;</span>Only one public class per file; put the one with main first, for both Java 25 and Java 17.</li>
    </ul></div>''',
        "speak": "So, to recap. An object can be another object's instance variable, that's a has-a relationship. Passing or returning an object copies its reference, not the object itself, so both sides end up pointing at the same thing. A defensive copy protects a mutable object from outside changes, whether you make it on the way in, through a constructor, or on the way out, through a getter, though an immutable object like a String never needs one. Chaining method calls compiles only if each call's declared return type actually has the next method in the chain. And a file can only have one public class, so put the class with main first, which works on both Java 25 and Java 17. Next up, lesson 7.4, where we look at data that belongs to the class itself, not to any one object.",
    },
]
