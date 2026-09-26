BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 15 &middot; Advanced Collections</div>
      <h1>Advanced Collections</h1>
      <p class="scr-sub">Set, Queue, Deque &mdash; and a deeper look at Map.</p>
    </div>''',
        "speak": "Chapter 9 covered ArrayList and a basic HashMap. Chapter 15 rounds out the toolbox with three more collection types, each solving a problem the others don't.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Three More Tools</h2><ul>
      <li><span class="num">1</span><span><strong>Set</strong> &mdash; no duplicates, ever</span></li>
      <li><span class="num">2</span><span><strong>Queue</strong> / <strong>Deque</strong> &mdash; order of processing matters more than random access</span></li>
      <li><span class="num">3</span><span><strong>Map</strong>, revisited &mdash; iterating keys and values together, and choosing an ordering</span></li>
    </ul></div>''',
        "speak": "Set, for when you need no duplicates, ever. Queue, and its double-ended cousin, the deck, for when the order of processing matters more than random access. And a deeper look at Map: iterating keys and values together, and choosing an ordering.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Quick Vocabulary Note</h2><ul>
      <li><span class="num">1</span><span>Just like <code>ArrayList</code> implements <code>List</code>, <code>Set</code>/<code>Queue</code>/<code>Deque</code>/<code>Map</code> are themselves <strong>interfaces</strong>, not classes</span></li>
      <li><span class="num">2</span><span><code>new Set&lt;Integer&gt;()</code> isn&rsquo;t legal &mdash; construct <code>HashSet</code>, <code>TreeSet</code>, and so on, stored as the interface type</span></li>
    </ul></div>''',
        "speak": "One quick vocabulary note before diving in. Just like ArrayList, from Chapter 9, is really an implementation of the List interface, Set, Queue, Deque, and Map are themselves interfaces, not classes. You never write new Set of Integer — that doesn't compile — only new HashSet, new TreeSet, and so on, stored in a variable declared by the interface type. Chapter 19 covers what an interface actually is; for now, read Set, Queue, and Map as the name for a family of collection classes that all support this common set of operations.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 15 &middot; Advanced Collections</div>
      <h1>Set: No Duplicates, Ever</h1>
      <p class="scr-sub">Adding something already present does nothing.</p>
    </div>''',
        "speak": "First up, Set. A Set is a collection that flatly refuses duplicate elements.",
    },
    {
        "screen": '''<pre class="code"><code>Set&lt;Integer&gt; usedCanIds = <span class="k">new</span> HashSet&lt;Integer&gt;();
usedCanIds.add(<span class="n">5</span>);  <span class="c">// true — added</span>
usedCanIds.add(<span class="n">5</span>);  <span class="c">// false — already present, nothing changed</span></code></pre>''',
        "speak": "Calling add with something that's already present just does nothing, and returns false, rather than adding a second copy. The first add of five returns true. The second returns false, and the set is unchanged.",
    },
    {
        "screen": '''<pre class="code"><code>Set&lt;Integer&gt; seenIds = <span class="k">new</span> HashSet&lt;Integer&gt;();
<span class="k">for</span> (<span class="t">int</span> id : allConfiguredCanIds)
{
    <span class="k">if</span> (!seenIds.add(id)) <span class="c">// add() returns false if it was already there</span>
    {
        reportWarning(<span class="s">"Duplicate CAN ID detected: "</span> + id);
    }
}</code></pre>''',
        "speak": "That makes Set the natural tool for catching configuration conflicts, like verifying no two devices on the robot were accidentally wired to the same Can ID. Because add returns false when the ID was already there, a single if-not-add check flags every duplicate as the loop finds it. Here, allConfiguredCanIds and reportWarning stand in for this team's own array and logging method — this snippet is a fragment, not a complete program.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>HashSet</code><span class="nlabel">fastest &mdash; no ordering guarantee (the usual default)</span></div>
      <div class="namerow"><code>LinkedHashSet</code><span class="nlabel">remembers insertion order</span></div>
      <div class="namerow"><code>TreeSet</code><span class="nlabel">keeps elements sorted</span></div>
    </div>''',
        "speak": "Hash Set is the usual default. It's the fastest, with no ordering guarantee. Linked Hash Set remembers insertion order, and Tree Set keeps elements sorted. All three still refuse duplicates. They mainly differ in iteration order, plus one extra requirement for Tree Set that's coming up in the pitfalls.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>s1.containsAll(s2)</code><span class="nlabel">subset &mdash; is s2 inside s1?</span></div>
      <div class="namerow"><code>s1.addAll(s2)</code><span class="nlabel">union</span></div>
      <div class="namerow"><code>s1.retainAll(s2)</code><span class="nlabel">intersection &mdash; keep only what&rsquo;s in both</span></div>
      <div class="namerow"><code>s1.removeAll(s2)</code><span class="nlabel">difference &mdash; remove anything also in s2</span></div>
    </div>''',
        "speak": "Set also supports set algebra directly as methods. contains All asks whether s2 is a subset of s1. add All is union. retain All is intersection, keeping only what's in both. And remove All is difference, removing anything that's also in s2. All three of add All, retain All, and remove All change s1 in place and return a boolean for whether s1 actually changed — none of them returns a new set. To keep the originals untouched, copy s1 first.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 15 &middot; Advanced Collections</div>
      <h1>Queue: First-In, First-Out</h1>
      <p class="scr-sub">Elements held for later processing, oldest first.</p>
    </div>''',
        "speak": "Next, Queue. A Queue holds elements for later processing, normally in first-in, first-out order. Think of a queue of autonomous routine steps, waiting to run in the order they were scheduled.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>add(e)</code><span class="nlabel">insert &mdash; throws on failure</span></div>
      <div class="namerow"><code>remove()</code><span class="nlabel">remove &mdash; throws on failure</span></div>
      <div class="namerow"><code>element()</code><span class="nlabel">peek, don&rsquo;t remove &mdash; throws on failure</span></div>
    </div>''',
        "speak": "Every Queue operation comes in two flavors. The first flavor throws an exception on failure: add to insert, remove to take one out, and element to look at the front without removing it.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>offer(e)</code><span class="nlabel">insert &mdash; returns false</span></div>
      <div class="namerow"><code>poll()</code><span class="nlabel">remove &mdash; returns null if empty</span></div>
      <div class="namerow"><code>peek()</code><span class="nlabel">peek, don&rsquo;t remove &mdash; returns null if empty</span></div>
    </div>''',
        "speak": "The second flavor returns a safe placeholder value instead. offer returns false if it can't insert. poll and peek return null if the queue is empty.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>Queue&lt;String&gt; pendingFaults = <span class="k">new</span> LinkedList&lt;String&gt;();
pendingFaults.add(<span class="s">"Camera 1 disconnected"</span>);
pendingFaults.add(<span class="s">"Low battery voltage"</span>);

<span class="k">while</span> (!pendingFaults.isEmpty())
{
    <span class="c">// poll() removes and returns the oldest fault first</span>
    System.out.println(<span class="s">"Handling: "</span> + pendingFaults.poll());
}</code></pre>''',
        "speak": "Here, two faults get added to a queue of pending faults. The while loop keeps going until the queue is empty, and each poll removes and returns the oldest fault first. So Camera 1 disconnected gets handled before low battery voltage.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">The Safer Default</h2><ul>
      <li><span class="num">1</span><span><code>poll()</code> / <code>peek()</code> hand back <code>null</code> instead of throwing when the queue is empty</span></li>
      <li><span class="num">2</span><span>An empty queue is often a completely normal state &mdash; no faults right now &mdash; not an error</span></li>
      <li><span class="num">3</span><span>Watch out with <code>Queue&lt;Integer&gt;</code>: <code>int x = q.poll();</code> on an empty queue throws NPE &mdash; unboxing <code>null</code> into <code>int</code></span></li>
    </ul></div>''',
        "speak": "In real code, poll and peek are usually the safer default. They hand back null instead of throwing when the queue happens to be empty, and an empty queue is often a completely normal state, no faults right now, rather than an error. One thing to watch for with a Queue of Integer, though: int x equals q dot poll, on an empty queue, throws a Null Pointer Exception, because assigning that null into a primitive int unboxes it immediately. Check isEmpty first, or keep the result as an Integer instead of unboxing right away.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 15 &middot; Advanced Collections</div>
      <h1>Deque: Both Ends at Once</h1>
      <p class="scr-sub">Pronounced &ldquo;deck&rdquo; &mdash; a double-ended queue.</p>
    </div>''',
        "speak": "A double-ended queue, pronounced deck, supports inserting and removing from either end. That means a single deck can act as a first-in, first-out queue, a last-in, first-out stack, or both.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>addFirst(e) / offerFirst(e)</code><span class="nlabel">insert at the front</span></div>
      <div class="namerow"><code>removeFirst() / pollFirst()</code><span class="nlabel">remove from the front</span></div>
      <div class="namerow"><code>getFirst() / peekFirst()</code><span class="nlabel">examine the front</span></div>
    </div>''',
        "speak": "The same two flavors show up again, once for each end. At the front: add First or offer First to insert, remove First or poll First to remove, and get First or peek First to examine.",
    },
    {
        "screen": '''<div class="scr-naming">
      <div class="namerow"><code>addLast(e) / offerLast(e)</code><span class="nlabel">insert at the back</span></div>
      <div class="namerow"><code>removeLast() / pollLast()</code><span class="nlabel">remove from the back</span></div>
      <div class="namerow"><code>getLast() / peekLast()</code><span class="nlabel">examine the back</span></div>
    </div>''',
        "speak": "And at the back, the exact mirror image: add Last or offer Last, remove Last or poll Last, and get Last or peek Last.",
        "continues": True,
    },
    {
        "screen": '''<pre class="code"><code>Deque&lt;String&gt; climbSteps = <span class="k">new</span> ArrayDeque&lt;String&gt;();
climbSteps.addLast(<span class="s">"Extend to high bar"</span>);
climbSteps.addLast(<span class="s">"Release from mid bar"</span>);

<span class="c">// "Release from mid bar" — undo the most recent step</span>
String lastStep = climbSteps.removeLast();</code></pre>''',
        "speak": "A common use: an undo stack for the last few climb sequence steps. You only ever add and remove from one end, so it's last-in, first-out. The last step added, release from mid bar, is the first one undone.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">ArrayDeque</h2><ul>
      <li><span class="num">1</span><span>The standard general-purpose <code>Deque</code> implementation</span></li>
      <li><span class="num">2</span><span>Generally faster than <code>LinkedList</code> for this purpose, with no capacity limit</span></li>
      <li><span class="num">3</span><span>Stack methods too: <code>push</code>/<code>pop</code>/<code>peek</code> work on the front &mdash; prefer it over the old <code>Stack</code> class</span></li>
    </ul></div>''',
        "speak": "Array Deck is the standard general-purpose implementation. It's generally faster than Linked List for this purpose, with no capacity limit. A Deque also has stack-flavored push, pop, and peek methods, which just work on the front. Prefer Array Deque over the old java-dot-util-dot-Stack class, a legacy holdover with locking overhead this course never needs. A Priority Queue is a different kind of Queue worth knowing the name of: it always polls back the smallest element first, rather than the oldest.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 15 &middot; Advanced Collections</div>
      <h1>Map, Revisited</h1>
      <p class="scr-sub">Iterating both keys and values in one pass.</p>
    </div>''',
        "speak": "Last, Map, revisited. Lesson 9.3 covered put, get, containsKey, getOrDefault, remove, size, and looping over key Set — all of that still applies here. Map's entry Set method gives you every key and value together, in one pass, avoiding a repeated get call for each key.",
    },
    {
        "screen": '''<pre class="code"><code>Map&lt;Integer, Double&gt; motorOffsets = <span class="k">new</span> HashMap&lt;Integer, Double&gt;();
motorOffsets.put(<span class="n">5</span>, <span class="n">0.02</span>);
motorOffsets.put(<span class="n">6</span>, -<span class="n">0.01</span>);

<span class="k">for</span> (Map.Entry&lt;Integer, Double&gt; entry : motorOffsets.entrySet())
{
    System.out.println(<span class="s">"CAN ID "</span> + entry.getKey() + <span class="s">" -&gt; offset "</span> + entry.getValue());
}</code></pre>''',
        "speak": "Each item in the entry Set is a Map dot Entry, a small read-only key and value pair object, with getKey and getValue. Inside the loop, get Key hands back the Can ID, and get Value hands back its offset, with no second lookup needed.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Copying Doesn&rsquo;t Record Put Order</h2><ul>
      <li><span class="num">1</span><span>A copy constructor only preserves the <em>source</em> map&rsquo;s own iteration order</span></li>
      <li><span class="num">2</span><span>Copying a HashMap into a TreeMap: fine &mdash; TreeMap re-sorts by key anyway</span></li>
      <li><span class="num">3</span><span>Copying a HashMap into a LinkedHashMap: keeps HashMap&rsquo;s order, <em>not</em> the original put order</span></li>
    </ul></div>''',
        "speak": "Just like Set, a plain HashMap gives no ordering guarantee. Swapping the implementation type changes that, but a copy constructor only ever preserves the source map's own iteration order. Copying a HashMap into a TreeMap is fine, because a TreeMap re-sorts by key regardless of where the entries came from. Copying a HashMap into a LinkedHashMap, though, just keeps the HashMap's unpredictable order, not the original put order, because that order was never recorded anywhere.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// sorted by key — copying in is fine here, TreeMap always re-sorts</span>
Map&lt;Integer, Double&gt; sorted = <span class="k">new</span> TreeMap&lt;Integer, Double&gt;(motorOffsets);

Map&lt;Integer, Double&gt; byInsertOrder = <span class="k">new</span> LinkedHashMap&lt;Integer, Double&gt;();
byInsertOrder.put(<span class="n">5</span>, <span class="n">0.02</span>);
byInsertOrder.put(<span class="n">6</span>, -<span class="n">0.01</span>); <span class="c">// LinkedHashMap remembers put order, starting from empty</span></code></pre>''',
        "speak": "To actually get insertion order, build the LinkedHashMap from empty and put into it directly, the same way motorOffsets itself was built.",
    },
    {
        "screen": '''<div class="scr-bullets"><h2 class="scr-h2">Declare by the Interface</h2><ul>
      <li><span class="num">1</span><span>Declare as <code>List&lt;E&gt;</code>, <code>Map&lt;K, V&gt;</code>, <code>Set&lt;E&gt;</code>, <code>Queue&lt;E&gt;</code> &mdash; not <code>ArrayList</code>, <code>HashMap</code>, <code>HashSet</code>, <code>LinkedList</code></span></li>
      <li><span class="num">2</span><span>Every line that <em>uses</em> the collection depends only on the interface &mdash; so swapping the implementation is a one-line change</span></li>
    </ul></div>''',
        "speak": "This is the payoff of always declaring a variable by its interface type, List, Map, Set, or Queue, rather than its concrete implementation, like ArrayList, HashMap, Hash Set, or Linked List. Changing which concrete class gets constructed is a one-line change, because every line that uses the collection only ever depends on the interface.",
    },
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 15 &middot; Advanced Collections</div>
      <h1>Fixed Collections</h1>
      <p class="scr-sub"><code>List.of</code>, <code>Set.of</code>, <code>Map.of</code> &mdash; built once, read-only.</p>
    </div>''',
        "speak": "One more tool: fixed collections. For data that's fixed once created, like a small lookup table or a set of valid states, List dot of, Set dot of, and Map dot of build an immutable collection in one line, with no new and no separate add or put calls.",
    },
    {
        "screen": '''<pre class="code"><code>List&lt;String&gt; allianceColors = List.of(<span class="s">"Red"</span>, <span class="s">"Blue"</span>);
Set&lt;Integer&gt; validPracticeFields = Set.of(<span class="n">1</span>, <span class="n">2</span>, <span class="n">3</span>);
Map&lt;String, Integer&gt; startingSlots = Map.of(<span class="s">"Left"</span>, <span class="n">1</span>, <span class="s">"Center"</span>, <span class="n">2</span>, <span class="s">"Right"</span>, <span class="n">3</span>);</code></pre>''',
        "speak": "Calling add, put, or remove on any of these throws an Unsupported Operation Exception. They're meant to be built once and only read afterward.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Assuming a HashSet or HashMap remembers insertion order &mdash; use LinkedHashSet/LinkedHashMap, or TreeSet/TreeMap for sorted order.</li>
      <li><span class="check">!</span>Using remove()/element() on a queue that might be empty &mdash; both throw; prefer poll()/peek().</li>
      <li><span class="check">!</span>Declaring a collection by its concrete type instead of its interface &mdash; it locks every line to that one implementation.</li>
      <li><span class="check">!</span>Putting your own class into a HashSet/HashMap without overriding both equals and hashCode (17.4).</li>
      <li><span class="check">!</span>Putting your own class into a TreeSet/TreeMap without a way to compare it &mdash; ClassCastException (Comparable/Comparator, Ch.19).</li>
    </ul></div>''',
        "speak": "Common pitfalls. Don't assume a Hash Set or HashMap remembers insertion order. Neither does. Reach for the linked versions if insertion order matters, or the tree versions if sorted order does. Don't use remove or element on a queue that might be empty, since both throw. Prefer poll and peek, unless an empty queue genuinely represents a bug that should crash loudly. Don't declare a collection variable by its concrete type. That locks every line that touches it to that one implementation's behavior. Declare it by the interface instead. Don't put your own class into a Hash Set or HashMap without overriding both equals and hashCode together, covered in Lesson 17.4. And don't put your own class into a Tree Set or Tree Map without teaching Java how to compare it, or it throws a Class Cast Exception the first time one gets added — Comparable and Comparator, the tools for that, are covered in Chapter 19.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>List, Set, Queue, Deque, and Map are interfaces, not classes &mdash; ArrayList, HashSet, LinkedList, and HashMap (and friends) implement them.</li>
      <li><span class="check">&#10003;</span>Set guarantees no duplicates: HashSet has no ordering, LinkedHashSet keeps insertion order, TreeSet keeps sorted order.</li>
      <li><span class="check">&#10003;</span>Queue is FIFO by default: add/remove/element throw, offer/poll/peek return a placeholder.</li>
      <li><span class="check">&#10003;</span>Deque supports both ends, so one type can be a queue or a stack; ArrayDeque is the standard choice.</li>
    </ul></div>''',
        "speak": "So, to recap Chapter 15. List, Set, Queue, Deque, and Map are interfaces, not classes — ArrayList, HashSet, LinkedList, and HashMap, and their relatives, are the classes that implement them; Chapter 19 covers what an interface actually is. Set guarantees no duplicates. Hash Set is fastest with no ordering, Linked Hash Set keeps insertion order, and Tree Set keeps sorted order. Queue processes elements first-in, first-out by default, and every operation has a throwing form, add, remove, and element, and a safe form, offer, poll, and peek, that returns a placeholder instead. A deck supports both ends at once, so one type can serve as either a queue or a stack, and Array Deck is the standard general-purpose implementation.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>Map.entrySet() iterates keys and values as Map.Entry pairs; a copy constructor only preserves the source's ordering.</li>
      <li><span class="check">&#10003;</span>List.of/Set.of/Map.of build small, fixed, immutable collections in one line.</li>
      <li><span class="check">&#10003;</span>Declare collection variables by their interface type &mdash; it makes swapping implementations a one-line change.</li>
    </ul></div>''',
        "speak": "Map's entry Set iterates keys and values together as Map dot Entry pairs, and a copy constructor only ever preserves the source map's own iteration order — build a Linked Hash Map from empty to get true insertion order. List dot of, Set dot of, and Map dot of build small, fixed, immutable collections in one line. And always declare collection variables by their interface type, not their concrete implementation. That's what makes swapping implementations a one-line change. Next up, Chapter 16: writing your own generics.",
        "continues": True,
    },
]
