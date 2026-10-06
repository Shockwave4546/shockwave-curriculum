---
outlineRef: "24 — Optional: Avoiding Null Pointer Exceptions (ORACLE 16.1) — renamed from \"Optional: Maybe a Value\" to disambiguate from optional method parameters; the deck's actual slide heading is unchanged"
pairsWith: "[`lessons/ch24-optional-avoiding-null-pointer-exceptions/24-optional-avoiding-null-pointer-exceptions.md`](../../lessons/ch24-optional-avoiding-null-pointer-exceptions/24-optional-avoiding-null-pointer-exceptions.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
---

# Optional: Avoiding Null Pointer Exceptions — Exercises

## Multiple Choice

**Question:** No alliance color has been reported yet, so a method returned an empty `Optional`. What does this code print?

```java
Optional<String> alliance = Optional.empty();
System.out.println(alliance.orElse("Unknown"));
```

**Options:**

- A. `Unknown`
- B. `null`
- C. Nothing prints. It throws `NoSuchElementException`
- D. `Optional.empty`

**Answer:** A

**Why:** `orElse` returns the wrapped value if there is one, and otherwise the fallback it was given. `alliance` is empty, so `orElse("Unknown")` returns `"Unknown"`, and that's what prints.

- B is wrong. An empty `Optional` isn't `null`, and `orElse` never hands back a `null` in place of the fallback. The fallback is the whole point.
- C is wrong. `NoSuchElementException` comes from calling bare `get()` on an empty `Optional`. `orElse` handles the empty case safely instead of throwing.
- D is wrong. `Optional.empty` is what you'd see from printing the `Optional` object *itself* (`System.out.println(alliance)`). Here, `orElse` unwraps it first, so what prints is a `String`.

## Micro-Parsons

**Problem:** These lines, once correctly ordered, form a complete program. The driver hasn't picked an autonomous routine yet, so `chosenAuto` is `null` (a stand-in for a real driver-station selection). The program safely wraps it in an `Optional`, prints `Running <name>` only if a routine was chosen, and always prints which routine is selected, falling back to `"None"`. Right now it prints `Selected: None`.

Reorder the fragments below into a working program:

- a. `        auto.ifPresent(name -> System.out.println("Running " + name));`
- b. `    public static void main(String[] args)`
- c. `}`
- d. `        Optional<String> auto = Optional.ofNullable(chosenAuto);`
- e. `public class AutoSelection`
- f. `    }`
- g. `        String chosenAuto = null;`
- h. `import java.util.Optional;`
- i. `        System.out.println("Selected: " + auto.orElse("None"));`
- j. `    {`
- k. `{`

**Answer:** h, e, k, b, j, g, d, a, i, f, c

**Interchangeable:** (a, i)

```java
import java.util.Optional;

public class AutoSelection
{
    public static void main(String[] args)
    {
        String chosenAuto = null;
        Optional<String> auto = Optional.ofNullable(chosenAuto);
        auto.ifPresent(name -> System.out.println("Running " + name));
        System.out.println("Selected: " + auto.orElse("None"));
    }
}
```

**Why this order:** The `import` (`h`) has to come before the class that uses `Optional`. Then come the usual class and `main` lines (`e`, `k`, `b`, `j`). `chosenAuto` (`g`) has to exist before it can be wrapped. `ofNullable` (`d`) is the right way to wrap it, because it might be `null`. `Optional.of(chosenAuto)` would throw immediately on a `null`. Both uses of `auto` (`a` and `i`) have to come after it's created. They can go in either order (hence **Interchangeable:** (a, i)): `auto` is empty here, so `ifPresent` does nothing, and the output is `Selected: None` either way. (That's specific to `chosenAuto` being `null` in *this* program — if a routine had actually been chosen, `ifPresent` would print a "Running ..." line, and swapping the two statements would change which line prints first. Both orders still print the same two lines either way, just in a different sequence.) The braces close in reverse: `main`'s body (`f`), then the class's body (`c`).

## Coding

**Mode:** full-program

**Problem:** A camera knows the distance to each AprilTag it can currently see, stored in a `Map<Integer, Double>` (a tag id the camera can't see is simply not in the map,
so `map.get(id)` returns `null`). Write the class `Vision`, whose methods turn that into `Optional` results:

- `Vision(Map<Integer, Double> distances)` stores the map.
- `Optional<Double> getDistance(int id)` returns the distance for that tag, or an **empty** `Optional` if the tag isn't in the map. It must never throw.
- `double distanceOrDefault(int id, double fallback)` returns the distance, or `fallback` if the tag isn't there.
- `double requireDistance(int id)` returns the distance, or throws `IllegalStateException` with the message `No tag ` followed by the id (for example `No tag 7`) if it isn't there.
- `Optional<Double> closeDistance(int id, double max)` returns the distance only if the tag is seen **and** its distance is at most `max` (equal counts as close); otherwise empty.

Do not call `get()` or `isPresent()` on an `Optional`. `main` reads the tag table, then a list of tag ids to look up.

**Starter:**

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        int tagCount = in.nextInt();
        Map<Integer, Double> distances = new HashMap<>();
        for (int i = 0; i < tagCount; i++)
        {
            int id = in.nextInt();
            distances.put(id, in.nextDouble());
        }
        Vision vision = new Vision(distances);

        int queries = in.nextInt();
        for (int i = 0; i < queries; i++)
        {
            int id = in.nextInt();
            System.out.println("Tag " + id);
            Optional<Double> distance = vision.getDistance(id);
            System.out.println("  seen: " + distance.map(d -> "distance " + d).orElse("not seen"));
            System.out.println("  or default: " + vision.distanceOrDefault(id, -1.0));
            try
            {
                System.out.println("  required: " + vision.requireDistance(id));
            }
            catch (IllegalStateException e)
            {
                System.out.println("  required: " + e.getMessage());
            }
            vision.closeDistance(id, 3.0).ifPresent(d -> System.out.println("  close: " + d));
        }
    }
}

// TODO: write the class Vision
```

**Scenario 1 (visible):**

**Input:**

```text
2
1 2.5
2 8.0
2
1
2
```

**Expected output:**

```text
Tag 1
  seen: distance 2.5
  or default: 2.5
  required: 2.5
  close: 2.5
Tag 2
  seen: distance 8.0
  or default: 8.0
  required: 8.0
```

**Scenario 2 (visible):**

**Input:**

```text
1
5 3.0
1
9
```

**Expected output:**

```text
Tag 9
  seen: not seen
  or default: -1.0
  required: No tag 9
```

**Scenario 3 (visible):**

**Input:**

```text
0
1
4
```

**Expected output:**

```text
Tag 4
  seen: not seen
  or default: -1.0
  required: No tag 4
```

**Scenario 4 (hidden):**

**Input:**

```text
3
10 3.0
11 3.5
12 0.5
3
10
11
12
```

**Expected output:**

```text
Tag 10
  seen: distance 3.0
  or default: 3.0
  required: 3.0
  close: 3.0
Tag 11
  seen: distance 3.5
  or default: 3.5
  required: 3.5
Tag 12
  seen: distance 0.5
  or default: 0.5
  required: 0.5
  close: 0.5
```

**Scenario 5 (hidden):**

**Input:**

```text
2
7 1.25
8 99.0
3
8
7
3
```

**Expected output:**

```text
Tag 8
  seen: distance 99.0
  or default: 99.0
  required: 99.0
Tag 7
  seen: distance 1.25
  or default: 1.25
  required: 1.25
  close: 1.25
Tag 3
  seen: not seen
  or default: -1.0
  required: No tag 3
```

**Scenario 6 (hidden):**

**Input:**

```text
1
1 0.0
2
1
1
```

**Expected output:**

```text
Tag 1
  seen: distance 0.0
  or default: 0.0
  required: 0.0
  close: 0.0
Tag 1
  seen: distance 0.0
  or default: 0.0
  required: 0.0
  close: 0.0
```

**Solution:**

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        int tagCount = in.nextInt();
        Map<Integer, Double> distances = new HashMap<>();
        for (int i = 0; i < tagCount; i++)
        {
            int id = in.nextInt();
            distances.put(id, in.nextDouble());
        }
        Vision vision = new Vision(distances);

        int queries = in.nextInt();
        for (int i = 0; i < queries; i++)
        {
            int id = in.nextInt();
            System.out.println("Tag " + id);
            Optional<Double> distance = vision.getDistance(id);
            System.out.println("  seen: " + distance.map(d -> "distance " + d).orElse("not seen"));
            System.out.println("  or default: " + vision.distanceOrDefault(id, -1.0));
            try
            {
                System.out.println("  required: " + vision.requireDistance(id));
            }
            catch (IllegalStateException e)
            {
                System.out.println("  required: " + e.getMessage());
            }
            vision.closeDistance(id, 3.0).ifPresent(d -> System.out.println("  close: " + d));
        }
    }
}

class Vision
{
    private final Map<Integer, Double> distances;

    public Vision(Map<Integer, Double> distances)
    {
        this.distances = distances;
    }

    public Optional<Double> getDistance(int id)
    {
        return Optional.ofNullable(distances.get(id));
    }

    public double distanceOrDefault(int id, double fallback)
    {
        return getDistance(id).orElse(fallback);
    }

    public double requireDistance(int id)
    {
        return getDistance(id).orElseThrow(() -> new IllegalStateException("No tag " + id));
    }

    public Optional<Double> closeDistance(int id, double max)
    {
        return getDistance(id).filter(d -> d <= max);
    }
}
```

**Why:** `getDistance` is the heart of it: `map.get(id)` can be `null`, so the right factory is `Optional.ofNullable`. `Optional.of(map.get(id))` throws `NullPointerException` the moment an unseen tag is looked up.
The other three methods all build on `getDistance`: `orElse` for the fallback, `orElseThrow` with a lambda (so the exception is only built when the value is missing), and `filter` to turn a too-far
distance into an empty `Optional`. A solution that uses `<` instead of `<=` in the filter fails the hidden scenario with a tag exactly at the limit, and one using `Optional.of` crashes on any unseen tag.
