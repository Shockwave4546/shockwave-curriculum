# The Builder Pattern

**Outline ref:** Ch.22 — The Builder Pattern (T5817 30.1)
**Status:** existing — pulled verbatim from the deck

```html
<div class="inner">
  <span class="tag">// 09 · builder.fluent_api()</span>
  <h2>The <span class="y">Builder</span> Pattern</h2>
  <p class="lead">Avoid "Constructor Hell" with many optional parameters.</p>
  <div class="code">
<span class="cl"><span class="t">ProfiledPIDController</span> controller = <span class="k">new</span> <span class="t">ProfiledPIDController</span>(<span class="n">1</span>, <span class="n">0</span>, <span class="n">0</span>,</span>
<span class="cl">&nbsp;&nbsp;<span class="k">new</span> <span class="t">Constraints</span>(<span class="n">2</span>, <span class="n">4</span>));</span>
<span class="cl">&nbsp;</span>
<span class="cl"><span class="c">// Versus a Fluent Builder:</span></span>
<span class="cl"><span class="t">MotorConfig</span> cfg = <span class="t">MotorConfig</span>.<span class="me">builder</span>()</span>
<span class="cl">&nbsp;&nbsp;.<span class="me">withCurrentLimit</span>(<span class="n">40</span>)</span>
<span class="cl">&nbsp;&nbsp;.<span class="me">inverted</span>(<span class="k">true</span>)</span>
<span class="cl">&nbsp;&nbsp;.<span class="me">build</span>();</span>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-2.js`, slide 8 ("BUILDERS")
