BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 3 &middot; APIs, Libraries &amp; Documentation</div>
      <h1>Packages &amp; Imports</h1>
      <p class="scr-sub">How Java organizes thousands of classes so you can actually find the ones you need.</p>
    </div>''',
        "speak": "WPILib alone gives you hundreds of classes. Java needs some way to organize all of them so names don't collide and you can actually find the one you want, that's what packages and imports are for.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">edu.wpi.first.wpilibj2.command</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">A package groups related classes together, the same way a folder groups related files.</p>''',
        "speak": "A package groups related classes together, exactly the same way a folder groups related files on a computer. This one, a real WPILib package, holds every class in the whole command-based framework.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">package</span> frc.robot.subsystems;</code></pre>''',
        "speak": "Every file starts by declaring which package it belongs to. This package line says where this particular file lives, frc dot robot dot subsystems.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">package</span> frc.robot.subsystems;

<span class="k">import</span> edu.wpi.first.wpilibj2.command.SubsystemBase;</code></pre>''',
        "speak": "To use a class from a different package, you import it at the top of the file. This line brings in Subsystem Base, from WPILib's own command package, so you can refer to it by its short name from here on instead of typing that whole path every time.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">package</span> frc.robot.subsystems;

<span class="k">import</span> edu.wpi.first.wpilibj2.command.SubsystemBase;
<span class="k">import</span> com.revrobotics.CANSparkMax;</code></pre>''',
        "speak": "A file can import as many classes as it needs. Here's a second one, CAN Spark Max, this time from REV Robotics' own library, a completely different package than WPILib's, but imported the exact same way.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">package</span> frc.robot.subsystems;

<span class="k">import</span> edu.wpi.first.wpilibj2.command.SubsystemBase;
<span class="k">import</span> com.revrobotics.CANSparkMax;

<span class="k">public</span> <span class="k">class</span> <span class="t">Drivetrain</span> <span class="k">extends</span> <span class="t">SubsystemBase</span> { ... }</code></pre>''',
        "speak": "And now that Subsystem Base is imported, this file can define its own Drive Train class and extend it directly, using just the short name, no full path required.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">One Package Needs No Import</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">java.lang &mdash; String, System, and a handful of others &mdash; is always available, everywhere.</p>''',
        "speak": "One package is special. java dot lang is always available in every single Java file, with no import needed at all. That's why you've been using System dot out dot print line and String this entire time without ever importing anything.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting an import &mdash; using a class that's not in java.lang and not in your own package is a compile error.</li>
      <li><span class="check">!</span>Importing something you don't use &mdash; not a functional bug, but most IDEs will flag it as clutter.</li>
    </ul></div>''',
        "speak": "Two pitfalls. Forgetting an import, if a class isn't in java dot lang and isn't already in your own package, using it without importing it is a compile error, full stop. And importing something you never actually use, that's not a functional bug, but most IDEs will flag it, and it's just clutter worth cleaning up.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>A package groups related classes together, like a folder groups files.</li>
      <li><span class="check">&#10003;</span>import brings a class from another package into your file, by its short name.</li>
      <li><span class="check">&#10003;</span>java.lang never needs an import &mdash; it's always available.</li>
    </ul></div>''',
        "speak": "So: a package groups related classes together, the same way a folder groups related files. Import brings a class from another package into your file so you can use its short name. And java dot lang, home to String and System among others, never needs an import, it's always there. That's Chapter 3 done, next up, Chapter 4, actually calling methods and working with objects hands-on.",
    },
]
