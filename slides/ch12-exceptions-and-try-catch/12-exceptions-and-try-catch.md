# Exceptions & try/catch

**Outline ref:** Ch.12 — Exceptions & try/catch (ORACLE 11.1-16)
**Status:** existing — pulled verbatim from the deck

```html
<div>
  <span class="tag">// 10 · exceptions.try_catch()</span>
  <h2>Exceptions & <span class="y">try/catch</span></h2>
  <div class="two">
    <div>
      <p class="lead">When something goes wrong, Java <strong>throws</strong> an exception. Uncaught, it crashes the program.</p>
      <ul class="bullets">
        <li><span class="bul">▸</span><span>An uncaught exception in <span class="me">periodic()</span> = <span class="r">"Robot Code: No"</span> on the Driver Station.</span></li>
        <li><span class="bul">▸</span><span><span class="k">catch</span> where you can recover; let it crash where you can't.</span></li>
        <li><span class="bul">▸</span><span>Never catch-and-ignore — at minimum, report it.</span></li>
      </ul>
    </div>
    <div class="code">
      <span class="cl"><span class="k">try</span> {</span>
      <span class="cl">&nbsp;&nbsp;config = <span class="me">loadFromFile</span>(<span class="s">"tuning.json"</span>);</span>
      <span class="cl">} <span class="k">catch</span> (<span class="t">IOException</span> e) {</span>
      <span class="cl">&nbsp;&nbsp;<span class="c">// Recover: fall back to defaults</span></span>
      <span class="cl">&nbsp;&nbsp;config = <span class="t">Config</span>.<span class="me">defaults</span>();</span>
      <span class="cl">&nbsp;&nbsp;<span class="me">reportWarning</span>(<span class="s">"Using default tuning"</span>);</span>
      <span class="cl">}</span>
    </div>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-1.js`, slide 11 ("EXCEPTIONS")
