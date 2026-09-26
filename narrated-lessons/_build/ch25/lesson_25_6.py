BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.6 &middot; Command-Based Programming</div>
      <h1>Binding Commands to Triggers</h1>
      <p class="scr-sub">The declarative glue: wrap a condition once, and the scheduler checks it forever.</p>
    </div>''',
        "speak": "A Trigger wraps any boolean condition, a button, a sensor, an arbitrary check, so a command can be bound to it once, declaratively, during setup. From then on the scheduler itself checks the condition every loop and queues or cancels the command as needed, no manual polling code required anywhere else.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Wrapping a Condition</div>
    <pre class="code"><code><span class="c">// From a controller button</span>
Trigger xButton = driverController.x();

<span class="c">// From an arbitrary condition — any BooleanSupplier (Lesson 19.1) works</span>
Trigger loaded = <span class="k">new</span> Trigger(intake::isLoaded);</code></pre>''',
        "speak": "In this chapter, driverController is a CommandXboxController, its methods a, b, x, y, leftBumper, rightBumper and so on each return a Trigger for that button. WPILib 2027 also has a generic CommandGamepad, which names the four face buttons by position, so the same code fits any gamepad. A Trigger is itself a BooleanSupplier, so it can be passed anywhere a condition is expected.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Core Bindings</div>
    <pre class="code"><code><span class="c">// Schedules once, the instant the trigger becomes true (e.g. the button is first pressed)</span>
driverController.y().onTrue(intake.retractCommand());

<span class="c">// Schedules while the trigger is true, cancels the instant it becomes false</span>
driverController.b().whileTrue(intake.runIntakeCommand());

<span class="c">// Schedules once, the instant the trigger becomes false — the mirror of onTrue</span>
driverController.a().onFalse(shooter.stopCommand());

<span class="c">// Schedules while the trigger is false, cancels the instant it becomes true</span>
loaded.whileFalse(leds.blinkCommand());</code></pre>''',
        "speak": "Four core bindings. onTrue fires once on the rising edge and doesn't re-fire unless the trigger goes false and true again. whileTrue keeps a command running for as long as the condition holds, and cancels it the moment the condition ends, the natural fit for run the intake while this button is held. whileFalse is its mirror image.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Composing Triggers</div>
    <pre class="code"><code><span class="c">// Only schedules when BOTH buttons are pressed together</span>
driverController.x().and(driverController.y()).onTrue(climber.deployCommand());</code></pre>''',
        "speak": "Triggers combine with and, or, and negate, just like boolean expressions from Chapter 5. Here, deploying the climber only schedules when both buttons are pressed together.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Chaining Multiple Bindings</div>
    <pre class="code"><code>driverController.rightBumper()
    .onTrue(hatch.grabCommand())      <span class="c">// runs when pressed</span>
    .onFalse(hatch.releaseCommand()); <span class="c">// runs when released</span></code></pre>''',
        "speak": "Binding methods return the same trigger they were called on, so several different bindings can be chained onto one trigger, grab on press, release on release, all off one right bumper.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Debouncing: Filtering Out Noise</div>
    <pre class="code"><code>loaded.debounce(Seconds.of(0.1)).onTrue(leds.flashCommand()); <span class="c">// needs 0.1 s of true first</span></code></pre>''',
        "speak": "A digital sensor's raw signal can flicker rapidly right at the transition point, and debounce filters that out, requiring the condition to hold steady for a set duration before it's treated as a real change. Like every v3 duration, that's a Time value. By default, debounce only filters the rising edge, a drop back to false passes through instantly.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Debouncing Both Directions</div>
    <pre class="code"><code>loaded.debounce(Seconds.of(0.1), DebounceType.BOTH).onTrue(leds.flashCommand());</code></pre>''',
        "speak": "A sensor that flickers off and on can still fire onTrue again after each fresh tenth of a second of true. To filter both directions, pass a debounce type of BOTH, from Debouncer dot DebounceType.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">More Bindings in v3</h2><ul>
      <li><span class="num">1</span><span><strong>toggleOnTrue</strong> &mdash; each press starts or cancels the command.</span></li>
      <li><span class="num">2</span><span><strong>retryWhileTrue</strong> &mdash; restarts the command if it ends while the condition is still true.</span></li>
      <li><span class="num">3</span><span><strong>risingEdge / fallingEdge</strong>, <strong>multiPress</strong>, and command-scoped bindings.</span></li>
    </ul></div>''',
        "speak": "A few more v3 bindings worth knowing. toggleOnTrue, each press starts the command if it's stopped or cancels it if it's running. retryWhileTrue, like whileTrue but restarts the command if it ends while the condition is still true. Rising and falling edge triggers, a multi-press trigger, and command-scoped bindings, a binding made inside a command's body that only exists while that command runs.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Expecting onTrue to re-fire while a button stays held &mdash; use whileTrue for that.</li>
      <li><span class="check">!</span>Not debouncing a noisy digital sensor.</li>
      <li><span class="check">!</span>Assuming the default debounce filters flicker in both directions &mdash; it only delays the rise.</li>
    </ul></div>''',
        "speak": "A few pitfalls. Expecting onTrue to keep firing while a button stays held, it only fires once, on the transition, use whileTrue for continuous behavior. Not debouncing a sensor near its trip point, that's exactly what causes repeated unwanted scheduling. And assuming the default debounce filters flicker in both directions, it only delays the change to true.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A Trigger wraps any boolean condition; controller buttons come from CommandXboxController.</li>
      <li><span class="check">&#10003;</span>onTrue/onFalse fire once on a transition; whileTrue/whileFalse run while the condition holds.</li>
      <li><span class="check">&#10003;</span>Triggers compose with and, or, negate; bindings chain onto one trigger.</li>
      <li><span class="check">&#10003;</span>debounce(Seconds.of(...)) filters flicker; DebounceType.BOTH filters both edges.</li>
    </ul></div>''',
        "speak": "So: a Trigger wraps any boolean condition so a command can be bound to it once. onTrue and onFalse fire once on a transition, whileTrue and whileFalse run for as long as the condition holds. Triggers compose just like booleans, and debounce filters out flicker, by default only on the rise. Next time, we put an entire project together, mechanisms, opmodes, and a v2 reading guide. See you in Lesson 25.7.",
    },
]
