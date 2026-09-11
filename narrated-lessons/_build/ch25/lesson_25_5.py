BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.5 &middot; Command-Based Programming</div>
      <h1>Managing Transitions</h1>
      <p class="scr-sub">Reading the current state, every loop, with a switch.</p>
    </div>''',
        "speak": "Last lesson gave a subsystem a single enum field for its current state. The natural place to actually act on that state, and decide when to transition to a different one, is a switch statement, from Chapter 5, inside the subsystem's periodic method, which the scheduler calls once every single loop.",
    },
    {
        "screen": '''<pre class="code" style="font-size:11.5px;"><code><span class="me">@Override</span>
<span class="k">public void</span> periodic()
{
    <span class="k">switch</span> (currentState)
    {
        <span class="k">case</span> INTAKING:
            motor.set(<span class="n">0.5</span>);
            <span class="k">if</span> (sensor.get())
            {
                currentState = <span class="t">IntakeState</span>.HOLDING; <span class="c">// transition: a sensor reading changed the state</span>
            }
            <span class="k">break</span>;
        <span class="k">case</span> IDLE:
            motor.set(<span class="n">0</span>);
            <span class="k">break</span>;
        <span class="k">case</span> HOLDING:
            motor.set(<span class="n">0.1</span>); <span class="c">// gentle hold pressure</span>
            <span class="k">break</span>;
        <span class="k">case</span> SCORING:
            motor.set(-<span class="n">0.5</span>);
            <span class="k">break</span>;
    }
}</code></pre>''',
        "speak": "Inside that switch, each case does two jobs. It runs whatever behavior belongs to that state, set the motor to some speed, and it checks whether a transition to a different state should happen. In this intake example, the Intaking case runs the motor, then checks a sensor, the moment that sensor trips, the state reassigns to Holding. That reassignment is the transition.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">currentState</div>
      <div class="darrow">=</div>
      <div class="dbox active">new value</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">No special syntax &mdash; just a plain reassignment, in the right case.</p>''',
        "speak": "A transition really is nothing more than assigning a new value to the state field, no special syntax beyond what you already know from variables and enums. What makes a state machine's behavior correct is where those reassignments happen, inside the specific case for the state that condition applies to, gated on whatever real-world signal, a sensor, a timer, a driver input, should actually trigger the change.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox active">periodic()</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;margin-top:16px;">Runs every scheduler loop &mdash; exactly the cadence a state machine needs.</p>''',
        "speak": "And this belongs in periodic specifically because periodic runs every single scheduler loop, exactly the cadence a state machine needs. Checking should I transition now, once per loop, is what makes a sensor-triggered transition, like an intake noticing a game piece, responsive in real time, instead of only checked occasionally.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting the break statement &mdash; the single most common bug in a switch-based state machine.</li>
      <li><span class="check">!</span>Putting transition logic in the wrong case.</li>
      <li><span class="check">!</span>Mutating the state field from outside periodic().</li>
    </ul></div>''',
        "speak": "A few common pitfalls here. Forgetting the break statement in a switch is the single most common bug in a switch-based state machine, without it, execution falls straight through into the next case's code, silently running the wrong state's behavior on top of the intended one. Putting transition logic in the wrong case means it either never triggers, or triggers behavior meant for a completely different state. And mutating the state field from outside periodic, scattering assignments across multiple methods, makes it much harder to reason about when and why transitions actually happen, keeping all of it inside that one switch keeps the whole state machine's behavior in one place.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A switch over the state enum, inside periodic(), runs behavior and checks transitions.</li>
      <li><span class="check">&#10003;</span>A transition is just a plain reassignment of the state field.</li>
      <li><span class="check">&#10003;</span>Running this in periodic() makes transitions responsive in real time.</li>
    </ul></div>''',
        "speak": "So that's managing transitions. A switch over the state enum, inside periodic, is the natural place to both run each state's behavior and check for transitions. A transition is just a plain reassignment of the state field, placed inside the correct case. And running this logic in periodic, called every scheduler loop, is what makes transitions responsive to sensors and other real-time signals. Next time, we bind commands to real triggers, buttons, sensors, and conditions. Nice work, see you in lesson 25.6.",
    },
]
