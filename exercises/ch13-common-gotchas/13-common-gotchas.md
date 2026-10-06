---
outlineRef: "13 — Common Gotchas (no citation — deck-original content)"
pairsWith: "[`lessons/ch13-common-gotchas/13-common-gotchas.md`](../../lessons/ch13-common-gotchas/13-common-gotchas.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
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

## Coding

**Mode:** harness

**Problem:** A scouting sheet lists the teams seen in each match as `String`s typed by hand, so they
are messy: random capitalisation, stray spaces around the name, and `null` where nobody entered
anything. Write `countMatches`, which returns how many entries in `scouted` name the same team as
`target`. An entry matches when, after removing the spaces at its start and end, it equals `target`
ignoring upper/lower case. A `null` entry never matches. `target` is never `null` and has no extra
spaces.

Examples:

- `countMatches(new String[] {"Shockwave", "Other", "shockwave "}, "Shockwave")` returns `2`
- `countMatches(new String[] {"  SHOCKWAVE"}, "Shockwave")` returns `1`
- `countMatches(new String[] {"Alpha", "Beta"}, "Gamma")` returns `0`

**Signature:** `public static int countMatches(String[] scouted, String target)`

**Starter:**

```java
public class Solution
{
    public static int countMatches(String[] scouted, String target)
    {
        // TODO: count the entries that name the same team as target
    }
}
```

**Tests:**

| Visible | Arguments | Expected |
|---|---|---|
| yes | `new String[] {"Shockwave", "Other", "shockwave "}, "Shockwave"` | `2` |
| yes | `new String[] {"  SHOCKWAVE"}, "Shockwave"` | `1` |
| yes | `new String[] {"Alpha", "Beta"}, "Gamma"` | `0` |
| no | `new String[] {null, "Shockwave", null}, "Shockwave"` | `1` |
| no | `new String[] {new String("Shockwave"), new String("Shockwave")}, "Shockwave"` | `2` |
| no | `new String[] {" shockWAVE ", null, "Shock wave", "SHOCKWAVE"}, "Shockwave"` | `2` |
| no | `new String[] {}, "Shockwave"` | `0` |

**Solution:**

```java
public class Solution
{
    public static int countMatches(String[] scouted, String target)
    {
        int count = 0;
        for (String entry : scouted)
        {
            if (entry != null)
            {
                String cleaned = entry.trim();
                if (cleaned.equalsIgnoreCase(target))
                {
                    count++;
                }
            }
        }
        return count;
    }
}
```

**Why:** This stacks three gotchas from the chapter. `==` on `String`s compares identity, so two
equal-looking strings can fail it (the `new String(...)` test shows this), and `equalsIgnoreCase`
compares the characters. `trim()` does not change `entry` because `String` is immutable, so its
result has to be kept (`cleaned`); calling `entry.trim();` alone does nothing. And calling a method
on a `null` entry throws `NullPointerException`, so the `null` check has to come first.
