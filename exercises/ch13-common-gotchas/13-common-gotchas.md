---
outlineRef: "13 — Common Gotchas (no citation — deck-original content)"
pairsWith: "[`lessons/ch13-common-gotchas/13-common-gotchas.md`](../../lessons/ch13-common-gotchas/13-common-gotchas.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
---

# Common Gotchas — Exercises

## Multiple Choice

**Question:** The driver picks an autonomous routine on the dashboard, and the code checks it against the routine the strategy team planned. What does this print?

```java
String selectedAuto = new String("TwoPieceCenter");
String plannedAuto = new String("TwoPieceCenter");

if (selectedAuto == plannedAuto)
{
    System.out.println("Running planned auto");
}
else
{
    System.out.println("Auto mismatch - check the dashboard");
}
```

**Options:**

- A. `Running planned auto`
- B. `Auto mismatch - check the dashboard`
- C. Nothing. It doesn't compile, because `==` can't be used on `String`s
- D. Nothing. It throws a `NullPointerException`

**Answer:** B

**Why:** For objects like `String`, `==` checks whether two variables point at the *exact same object in memory*, not whether their text matches. Each `new String(...)` builds a separate object, so `selectedAuto == plannedAuto` is `false` even though both hold `"TwoPieceCenter"`. The `else` branch runs. The fix is `selectedAuto.equals(plannedAuto)`, which compares the actual characters and would print `Running planned auto`.

- A is wrong. That's what `.equals()` would print. `==` isn't comparing the text here.
- C is wrong. `==` on two `String`s compiles and runs without complaint. That's what makes this gotcha dangerous: it silently gives the wrong answer instead of an error.
- D is wrong. Both variables are assigned real objects with `new`, so neither is `null`. Nothing is being called on a missing object.

## Micro-Parsons

**Problem:** These lines, once correctly ordered, form a complete program that keeps a list of pit repairs. The list is declared as a field at the top of the class, and `main` adds one repair and prints how many repairs are on the list. Watch the order inside `main`: a field that's declared but never assigned an object is `null`, so any method called on it before `new` runs throws a `NullPointerException`.

Reorder the fragments below into a working program:

- a. `        repairs.add("Re-tension intake belt");`
- b. `public class PitRepairs`
- c. `    }`
- d. `    private static ArrayList<String> repairs;`
- e. `        repairs = new ArrayList<String>();`
- f. `}`
- g. `    public static void main(String[] args)`
- h. `import java.util.ArrayList;`
- i. `        System.out.println(repairs.size());`
- j. `{`
- k. `    {`

**Answer:** h, b, j, d, g, k, e, a, i, c, f

```java
import java.util.ArrayList;

public class PitRepairs
{
    private static ArrayList<String> repairs;

    public static void main(String[] args)
    {
        repairs = new ArrayList<String>();
        repairs.add("Re-tension intake belt");
        System.out.println(repairs.size());
    }
}
```

Output: `1`

**Why this order:** The `import` (`h`) comes before the class that uses `ArrayList`. The class line and its brace (`b`, `j`) come next, then the field (`d`), placed at the top of the class as the problem states. `main`'s signature and brace (`g`, `k`) follow. Inside `main`, order is the whole point. The field starts out `null`, so the list has to be constructed (`e`) before anything calls a method on it. Putting `a` first compiles fine but crashes at run time with a `NullPointerException`, because there's no list yet to add to. After construction, the repair is added (`a`), and only then does `size()` (`i`) report `1`. The braces close in reverse: `main`'s body (`c`), then the class's body (`f`).
