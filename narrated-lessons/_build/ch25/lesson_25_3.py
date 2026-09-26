BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.3 &middot; Command-Based Programming</div>
      <h1>The Command Scheduler</h1>
      <p class="scr-sub">The engine underneath everything &mdash; six steps, every 20 milliseconds.</p>
    </div>''',
        "speak": "The default scheduler, Scheduler dot getDefault, is the object that actually runs commands. Everything from Lessons 25.1 and 25.2 depends on it silently doing its job every single loop. It has to be told to run explicitly, from robotPeriodic, or nothing in the whole command-based framework ever executes.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">The Most Important Line in the Project</div>
    <pre class="code"><code><span class="me">@Override</span>
<span class="k">public void</span> robotPeriodic()
{
    Scheduler.getDefault().run();
}</code></pre>''',
        "speak": "This is that one line. In v2 code you'd see CommandScheduler dot getInstance dot run in this same spot, same job, older name. Without this call, commands never run and triggers never fire, full stop.",
    },
    {
        "screen": '''<div class="scr-steps"><h2 class="scr-h2">One Scheduler Loop, Six Steps</h2><ol>
      <li>Clean up ended scopes.</li>
      <li>Run periodic side jobs (addPeriodic).</li>
      <li>Poll triggers &mdash; a changed condition queues a command.</li>
    </ol></div>''',
        "speak": "Every 20 milliseconds, one call to run works through six steps, always in this order. First, clean up any commands and trigger bindings whose scope has ended. Second, run periodic side jobs, things registered with addPeriodic, data updates like odometry or logging. Third, poll every registered trigger, a binding whose condition changed queues its command, it doesn't start it yet.",
    },
    {
        "screen": '''<div class="scr-steps"><h2 class="scr-h2">One Scheduler Loop, Six Steps</h2><ol>
      <li>Queue default commands for free mechanisms.</li>
      <li>Start the queued commands &mdash; conflicts settled by priority.</li>
      <li>Run every running command until it yields or finishes.</li>
    </ol></div>''',
        "speak": "Fourth, queue a default command for every mechanism that has nothing running or queued. Fifth, start the queued commands, requirement conflicts are settled here, by priority. And sixth, run every running command, one at a time, until each one calls coroutine dot yield or finishes. Because triggers only queue commands in step three, a button-bound command actually starts in step five and gets its first turn in step six, all in that same loop.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Priorities Settle Conflicts</div>
    <pre class="code"><code><span class="k">public</span> Command lowBatteryWarning()
{
    <span class="k">return</span> run(coroutine -&gt; {
        showRed();
        coroutine.wait(Seconds.of(2));
    }).withPriority(10).named(<span class="s">"Low Battery Warning"</span>); <span class="c">// beats any priority-0 LED command</span>
}</code></pre>''',
        "speak": "Every command has an integer priority, default is zero. When a new command needs a mechanism a running command already has, equal-or-higher priority cancels the running one and takes over; lower priority is simply refused and the running command keeps going. Here, priority ten beats any ordinary priority-zero LED command. In v2 code you'd see this job done by an interruption behavior instead, cancel-self or cancel-incoming.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Default Commands</div>
    <pre class="code"><code>drive.setDefaultCommand(
    drive.runRepeatedly(() -&gt; drive.arcade(forward.getAsDouble(), turn.getAsDouble()))
        .withPriority(Command.LOWEST_PRIORITY)
        .named(<span class="s">"Arcade Drive"</span>));</code></pre>''',
        "speak": "A mechanism's default command runs whenever no other command requires that mechanism. Give it a priority below the default, usually LOWEST_PRIORITY, so any ordinary command can take the mechanism away from it, and once that other command ends, the default command starts right back up from the top of its own body. This exact shape is what Lesson 25.5 uses to run a state machine.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Finished, Canceled, and Scopes</h2><ul>
      <li><span class="num">1</span><span>A command <strong>finishes</strong> when its body returns.</span></li>
      <li><span class="num">2</span><span>It's <strong>canceled</strong> when something stops it early &mdash; it stops wherever it last yielded.</span></li>
      <li><span class="num">3</span><span><strong>Scopes</strong> auto-cancel commands when autonomous or an opmode ends.</span></li>
    </ul></div>''',
        "speak": "A command finishes when its body returns on its own. It's canceled when something stops it early, a button released, a timeout, a higher-priority command taking its mechanism, and a canceled command stops wherever it last yielded, the code after its loop never runs. That's exactly why cleanup belongs in whenExited, not after the loop. And v3 tracks the scope a command was created in, a command scheduled during autonomous is canceled automatically when autonomous ends, no remember-to-cancel step required.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">addPeriodic Is for Data, Not Motors</div>
    <pre class="code"><code>Scheduler.getDefault().addPeriodic(() -&gt; drive.updateOdometry());</code></pre>''',
        "speak": "v3 mechanisms have no periodic method at all. For work that has to happen every loop but doesn't control anything, updating odometry, logging, register a side job like this one. Side jobs run before triggers and commands, so commands always see fresh data, but they must never drive a motor, a side job has no requirements, so it would completely bypass the requirement system.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting Scheduler.getDefault().run() in robotPeriodic &mdash; nothing runs without it.</li>
      <li><span class="check">!</span>Assuming a trigger starts its command the instant its condition changes &mdash; it only queues in step 3.</li>
      <li><span class="check">!</span>Controlling a motor from an addPeriodic side job &mdash; use a command instead.</li>
    </ul></div>''',
        "speak": "A few pitfalls. Forgetting that one robotPeriodic call means the entire framework does nothing. Assuming a trigger starts its command the instant its condition changes, it only queues in step three and starts in step five. And controlling a motor from an addPeriodic side job, since side jobs have no requirements, they'll fight whatever command actually owns that mechanism.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Scheduler.getDefault().run() must be called every loop, from robotPeriodic.</li>
      <li><span class="check">&#10003;</span>Six fixed steps: clean up, side jobs, poll triggers, queue defaults, start queued, run commands.</li>
      <li><span class="check">&#10003;</span>Priority settles conflicts; scopes auto-cancel commands and bindings.</li>
      <li><span class="check">&#10003;</span>addPeriodic is for data only &mdash; never for controlling a mechanism.</li>
    </ul></div>''',
        "speak": "So: the scheduler must be run every loop, from robotPeriodic, and it always works through the same six steps in the same order. Priority settles requirement conflicts, and scopes clean up autonomous- and opmode-scoped commands for you. Next time, we take everything we've built and design a real state machine on top of it. See you in Lesson 25.4.",
    },
]
