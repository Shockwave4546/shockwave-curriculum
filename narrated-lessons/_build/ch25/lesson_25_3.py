BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 25.3 &middot; Command-Based Programming</div>
      <h1>The Command Scheduler</h1>
      <p class="scr-sub">The engine that runs every command, every 20 milliseconds, in a fixed order.</p>
    </div>''',
        "speak": "The CommandScheduler is the singleton that actually runs commands, everything from the last two lessons depends on it silently doing its job every single loop. It has to be told to run explicitly: CommandScheduler dot get instance dot run needs to be called from robot periodic, or nothing in the whole command-based framework ever executes. We'll see exactly where that call goes when we structure a whole project.",
    },
    {
        "screen": '''<div class="scr-steps">
      <div class="step"><span class="n">1</span><span>Run every Subsystem's periodic()</span></div>
    </div>''',
        "speak": "Every 20 milliseconds, WPILib's default loop rate, the scheduler works through four steps, always in the same order. Step one: run every registered subsystem's periodic method, so subsystems can update their own state, like odometry, before any commands act on it this loop.",
    },
    {
        "screen": '''<div class="scr-steps">
      <div class="step"><span class="n">1</span><span>Run every Subsystem's periodic()</span></div>
      <div class="arrow">&darr;</div>
      <div class="step"><span class="n">2</span><span>Poll triggers for new commands</span></div>
    </div>''',
        "speak": "Step two: poll triggers for new commands to schedule, every registered trigger gets checked, and if a binding's condition is met, its command is scheduled and its initialize method runs immediately.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-steps">
      <div class="step"><span class="n">1</span><span>Run every Subsystem's periodic()</span></div>
      <div class="arrow">&darr;</div>
      <div class="step"><span class="n">2</span><span>Poll triggers for new commands</span></div>
      <div class="arrow">&darr;</div>
      <div class="step"><span class="n">3</span><span>Run every scheduled command</span></div>
    </div>''',
        "speak": "Step three: run every currently scheduled command, call execute, then check isFinished, and if it's true, call end with false and remove the command, freeing its subsystem requirements for anything else.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-steps">
      <div class="step"><span class="n">1</span><span>Run every Subsystem's periodic()</span></div>
      <div class="arrow">&darr;</div>
      <div class="step"><span class="n">2</span><span>Poll triggers for new commands</span></div>
      <div class="arrow">&darr;</div>
      <div class="step"><span class="n">3</span><span>Run every scheduled command</span></div>
      <div class="arrow">&darr;</div>
      <div class="step"><span class="n">4</span><span>Schedule default commands</span></div>
    </div>''',
        "speak": "Step four: schedule default commands, any subsystem not currently claimed by another command gets its default command scheduled, if it has one. That's how a drivetrain just keeps driving from joystick input whenever nothing more specific is happening.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">New Command</div>
      <div class="darrow">&times;</div>
      <div class="dbox err">Running Command</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Default: kCancelSelf &mdash; the running command is canceled, the new one takes over.</p>''',
        "speak": "So what happens when two commands want the same subsystem? The scheduler checks the already-running command's interruption behavior. By default, that's kCancelSelf, the already-running command gets canceled, its end method runs with interrupted true, and the new command takes over. A command can instead be marked kCancelIncoming, in which case the new command simply fails to schedule, and the original just keeps running.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox active">periodic()</div><div class="darrow">&rarr;</div>
      <div class="dbox">triggers</div><div class="darrow">&rarr;</div>
      <div class="dbox">execute()</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Same fixed order, every single loop &mdash; no exceptions.</p>''',
        "speak": "Why does the call order matter? Subsystem periodic methods run before triggers get polled and commands execute, every loop, so a subsystem's periodic logic is always working from the previous loop's final state, and any command reading that subsystem this loop sees it freshly updated. That fixed order is a big part of why command-based code behaves predictably, loop after loop, without exception.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting to call CommandScheduler.getInstance().run() in robotPeriodic() &mdash; the single most common mistake.</li>
      <li><span class="check">!</span>Assuming initialize() runs when run() is called, not when the command is scheduled.</li>
      <li><span class="check">!</span>Expecting a canceled command's end() to report interrupted = false.</li>
    </ul></div>''',
        "speak": "Common pitfalls. Forgetting to call CommandScheduler dot get instance dot run in robot periodic is the single most common mistake, without that one line, nothing in the framework does anything. Don't assume a command's initialize runs exactly when run is called, it actually runs the moment the command is scheduled, which for a trigger-bound command happens during step two, whichever loop the condition first becomes true. And don't expect a canceled command's end to report interrupted false, a command that's forcibly interrupted, whether by a conflicting command or an explicit cancel, always gets end with interrupted true. Only a command that finishes on its own gets interrupted false.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>The scheduler must be run explicitly from robotPeriodic().</li>
      <li><span class="check">&#10003;</span>Four fixed steps every loop: periodic, triggers, execute/finish, defaults.</li>
      <li><span class="check">&#10003;</span>Conflicts resolve via interruption behavior (kCancelSelf by default).</li>
      <li><span class="check">&#10003;</span>The fixed order is why command-based code behaves predictably.</li>
    </ul></div>''',
        "speak": "So that's the scheduler. It must be run explicitly, from robot periodic, or nothing happens. Every loop runs four fixed steps: subsystem periodic, poll triggers, execute and finish scheduled commands, then schedule any free subsystem's default command. Requirement conflicts resolve through interruption behavior, canceling the running command by default. And that fixed order is why command-based code behaves predictably, loop after loop. Next time, we tackle state machines, using enums to track what a subsystem is currently doing. Nice work, see you in lesson 25.4.",
    },
]
