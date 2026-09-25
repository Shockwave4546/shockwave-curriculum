---
outlineRef: "15 — Advanced Collections (Set/Queue/Map) (ORACLE 13.1-4)"
pairsWith: "[`lessons/ch15-advanced-collections/15-advanced-collections.md`](../../lessons/ch15-advanced-collections/15-advanced-collections.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
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
