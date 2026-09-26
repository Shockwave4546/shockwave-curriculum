BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 24 &middot; Optional: Avoiding NullPointerExceptions</div>
      <h1>Optional: Avoiding Null Pointer Exceptions</h1>
      <p class="scr-sub">Making &ldquo;there might not be a value&rdquo; part of the type itself.</p>
    </div>''',
        "speak": "Welcome to Chapter 24. Today is about Optional, a way to make the possibility of no value visible right in a method's type, instead of hiding it behind a null.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Null Problem</h2><ul>
      <li><span class="num">1</span><span>Returning <code>null</code> to mean &ldquo;no value here&rdquo; is one of Java's most common bug sources</span></li>
    </ul></div>''',
        "speak": "Returning null to mean there's no value here is one of the most common sources of bugs in any Java program. Tony Hoare, who introduced the null reference in nineteen sixty-five, later called it his billion-dollar mistake.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Null Problem</h2><ul>
      <li><span class="num">1</span><span>Returning <code>null</code> to mean &ldquo;no value here&rdquo; is one of Java's most common bug sources</span></li>
      <li><span class="num">2</span><span><code>null</code> is invisible in a signature &mdash; nothing about <code>Pose2d getVisionPose()</code> warns you</span></li>
    </ul></div>''',
        "speak": "The trouble is that null is invisible in a method's signature. Nothing about Pose2d get vision pose warns a caller that it might come back null. So it's easy to forget the check, and get a Null Pointer Exception instead, the same one from Chapters 12 and 13.",
        "continues": True,
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Classic FRC Case</h2><ul>
      <li><span class="num">1</span><span>A vision pose estimator can only report a position if a camera sees an AprilTag <strong>this frame</strong></span></li>
      <li><span class="num">2</span><span>Returning <code>null</code> on the other frames makes every caller remember to check</span></li>
    </ul></div>''',
        "speak": "The classic FRC case is vision. A pose estimator can only report a robot position if a camera actually sees an April Tag this frame, and plenty of frames, it can't. Returning null on those frames leaves every single caller responsible for remembering to check first.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2"><code>Optional&lt;T&gt;</code></h2><ul>
      <li><span class="num">1</span><span>A container that either holds a value, or is explicitly <strong>empty</strong></span></li>
      <li><span class="num">2</span><span>Unlike <code>null</code>, that possibility is written into the return type</span></li>
    </ul></div>''',
        "speak": "Java's Optional is a container that either holds a value, or is explicitly empty. And unlike null, that possibility is written directly into the method's return type.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public</span> <span class="t">Optional&lt;Pose2d&gt;</span> <span class="me">getPose</span>()
{
    <span class="k">if</span> (!hasTargetThisFrame())
    {
        <span class="k">return</span> Optional.empty();       <span class="c">// explicitly "no value" — not null</span>
    }
    <span class="k">return</span> Optional.of(currentPose);   <span class="c">// wraps a real, non-null value</span>
}</code></pre>''',
        "speak": "Here's the vision method, rewritten. With no target this frame, it returns Optional dot empty, explicitly no value, not null. Otherwise, it returns Optional dot of the current pose, wrapping a real, non-null value.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Type Documents It</h2><ul>
      <li><span class="num">1</span><span>Just reading <code>Optional&lt;Pose2d&gt; getPose()</code>, a caller knows the pose might not be there</span></li>
      <li><span class="num">2</span><span>No comment or tribal knowledge required</span></li>
    </ul></div>''',
        "speak": "Just by reading that signature, an Optional of Pose2d, a caller already knows the pose might not be there this frame. The type itself documents it, instead of relying on a comment, or on tribal knowledge.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Optional&lt;Pose2d&gt;</span> empty = Optional.empty();       <span class="c">// definitely no value</span>

<span class="c">// wraps a value — throws immediately if currentPose is null</span>
<span class="t">Optional&lt;Pose2d&gt;</span> present = Optional.of(currentPose);

<span class="c">// empty if currentPose is null, present otherwise</span>
<span class="t">Optional&lt;Pose2d&gt;</span> maybe = Optional.ofNullable(currentPose);</code></pre>''',
        "speak": "There are three ways to create one. Optional dot empty, definitely no value. Optional dot of, which wraps a value, and throws immediately if that value is null. And Optional dot of nullable, which gives you an empty Optional if the value is null, and a present one otherwise.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2"><code>Optional.of(...)</code> Is a Safety Check</h2><ul>
      <li><span class="num">1</span><span>Pass it a <code>null</code> by accident, and it throws right away</span></li>
      <li><span class="num">2</span><span>Fail loudly at the source, not confusingly somewhere else later</span></li>
    </ul></div>''',
        "speak": "That throwing behavior in Optional dot of is a deliberate safety check. If you accidentally pass it a null, it throws right away. It's better to fail loudly at the source, than to silently wrap a null and have it surface as a confusing failure somewhere else, later.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">Optional&lt;Pose2d&gt;</span> visionPose = vision.getPose();

<span class="c">// Run logic only when a value exists</span>
visionPose.ifPresent(pose -&gt; estimator.addVisionMeasurement(pose, timestamp));

<span class="c">// Or supply a fallback value for the empty case</span>
<span class="t">Pose2d</span> fallbackPose = visionPose.orElse(lastKnownPose);

<span class="c">// Or throw a specific exception if a value was truly required</span>
<span class="t">Pose2d</span> requiredPose = visionPose.orElseThrow(
    () -&gt; <span class="k">new</span> IllegalStateException(<span class="s">"No vision pose"</span>));</code></pre>''',
        "speak": "Now the caller's side, handling both cases honestly. Three options. If present runs some logic only when a value exists. Or else supplies a fallback value for the empty case. And or else throw, given a lambda that builds the exception, throws a specific exception, here an Illegal State Exception, only if a value was truly required and never found.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three Honest Ways to Handle It</h2><ul>
      <li><span class="num">1</span><span><code>ifPresent</code> &mdash; runs a lambda only if a value is there</span></li>
      <li><span class="num">2</span><span><code>orElse</code> &mdash; supplies a fallback for the empty case</span></li>
      <li><span class="num">3</span><span><code>orElseThrow</code> &mdash; for when empty really means something went wrong</span></li>
    </ul></div>''',
        "speak": "If present runs a lambda, from Lesson 19.1, only if a value is actually there, and nothing happens otherwise. Or else supplies a fallback value for the empty case. And or else throw is for the rarer case where an empty Optional really does mean something has gone wrong, and continuing anyway wouldn't make sense.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">A Few More Useful Methods</h2><ul>
      <li><span class="num">1</span><span>No-argument <code>orElseThrow()</code> &mdash; throws <code>NoSuchElementException</code></span></li>
      <li><span class="num">2</span><span><code>orElseGet(supplier)</code> &mdash; lazy, unlike eager <code>orElse</code></span></li>
      <li><span class="num">3</span><span><code>ifPresentOrElse(consumer, runnable)</code> &mdash; a present/empty pair of callbacks</span></li>
    </ul></div>''',
        "speak": "A few less common, but genuinely useful, methods round this out. A no-argument or else throw, which throws No Such Element Exception when nothing more specific is needed. Or else get, like or else, but it only computes its fallback value when it's actually needed, instead of always. And if present or else, which runs one callback if a value is present, and a different one if it's empty, since if present alone has no else.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// never do this blind — this is a NullPointerException with extra steps</span>
<span class="t">Pose2d</span> uncheckedPose = visionPose.get();</code></pre>''',
        "speak": "Now the one pitfall that defeats the whole point. Optional also has a get method, that returns the wrapped value. But calling get on an empty Optional, without checking first, throws a No Such Element Exception. That's exactly the same class of crash Optional exists to prevent, just under a different exception name, a null pointer exception with extra steps.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Skip Bare <code>get()</code></h2><ul>
      <li><span class="num">1</span><span>Even <code>isPresent()</code> + <code>get()</code> is discouraged &mdash; a null check in disguise</span></li>
      <li><span class="num">2</span><span><code>ifPresent</code>, <code>orElse</code>, and <code>orElseThrow</code> handle both cases directly</span></li>
    </ul></div>''',
        "speak": "Even the safer pairing, checking is present first, and then calling get, is discouraged. It's really just a nested null check in disguise. If present, or else, and or else throw all handle both cases directly, without ever needing to call bare get.",
    },
    {
        "screen": '''<pre class="code"><code>visionPose
    <span class="c">// only proceed if the pose has a valid X coordinate</span>
    .filter(pose -&gt; pose.getX() &gt;= <span class="n">0</span>)
    .ifPresent(pose -&gt; estimator.addVisionMeasurement(pose, timestamp));</code></pre>''',
        "speak": "One brief look beyond the core methods. Filter keeps the value only if it matches a condition, and otherwise becomes empty. Here, a pose only gets passed on to the estimator if it has a valid X coordinate.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">double</span> dashboardX = visionPose.map(pose -&gt; pose.getX()).orElse(<span class="n">0.0</span>);</code></pre>''',
        "speak": "Map transforms the value inside an Optional, without ever having to check is present first. Here, visionPose dot map, pose arrow pose dot get X, turns an Optional of Pose2d into an Optional of Double, present with the X coordinate if visionPose had a value, empty otherwise. And or else zero point zero then unwraps that down to a plain double either way.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Filtering and Transforming</h2><ul>
      <li><span class="num">1</span><span><code>filter</code> &mdash; keep the value only if it matches a condition</span></li>
      <li><span class="num">2</span><span><code>map</code> &mdash; transform the value, if present, into something else</span></li>
    </ul></div>''',
        "speak": "Filter and map are useful for chaining a couple of extra checks without falling back into nested if statements. They compose well for simple cases, though genuinely complex chains of Optional transformations are a more advanced topic than this curriculum covers in depth.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Calling <code>.get()</code> without checking first &mdash; it throws on an empty Optional.</li>
      <li><span class="check">!</span>Using Optional for every field or parameter, out of habit.</li>
      <li><span class="check">!</span>Passing a <code>null</code> to <code>Optional.of(...)</code> &mdash; use <code>ofNullable</code> instead.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Calling get without checking first, it throws on an empty Optional, defeating the entire purpose of using one. Using Optional for every field or parameter, out of habit, it's meant for genuinely optional results, especially return values, not as a blanket replacement for every reference type in a program. And passing a null to Optional dot of, that throws immediately, so use Optional dot of nullable instead, whenever the value genuinely might be null.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Optional&lt;T&gt; makes &ldquo;might not have a value&rdquo; visible in the return type.</li>
      <li><span class="check">&#10003;</span>Create with empty(), of(value), or ofNullable(value).</li>
      <li><span class="check">&#10003;</span>Handle with ifPresent, orElse, or orElseThrow &mdash; never bare get().</li>
      <li><span class="check">&#10003;</span>filter and map chain extra checks without nested ifs.</li>
      <li><span class="check">&#10003;</span>orElseGet, ifPresentOrElse, and no-arg orElseThrow cover the less common cases.</li>
    </ul></div>''',
        "speak": "So, to recap. Optional makes this might not have a value visible directly in a method's return type, instead of relying on an invisible, easy to forget null check. Create one with Optional dot empty, Optional dot of, which throws if the value is null, or Optional dot of nullable, which is safe either way. Handle both cases with if present, with or else, or with or else throw, and never call bare get without checking first. Filter and map let you chain a couple of extra conditions and transformations, without falling back into nested if checks. And or else get, if present or else, and a no-argument or else throw round out the less common cases. Next up, Chapter 25: command-based programming.",
    },
]
