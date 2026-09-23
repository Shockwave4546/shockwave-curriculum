BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>ArrayList Traversals</h1>
      <p class="scr-sub">Same loop shapes as arrays &mdash; with one real restriction to respect.</p>
    </div>''',
        "speak": "Everything you already know about looping through an array carries straight over to array list. For-each, indexed for, and while all work exactly the same way, just with get of i instead of square-bracket i, and size instead of length.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="t">String</span> log : logs) { System.out.println(log); }             <span class="c">// for-each — read-only pass</span>
<span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; logs.size(); i++) { System.out.println(logs.get(i)); } <span class="c">// indexed</span></code></pre>''',
        "speak": "Here they are side by side, for-each for a simple read-only pass, and the indexed version when you need the position, or plan to change something as you go.",
    },
    {
        "screen": '''<div class="scr-diagram">
      <div class="dbox err">for-each</div>
      <div class="darrow">&times;</div>
      <div class="dbox">add / remove</div>
    </div>
    <p style="text-align:center;color:var(--ink-soft);font-size:13px;margin-top:16px;">Resizing an ArrayList mid-for-each throws ConcurrentModificationException.</p>''',
        "speak": "Here's the one real restriction, and it matters. Adding or removing elements from an array list while a for-each loop is actively traversing it throws a Concurrent Modification Exception. If you need to add or remove while looping, you have to switch to an indexed for loop, or a while loop, instead.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">int</span> i = <span class="n">0</span>;
<span class="k">while</span> (i &lt; logs.size())
{
    <span class="k">if</span> (shouldRemove(logs.get(i)))
    {
        logs.remove(i); <span class="c">// don't increment i here — the next element just shifted into index i</span>
    }
    <span class="k">else</span>
    {
        i++; <span class="c">// only advance when nothing was removed this iteration</span>
    }
}</code></pre>''',
        "speak": "Removing while looping needs real care. Removing an element shifts every later element down by one index. If you increment the index unconditionally right after a removal, you skip checking the element that just got shifted into the spot you were on. The fix: only advance i on the iterations where nothing got removed.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">Subsystem</span>&gt; subsystems = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">Subsystem</span>&gt;();
<span class="t">String</span> firstName = subsystems.get(<span class="n">0</span>).getName(); <span class="c">// chain: get the object, then call a method on it</span></code></pre>''',
        "speak": "Chapter 7's chaining idea applies directly here too, get the object out of the list, then immediately call a method on it, one line, as long as you know exactly what get returns.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Adding/removing inside a for-each loop &mdash; throws ConcurrentModificationException.</li>
      <li><span class="check">!</span>Incrementing the index unconditionally after a remove &mdash; skips the shifted element.</li>
      <li><span class="check">!</span>Using less-than-or-equal against size() &mdash; same off-by-one risk as arrays.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Never add or remove inside a for-each loop, that throws a Concurrent Modification Exception every time. Don't increment the index unconditionally right after a remove, that skips the element that just shifted into the vacated slot. And watch for less-than-or-equal-to against size, same off-by-one risk as an array, the last valid index is always size minus 1.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>ArrayList supports the same loop shapes as arrays, with get(i)/size() instead of [i]/length.</li>
      <li><span class="check">&#10003;</span>Never add or remove elements from an ArrayList while traversing it with for-each.</li>
      <li><span class="check">&#10003;</span>When removing in an indexed/while loop, only advance the index when nothing was removed.</li>
    </ul></div>''',
        "speak": "So, to recap. Array list supports the exact same loop shapes as arrays, just with get of i and size instead of square brackets and length. Never add or remove elements from an array list while a for-each loop is traversing it. And when removing inside an indexed or while loop, only advance the index on iterations where nothing was removed. Next up, lesson 9.7, real algorithms built on array list.",
    },
]
