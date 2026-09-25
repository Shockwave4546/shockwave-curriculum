---
outlineRef: "15 — Advanced Collections (Set/Queue/Map) (ORACLE 13.1-4)"
pairsWith: "[`lessons/ch15-advanced-collections/15-advanced-collections.md`](../../lessons/ch15-advanced-collections/15-advanced-collections.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Advanced Collections (Set/Queue/Map) — Worked Example

## Problem

At an event, the team's scouting tablets need to sync up before alliance selection. Three separate jobs:

1. Scouts sometimes cover the same team twice. From the list of team numbers scouted so far, flag every repeat, count how many *different* teams were scouted, and print them in numeric order.
2. Match reports are waiting to upload. Upload them in the order they were saved, oldest first.
3. Each team's best auto score has been recorded. Print every team with its score, sorted by team number.

## Step 1: Plan It First

1. "No repeats" plus "numeric order" means a `Set`. Specifically a `TreeSet`, since the output should be sorted.
2. "Oldest first" is first-in, first-out, so this is a `Queue`.
3. Team number → score is a key/value lookup, so this is a `Map`. Printing keys *and* values together means `entrySet()`. Sorted by key means a `TreeMap`.

Each job uses its own collection on its own data. None of them feeds into another.

## Step 2: Flag Repeats and Count Unique Teams — `Set`

```java
import java.util.Set;
import java.util.TreeSet;

int[] scoutedTeams = {254, 1622, 4414, 254, 1678, 1622};

Set<Integer> uniqueTeams = new TreeSet<Integer>();
for (int team : scoutedTeams)
{
    if (!uniqueTeams.add(team)) // add() returns false if the team was already in the set
    {
        System.out.println("Already scouted: " + team);
    }
}
System.out.println(uniqueTeams.size() + " different teams scouted");
```

Output:

```
Already scouted: 254
Already scouted: 1622
4 different teams scouted
```

The second `add(254)` and second `add(1622)` return `false` and change nothing, so the set ends with 4 teams, not 6. The variable is declared as the interface type `Set<Integer>`. Only the right-hand side says `TreeSet`.

Now print the teams:

```java
for (int team : uniqueTeams)
{
    System.out.println(team);
}
```

Output:

```
254
1622
1678
4414
```

That's numeric order, not the order the teams were scouted (254, 1622, 4414, 1678). A `TreeSet` keeps its elements sorted. If this had been a `HashSet`, the same 4 teams would print in *no guaranteed order*. Changing `new TreeSet<Integer>()` to `new HashSet<Integer>()` is the only edit needed to switch, and the rest of the code stays the same because it only depends on `Set`.

## Step 3: Upload Reports Oldest First — `Queue`

```java
import java.util.LinkedList;
import java.util.Queue;

Queue<String> pendingUploads = new LinkedList<String>();
pendingUploads.offer("Qual 12 report");
pendingUploads.offer("Qual 13 report");
pendingUploads.offer("Qual 14 report");

System.out.println("Next up: " + pendingUploads.peek());

while (!pendingUploads.isEmpty())
{
    System.out.println("Uploading " + pendingUploads.poll());
}
```

Output:

```
Next up: Qual 12 report
Uploading Qual 12 report
Uploading Qual 13 report
Uploading Qual 14 report
```

`peek()` looks at the oldest report without removing it, so the queue still holds all 3 when the loop starts. Each `poll()` then removes and returns the oldest remaining report, which is FIFO order.

Once the loop ends, the queue is empty. An empty upload queue is completely normal (nothing left to send), so the safe forms are the right choice here:

```java
System.out.println(pendingUploads.poll()); // null — no exception
```

`remove()` in that same spot would throw an exception instead of returning `null`.

## Step 4: Print Every Team's Auto Score, Sorted — `Map` and `entrySet()`

The scores were recorded into a plain `HashMap`:

```java
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

Map<Integer, Integer> autoPoints = new HashMap<Integer, Integer>();
autoPoints.put(4414, 15);
autoPoints.put(254, 18);
autoPoints.put(1622, 12);
```

Looping over a `HashMap` gives no ordering guarantee. To print sorted by team number, copy it into a `TreeMap`, then loop over `entrySet()` so each key and its value come out together, with no extra `get()` call:

```java
Map<Integer, Integer> sortedAutoPoints = new TreeMap<Integer, Integer>(autoPoints);
for (Map.Entry<Integer, Integer> entry : sortedAutoPoints.entrySet())
{
    System.out.println("Team " + entry.getKey() + ": " + entry.getValue() + " auto points");
}
```

Output:

```
Team 254: 18 auto points
Team 1622: 12 auto points
Team 4414: 15 auto points
```

The teams were `put()` in as 4414, 254, 1622, but they print as 254, 1622, 4414 because a `TreeMap` keeps its keys sorted.

## Recap

- A `Set` quietly refuses duplicates. `add()` returns `false` for a repeat, which makes it an easy duplicate detector.
- `TreeSet`/`TreeMap` keep sorted order. `HashSet`/`HashMap` guarantee no order at all.
- A `Queue` hands elements back oldest-first. `peek()` looks without removing, `poll()` removes, and both return `null` on an empty queue instead of throwing.
- `entrySet()` loops over a map's keys and values together as `Map.Entry` pairs.
- Declaring every variable by its interface type (`Set`, `Queue`, `Map`) means switching implementations only changes the `new ...` part.
