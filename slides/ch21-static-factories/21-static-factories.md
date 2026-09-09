# Static Factories

**Outline ref:** Ch.21 — Static Factories (T5817 30.2)
**Status:** existing — pulled verbatim from the deck

```html
<div class="inner">
  <span class="tag">// 08 · factory.static_methods()</span>
  <h2>Static <span class="y">Factories</span></h2>
  <p class="lead">Why use <span class="t">Subsystem</span>.<span class="me">create</span>() instead of <span class="k">new</span> <span class="t">Subsystem</span>()?</p>
  <ul class="bullets">
    <li><span class="bul">▸</span><span><span class="y">Descriptive Names</span>: "fromId(5)" is clearer than just passing 5 to a constructor.</span></li>
    <li><span class="bul">▸</span><span><span class="b">Caching</span>: You can return an existing instance instead of creating a new one.</span></li>
  </ul>
  <div class="code">
<span class="cl"><span class="k">public static</span> <span class="t">Command</span> <span class="me">printMessage</span>(<span class="t">String</span> msg) {</span>
<span class="cl">&nbsp;&nbsp;<span class="k">return new</span> <span class="t">InstantCommand</span>(() -&gt; <span class="t">System</span>.out.<span class="me">println</span>(msg));</span>
<span class="cl">}</span>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-2.js`, slide 7 ("FACTORIES")
