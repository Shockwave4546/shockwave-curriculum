---
outlineRef: "24 — Optional: Avoiding Null Pointer Exceptions (ORACLE 16.1) — renamed from \"Optional: Maybe a Value\" to disambiguate from optional method parameters; the deck's actual slide heading is unchanged"
pairsWith: "[`lessons/ch24-optional-avoiding-null-pointer-exceptions/24-optional-avoiding-null-pointer-exceptions.md`](../../lessons/ch24-optional-avoiding-null-pointer-exceptions/24-optional-avoiding-null-pointer-exceptions.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
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
