---
outlineRef: "15 — Advanced Collections (Set/Queue/Map) (ORACLE 13.1-4)"
pairsWith: "[`lessons/ch15-advanced-collections/15-advanced-collections.md`](../../lessons/ch15-advanced-collections/15-advanced-collections.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
---

# Advanced Collections (Set/Queue/Map) — Exercises

## Multiple Choice

**Question:** A pit checklist adds subsystem names to a set in this order:

```java
checkedSubsystems.add("Shooter");
checkedSubsystems.add("Intake");
checkedSubsystems.add("Climber");
```

The team wants a for-each loop over `checkedSubsystems` to be **guaranteed** to print `Shooter`, `Intake`, `Climber`, in exactly the order they were added. Which declaration guarantees that?

**Options:**

- A. `Set<String> checkedSubsystems = new HashSet<String>();`
- B. `Set<String> checkedSubsystems = new LinkedHashSet<String>();`
- C. `Set<String> checkedSubsystems = new TreeSet<String>();`
- D. Any of the three. Every `Set` remembers the order elements were added.

**Answer:** B

**Why:** `LinkedHashSet` is the `Set` implementation that remembers insertion order. Looping over it gives `Shooter`, `Intake`, `Climber`, exactly as added.

- A is wrong because a `HashSet` makes no ordering guarantee at all. It might happen to print in insertion order on some run, but nothing guarantees it, and the lesson warns against assuming it does.
- C is wrong because a `TreeSet` keeps its elements *sorted*, not in insertion order. It would print `Climber`, `Intake`, `Shooter` (alphabetical).
- D is wrong because the three implementations all refuse duplicates, but they differ in exactly this way: iteration order. Only `LinkedHashSet` keeps insertion order.

## Micro-Parsons

**Problem:** These lines, once correctly ordered, form a complete program that loads two game pieces into a hopper, one after the other, then feeds out the piece that was loaded **most recently** (last-in, first-out) and prints it. The program should print `Note 2`.

Reorder the fragments below into a working program:

- a. `        hopper.addLast("Note 2");`
- b. `public class HopperStack`
- c. `    }`
- d. `import java.util.Deque;`
- e. `        Deque<String> hopper = new ArrayDeque<String>();`
- f. `{`
- g. `        System.out.println(hopper.removeLast());`
- h. `    public static void main(String[] args)`
- i. `import java.util.ArrayDeque;`
- j. `}`
- k. `        hopper.addLast("Note 1");`
- l. `    {`

**Answer:** i, d, b, f, h, l, e, k, a, g, c, j

**Interchangeable:** (i, d)

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class HopperStack
{
    public static void main(String[] args)
    {
        Deque<String> hopper = new ArrayDeque<String>();
        hopper.addLast("Note 1");
        hopper.addLast("Note 2");
        System.out.println(hopper.removeLast());
    }
}
```

**Why this order:** Both imports (`i`, `d`) come before the class, in either order, since neither depends on the other. The usual class/main scaffolding (`b`, `f`, `h`, `l`) follows. The `Deque` has to be created (`e`) before anything can be added to it. `"Note 1"` must be added (`k`) before `"Note 2"` (`a`). Swapping those two would make `"Note 1"` the most recent piece and change what gets printed. `removeLast()` (`g`) then takes from the same end the pieces were added to, so it returns the most recently added piece, `"Note 2"`. The braces close in reverse: `main`'s body (`c`), then the class's body (`j`).


## Coding

**Mode:** full-program

**Problem:** Before a match, the wiring team lists every CAN ID on the robot. Write the class
`CanChecker` with a static method `findDuplicates` that takes the array of IDs and returns a
`Set<Integer>` of every ID that appears **more than once**. The set must list the duplicates in the
order each one was **first caught as a duplicate** while reading the array left to right (the first
time an ID shows up a second time). Each duplicate ID appears in the set only once, even if it is
wired three times. If nothing is duplicated, return an empty set.

The fixed `main` reads the number of IDs, then the IDs, and prints the set you return.

For example, the IDs `4 7 4 2 7 7` print `[4, 7]`: `4` repeats at index 2 and `7` repeats at index 4,
so `4` is caught first. The IDs `1 2 3` print `[]`.

**Starter:**

```java
import java.util.*;

public class Main
{
    // Don't change main
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int count = in.nextInt();
        int[] ids = new int[count];
        for (int i = 0; i < count; i++)
        {
            ids[i] = in.nextInt();
        }
        System.out.println(CanChecker.findDuplicates(ids));
    }
}

class CanChecker
{
    public static Set<Integer> findDuplicates(int[] ids)
    {
        // TODO: return the IDs that appear more than once, in the order each was first caught
        return null;
    }
}
```

**Scenario 1 (visible):**

**Input:**

```text
6
4 7 4 2 7 7
```

**Expected output:**

```text
[4, 7]
```

**Scenario 2 (visible):**

**Input:**

```text
3
1 2 3
```

**Expected output:**

```text
[]
```

**Scenario 3 (hidden):**

**Input:**

```text
7
9 3 3 9 12 3 9
```

**Expected output:**

```text
[3, 9]
```

**Scenario 4 (hidden):**

**Input:**

```text
5
20 9 9 20 20
```

**Expected output:**

```text
[9, 20]
```

**Scenario 5 (hidden):**

**Input:**

```text
8
15 2 31 31 2 8 15 15
```

**Expected output:**

```text
[31, 2, 15]
```

**Solution:**

```java
import java.util.*;

public class Main
{
    // Don't change main
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int count = in.nextInt();
        int[] ids = new int[count];
        for (int i = 0; i < count; i++)
        {
            ids[i] = in.nextInt();
        }
        System.out.println(CanChecker.findDuplicates(ids));
    }
}

class CanChecker
{
    public static Set<Integer> findDuplicates(int[] ids)
    {
        Set<Integer> seen = new HashSet<Integer>();
        Set<Integer> duplicates = new LinkedHashSet<Integer>();
        for (int id : ids)
        {
            if (!seen.add(id))
            {
                duplicates.add(id);
            }
        }
        return duplicates;
    }
}
```

**Why:** Two sets do two different jobs. `seen` is the lesson's duplicate-ID check: `add` returns
`false` when the ID is already there, which is exactly the "second time" signal. `duplicates` has to
remember the order each repeat was caught, so it is a `LinkedHashSet` rather than a `HashSet`; it
also silently ignores a third `add` of the same ID, so each duplicate is listed once. A plain
`HashSet` promises no order at all, so it can print `[20, 9]` where scenario 4 expects `[9, 20]`.
