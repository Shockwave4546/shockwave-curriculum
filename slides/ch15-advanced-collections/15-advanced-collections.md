# Advanced Collections

**Outline ref:** Ch.15 — Advanced Collections (ORACLE 13.1-4)
**Status:** existing — pulled verbatim from the deck

```html
<div class="inner">
  <span class="tag">// 02 · collections.generics()</span>
  <h2>Advanced <span class="y">Collections</span></h2>
  <div class="two">
    <ul class="bullets">
      <li><span class="bul">▸</span><span><span class="y">Set&lt;T&gt;</span>: Unordered, unique items. No duplicates allowed.</span></li>
      <li><span class="bul">▸</span><span><span class="b">Queue&lt;T&gt;</span>: First-in, first-out (FIFO). Great for command buffers.</span></li>
      <li><span class="bul">▸</span><span><span class="g">Map&lt;K, V&gt;</span>: Key-value pairs. Fast lookups (e.g., constants by name).</span></li>
    </ul>
    <div class="code">
<span class="cl"><span class="t">Map</span>&lt;<span class="t">String</span>, <span class="t">Double</span>&gt; gains = <span class="k">new</span> <span class="t">HashMap</span>&lt;&gt;();</span>
<span class="cl">gains.<span class="me">put</span>(<span class="s">"kP"</span>, <span class="n">0.1</span>);</span>
<span class="cl">gains.<span class="me">put</span>(<span class="s">"kD"</span>, <span class="n">0.01</span>);</span>
<span class="cl">&nbsp;</span>
<span class="cl"><span class="k">double</span> p = gains.<span class="me">get</span>(<span class="s">"kP"</span>);</span>
<span class="cl">&nbsp;</span>
<span class="cl"><span class="t">Queue</span>&lt;<span class="t">Command</span>&gt; q = <span class="k">new</span> <span class="t">LinkedList</span>&lt;&gt;();</span>
<span class="cl">q.<span class="me">add</span>(autonomousCommand);</span>
    </div>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-2.js`, slide 2 ("ADVANCED DATASTRUCTURES")
