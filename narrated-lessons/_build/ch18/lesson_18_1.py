BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 18 &middot; Polymorphism: Many Forms</div>
      <h1>Overriding Methods</h1>
      <p class="scr-sub">Replacing an inherited method with a subclass&rsquo;s own version.</p>
    </div>''',
        "speak": "Welcome to Chapter 18. Last chapter, a subclass inherited everything its superclass offered, unchanged. This lesson is about the moment a subclass says, thanks, but I'll do this one my own way. That's called overriding.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What Overriding Is</h2><ul>
      <li><span class="num">1</span><span>A subclass inherits its superclass&rsquo;s <strong>public</strong> methods unchanged.</span></li>
      <li><span class="num">2</span><span>It can <strong>override</strong> one &mdash; replacing the inherited version with its own.</span></li>
      <li><span class="num">3</span><span>Same <strong>signature</strong> (name and parameter list); return type the same or a subtype (<em>covariant</em>).</span></li>
    </ul></div>''',
        "speak": "A subclass inherits all of its superclass's public methods unchanged, but it can also override one, replacing the inherited version with its own. The catch: overriding requires matching the superclass method's signature, the same name and the same parameter list. And the return type must be the same as the superclass method's, or a subtype of it. That's called a covariant return type.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">RobotPart&rsquo;s stop()</h2><ul>
      <li><span class="num">1</span><span>From Lesson 17.1: <strong>public void stop() { log(&quot;stopped&quot;); }</strong></span></li>
      <li><span class="num">2</span><span>General-purpose &mdash; it only logs a message.</span></li>
    </ul></div>''',
        "speak": "Robot Part, from lesson 17.1, has a general-purpose stop method that only logs the word stopped.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">RobotPart</span>
{
    <span class="k">public</span> <span class="t">Intake</span>(<span class="t">String</span> name) { <span class="k">super</span>(name); }

    <span class="k">@Override</span>
    <span class="k">public void</span> stop()
    {
        <span class="c">// Intake's own, specific version replaces RobotPart's</span>
        log(<span class="s">"rollers off, game piece held"</span>);
    }
}</code></pre>''',
        "speak": "Intake overrides it. Same name, same empty parameter list, same void return type. Now when an Intake is told to stop, it runs its own, specific version, logging that its rollers are off and its game piece is held, instead of Robot Part's generic one.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Why Always Write @Override</h2><ul>
      <li><span class="num">1</span><span>It tells the compiler: &ldquo;I intend to override an inherited method here.&rdquo;</span></li>
      <li><span class="num">2</span><span>The compiler then checks the signature truly matches.</span></li>
      <li><span class="num">3</span><span>A typo like <strong>stopp()</strong> becomes a compile error &mdash; not a silent new method.</span></li>
    </ul></div>''',
        "speak": "That at Override line is optional, but always worth writing. It tells the compiler, I intend to override an inherited method here, and the compiler then checks that the signature really matches. Without it, a typo, say, stop spelled with two P's, would silently create a brand-new, unrelated method that overrides nothing. With at Override, that same typo becomes a compile error, instead of a bug that only shows up at runtime.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Overriding vs. Overloading</h2><ul>
      <li><span class="num">1</span><span><strong>Overriding</strong> &mdash; same signature, in a <em>subclass</em>, replacing the superclass&rsquo;s version.</span></li>
      <li><span class="num">2</span><span><strong>Overloading</strong> &mdash; same method <em>name</em>, different parameter list: in the same class, or added in a subclass.</span></li>
    </ul></div>''',
        "speak": "Overriding sounds a lot like another term, overloading, but they're entirely different things. Overriding means the same signature, in a subclass, replacing the superclass's version. Overloading means the same method name, with a different parameter list, either in the same class, or added by a subclass alongside the method it inherited.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">RobotPart</span>
{
    <span class="c">// ...name field, constructor, getName(), and stop() as in Lesson 17.1</span>
    <span class="k">public void</span> log(<span class="t">String</span> msg) { <span class="t">System</span>.out.println(<span class="s">"["</span> + name + <span class="s">"] "</span> + msg); }

    <span class="c">// overload — same name, different parameters</span>
    <span class="k">public void</span> log(<span class="t">String</span> msg, <span class="k">int</span> code) { log(msg + <span class="s">" (code "</span> + code + <span class="s">")"</span>); }
}</code></pre>''',
        "speak": "Here's overloading. Robot Part gets a second method named log. The original takes just a message. The new one takes a message and a number code, and passes a combined message to the first one. Different parameter lists, so they're two separate methods that happen to share a name. Nothing is being replaced.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Return Type Alone Doesn&rsquo;t Count</h2><ul>
      <li><span class="check">!</span>Two methods can never differ <em>only</em> in return type &mdash; not a valid overload.</li>
      <li><span class="check">!</span>Same name and parameters as an inherited method, but an <em>incompatible</em> return type (int vs. void): compile error, not an override.</li>
    </ul></div>''',
        "speak": "One rule to lock in: two methods can never differ only in return type. That alone doesn't count as a valid overload. And a subclass method with the same name and parameters as an inherited one, but an incompatible return type, like int where the superclass method returns void, isn't an override either. It's a compile error.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Inherited Getters Still Apply</div>
    <pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">RobotPart</span>
{
    <span class="c">// ...constructor and stop() as above</span>

    <span class="k">public void</span> announce()
    {
        <span class="c">// must go through the inherited getter — direct access to name isn't legal here</span>
        <span class="t">System</span>.out.println(<span class="s">"Intake online: "</span> + getName());
    }
}</code></pre>''',
        "speak": "One more thing subclasses inherit: getters and setters. Robot Part keeps its name field private, and exposes a public get Name. Since name is private, that inherited getter is the only way to reach it, even from inside the subclass itself, unless the superclass marks the field protected, from lesson 17.2. So Intake's announce method goes through get Name. Touching name directly wouldn't compile.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Preventing an Override: final</h2><ul>
      <li><span class="num">1</span><span>A <strong>final</strong> method can&rsquo;t be overridden &mdash; trying is a compile error.</span></li>
      <li><span class="num">2</span><span>A <strong>final</strong> class can&rsquo;t be extended at all &mdash; <strong>String</strong> is one.</span></li>
      <li><span class="num">3</span><span>Lesson 23.1 covers final in full.</span></li>
    </ul></div>''',
        "speak": "And one way to stop overriding. A method declared final can't be overridden. If Robot Part declared get Name as final, any subclass that tried to write its own get Name would fail to compile. A whole class can be final too, which means it can't be extended at all. String is one. Lesson 23.1 covers final in full.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Changing the parameter list and expecting an override &mdash; that&rsquo;s an overload; the original is still inherited.</li>
      <li><span class="check">!</span>Forgetting <strong>@Override</strong> &mdash; it removes the compiler&rsquo;s safety net against typos.</li>
      <li><span class="check">!</span>Changing only the return type &mdash; incompatible, so neither an override nor an overload; it won&rsquo;t compile.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Changing the parameter list, even by adding one parameter, makes it an overload, not an override, and the original method is still inherited unchanged, sitting right alongside the new one. Forgetting at Override doesn't break anything when the signature is right, but it removes the compiler's safety net against typos, so always include it. And changing only the return type, like an int stop next to the superclass's void stop, simply doesn't compile.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Overriding: same name and parameters; return type the same or a subtype (covariant).</li>
      <li><span class="check">&#10003;</span>Always use <strong>@Override</strong> &mdash; it turns a signature typo into a compile error.</li>
      <li><span class="check">&#10003;</span>Overloading: same name, different parameter list &mdash; same class or added in a subclass.</li>
      <li><span class="check">&#10003;</span>Two methods can never differ only in return type.</li>
      <li><span class="check">&#10003;</span>Inherited getters/setters are the only way to reach a superclass&rsquo;s private fields.</li>
      <li><span class="check">&#10003;</span>A <strong>final</strong> method can&rsquo;t be overridden; a <strong>final</strong> class can&rsquo;t be extended.</li>
    </ul></div>''',
        "speak": "So, to recap. Overriding replaces an inherited method with a new version in the subclass, with the same name and parameter list, and a return type that's the same or a subtype. Always use at Override, it turns a signature typo into a compile error instead of a silent new method. Overloading is different, same name, different parameter list, in the same class or added in a subclass. Two methods can never differ only in return type. Inherited getters and setters remain the only way to reach a superclass's private fields, even from inside the subclass. And a final method can't be overridden, while a final class can't be extended. Next up, lesson 18.2, the super keyword.",
    },
]
