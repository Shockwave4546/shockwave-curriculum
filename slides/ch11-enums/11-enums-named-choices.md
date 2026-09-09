# Enums: Named Choices

**Outline ref:** Ch.11 — Enums: Named Choices (ORACLE 10.1)
**Status:** existing — pulled verbatim from the deck

```html
<div>
  <span class="tag">// 08 · enums()</span>
  <h2>Enums: <span class="y">Named Choices</span></h2>
  <div class="two">
    <div>
      <p class="lead">An enum is a type with a fixed set of named values. No magic numbers, no invalid states.</p>
      <ul class="bullets">
        <li><span class="bul">▸</span><span>The compiler rejects anything not in the list.</span></li>
        <li><span class="bul">▸</span><span><span class="k">switch</span> over an enum reads like English.</span></li>
        <li><span class="bul">▸</span><span>This becomes the <strong>State Machine</strong> pattern in Java II.</span></li>
      </ul>
    </div>
    <div class="code">
      <span class="cl"><span class="k">public enum</span> <span class="t">ArmPosition</span> {</span>
      <span class="cl">&nbsp;&nbsp;STOWED, INTAKE, SCORE</span>
      <span class="cl">}</span>
      <span class="cl">&nbsp;</span>
      <span class="cl"><span class="k">switch</span> (position) {</span>
      <span class="cl">&nbsp;&nbsp;<span class="k">case</span> STOWED -&gt; arm.<span class="me">setAngle</span>(<span class="n">0</span>);</span>
      <span class="cl">&nbsp;&nbsp;<span class="k">case</span> INTAKE -&gt; arm.<span class="me">setAngle</span>(<span class="n">35</span>);</span>
      <span class="cl">&nbsp;&nbsp;<span class="k">case</span> SCORE&nbsp; -&gt; arm.<span class="me">setAngle</span>(<span class="n">110</span>);</span>
      <span class="cl">}</span>
    </div>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-1.js`, slide 9 ("ENUMS")
