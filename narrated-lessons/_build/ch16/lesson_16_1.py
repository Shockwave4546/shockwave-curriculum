BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 16 &middot; Writing Your Own Generics</div>
      <h1>Writing Your Own Generics</h1>
      <p class="scr-sub">From using generic types to writing them.</p>
    </div>''',
        "speak": "List of String, Map of Integer and Double, ArrayList of Talon F X. Every collection since Chapter 9 has used a generic type someone else wrote. Chapter 16 is about writing your own.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 16 &middot; Writing Your Own Generics</div>
      <h1>Why Generics Exist</h1>
      <p class="scr-sub">Compile-time type safety instead of casts.</p>
    </div>''',
        "speak": "First, why generics exist at all.",
    },
    {
        "screen": '''<pre class="code"><code>List list = <span class="k">new</span> ArrayList();         <span class="c">// no generics</span>
list.add(<span class="s">"hello"</span>);
String s = (String) list.get(<span class="n">0</span>);     <span class="c">// cast required, and could fail at runtime</span></code></pre>''',
        "speak": "Before generics, a reusable container had to work with the generic Object type. That meant an explicit cast every time you got something back out, and nothing stopped the wrong type from going in in the first place. If it did, that cast could fail at runtime.",
    },
    {
        "screen": '''<pre class="code"><code>List&lt;String&gt; list = <span class="k">new</span> ArrayList&lt;String&gt;();
list.add(<span class="s">"hello"</span>);
String s = list.get(<span class="n">0</span>);              <span class="c">// no cast — the compiler already knows it's a String</span></code></pre>''',
        "speak": "With a type parameter, the compiler enforces correctness before the program ever runs, and the cast disappears entirely. The compiler already knows get returns a String.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 16 &middot; Writing Your Own Generics</div>
      <h1>Writing a Generic Class</h1>
      <p class="scr-sub">Type parameters go in angle brackets after the class name.</p>
    </div>''',
        "speak": "A generic class introduces one or more type parameters, in angle brackets, right after the class name.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> LoggedValue&lt;T&gt;
{
    <span class="k">private</span> T value;

    <span class="k">public void</span> <span class="me">set</span>(T v) { value = v; }
    <span class="k">public</span> T <span class="me">get</span>() { <span class="k">return</span> value; }
}</code></pre>''',
        "speak": "Here's a value wrapper, a natural fit for logging a tunable robot value alongside its current setpoint. Instead of committing to double or String up front, it uses a placeholder type, T. T isn't a real type. It's a type variable, a placeholder standing in for whatever concrete type gets supplied when the class is actually used.",
    },
    {
        "screen": '''<pre class="code"><code>LoggedValue&lt;Double&gt; setpoint = <span class="k">new</span> LoggedValue&lt;&gt;(); <span class="c">// the "diamond" &lt;&gt; — compiler infers Double from the left side</span>
setpoint.set(<span class="n">3.5</span>);    <span class="c">// OK</span>
setpoint.set(<span class="s">"fast"</span>); <span class="c">// compile error — a String doesn't belong in a LoggedValue&lt;Double&gt;</span></code></pre>''',
        "speak": "Using it: a Logged Value of Double. The empty angle brackets on the right are called the diamond. The compiler infers Double from the left side. Setting three point five is fine, but setting the String fast is a compile error. A String doesn't belong in a Logged Value of Double.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>T</code><span class="nlabel">Type</span></div>
      <div class="namerow"><code>E</code><span class="nlabel">Element &mdash; used throughout the collections</span></div>
      <div class="namerow"><code>K / V</code><span class="nlabel">Key / Value, as in Map&lt;K, V&gt;</span></div>
      <div class="namerow"><code>N</code><span class="nlabel">Number</span></div>
    </div>''',
        "speak": "By convention, type parameters are single uppercase letters. T for Type. E for Element, used throughout the collections you already know. K and V for Key and Value, as in Map. And N for Number. The convention exists so a type variable is instantly recognizable, and never confused with a real class name.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> Pair&lt;K, V&gt;
{
    <span class="k">private</span> K key;
    <span class="k">private</span> V value;

    <span class="k">public</span> <span class="me">Pair</span>(K key, V value)
    {
        <span class="k">this</span>.key = key;
        <span class="k">this</span>.value = value;
    }
</code></pre>''',
        "speak": "A generic class can take more than one type parameter, exactly like Map does. This Pair class takes two, K and V, stores one of each, and sets both in its constructor.",
    },
    {
        "screen": '''<pre class="code"><code>    <span class="k">public</span> K <span class="me">getKey</span>()   { <span class="k">return</span> key; }
    <span class="k">public</span> V <span class="me">getValue</span>() { <span class="k">return</span> value; }
}

Pair&lt;String, Double&gt; reading = <span class="k">new</span> Pair&lt;&gt;(<span class="s">"Front-Left Current"</span>, <span class="n">12.4</span>);</code></pre>''',
        "speak": "Its getters return K and V. And using it, a Pair of String and Double holds a label, front-left current, alongside its reading, twelve point four.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 16 &middot; Writing Your Own Generics</div>
      <h1>Generic Methods</h1>
      <p class="scr-sub">A type parameter scoped to just one method.</p>
    </div>''',
        "speak": "A single method, even inside an otherwise non-generic class, can introduce its own type parameter, written in angle brackets right before the return type. Its scope is limited to that one method.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> Util
{
    <span class="k">public static</span> &lt;K, V&gt; <span class="t">boolean</span> <span class="me">sameEntry</span>(Pair&lt;K, V&gt; p1, Pair&lt;K, V&gt; p2)
    {
        <span class="k">return</span> p1.getKey().equals(p2.getKey()) &amp;&amp; p1.getValue().equals(p2.getValue());
    }
}</code></pre>''',
        "speak": "Here, same Entry introduces K and V just before its boolean return type. It takes two Pairs of the same K and V, and returns true only if both keys and both values are equal.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Type Inference</h2><ul>
      <li><span class="num">1</span><span>The compiler almost always figures out the type on its own from how you call the method</span></li>
      <li><span class="num">2</span><span>Just call <code>Util.sameEntry(p1, p2)</code> &mdash; no need to write the type parameter yourself</span></li>
    </ul></div>''',
        "speak": "Almost always, the compiler figures out the type on its own from how you call it. That's called type inference. So you can call Util dot same Entry, passing p1 and p2 directly, without ever writing the type parameter yourself.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 16 &middot; Writing Your Own Generics</div>
      <h1>Bounded Type Parameters</h1>
      <p class="scr-sub"><code>extends</code> restricts what a type parameter can be.</p>
    </div>''',
        "speak": "Sometimes a generic type shouldn't accept just anything. A method built around numeric comparisons only makes sense for actual numbers. The extends keyword restricts a type parameter to a specific type, or any subtype of it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static</span> &lt;T <span class="k">extends</span> Number&gt; <span class="t">double</span> <span class="me">clampedValue</span>(T value, <span class="t">double</span> min, <span class="t">double</span> max)
{
    <span class="t">double</span> v = value.doubleValue(); <span class="c">// legal — Number guarantees a doubleValue() method</span>
    <span class="k">if</span> (v &lt; min) <span class="k">return</span> min;
    <span class="k">if</span> (v &gt; max) <span class="k">return</span> max;
    <span class="k">return</span> v;
}</code></pre>''',
        "speak": "Here, T extends Number means any subtype of Number, which covers Integer, Double, and the rest. Because Number guarantees a double Value method, calling it on value is legal. Then the result gets clamped between min and max.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">What the Bound Unlocks</h2><ul>
      <li><span class="num">1</span><span>Without <code>extends Number</code>, <code>value.doubleValue()</code> doesn&rsquo;t compile</span></li>
      <li><span class="num">2</span><span>The compiler would only know <code>value</code> is <em>some</em> type &mdash; with no guaranteed <code>doubleValue()</code></span></li>
    </ul></div>''',
        "speak": "Without the extends Number bound, value dot double Value wouldn't compile at all. The compiler would only know value is some type, with no guarantee it has that method to call. The bound is what unlocks calling methods that only Number, and its subtypes, actually have.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Wildcards: A Quick Preview</h2><ul>
      <li><span class="num">1</span><span><code>?</code> represents an unknown type &mdash; e.g. accepting &ldquo;a <code>List</code> of anything&rdquo;</span></li>
      <li><span class="num">2</span><span>Never used when <em>creating</em> a generic type &mdash; <code>new Box&lt;?&gt;()</code> isn&rsquo;t a thing</span></li>
    </ul></div>''',
        "speak": "Last, a quick preview of wildcards. The question mark wildcard represents an unknown type. It's mostly useful for parameters and fields where you want to accept a List of anything, without pinning down exactly what. The upper-bounded and lower-bounded variations go beyond this chapter. The short version to remember for now: the wildcard is never used when creating a generic type, only when referring to one you don't need to be specific about.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting the &lt;T&gt; on the class declaration &mdash; T has to be introduced with <code>class Box&lt;T&gt;</code> before it&rsquo;s used.</li>
      <li><span class="check">!</span>Using a primitive as a type argument &mdash; LoggedValue&lt;double&gt; doesn&rsquo;t compile; use LoggedValue&lt;Double&gt;.</li>
      <li><span class="check">!</span>Calling a bound-specific method without the bound &mdash; doubleValue() needs T declared extends Number.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Don't forget the T in angle brackets on the class declaration itself. T has to be introduced in the class header before it can be used anywhere inside the class. Don't use a primitive as a type argument. A Logged Value of lowercase double doesn't compile, since type arguments must be reference types, so use the wrapper, capital Double, same rule as ArrayList in lesson 9.2. And don't call a bound-specific method without the bound. double Value only compiles once T is declared extends Number. Without it, the compiler only knows T is some type, with no guaranteed methods beyond what every Object has.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A generic class introduces type parameters in angle brackets after its name; the type variable stands in for a real type.</li>
      <li><span class="check">&#10003;</span>Generics replace cast-from-Object with compile-time safety &mdash; a wrong type is a compile error, not a runtime surprise.</li>
      <li><span class="check">&#10003;</span>A generic method introduces its own type parameter, scoped to that method; the compiler usually infers it.</li>
    </ul></div>''',
        "speak": "So, to recap Chapter 16. A generic class introduces type parameters in angle brackets after its name, and the type variable then stands in for a real type anywhere in the class. Generic types replace the old cast-from-Object pattern with compile-time type safety. A wrong type is now a compile error, not a runtime surprise. And a generic method can introduce its own type parameter, scoped to just that method, and the compiler usually infers the type automatically.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>&lt;T extends SomeType&gt; restricts what T can be, and unlocks calling SomeType&rsquo;s own methods.</li>
      <li><span class="check">&#10003;</span>The ? wildcard refers to an unknown type &mdash; it&rsquo;s never used when constructing one.</li>
    </ul></div>''',
        "speak": "T extends some type restricts what a type parameter can be, and unlocks calling that type's own methods on its values. And the question mark wildcard represents an unknown type, for referring to a generic type generically. It's never used when constructing one. Next up, Chapter 17: inheritance and abstractions.",
        "continues": True,
    },
]
