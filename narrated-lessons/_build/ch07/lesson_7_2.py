BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 7 &middot; The Class Blueprint</div>
      <h1>Methods: How to Write Them</h1>
      <p class="scr-sub">Getters, setters, and toString &mdash; the methods almost every class needs.</p>
    </div>''',
        "speak": "Last lesson we sketched the shape of a class. Now let's actually fill in the methods part, starting with the same void versus non-void rule from Chapter 4, now applied to methods inside your own class.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">Intake</span>
{
    <span class="k">private double</span> currentSpeed;

    <span class="k">public void</span> spin(<span class="k">double</span> speed) <span class="c">// void — acts, doesn't return anything</span>
    {
        currentSpeed = speed;
    }
}</code></pre>''',
        "speak": "Void methods act, they don't hand anything back. Here, spin takes a speed and just updates the instance variable. Non-void methods, on the other hand, compute something and return it, which is exactly what a getter does.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public double</span> getCurrentSpeed()
{
    <span class="k">return</span> currentSpeed;
}</code></pre>''',
        "speak": "Since instance variables are private, other classes need some way to read them, and that's what a getter is, sometimes called an accessor. It's public, takes no arguments, and returns exactly one instance variable's value. By convention its name starts with get. You don't need one for every instance variable, only write a getter for the ones other code genuinely needs to read.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public void</span> setCurrentSpeed(<span class="k">double</span> newSpeed)
{
    currentSpeed = newSpeed;
}</code></pre>''',
        "speak": "A setter, sometimes called a mutator, is the write-side equivalent. It's void, its name starts with set, and it takes exactly one parameter, the new value, assigning it straight to the instance variable.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Think Before You Write a Setter</h2><ul>
      <li><span class="num">1</span><span>Not every instance variable should be freely settable from outside the class.</span></li>
      <li><span class="num">2</span><span>Sometimes the class should only change its own data through a method that enforces a rule &mdash; like spin, not a bare setter.</span></li>
    </ul></div>''',
        "speak": "Think just as hard before writing a setter as before writing a getter, though, maybe harder. Not every instance variable should be freely settable from the outside. Sometimes a class should only ever change its own data through a specific method, like spin from a moment ago, that also enforces some rule, rather than through a bare setter that lets absolutely anyone assign absolutely anything.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="t">String</span> toString()
{
    <span class="k">return</span> <span class="s">"Intake[speed="</span> + currentSpeed + <span class="s">", deployed="</span> + isDeployed + <span class="s">"]"</span>;
}</code></pre>''',
        "speak": "to string is a special method Java calls automatically, any time it needs to turn an object into text, including every single time you print an object directly, or concatenate it with plus. Without your own to string, printing an object gives you an unhelpful default, something like Intake, at sign, then a jumble of characters. Writing your own, like this one, gives every print statement genuinely useful output instead.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">caller's variable</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox">copy</div>
      <div class="darrow">&rarr;</div>
      <div class="dbox active">method parameter</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">A primitive parameter is a copy &mdash; changing it inside the method never touches the caller's original.</p>''',
        "speak": "One rule carries over unchanged from Chapter 4: call by value. A primitive parameter, like the speed passed into spin, gets a copy. Whatever the method does with that copy inside its own body never reaches back and affects the caller's original variable.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Writing a getter or setter for every instance variable reflexively.</li>
      <li><span class="check">!</span>Forgetting toString, and being surprised by ugly default output when you print an object.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Don't write a getter or setter for every single instance variable out of reflex, only add one when something outside the class genuinely needs it, a setter in particular can quietly undermine whatever rules the class's own methods were meant to enforce. And don't forget to string, if you're going to print an object for debugging or status, it's worth the two minutes it takes to write your own.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Getters return a value, no parameters; setters assign one, void return.</li>
      <li><span class="check">&#10003;</span>Only add a getter or setter when something outside the class actually needs it.</li>
      <li><span class="check">&#10003;</span>toString is called automatically whenever Java needs to convert an object to text.</li>
      <li><span class="check">&#10003;</span>Method parameters follow the same call-by-value rule as before.</li>
    </ul></div>''',
        "speak": "So, to recap. Getters return an instance variable's value with no parameters; setters assign a new value and return void. Only add either one when something outside the class genuinely needs it. to string gets called automatically whenever Java needs to turn an object into text, and writing your own is always worth it. And method parameters still follow the same call-by-value rule as always, primitives get copied. Next up, lesson 7.3, where objects themselves become the thing being passed around.",
    },
]
