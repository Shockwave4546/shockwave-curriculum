BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.6 &middot; Command-Based Programming</div>
      <h1>Binding Commands to Triggers</h1>
      <p class="scr-sub">The declarative glue that connects a condition to a command.</p>
    </div>''',
        "speak": "A Trigger wraps any boolean condition, a button, a sensor, an arbitrary check, so a command can be bound to it once, declaratively, during setup. From then on, the scheduler itself checks that condition every loop, and schedules or cancels the command as needed, no manual polling code required anywhere else.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// From a controller button</span>
<span class="t">Trigger</span> xButton = driverController.x();

<span class="c">// From an arbitrary condition — any BooleanSupplier (Lesson 19.1) works</span>
<span class="t">Trigger</span> loaded = <span class="k">new</span> Trigger(intake::isLoaded);</code></pre>''',
        "speak": "A trigger can come straight from a controller button, or be built from any boolean supplier, like an intake reporting whether it's loaded.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Core Bindings</h2><ul>
      <li><span class="num">1</span><span><strong>onTrue</strong> &mdash; schedules once, the instant the trigger becomes true.</span></li>
    </ul></div>''',
        "speak": "Each binding schedules a command in response to a specific kind of state change. On-true schedules once, the instant the trigger becomes true, like the moment a button is first pressed.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Core Bindings</h2><ul>
      <li><span class="num">1</span><span><strong>onTrue</strong> &mdash; schedules once, the instant the trigger becomes true.</span></li>
      <li><span class="num">2</span><span><strong>whileTrue</strong> &mdash; runs for as long as it's true, cancels the instant it's false.</span></li>
    </ul></div>''',
        "speak": "While-true schedules for as long as the trigger stays true, and cancels the instant it becomes false, the natural fit for run the intake while this button is held down.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Core Bindings</h2><ul>
      <li><span class="num">1</span><span><strong>onTrue</strong> &mdash; schedules once, the instant the trigger becomes true.</span></li>
      <li><span class="num">2</span><span><strong>whileTrue</strong> &mdash; runs for as long as it's true, cancels the instant it's false.</span></li>
      <li><span class="num">3</span><span><strong>onFalse</strong> &mdash; schedules once, the instant the trigger becomes false.</span></li>
    </ul></div>
    <pre class="code" style="font-size:11.5px;margin-top:10px;"><code><span class="c">// Schedules once, the instant the trigger becomes true (e.g. the button is first pressed)</span>
driverController.y().onTrue(intake.retractCommand());

<span class="c">// Schedules while the trigger is true, cancels the instant it becomes false</span>
driverController.b().whileTrue(intake.runIntakeCommand());

<span class="c">// Schedules once, the instant the trigger becomes false — the mirror of onTrue</span>
driverController.a().onFalse(shooter.stopCommand());</code></pre>''',
        "speak": "On-false schedules once, the instant the trigger becomes false, the mirror of on-true. One nuance worth repeating: on-true fires once on the rising edge, and it won't fire again unless the trigger goes false and then true again. It does not keep re-firing while the button stays held, that's what while-true is for.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// Only schedules when BOTH buttons are pressed together</span>
driverController.x().and(driverController.y()).onTrue(<span class="k">new</span> ExampleCommand());</code></pre>
    <pre class="code" style="margin-top:10px;"><code>exampleButton
    .onTrue(<span class="k">new</span> FooCommand())   <span class="c">// runs when pressed</span>
    .onFalse(<span class="k">new</span> BarCommand()); <span class="c">// runs when released</span></code></pre>''',
        "speak": "Triggers also compose, just like boolean expressions from Chapter 5, and, or, and negate all work exactly as you'd expect. You can require two buttons pressed together, or invert a condition, and get back another trigger you can bind normally. Binding methods return the same trigger they were called on, so you can chain multiple bindings onto one trigger, on-true for one command, on-false for another, right off the same button.",
    },
    {
        "screen": '''<pre class="code"><code>exampleButton.debounce(0.1).onTrue(<span class="k">new</span> ExampleCommand()); <span class="c">// ignores flickers under 0.1s</span></code></pre>''',
        "speak": "One more tool: debounce. A digital sensor's raw signal can flicker rapidly right at the transition point, and debounce filters that out, requiring the condition to hold steady for a set duration before it's treated as a real change.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Expecting onTrue to keep firing while a button stays held &mdash; it only fires once, on the transition.</li>
      <li><span class="check">!</span>Confusing a Trigger's boolean condition with the command it's bound to.</li>
      <li><span class="check">!</span>Not debouncing a noisy digital sensor.</li>
    </ul></div>''',
        "speak": "A few pitfalls to avoid. Don't expect on-true to keep firing while a button stays held, it only fires once, on the transition. Don't confuse a trigger's boolean condition with the command it's bound to, a trigger is just the wrapped condition, the binding methods are what actually connect it to a command. And don't skip debouncing a noisy digital sensor, one near its trip point can flicker and cause repeated, unwanted scheduling.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A Trigger wraps any boolean condition and binds a command declaratively.</li>
      <li><span class="check">&#10003;</span>onTrue/onFalse fire once; whileTrue/whileFalse run for as long as it holds.</li>
      <li><span class="check">&#10003;</span>Triggers compose with and(), or(), negate().</li>
      <li><span class="check">&#10003;</span>debounce() filters out rapid flickering.</li>
    </ul></div>''',
        "speak": "So that's binding commands to triggers. A trigger wraps any boolean condition, and a command binds to it once, declaratively. On-true and on-false fire once, on a transition; while-true and while-false run for as long as the condition holds. Triggers compose with and, or, and negate, same boolean logic as always. And debounce filters out rapid flickering near a condition's trip point. Next time, we put it all together and structure a whole command-based project. Nice work, see you in lesson 25.7.",
    },
]
