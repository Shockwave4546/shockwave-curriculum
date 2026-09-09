# Interfaces as Contracts

**Outline ref:** Ch.19 — Interfaces as Contracts (ORACLE 15.1-6)
**Status:** existing — pulled verbatim from the deck

```html
<div class="inner">
  <span class="tag">// 06 · interfaces.contracts()</span>
  <h2>Interfaces as <span class="y">Contracts</span></h2>
  <p class="lead">An interface defines <strong>what</strong> an object can do, without caring <strong>how</strong> it does it.</p>
  <div class="code">
<span class="cl"><span class="k">public interface</span> <span class="t">IntakeIO</span> {</span>
<span class="cl">&nbsp;&nbsp;<span class="k">public default void</span> <span class="me">updateInputs</span>(<span class="t">IntakeInputs</span> inputs) {}</span>
<span class="cl">&nbsp;&nbsp;<span class="k">public default void</span> <span class="me">setVoltage</span>(<span class="k">double</span> volts) {}</span>
<span class="cl">}</span>
<span class="cl">&nbsp;</span>
<span class="cl"><span class="c">// Multiple interfaces? No problem!</span></span>
<span class="cl"><span class="k">public class</span> <span class="t">Robot</span> <span class="k">implements</span> <span class="t">Loggable</span>, <span class="t">Sendable</span> { ... }</span>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-2.js`, slide 5 ("INTERFACES (CONTRACT)")
