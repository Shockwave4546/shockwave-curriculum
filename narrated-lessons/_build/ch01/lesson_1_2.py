BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 1 &middot; Java Foundations</div>
      <h1>Intro to Algorithms, Programming and Compilers</h1>
      <p class="scr-sub">A live walkthrough &mdash; press play and follow along.</p>
    </div>''',
        "speak": "Welcome back. Now that you know why FRC teams use Java, let's get your very first Java program up and running.",
    },
    {
        "screen": '''<div class="scr-steps">
      <div class="step"><span class="n">1</span><span>Wake up</span></div>
      <div class="arrow">&darr;</div>
      <div class="step"><span class="n">2</span><span>Get dressed</span></div>
      <div class="arrow">&darr;</div>
      <div class="step"><span class="n">3</span><span>Drive to school</span></div>
      <div class="label">= an algorithm &mdash; an ordered set of steps</div>
    </div>''',
        "speak": "First, what is an algorithm? It's just an ordered set of steps, a recipe, directions to a friend's house. Your program is exactly the same idea: steps that run one at a time, in order. We call that sequencing.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// pseudocode &mdash; not real code, just the plan</span>
<span class="k">IF</span> sensor sees game piece
    <span class="k">THEN</span> stop intake motor</code></pre>''',
        "speak": "Before you write real code, it actually helps to plan it out first, in plain English, or what's called pseudocode. Getting the steps straight on paper is what turns a half-baked idea into code that actually works.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">MyClass</span>
{

}</code></pre>''',
        "speak": "Every Java program starts inside a class. Here's the shell we'll build on next -- nothing runs yet, since there's no main method inside it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">MyClass</span>
{
    <span class="k">public static void</span> <span class="me">main</span>(<span class="t">String</span>[] args)
    {

    }
}</code></pre>''',
        "speak": "And every class you actually run needs one very specific method, with this exact signature: main. That's where execution starts. Treat the signature itself as boilerplate for now -- each piece gets its own full explanation later, String array args in Chapter 4, public and static more fully in Chapter 7.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">MyClass</span>
{
    <span class="k">public static void</span> <span class="me">main</span>(<span class="t">String</span>[] args)
    {
        System.out.<span class="me">println</span>(<span class="s">"Hi there!"</span>);
    }
}</code></pre>''',
        "speak": "Drop one line inside, and you've got a complete, runnable program.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">public class MyClass</div>
      <div class="darrow">=</div>
      <div class="dbox active">MyClass.java</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:14px;margin-top:18px;">When you compile normally, the file name must match the class name &mdash; exactly.</p>''',
        "speak": "One more rule about that class: when you compile normally, the file itself has to be named exactly after the public class inside it. Since we wrote public class MyClass, the file has to be named MyClass dot java. Running a single file directly skips this rule, but matching the names is still the habit to build.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">void</span> <span class="me">main</span>()
{
    System.out.<span class="me">println</span>(<span class="s">"Hi there!"</span>);
}</code></pre>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:14px;">Java 25 (JEP 512) &mdash; a shorter form for quick scripts. This course always uses the full form above.</p>''',
        "speak": "On Java 25, you might also see an even shorter form: void main, with no class and no public static. It's a newer shortcut for quick scripts, added by a change called JEP 512. This course always uses the full form you just saw, since it works unchanged on Java 17 too.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public class</span> <span class="t">MyClass</span>
<span class="hl">{</span>
    <span class="k">public static void</span> <span class="me">main</span>(<span class="t">String</span>[] args)
    <span class="hl">{</span>
        System.out.<span class="me">println</span>(<span class="s">"Hi there!"</span>);
    <span class="hl">}</span>
<span class="hl">}</span></code></pre>''',
        "speak": "Notice something: every open curly brace needs a matching close brace. Miscount those, and the compiler will let you know.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>System.out.<span class="me">println</span>(<span class="s">"Hi there!"</span>)<span class="hl">;</span></code></pre>''',
        "speak": "Every single instruction, we call it a statement, ends with a semicolon. Think of it like a period at the end of a sentence. Forget it, and the code won't even compile. Everybody forgets this one at some point, it's basically a rite of passage. Not everything ends with a semicolon, though. A line that just opens a block, like the class line or the main line, has no semicolon before its curly brace.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox">Your Code</div><div class="darrow">&rarr;</div>
      <div class="dbox active">Compiler</div><div class="darrow">&rarr;</div>
      <div class="dbox">Runs on the Robot</div>
    </div>
    <div class="scr-diagram" style="margin-top:14px;">
      <div class="darrow" style="transform:rotate(90deg);">&#8618;</div>
      <div class="dbox err">Syntax Error</div>
    </div>''',
        "speak": "So how does your code actually become something the robot runs? A compiler reads it, checks for mistakes, and translates it into something the machine understands. If it finds a problem, that's called a syntax error, caught before your program ever runs a single line.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Where You'll Actually Write This</h2><ul>
      <li><span class="num">1</span><span><strong>Your own IDE</strong> &mdash; like VS Code with the Java extension. This is genuinely how most FRC teams write real robot code.</span></li>
      <li><span class="num">2</span><span><strong>An online IDE</strong> &mdash; like Replit, if you don't want to install anything yet.</span></li>
    </ul></div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:14px;">Write and run it there to see it actually work. This lesson's exercises are multiple-choice and reorder puzzles.</p>''',
        "speak": "So where do you actually write and run this? For this course, you've got two options. Use your own IDE, something like Visual Studio Code with the Java extension, which is genuinely how most FRC teams write real robot code, so it's good practice either way. Or, if you don't want to install anything yet, use an online IDE like Replit. Write and run your code there to see it actually work -- this lesson's own exercises are multiple-choice and reorder puzzles, so there's no code to submit for them yet. A text-submit coding checker, for later chapters, is still being built.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>public&nbsp;&nbsp;class&nbsp;&nbsp;void</code><div class="nlabel">keywords &mdash; reserved, always lowercase</div></div>
    </div>''',
        "speak": "Now, naming things. Words like public, class, and void are keywords. They're reserved, always lowercase, and you can't reuse them for your own names.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code style="color:var(--blue);">motorSpeed</code><code style="color:var(--blue);opacity:0.65;margin-left:10px;">calculateTotal()</code><div class="nlabel">lowerCamelCase &mdash; variables &amp; methods</div></div>
      <div class="namerow"><code style="color:var(--vsc-ty);">Drivetrain</code><code style="color:var(--vsc-ty);opacity:0.65;margin-left:10px;">String</code><div class="nlabel">PascalCase &mdash; classes &amp; interfaces</div></div>
      <div class="namerow"><code style="color:var(--accent);">MAX_SPEED</code><code style="color:var(--accent);opacity:0.65;margin-left:10px;">PI</code><div class="nlabel">SCREAMING_SNAKE_CASE &mdash; constants</div></div>
    </div>''',
        "speak": "Everything else you name yourself follows one of three styles. LowerCamelCase, start lowercase, then capitalize each new word, that's for variables and methods, like motorSpeed, or a method like calculateTotal. PascalCase, capitalize every word including the first, that's for classes and interfaces, like Drive Train, or a built-in one like String. And SCREAMING SNAKE CASE, all uppercase, underscores between words, that's for constants, values that never change, like Max underscore Speed, or PI. You'll meet real constants starting in Chapter 7.4; final, what actually makes a value a constant, gets full treatment in Chapter 23.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t" style="text-decoration:underline;text-decoration-color:var(--vsc-ty);text-underline-offset:4px;">System</span>.out.<span class="me" style="text-decoration:underline;text-decoration-color:var(--vsc-me);text-underline-offset:4px;">println</span>(<span class="s">"Hi there!"</span>);</code></pre>
    <div style="display:flex;gap:24px;justify-content:center;margin-top:16px;font-size:13px;">
      <div style="color:var(--vsc-ty);">System &mdash; a class, so PascalCase</div>
      <div style="color:var(--vsc-me);">println &mdash; a method, so lowerCamelCase</div>
    </div>''',
        "speak": "That's actually why System dot out dot println looks the way it does. System is a class, so it's PascalCase. println is a method, here it's just one word, so there's no second word to capitalize, but it still starts lowercase like every method name does. Once you know the naming rules, code like this stops looking arbitrary.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox err">Syntax Error</div>
      <div class="dbox">Run-Time Error</div>
    </div>
    <div style="display:flex;gap:14px;justify-content:center;margin-top:12px;max-width:520px;margin-left:auto;margin-right:auto;">
      <div style="flex:1;font-size:13px;color:var(--ink-soft);text-align:center;">Caught by the compiler, before your program ever runs.</div>
      <div style="flex:1;font-size:13px;color:var(--ink-soft);text-align:center;">Happens while the program is running, after it already compiled.</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Both are normal. Finding and fixing them is called <strong style="color:var(--accent);">debugging</strong> &mdash; an error is informally a &ldquo;bug.&rdquo;</p>''',
        "speak": "Errors come in two flavors. A syntax error is caught by the compiler, before your program ever runs, a missing semicolon, an unmatched brace or quote. A run-time error happens while the program is actually running, after it already compiled, like dividing a whole number by zero. Both are completely normal. Finding and fixing them is called debugging, informally, an error is just a bug. And if you're ever stuck, try explaining your code out loud, line by line, even to an inanimate object, it's a real technique called rubber duck debugging, and it often reveals the problem before you even finish explaining it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">/*
 * MyClass.java
 * Prints a friendly greeting to the console.
 */</span>
<span class="k">public class</span> <span class="t">MyClass</span>
{
    ...
}</code></pre>
    <p style="text-align:center;color:var(--ink-soft);font-size:12.5px;margin-top:12px;">A <strong style="color:var(--accent);">block comment</strong> (<code>/* ... */</code>) can span multiple lines &mdash; the classic way to explain what a whole file does, right at the top.</p>
    <pre class="code" style="margin-top:14px;padding:12px 18px;"><code><span class="c">// this line is ignored by the compiler</span>
System.out.<span class="me">println</span>(<span class="s">"Hi there!"</span>); <span class="c">// so is this part, after the //</span></code></pre>
    <p style="text-align:center;color:var(--ink-soft);font-size:12px;margin-top:8px;">A <strong>line comment</strong> (<code>//</code>) only runs to the end of that one line.</p>''',
        "speak": "One more thing before we wrap up: comments. A block comment, slash-star, star-slash, can span multiple lines, and it's the classic way to explain what an entire file does, right at the top, what this class is for, what it's responsible for. You'll see this pattern constantly in real FRC codebases. Two slashes work differently, they only comment out the rest of that one line, handy for a quick note right next to a specific piece of code. Either way, the compiler ignores comments completely. They exist purely to explain your code to yourself, and to your teammates.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Missing a semicolon &mdash; the single most common first error. Check the end of the line the compiler points at, and the line just before it.</li>
      <li><span class="check">!</span>Mismatched capitalization &mdash; System is capitalized because it's a class; public, class, void are not, because they're keywords.</li>
      <li><span class="check">!</span>Trusting the error's line number completely &mdash; the compiler tells you where it noticed the problem, sometimes a line or two after the real mistake.</li>
    </ul></div>''',
        "speak": "Before we wrap up, three common pitfalls to watch for. Missing a semicolon is the single most common first error, check the end of the line the compiler points at, and the line just before it. Mismatched capitalization trips people up too, System is capitalized because it's a class, but public, class, and void are not, because they're keywords. Java is case-sensitive everywhere. And don't trust the error's line number completely, the compiler tells you where it noticed the problem, which is sometimes a line or two after where the actual mistake actually is.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>An algorithm is ordered steps, run in sequence.</li>
      <li><span class="check">&#10003;</span>Plan in plain English or pseudocode before you code.</li>
      <li><span class="check">&#10003;</span>Every program has a class and a main method &mdash; file name must match when you compile normally.</li>
      <li><span class="check">&#10003;</span>Every statement ends with a semicolon (except block openers).</li>
      <li><span class="check">&#10003;</span>Three naming styles: camelCase, PascalCase, SCREAMING_SNAKE_CASE.</li>
      <li><span class="check">&#10003;</span>A compiler catches syntax errors before runtime; run-time errors happen after.</li>
      <li><span class="check">&#10003;</span>Write code in a real IDE (or online one) to see it run; exercises here are multiple-choice and reorder puzzles.</li>
      <li><span class="check">&#10003;</span>Comments (// and /* */) are ignored by the compiler.</li>
    </ul></div>''',
        "speak": "Let's recap. An algorithm is just an ordered set of steps, run in sequence. Before writing real code, plan it out in plain English or pseudocode. Every program needs a class and a main method, and remember, the file name has to match the class name exactly when you compile normally. Every statement ends with a semicolon, except lines that just open a block. Naming follows three styles: camelCase, PascalCase, and SCREAMING SNAKE CASE. A compiler catches syntax errors before your code ever runs, while run-time errors show up after it's already running. Write your code in a real IDE, or an online one, to see it actually run -- this chapter's exercises are multiple-choice and reorder puzzles, not a code checker. And comments, both two slashes, and slash-star star-slash, are ignored by the compiler entirely. That's the full foundation for Chapter 1. From here, you can continue on to Chapter 2, or if you'd like some hands-on practice first, head over to the exercises section. Nice work, see you next time.",
    },
]
