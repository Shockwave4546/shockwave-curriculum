BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.5 &middot; Command-Based Programming</div>
      <h1>Managing Transitions (switch)</h1>
      <p class="scr-sub">From diagram to code: one switch, one case per state.</p>
    </div>''',
        "speak": "Lesson 25.4 designed the intake's state machine, four states, a start state, and a transition table, and gave the mechanism a single enum field, currentState. Turning that design into code takes one switch over that field, using the arrow form from Lesson 5.12. Each case does two jobs: it runs that state's action, then checks the guard conditions of that state's outgoing transitions.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">One Switch, One Case per State</div>
    <pre class="code"><code><span class="k">private void</span> update()
{
    <span class="k">switch</span> (currentState)
    {
        <span class="k">case</span> IDLE -&gt;
        {
            motor.setThrottle(0.0);
            <span class="k">if</span> (intakeButton.getAsBoolean())
            {
                enter(IntakeState.INTAKING); <span class="c">// the way out of the start state</span>
            }
        }
        <span class="k">case</span> INTAKING -&gt;
        {
            motor.setThrottle(0.5);
            <span class="k">if</span> (pieceSensor.get())
            {
                enter(IntakeState.HOLDING);
            }
        }
        <span class="k">case</span> HOLDING -&gt;
        {
            motor.setThrottle(0.1); <span class="c">// gentle hold pressure</span>
            <span class="k">if</span> (scoreButton.getAsBoolean())
            {
                enter(IntakeState.SCORING);
            }
        }
        <span class="k">case</span> SCORING -&gt;
        {
            motor.setThrottle(-0.5);
            <span class="k">if</span> (!pieceSensor.get())
            {
                enter(IntakeState.IDLE);
            }
        }
    }
}</code></pre>''',
        "speak": "Compare it with the transition table, every row became one if inside the case for its from-state. The arrow form can't fall through from one case into the next, so no break is needed anywhere here, that's one reason we prefer arrow form for state machines like this one.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Entry Actions Go Through One Method</div>
    <pre class="code"><code><span class="k">private void</span> enter(IntakeState next)
{
    <span class="c">// entry action: log every change, once</span>
    System.out.println(<span class="s">"Intake: "</span> + currentState + <span class="s">" -&gt; "</span> + next);
    currentState = next;
}</code></pre>''',
        "speak": "A transition is just a new value in the state field, but routing every transition through one small method gives the machine a single place for entry actions, things that should happen exactly once, on entering a state, like logging the change here. Logging every transition like this is one of the most useful debugging tools a state machine can have.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">How the Machine Leaves Its Start State</div>''',
        "speak": "Trace it from power-on. currentState starts as idle, so every loop runs the idle case, the rollers stay stopped, and the guard is checked. The first loop where the driver is actually pressing the intake button, the guard is true and the machine enters intaking. From the next loop on, the intaking case runs instead. Outside inputs never assign currentState directly, they only feed the guards, and the machine decides for itself when to move.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Running It Every Loop: A Default Command</div>
    <pre class="code"><code><span class="k">public</span> Command stateMachineCommand()
{
    <span class="k">return</span> runRepeatedly(<span class="k">this</span>::update)
        .withPriority(Command.LOWEST_PRIORITY)
        .named(<span class="s">"Intake State Machine"</span>);
}</code></pre>''',
        "speak": "A state machine has to be checked every loop, and in Commands v3 anything that controls a mechanism every loop belongs in a command. The natural fit is the mechanism's default command, built with runRepeatedly so update runs once per loop, at the lowest priority so any ordinary command, say a manual eject button, can take over whenever it needs to.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Sidebar: v3's Built-In StateMachine (Alpha)</div>''',
        "speak": "One more thing worth knowing about: Commands v3 also includes a built-in StateMachine class, where each state is a whole command and transitions are declared with methods like switchTo dot when. It was added in May 2026 and changed again in September 2026, so it's still settling. This course teaches the enum-and-switch pattern instead, since it works the same in any version, and it's what the later subsystem chapters build on.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Putting transition logic in the wrong case.</li>
      <li><span class="check">!</span>Assigning currentState directly instead of calling enter(...) &mdash; skips entry actions.</li>
      <li><span class="check">!</span>Leaving a state out of the switch &mdash; it compiles fine, and that state has no way out.</li>
    </ul></div>''',
        "speak": "A few pitfalls. Putting a guard inside the wrong state's case, either it never triggers or it moves the machine out of a state it wasn't actually in. Assigning currentState directly instead of calling enter, that skips every entry action. And leaving a state out of the switch entirely, a switch statement doesn't have to list every enum constant, so it compiles just fine, and a machine that enters that state does absolutely nothing and never leaves it.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An arrow-form switch, one case per state, runs the state action and checks that state's guards.</li>
      <li><span class="check">&#10003;</span>Routing transitions through one enter(...) method gives entry actions a single home.</li>
      <li><span class="check">&#10003;</span>In v3, the switch runs as the mechanism's default command, at LOWEST_PRIORITY.</li>
      <li><span class="check">&#10003;</span>The built-in StateMachine class exists, but it's alpha; the enum-and-switch pattern is what this course builds on.</li>
    </ul></div>''',
        "speak": "So: one arrow-form switch, one case per state, running that state's action and checking only that state's guards. Route every transition through one enter method so entry actions have a single home. In Commands v3, the whole thing runs as the mechanism's default command, at the lowest priority, so anything else can take over when it needs to. Next time, we wire up buttons and sensors to actually drive commands. See you in Lesson 25.6.",
    },
]
