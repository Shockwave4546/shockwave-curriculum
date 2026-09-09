# The IO-Layer Pattern

**Outline ref:** Ch.20 — The IO-Layer Pattern (ADVKIT 40.1-11, JDP 50.1)
**Status:** existing — pulled verbatim from the deck

```html
<div class="inner">
  <span class="tag">// 07 · architecture.io_layer()</span>
  <h2>The <span class="y">IO-Layer</span> Pattern</h2>
  <p class="lead">This is how Team 6328 handles Simulation vs Real hardware.</p>
  <div class="fgrid">
    <div class="fcard no-bracket">
      <div class="flabel">Implementation A</div>
      <div class="ftitle g">IntakeIOSparkMax</div>
      <div class="fdesc">Uses real CAN IDs and hardware APIs to move physical rollers.</div>
    </div>
    <div class="fcard no-bracket">
      <div class="flabel">Implementation B</div>
      <div class="ftitle b">IntakeIOSim</div>
      <div class="fdesc">Uses physics math (moment of inertia) to "fake" the robot in code.</div>
    </div>
  </div>
  <div class="frow">
    <div class="ftitle">The Subsystem only talks to the <strong>Interface</strong>, so it never knows which one is running!</div>
  </div>
</div>
```

**Deck context:** `mechacoder-test/src/lessons/java-2.js`, slide 6 ("IO LAYER")
