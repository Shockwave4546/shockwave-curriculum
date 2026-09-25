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
      <div class="dbox">org.wpilib.hardware.discrete</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">A package groups related classes together, the same way a folder groups related files.</p>''',
        "speak": "A package groups related classes together, exactly the same way a folder groups related files on a computer. This one, a real W P I Lib package, org dot W P I Lib dot hardware dot discrete, holds Digital Input and Digital Output. Another, org dot W P I Lib dot command 3, holds the command-based framework's classes, that's chapter 25. And package names match folders on disk, a class in the package frc dot robot dot subsystems lives in an frc, robot, subsystems folder.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">package</span> frc.robot.subsystems;</code></pre>''',
        "speak": "Every file starts by declaring which package it belongs to. This package line says where this particular file lives, frc dot robot dot subsystems.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">package</span> frc.robot.subsystems;

<span class="k">import</span> org.wpilib.hardware.discrete.<span class="t">DigitalInput</span>;</code></pre>''',
        "speak": "To use a class from a different package, you import it at the top of the file. This line brings in Digital Input, from W P I Lib's hardware discrete package, so you can refer to it by its short name from here on, instead of typing that whole path every time.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">package</span> frc.robot.subsystems;

<span class="k">import</span> org.wpilib.hardware.discrete.<span class="t">DigitalInput</span>;
<span class="k">import</span> org.wpilib.hardware.rotation.<span class="t">Encoder</span>;</code></pre>''',
        "speak": "A file can import as many classes as it needs. Here's a second one, Encoder, from a different W P I Lib package, hardware dot rotation, imported the exact same way.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">package</span> frc.robot.subsystems;

<span class="k">import</span> org.wpilib.hardware.discrete.<span class="t">DigitalInput</span>;
<span class="k">import</span> org.wpilib.hardware.rotation.<span class="t">Encoder</span>;

<span class="k">public</span> <span class="k">class</span> <span class="t">Arm</span> { ... }</code></pre>''',
        "speak": "And now the file defines its own class, Arm, which can use Digital Input and Encoder by their short names, no full path required. The order is always the same, package first, then the imports, then the class.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Other Ways to Reach a Class</h2><ul>
      <li><span class="num">1</span><span><strong>Fully-qualified name</strong> &mdash; write the whole path: org.wpilib.system.Timer clock = new org.wpilib.system.Timer();</span></li>
    </ul></div>''',
        "speak": "There are a few other ways to reach a class. You can skip the import and write the fully-qualified name, the whole path, right where you use it, org dot W P I Lib dot system dot Timer. Legal, just long.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Other Ways to Reach a Class</h2><ul>
      <li><span class="num">1</span><span><strong>Fully-qualified name</strong> &mdash; write the whole path: org.wpilib.system.Timer clock = new org.wpilib.system.Timer();</span></li>
      <li><span class="num">2</span><span><strong>Wildcard import</strong> &mdash; import org.wpilib.hardware.discrete.*; imports every class in that one package.</span></li>
    </ul></div>''',
        "speak": "A wildcard import, ending in dot star, imports every class in that one package, but not the packages inside it.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Other Ways to Reach a Class</h2><ul>
      <li><span class="num">1</span><span><strong>Fully-qualified name</strong> &mdash; write the whole path: org.wpilib.system.Timer clock = new org.wpilib.system.Timer();</span></li>
      <li><span class="num">2</span><span><strong>Wildcard import</strong> &mdash; import org.wpilib.hardware.discrete.*; imports every class in that one package.</span></li>
      <li><span class="num">3</span><span><strong>Static import</strong> &mdash; import static java.lang.Math.sqrt; lets you write sqrt(9.0) instead of Math.sqrt(9.0).</span></li>
    </ul></div>''',
        "speak": "A static import lets you call one static method without its class name, square root of 9, instead of Math dot square root of 9. Static methods are lesson 4.2.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Other Ways to Reach a Class</h2><ul>
      <li><span class="num">1</span><span><strong>Fully-qualified name</strong> &mdash; write the whole path: org.wpilib.system.Timer clock = new org.wpilib.system.Timer();</span></li>
      <li><span class="num">2</span><span><strong>Wildcard import</strong> &mdash; import org.wpilib.hardware.discrete.*; imports every class in that one package.</span></li>
      <li><span class="num">3</span><span><strong>Static import</strong> &mdash; import static java.lang.Math.sqrt; lets you write sqrt(9.0) instead of Math.sqrt(9.0).</span></li>
      <li><span class="num">4</span><span><strong>Same package, no import</strong> &mdash; classes in your own package are used by their short name.</span></li>
    </ul></div>''',
        "speak": "And a class in the same package as your file needs no import at all, you just use its short name.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">One Package Needs No Import</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">java.lang &mdash; String, System, Math, and a handful of others &mdash; is always available, everywhere.</p>''',
        "speak": "One package is special. java dot lang is always available in every single Java file, with no import needed at all. That's why you've been using System dot out dot print line and String this entire time without ever importing anything, and why Math, in lesson 4.3, needs no import either.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Java 25 Note</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">import module java.base; imports all of Java's core library at once. Compact source files get it automatically.</p>''',
        "speak": "A version note. Java 25 adds import module java dot base, which imports every public class in Java's core library at once, and a compact source file, one that's just void main with no class line around it, gets that import automatically. On Java 17 neither exists, so import classes one at a time.",
    },
    {
        "screen": '''<div class="scr-h2" style="text-align:center;">Keep Files in Their Package's Folder</div>
    <p style="text-align:center;color:var(--ink-soft);font-size:15px;max-width:52ch;margin:0 auto;">On Java 22+, java SelfTest.java refuses a file whose package line doesn't match its folder.</p>''',
        "speak": "And one practical note. Keep a file with a package line in the folder its package names. On Java 22 and later, running it directly with the java command refuses a file whose package line doesn't match the folder it's in.",
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
      <li><span class="check">&#10003;</span>A package groups related classes together, like a folder groups files &mdash; and its name matches the folder path.</li>
      <li><span class="check">&#10003;</span>import brings a class from another package into your file, by its short name.</li>
      <li><span class="check">&#10003;</span>Alternatives: a fully-qualified name, a .* wildcard, or import static; same-package classes need no import.</li>
      <li><span class="check">&#10003;</span>java.lang (String, System, Math) never needs an import &mdash; it's always available.</li>
    </ul></div>''',
        "speak": "So: a package groups related classes together, the same way a folder groups related files, and its name matches the folder path on disk. Import brings a class from another package into your file so you can use its short name. You can also write a fully-qualified name, import a whole package with a wildcard, or static import a single static member, and classes in your own package need no import. And java dot lang, home to String, System, and Math, never needs an import, it's always there. That's Chapter 3 done, next up, Chapter 4, actually calling methods and working with objects hands-on.",
    },
]
