# Common Gotchas

**Outline ref:** Ch.13 — Common Gotchas
**Status:** existing — pulled verbatim from the deck. Slide-only chapter (see `OUTLINE.md`'s
"Slide-only chapters" section) — likely thinner than it should be; flagged for expansion once
real practice/exercise content surfaces more gotchas.

```html
<div>
  <span class="tag">// 12 · debugging()</span>
  <h2>Common <span class="y">Gotchas</span></h2>
  <div class="fgrid">
    <div class="fcard">
      <div class="flabel">COMPARISON</div>
      <div class="ftitle">== vs .equals()</div>
      <div class="fdesc">Use <span class="k">==</span> for primitives (int, double). Use <span class="me">.equals()</span> for Objects (Strings).</div>
    </div>
    <div class="fcard">
      <div class="flabel">MATH</div>
      <div class="ftitle">Integer Division</div>
      <div class="fdesc"><span class="n">5</span> / <span class="n">2</span> is <span class="n">2</span>. Use <span class="n">5.0</span> / <span class="n">2.0</span> to get <span class="n">2.5</span>.</div>
    </div>
    <div class="fcard">
      <div class="flabel">SAFETY</div>
      <div class="ftitle">NullPointerExceptions</div>
      <div class="fdesc">Always initialize your objects before using them, or the robot code will crash.</div>
    </div>
    <div class="fcard">
      <div class="flabel">LOGIC</div>
      <div class="ftitle">Off-by-One</div>
      <div class="fdesc">Arrays start at index <span class="n">0</span>. An array of size 10 goes from 0 to 9.</div>
    </div>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-1.js`, slide 13 ("COMMON GOTCHAS")
