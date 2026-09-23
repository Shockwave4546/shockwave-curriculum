BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>Implementing ArrayList Algorithms</h1>
      <p class="scr-sub">Every array pattern from 9.5, now on ArrayList.</p>
    </div>''',
        "speak": "Good news: every single pattern from lesson 9.5, sum, average, min, max, search, property checks, duplicates, reversing, transfers directly to array list. Just swap square-bracket i and length for get of i and size.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static double</span> average(<span class="t">ArrayList</span>&lt;<span class="t">Double</span>&gt; nums)
{
    <span class="k">double</span> sum = <span class="n">0</span>;
    <span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; nums.size(); i++)
    {
        sum += nums.get(i);
    }
    <span class="k">return</span> sum / nums.size();
}</code></pre>''',
        "speak": "The accumulator pattern, unchanged in shape, just with get and size instead of square brackets and length.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">for</span> (<span class="k">int</span> i = <span class="n">0</span>; i &lt; nums.size(); i++)
{
    <span class="k">for</span> (<span class="k">int</span> j = i + <span class="n">1</span>; j &lt; nums.size(); j++)
    {
        <span class="k">if</span> (nums.get(i).equals(nums.get(j))) <span class="c">// .equals(), not ==</span>
        {
            <span class="k">return true</span>;
        }
    }
}</code></pre>''',
        "speak": "But there's one genuinely important difference. For an array list of Integer, or any object type, comparing with double equals checks identity, not value, so duplicates checks have to use dot equals instead. This is the single most common array-list-specific mistake, so get comfortable with it now.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static void</span> rotateRight(<span class="t">ArrayList</span>&lt;<span class="t">Double</span>&gt; nums)
{
    <span class="k">double</span> last = nums.get(nums.size() - <span class="n">1</span>);
    <span class="k">for</span> (<span class="k">int</span> i = nums.size() - <span class="n">1</span>; i &gt; <span class="n">0</span>; i--)
    {
        nums.set(i, nums.get(i - <span class="n">1</span>));
    }
    nums.set(<span class="n">0</span>, last);
}</code></pre>''',
        "speak": "Here's rotate right, done in place, purely with get and set. Save the last element first, then walk backward, shifting every element up one slot into its neighbor's old spot, and finally drop the saved last element into slot 0.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt; autoNames = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt;();
<span class="t">ArrayList</span>&lt;<span class="t">Double</span>&gt; autoTimes = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">Double</span>&gt;();
<span class="c">// autoTimes.get(i) is the recorded time for autoNames.get(i)</span></code></pre>''',
        "speak": "And the same parallel-collections idea from Chapter 9's very first lesson works here too, two array lists, kept in sync by index, instead of two arrays.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Comparing objects with double equals instead of .equals() &mdash; unreliable, even for boxed numbers.</li>
      <li><span class="check">!</span>Using array syntax (square brackets) out of habit &mdash; doesn't compile on an ArrayList.</li>
      <li><span class="check">!</span>Forgetting size() changes as you add/remove &mdash; a bound computed once can go stale.</li>
    </ul></div>''',
        "speak": "Three pitfalls. Comparing objects with double equals instead of dot equals, this is unreliable even for boxed numbers like Integer, always use dot equals for content. Using square brackets out of habit, that simply doesn't compile on an array list. And forgetting that size changes as you add or remove, a loop bound computed once before a series of removals can quietly go stale.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Every array algorithm pattern transfers directly to ArrayList.</li>
      <li><span class="check">&#10003;</span>Compare ArrayList elements with .equals(), not ==, for object types.</li>
      <li><span class="check">&#10003;</span>Parallel ArrayLists keep related data in sync by index, same as parallel arrays.</li>
    </ul></div>''',
        "speak": "So, to recap. Every array algorithm pattern, accumulator, min, max, search, duplicates, rotate, reverse, transfers directly to array list. Always compare array list elements with dot equals, not double equals, whenever the element type is an object. And parallel array lists keep related data in sync by index, exactly like parallel arrays. Next up, lesson 9.8, reading real data in from a text file.",
    },
]
