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
      <li><span class="num">3</span><span>The <strong>signature</strong> must match: same name, same parameter list, same (or a subtype of the) return type.</span></li>
    </ul></div>''',
        "speak": "A subclass inherits all of its superclass's public methods unchanged, but it can also override one, replacing the inherited version with its own. The catch: overriding requires matching the superclass method's exact signature. Same name, same parameter list, and the same return type, or a subtype of it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public abstract class</span> <span class="t">Subsystem</span>
{
    <span class="k">public void</span> stop() { System.out.println(<span class="s">"Stopping subsystem"</span>); }
}</code></pre>''',
        "speak": "Here's a superclass, Subsystem, with a general-purpose stop method that just prints a message.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">Subsystem</span>
{
    <span class="k">@Override</span>
    <span class="k">public void</span> stop()
    {
        motor.set(<span class="n">0</span>); <span class="c">// Intake's own, specific version replaces Subsystem's</span>
    }
}</code></pre>''',
        "speak": "And here's Intake, which extends Subsystem and overrides stop. Same name, same empty parameter list, same void return type. Now when an Intake is told to stop, it runs its own, specific version, setting its motor to zero, instead of Subsystem's generic one.",
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
      <li><span class="num">1</span><span><strong>Overriding</strong> &mdash; exact same signature, in a <em>subclass</em>, replacing the superclass&rsquo;s version.</span></li>
      <li><span class="num">2</span><span><strong>Overloading</strong> &mdash; same method <em>name</em>, in the <em>same</em> class, different parameter list.</span></li>
    </ul></div>''',
        "speak": "Overriding sounds a lot like another term, overloading, but they're entirely different things. Overriding means the exact same signature, in a subclass, replacing the superclass's version. Overloading means the same method name, in the same class, with a different parameter list.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">public void</span> log(<span class="t">String</span> message) { System.out.println(message); }
    <span class="k">public void</span> log(<span class="t">String</span> message, <span class="t">int</span> code) { System.out.println(message + <span class="s">" ["</span> + code + <span class="s">"]"</span>); } <span class="c">// overload — different parameters</span>
}</code></pre>''',
        "speak": "Here's overloading. Two methods, both named log, both in Subsystem. One takes just a message; the other takes a message and a number code. Different parameter lists, so they're two separate methods that happen to share a name. Nothing is being replaced.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Return Type Alone Doesn&rsquo;t Count</h2><ul>
      <li><span class="check">!</span>Two methods can never differ <em>only</em> in return type.</li>
      <li><span class="check">!</span>That&rsquo;s not a valid overload, and not an override either &mdash; it&rsquo;s a compile error.</li>
    </ul></div>''',
        "speak": "One rule to lock in: two methods can never differ only in return type. That alone doesn't count as a valid overload, and it doesn't count as an override either. A mismatched return type on an otherwise identical signature is just a compile error.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Subsystem</span>
{
    <span class="k">private</span> <span class="t">String</span> name;
    <span class="k">public</span> <span class="t">String</span> getName() { <span class="k">return</span> name; }
    <span class="k">public void</span> setName(<span class="t">String</span> name) { <span class="k">this</span>.name = name; }
}</code></pre>''',
        "speak": "One more thing subclasses inherit: getters and setters. Here, Subsystem keeps its name field private, and exposes a public get Name and set Name.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span> <span class="k">extends</span> <span class="t">Subsystem</span>
{
    <span class="k">public void</span> rename(<span class="t">String</span> newName)
    {
        setName(newName); <span class="c">// must go through the inherited setter — direct access to name isn't legal here</span>
    }
}</code></pre>''',
        "speak": "Intake gets those accessor methods automatically. But since name is private to Subsystem, those inherited accessors are the only way to reach it, even from inside the subclass itself. So Intake's rename method has to go through the inherited set Name. Touching name directly wouldn't compile.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Changing the parameter list and expecting an override &mdash; that&rsquo;s an overload; the original is still inherited.</li>
      <li><span class="check">!</span>Forgetting <strong>@Override</strong> &mdash; it removes the compiler&rsquo;s safety net against typos.</li>
      <li><span class="check">!</span>Differing only by return type &mdash; neither an override nor an overload; it won&rsquo;t compile.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Changing the parameter list, even by adding one parameter, makes it an overload, not an override, and the original method is still inherited unchanged, sitting right alongside the new one. Forgetting at Override doesn't break anything when the signature is right, but it removes the compiler's safety net against typos, so always include it. And trying to differ only by return type, like an int stop next to the superclass's void stop, simply doesn't compile.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Overriding replaces an inherited method using the exact same signature.</li>
      <li><span class="check">&#10003;</span>Always use <strong>@Override</strong> &mdash; it turns a signature typo into a compile error.</li>
      <li><span class="check">&#10003;</span>Overloading: same name, same class, different parameter list.</li>
      <li><span class="check">&#10003;</span>Two methods can never differ only in return type.</li>
      <li><span class="check">&#10003;</span>Inherited getters/setters are the only way to reach a superclass&rsquo;s private fields.</li>
    </ul></div>''',
        "speak": "So, to recap. Overriding replaces an inherited method with a new version in the subclass, using the exact same signature. Always use at Override, it turns a signature typo into a compile error instead of a silent new method. Overloading is different, same name, same class, different parameter list. Two methods can never differ only in return type. And inherited getters and setters remain the only way to reach a superclass's private fields, even from inside the subclass. Next up, lesson 18.2, the super keyword.",
    },
]
