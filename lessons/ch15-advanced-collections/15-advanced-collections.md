# Advanced Collections (Set/Queue/Map)

**Outline ref:** 15 — Advanced Collections (Set/Queue/Map) (ORACLE 13.1-4)
**Status:** new — authored lesson

Ch.9 covered `ArrayList` and a basic `HashMap`. Three more collection types round out the toolbox, each solving a problem the others don't: **`Set`** (no duplicates, ever), **`Queue`**/**`Deque`** (order of processing matters more than random access), and a deeper look at **`Map`** (iterating both keys and values together, and choosing an ordering).

## Set: No Duplicates, Ever

A `Set` is a collection that flatly refuses duplicate elements — calling `add` with something already present just does nothing (and returns `false`), rather than adding a second copy:

```java
Set<Integer> usedCanIds = new HashSet<Integer>();
usedCanIds.add(5);  // true — added
usedCanIds.add(5);  // false — already present, nothing changed
```

That makes `Set` the natural tool for catching configuration conflicts — e.g. verifying no two devices on the robot were accidentally wired to the same CAN ID:

```java
Set<Integer> seenIds = new HashSet<Integer>();
for (int id : allConfiguredCanIds)
{
    if (!seenIds.add(id)) // add() returns false if it was already there
    {
        reportWarning("Duplicate CAN ID detected: " + id);
    }
}
```

`HashSet` (fastest, no ordering guarantee) is the usual default; `LinkedHashSet` remembers insertion order; `TreeSet` keeps elements sorted. All three still refuse duplicates — they only differ in iteration order.

`Set` also supports set algebra directly as methods: `s1.containsAll(s2)` (is `s2` a subset of `s1`?), `s1.addAll(s2)` (union), `s1.retainAll(s2)` (intersection — keep only what's in both), `s1.removeAll(s2)` (difference — remove anything also in `s2`).

## Queue: First-In, First-Out

A `Queue` holds elements for later processing, normally in **FIFO** order (first-in-first-out) — think of a queue of autonomous routine steps waiting to run in the order they were scheduled. Every operation comes in two flavors: one throws an exception on failure, the other returns a safe placeholder value instead.

| Operation | Throws on failure | Returns a placeholder |
|---|---|---|
| Insert | `add(e)` | `offer(e)` (returns `false`) |
| Remove | `remove()` | `poll()` (returns `null` if empty) |
| Peek (don't remove) | `element()` | `peek()` (returns `null` if empty) |

```java
Queue<String> pendingFaults = new LinkedList<String>();
pendingFaults.add("Camera 1 disconnected");
pendingFaults.add("Low battery voltage");

while (!pendingFaults.isEmpty())
{
    System.out.println("Handling: " + pendingFaults.poll()); // removes and returns the oldest fault first
}
```

`poll()`/`peek()` are usually the safer default in real code — they hand back `null` instead of throwing when the queue happens to be empty, which is often a completely normal state (no faults right now) rather than an error.

## Deque: Both Ends at Once

A **`Deque`** ("deck," double-ended queue) supports inserting and removing from *either* end, which means a single `Deque` can act as a FIFO queue, a LIFO stack, or both:

| Operation | First (front) | Last (back) |
|---|---|---|
| Insert | `addFirst(e)` / `offerFirst(e)` | `addLast(e)` / `offerLast(e)` |
| Remove | `removeFirst()` / `pollFirst()` | `removeLast()` / `pollLast()` |
| Examine | `getFirst()` / `peekFirst()` | `getLast()` / `peekLast()` |

A common use: an undo stack for the last few climb-sequence steps, where you only ever add/remove from one end (LIFO — last one added is the first one undone):

```java
Deque<String> climbSteps = new ArrayDeque<String>();
climbSteps.addLast("Extend to high bar");
climbSteps.addLast("Release from mid bar");

String lastStep = climbSteps.removeLast(); // "Release from mid bar" — undo the most recent step
```

`ArrayDeque` is the standard general-purpose `Deque` implementation — generally faster than `LinkedList` for this purpose, with no capacity limit.

## Map, Revisited: Iterating Both Keys and Values

Ch.9.3 covered `put`/`get` and looping over `keySet()`. `Map.entrySet()` gives every key *and* value together in one pass, avoiding a repeated `get()` call for each key:

```java
Map<Integer, Double> motorOffsets = new HashMap<Integer, Double>();
motorOffsets.put(5, 0.02);
motorOffsets.put(6, -0.01);

for (Map.Entry<Integer, Double> entry : motorOffsets.entrySet())
{
    System.out.println("CAN ID " + entry.getKey() + " -> offset " + entry.getValue());
}
```

Just like `Set`, a plain `HashMap` gives no ordering guarantee. Swapping the implementation type is enough to change that, with no other code changes needed:

```java
Map<Integer, Double> sorted = new TreeMap<Integer, Double>(motorOffsets);       // sorted by key
Map<Integer, Double> byInsertOrder = new LinkedHashMap<Integer, Double>(motorOffsets); // insertion order
```

This is the payoff of always declaring a variable by its interface type (`Map<K, V>`, `Set<E>`, `Queue<E>`) rather than its concrete implementation (`HashMap`, `HashSet`, `LinkedList`) — changing which concrete class gets constructed is a one-line change, because every line that *uses* the collection only ever depends on the interface.

## Common Pitfalls

- **Assuming a `HashSet` or `HashMap` remembers insertion order.** Neither does — reach for `LinkedHashSet`/`LinkedHashMap` if insertion order actually matters, or `TreeSet`/`TreeMap` if sorted order does.
- **Using `remove()`/`element()` on a queue that might be empty.** Both throw when empty — prefer `poll()`/`peek()` unless an empty queue genuinely represents a bug that should crash loudly.
- **Declaring a collection variable by its concrete type instead of its interface.** `HashMap<K,V> m = new HashMap<>();` locks every line that touches `m` to `HashMap`'s specific behavior — declare it `Map<K,V> m = new HashMap<>();` instead, so the implementation can change later without touching anything else.

## Key Takeaways

- `Set` guarantees no duplicates; `HashSet` is fastest with no ordering, `LinkedHashSet` keeps insertion order, `TreeSet` keeps sorted order.
- `Queue` processes elements FIFO by default; every operation has a throwing form (`add`/`remove`/`element`) and a safe form (`offer`/`poll`/`peek`) that returns a placeholder instead of throwing.
- `Deque` supports both ends at once, letting one type serve as either a queue or a stack; `ArrayDeque` is the standard general-purpose implementation.
- `Map.entrySet()` iterates keys and values together; switching between `HashMap`, `TreeMap`, and `LinkedHashMap` changes ordering with no other code changes.
- Always declare collection variables by their interface type, not their concrete implementation — it's what makes swapping implementations a one-line change.

Derived from `other-reference-repo`: `oracle-java-tutorials/collections-interfaces/01-the-set-interface.md`, `02-the-queue-interface.md`, `03-the-deque-interface.md`, `04-the-map-interface.md` (ORACLE 13.1-4)
