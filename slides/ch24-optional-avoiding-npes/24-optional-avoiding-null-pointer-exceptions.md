# Optional: Maybe a Value

**Outline ref:** Ch.24 — Optional: Avoiding Null Pointer Exceptions (ORACLE 16.1)
**Status:** existing — pulled verbatim from the deck. The deck's actual slide heading is still
"Optional: Maybe a Value" — the outline-level rename to "Optional: Avoiding Null Pointer
Exceptions" is a curriculum-label-only change; `mechacoder-test` stays frozen, never edited
directly.

```html
<div class="inner">
  <span class="tag">// 11 · optional.empty_or_value()</span>
  <h2><span class="y">Optional</span>: Maybe a Value</h2>
  <p class="lead">An <span class="t">Optional</span>&lt;<span class="t">T</span>&gt; either holds a value or is explicitly empty — no nulls, no surprises.</p>
  <div class="two">
    <ul class="bullets">
      <li><span class="bul">▸</span><span>The motivating case: <span class="y">vision pose estimators</span> return <span class="t">Optional</span> because the camera may see no tags.</span></li>
      <li><span class="bul">▸</span><span><span class="r">Never call .get() blind</span> — that's just a NullPointerException with extra steps.</span></li>
      <li><span class="bul">▸</span><span>Use <span class="me">ifPresent</span> or <span class="me">orElse</span> to handle both cases honestly.</span></li>
    </ul>
    <div class="code">
<span class="cl"><span class="t">Optional</span>&lt;<span class="t">Pose2d</span>&gt; visionPose = vision.<span class="me">getPose</span>();</span>
<span class="cl">&nbsp;</span>
<span class="cl"><span class="c">// Run logic only when a value exists</span></span>
<span class="cl">visionPose.<span class="me">ifPresent</span>(pose -&gt;</span>
<span class="cl">&nbsp;&nbsp;estimator.<span class="me">addVisionMeasurement</span>(pose, time));</span>
<span class="cl">&nbsp;</span>
<span class="cl"><span class="c">// Or supply a fallback</span></span>
<span class="cl"><span class="t">Pose2d</span> pose = visionPose.<span class="me">orElse</span>(lastKnownPose);</span>
    </div>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-2.js`, slide 9b ("OPTIONAL")
