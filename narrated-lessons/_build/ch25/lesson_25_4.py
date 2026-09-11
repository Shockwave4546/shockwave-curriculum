BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.4 &middot; Command-Based Programming</div>
      <h1>State Machines: Logic</h1>
      <p class="scr-sub">Tracking what a subsystem is currently doing &mdash; the enum way.</p>
    </div>''',
        "speak": "A subsystem often needs to remember what it's currently doing, an intake might be idle, actively intaking, holding a game piece, or scoring.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">private boolean</span> isIdle;
<span class="k">private boolean</span> isIntaking;
<span class="k">private boolean</span> isHolding;
<span class="k">private boolean</span> isScoring;</code></pre>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:14px;">Nothing stops two of these from accidentally being true at once.</p>''',
        "speak": "Tracking that with a pile of booleans gets unmanageable fast. Nothing stops two of them from accidentally being true at the same time, a bug that's easy to introduce and hard to spot, since impossible combinations, like idle and scoring both true, compile just fine.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public enum</span> <span class="t">IntakeState</span>
{
    IDLE,
    INTAKING,
    HOLDING,
    SCORING
}

<span class="k">private</span> <span class="t">IntakeState</span> currentState = <span class="t">IntakeState</span>.IDLE;</code></pre>''',
        "speak": "Enums, from Chapter 11, are exactly the tool for this, a fixed, named set of mutually exclusive states, with the compiler enforcing that a variable can only ever be one of them. Define an Intake State enum with values like Idle, Intaking, Holding, and Scoring, and keep a single current-state field initialized to Idle. Now the subsystem's state is one variable, and it's structurally impossible for it to be two states at once. That's a state machine, a system that's always in exactly one of a fixed set of named states, and moves between them according to defined rules.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">This Scales to Real Codebases</h2><ul>
      <li><span class="num">1</span><span>Team 5817's own production code uses exactly this pattern &mdash; just with more states.</span></li>
      <li><span class="num">2</span><span>An elevator's states might carry interpolated target heights.</span></li>
      <li><span class="num">3</span><span>A roller's states might each carry their own target voltage.</span></li>
    </ul></div>''',
        "speak": "This isn't just a teaching example, real, competitive FRC codebases, like Team 5817's own production code, structure their subsystems exactly this way, just with more states and richer per-state behavior. An elevator's states might tie to interpolated target heights that shift based on scoring distance. A roller's states might each carry their own target voltage. The underlying idea is identical, a state machine core built on an enum, just dressed up with more sophisticated data as a subsystem's real requirements grow.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox active">Named State</div>
      <div class="darrow">+</div>
      <div class="dbox">Logic</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Having a named state is only half the picture.</p>''',
        "speak": "Having a named state is only half the picture, though. A state machine also needs logic that reads the current state and decides what to do, and when to move to a different state, and that's exactly what the next lesson covers.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Reaching for several independent booleans instead of one enum &mdash; allows impossible combinations.</li>
      <li><span class="check">!</span>Forgetting a state machine needs an initial value &mdash; an uninitialized state is a NullPointerException waiting to happen.</li>
    </ul></div>''',
        "speak": "Two pitfalls to watch for. Reaching for several independent booleans instead of one enum lets impossible combinations exist in your code, even though only one is ever supposed to be true. And don't forget a state machine needs an initial value, current state should always start as a real value, like Idle. An uninitialized state variable is a null pointer exception waiting to happen the first time anything reads it.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Tracking state with multiple booleans allows impossible combinations.</li>
      <li><span class="check">&#10003;</span>One enum field, initialized to a real starting value, fixes that structurally.</li>
      <li><span class="check">&#10003;</span>Real FRC codebases use exactly this pattern, just with richer per-state data.</li>
    </ul></div>''',
        "speak": "So that's state machine logic. Tracking state with multiple booleans allows impossible combinations and doesn't scale. One enum field, initialized to a sensible starting value, makes a subsystem's current state self-documenting and structurally guaranteed to be exactly one thing at a time. And this is exactly what real, competitive FRC codebases use, just with richer per-state data as requirements grow. Next time, we write the logic that actually reads this state and transitions between them. Nice work, see you in lesson 25.5.",
    },
]
