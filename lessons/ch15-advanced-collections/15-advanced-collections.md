---
outlineRef: "15 — Advanced Collections (Set/Queue/Map) (ORACLE 13.1-4)"
status: "new — authored lesson"
---

# Advanced Collections (Set/Queue/Map)

Ch.9 covered `ArrayList` and a basic `HashMap`. Three more collection types round out the toolbox, each solving a problem the others don't: **`Set`** (no duplicates, ever), **`Queue`**/**`Deque`** (order of processing matters more than random access), and a deeper look at **`Map`** (iterating both keys and values together, and choosing an ordering).

Quick vocabulary note before diving in: just like `ArrayList` (Ch.9) is really an implementation of the `List` interface, `Set`, `Queue`, `Deque`, and `Map` are themselves **interfaces**, not classes — you never write `new Set<Integer>()` (that doesn't compile), only `new HashSet<Integer>()`, `new TreeSet<Integer>()`, and so on, stored in a variable declared by the interface type. Ch.19 covers what an interface actually is; for now, read `Set`/`Queue`/`Map` as "the name for a family of collection classes that all support this common set of operations."

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

(`allConfiguredCanIds` and `reportWarning` stand in for this team's own array and logging method — this snippet is a fragment, not a complete program.)

`HashSet` (fastest, no ordering guarantee) is the usual default; `LinkedHashSet` remembers insertion order; `TreeSet` keeps elements sorted. All three still refuse duplicates — they mainly differ in iteration order (and, for `TreeSet`, in one extra requirement covered in the pitfalls below).

`Set` also supports set algebra directly as methods: `s1.containsAll(s2)` (is `s2` a subset of `s1`?), `s1.addAll(s2)` (union), `s1.retainAll(s2)` (intersection — keep only what's in both), `s1.removeAll(s2)` (difference — remove anything also in `s2`). All three of `addAll`/`retainAll`/`removeAll` **change `s1` in place** and return a `boolean` (whether `s1` actually changed) — none of them returns a new set. To keep the originals untouched, copy first: `Set<Integer> intersection = new HashSet<Integer>(s1); intersection.retainAll(s2);`

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
    // poll() removes and returns the oldest fault first
    System.out.println("Handling: " + pendingFaults.poll());
}
```

`poll()`/`peek()` are usually the safer default in real code — they hand back `null` instead of throwing when the queue happens to be empty, which is often a completely normal state (no faults right now) rather than an error. Watch out with a `Queue<Integer>` (or any primitive wrapper) though: `int x = intQueue.poll();` on an empty queue throws `NullPointerException`, because assigning `poll()`'s `null` into a primitive `int` unboxes it immediately (Ch.9.2). Check `isEmpty()` first, or keep the result as `Integer` instead of unboxing right away.

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

// "Release from mid bar" — undo the most recent step
String lastStep = climbSteps.removeLast();
```

`ArrayDeque` is the standard general-purpose `Deque` implementation — generally faster than `LinkedList` for this purpose, with no capacity limit. A `Deque` also has stack-flavored `push(e)`/`pop()`/`peek()` methods, which just work on the front (`push` = `addFirst`, `pop` = `removeFirst`). Prefer `ArrayDeque` over the old `java.util.Stack` class — `Stack` is a legacy holdover with locking overhead this course never needs. (A `PriorityQueue` is a different `Queue` implementation worth knowing the name of: it always polls back the *smallest* element first, rather than the oldest — outside what this lesson covers.)

## Map, Revisited: Iterating Both Keys and Values

Ch.9.3 covered `put`/`get`, `containsKey`/`getOrDefault`/`remove`/`size`, and looping over `keySet()` — all of that still applies here. `Map.entrySet()` gives every key *and* value together in one pass, avoiding a repeated `get()` call for each key. Each item it hands back is a `Map.Entry<K, V>` — a small read-only key/value pair object, with `getKey()` and `getValue()`:

```java
Map<Integer, Double> motorOffsets = new HashMap<Integer, Double>();
motorOffsets.put(5, 0.02);
motorOffsets.put(6, -0.01);

for (Map.Entry<Integer, Double> entry : motorOffsets.entrySet())
{
    System.out.println("CAN ID " + entry.getKey() + " -> offset " + entry.getValue());
}
```

Just like `Set`, a plain `HashMap` gives no ordering guarantee. Swapping the implementation type is enough to change that, with no other code changes needed to the lines that *use* the map — but a copy constructor only ever preserves the *source* map's own iteration order. Copying a `HashMap` into a `TreeMap` is fine, because a `TreeMap` re-sorts by key regardless of where the entries came from. Copying a `HashMap` into a `LinkedHashMap`, though, just keeps the `HashMap`'s unpredictable order — the original `put` order was never recorded anywhere, so there's nothing to preserve. To actually get insertion order, build the `LinkedHashMap` from empty and `put` into it directly:

```java
// sorted by key — copying in is fine here, TreeMap always re-sorts
Map<Integer, Double> sorted = new TreeMap<Integer, Double>(motorOffsets);

Map<Integer, Double> byInsertOrder = new LinkedHashMap<Integer, Double>();
byInsertOrder.put(5, 0.02);
byInsertOrder.put(6, -0.01); // LinkedHashMap remembers put order, starting from empty
```

This is the payoff of always declaring a variable by its interface type (`List<E>`, `Map<K, V>`, `Set<E>`, `Queue<E>`) rather than its concrete implementation (`ArrayList`, `HashMap`, `HashSet`, `LinkedList`) — changing which concrete class gets constructed is a one-line change, because every line that *uses* the collection only ever depends on the interface.

## Fixed Collections: List.of, Set.of, Map.of

For data that's fixed once created — a small lookup table, a set of valid states — `List.of(...)`, `Set.of(...)`, and `Map.of(...)` build an **immutable** collection in one line, with no `new` and no separate `add`/`put` calls:

```java
List<String> allianceColors = List.of("Red", "Blue");
Set<Integer> validPracticeFields = Set.of(1, 2, 3);
Map<String, Integer> startingSlots = Map.of("Left", 1, "Center", 2, "Right", 3);
```

Calling `add`, `put`, or `remove` on any of these throws `UnsupportedOperationException` — they're meant to be built once and only read afterward.

## Common Pitfalls

- **Assuming a `HashSet` or `HashMap` remembers insertion order.** Neither does — reach for `LinkedHashSet`/`LinkedHashMap` if insertion order actually matters, or `TreeSet`/`TreeMap` if sorted order does.
- **Using `remove()`/`element()` on a queue that might be empty.** Both throw when empty — prefer `poll()`/`peek()` unless an empty queue genuinely represents a bug that should crash loudly.
- **Declaring a collection variable by its concrete type instead of its interface.** `HashMap<K,V> m = new HashMap<K,V>();` locks every line that touches `m` to `HashMap`'s specific behavior — declare it `Map<K,V> m = new HashMap<K,V>();` instead, so the implementation can change later without touching anything else.
- **Putting your own class into a `HashSet`/`HashMap` without overriding both `equals` and `hashCode`.** Two objects that "look equal" still count as different keys/elements unless both methods are overridden together — covered in full in Lesson 17.4.
- **Putting your own class into a `TreeSet`/`TreeMap` without teaching Java how to compare it.** Both need elements/keys that can be compared to each other; a class with no defined ordering throws `ClassCastException` the first time one gets added. `Comparable`/`Comparator`, the tools for that, are covered in Ch.19 — until then, only use `TreeSet`/`TreeMap` with types Java already knows how to order (`Integer`, `String`, `Double`, ...).

## Key Takeaways

- `List`, `Set`, `Queue`, `Deque`, and `Map` are interfaces, not classes — `ArrayList`, `HashSet`/`TreeSet`/`LinkedHashSet`, `LinkedList`/`ArrayDeque`, and `HashMap`/`TreeMap`/`LinkedHashMap` are the classes that implement them (Ch.19 covers interfaces in full).
- `Set` guarantees no duplicates; `HashSet` is fastest with no ordering, `LinkedHashSet` keeps insertion order, `TreeSet` keeps sorted order (and needs comparable elements).
- `Queue` processes elements FIFO by default; every operation has a throwing form (`add`/`remove`/`element`) and a safe form (`offer`/`poll`/`peek`) that returns a placeholder instead of throwing.
- `Deque` supports both ends at once, letting one type serve as either a queue or a stack (`push`/`pop`/`peek`); `ArrayDeque` is the standard general-purpose implementation.
- `Map.entrySet()` iterates keys and values together as `Map.Entry` pairs; a copy constructor only preserves the *source's* iteration order, so build a `LinkedHashMap` from empty to get true insertion order.
- `List.of`/`Set.of`/`Map.of` build small, fixed, immutable collections in one line.
- Always declare collection variables by their interface type, not their concrete implementation — it's what makes swapping implementations a one-line change.

Derived from `other-reference-repo`: `oracle-java-tutorials/collections-interfaces/01-the-set-interface.md`, `02-the-queue-interface.md`, `03-the-deque-interface.md`, `04-the-map-interface.md` (ORACLE 13.1-4)
