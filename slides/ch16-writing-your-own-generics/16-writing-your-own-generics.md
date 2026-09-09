# Writing Your Own Generics

**Outline ref:** Ch.16 — Writing Your Own Generics (ORACLE 14.1-5)
**Status:** existing — pulled verbatim from the deck

```html
<div class="inner">
  <span class="tag">// 03 · generics.type_params()</span>
  <h2>Writing Your Own <span class="y">Generics</span></h2>
  <p class="lead">You've been <em>using</em> <span class="t">List</span>&lt;<span class="t">T</span>&gt;. Now write your own — one class, any type, full compiler protection.</p>
  <div class="two">
    <ul class="bullets">
      <li><span class="bul">▸</span><span><span class="y">&lt;T&gt;</span> is a type parameter — a placeholder filled in at use time.</span></li>
      <li><span class="bul">▸</span><span>The compiler rejects a <span class="t">String</span> where a <span class="t">Double</span> belongs — <span class="g">at build time</span>, not on the field.</span></li>
      <li><span class="bul">▸</span><span>You'll see this shape in tunable values and IO-inputs wrappers.</span></li>
    </ul>
    <div class="code">
<span class="cl"><span class="k">public class</span> <span class="t">LoggedValue</span>&lt;<span class="t">T</span>&gt; {</span>
<span class="cl">&nbsp;&nbsp;<span class="k">private</span> <span class="t">T</span> value;</span>
<span class="cl">&nbsp;</span>
<span class="cl">&nbsp;&nbsp;<span class="k">public void</span> <span class="me">set</span>(<span class="t">T</span> v) { value = v; }</span>
<span class="cl">&nbsp;&nbsp;<span class="k">public</span> <span class="t">T</span> <span class="me">get</span>() { <span class="k">return</span> value; }</span>
<span class="cl">}</span>
<span class="cl">&nbsp;</span>
<span class="cl"><span class="t">LoggedValue</span>&lt;<span class="t">Double</span>&gt; setpoint = <span class="k">new</span> <span class="t">LoggedValue</span>&lt;&gt;();</span>
<span class="cl">setpoint.<span class="me">set</span>(<span class="n">3.5</span>);&nbsp;&nbsp;<span class="c">// OK</span></span>
<span class="cl">setpoint.<span class="me">set</span>(<span class="s">"fast"</span>); <span class="c">// Compile error!</span></span>
    </div>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-2.js`, slide 2b ("GENERICS")
