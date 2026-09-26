BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.4 &middot; Command-Based Programming</div>
      <h1>State Machines: Logic</h1>
      <p class="scr-sub">The design pattern behind every mechanism that remembers what it's doing.</p>
    </div>''',
        "speak": "A mechanism often needs to remember what it's currently doing, an intake might be idle, actively intaking, holding a game piece, or scoring. Tracking that with a pile of booleans gets unmanageable fast, and nothing stops two of them from accidentally being true at the same time.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Booleans Don't Scale</div>
    <pre class="code"><code><span class="k">private boolean</span> isIdle;
<span class="k">private boolean</span> isIntaking;
<span class="k">private boolean</span> isHolding;
<span class="k">private boolean</span> isScoring;</code></pre>''',
        "speak": "Here's the problem in code. This compiles perfectly fine even with isIdle and isScoring both true at once, a contradiction that means nothing in the real world, and the compiler has no way to catch it.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The State Machine Pattern, Five Parts</h2><ul>
      <li><span class="num">1</span><span><strong>States</strong> &mdash; every situation, each with a name and a state action that repeats every loop.</span></li>
      <li><span class="num">2</span><span><strong>Start state</strong> &mdash; the one state the machine is in when the robot turns on.</span></li>
      <li><span class="num">3</span><span><strong>Transitions</strong> &mdash; the allowed moves from one state to another.</span></li>
    </ul></div>''',
        "speak": "A state machine is a design pattern for exactly this problem, a system that's always in exactly one of a fixed set of named states, moving between them by defined rules. States, each with its own state action that repeats every loop. A start state, the one the machine is in when the robot turns on. And transitions, the allowed moves between states, a move that isn't listed simply can't happen.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The State Machine Pattern, Five Parts</h2><ul>
      <li><span class="num">4</span><span><strong>Guard conditions</strong> &mdash; what must be true for a transition to fire.</span></li>
      <li><span class="num">5</span><span><strong>Entry actions</strong> &mdash; things that happen exactly once, on entering a state.</span></li>
    </ul></div>''',
        "speak": "Guard conditions, what has to be true for a transition to actually happen, a sensor, a timer, a driver's button. And entry actions, anything that should happen exactly once, at the moment the machine enters a state, like logging the change, which is different from the state action that repeats every loop.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram-wrap"><h2 class="scr-h2" style="text-align:center;">Draw It First</h2>
    <pre class="code"><code>             start
               │
               ▼
         ┌───────────┐   intake button pressed   ┌───────────┐
         │   IDLE    │ ────────────────────────▶ │ INTAKING  │
         └───────────┘                           └───────────┘
               ▲                                       │
               │ sensor no longer                      │ sensor sees
               │ sees a piece                          │ a piece
               │                                       ▼
         ┌───────────┐   score button pressed    ┌───────────┐
         │  SCORING  │ ◀──────────────────────── │  HOLDING  │
         └───────────┘                           └───────────┘</code></pre></div>''',
        "speak": "Before writing any code, draw the machine. Each box is a state, each arrow a transition labeled with its guard. Idle to intaking when the button's pressed, intaking to holding once the sensor sees a piece, holding to scoring on the score button, and scoring back to idle once the sensor no longer sees anything. The diagram and a transition table carry the same information, and the table maps almost line for line onto code, that's Lesson 25.5.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Leaving the Start State</div>''',
        "speak": "Follow the arrows from start. The machine begins in idle and stays there, every single loop, until a guard on one of idle's outgoing arrows becomes true. If the start state had no outgoing transition at all, the machine would sit there forever and the intake would never do anything. Every state needs at least one way out, unless it's deliberately a final state.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">One Enum, One Field</div>
    <pre class="code"><code><span class="k">public enum</span> IntakeState
{
    IDLE,
    INTAKING,
    HOLDING,
    SCORING
}

<span class="k">private</span> IntakeState currentState = IntakeState.IDLE;</code></pre>''',
        "speak": "Enums are exactly the tool for the states, a fixed, named set of mutually exclusive values, with the compiler enforcing that a variable can only ever be one of them at a time. Now the mechanism's state is a single variable, initialized to the start state, and it's structurally impossible for it to be two states at once. The enum only covers the states, though, transitions, guards, and actions are logic, and that's Lesson 25.5's job.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Reaching for several booleans instead of one enum &mdash; lets impossible combinations exist.</li>
      <li><span class="check">!</span>Forgetting the state machine needs an initial value.</li>
      <li><span class="check">!</span>Designing a state with no way out &mdash; especially the start state.</li>
    </ul></div>''',
        "speak": "A few pitfalls. Reaching for several booleans instead of one enum lets impossible combinations back in. Forgetting to give the state field a real starting value leaves it null, waiting to throw a NullPointerException the first time anything reads it. And designing a state, especially the start state, with no way out, the machine gets stuck there for the rest of the match.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A state machine is always in exactly one of a fixed set of states.</li>
      <li><span class="check">&#10003;</span>Five parts: states, start state, transitions, guard conditions, entry actions.</li>
      <li><span class="check">&#10003;</span>Draw the diagram first &mdash; every state needs a way out.</li>
      <li><span class="check">&#10003;</span>A single enum field, initialized to the start state, is the whole representation.</li>
    </ul></div>''',
        "speak": "So: a state machine is always in exactly one of a fixed set of states, with a start state, transitions, guard conditions, and entry actions. Draw the diagram before the code, and make sure every state has a way out. A single enum field, initialized to the real start state, is the entire representation, and this exact pattern is what real, competitive FRC codebases use at scale. Next time, we turn this design into actual running code. See you in Lesson 25.5.",
    },
]
