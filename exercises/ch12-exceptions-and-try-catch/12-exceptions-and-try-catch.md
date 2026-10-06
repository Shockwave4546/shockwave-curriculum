---
outlineRef: "12 — Exceptions & try/catch (ORACLE 11.1-16)"
pairsWith: "[`lessons/ch12-exceptions-and-try-catch/12-exceptions-and-try-catch.md`](../../lessons/ch12-exceptions-and-try-catch/12-exceptions-and-try-catch.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
---

# Exceptions & try/catch — Exercises

## Multiple Choice

**Question:** A teammate writes this method to save a short match summary to a file. The class it lives in already has `import java.io.*;` at the top. It doesn't compile. Why?

```java
public static void saveMatchLog()
{
    PrintWriter out = new PrintWriter(new FileWriter("match_log.txt"));
    out.println("Match 12: 3 notes scored, climbed");
    out.close();
}
```

**Options:**

- A. `new FileWriter(...)` can throw an `IOException`, which is a checked exception, so the method has to either catch it or declare `throws IOException`
- B. It compiles fine. It only fails at run time, and only if the file can't be created
- C. `out.close()` has to be inside a `finally` block, or the compiler rejects the method
- D. The method has to declare `throws NullPointerException`, in case `out` is `null`

**Answer:** A

**Why:** `IOException` is a checked exception. The compiler requires every piece of code that can throw one to either handle it with `try`/`catch` or pass it up to the caller with a `throws` clause. This method does neither, so the compiler stops with an error. Adding `throws IOException` after `saveMatchLog()` fixes it.

- B is wrong. The whole point of a checked exception is that the compiler checks for it before the program ever runs. The code never gets far enough to try creating the file.
- C is wrong. `finally` is a good place for cleanup like `close()`, but the compiler never requires it. The missing handler for `IOException` is the only problem here.
- D is wrong. `NullPointerException` is unchecked, so it never needs a `throws` clause. Declaring it also wouldn't fix anything, because the `IOException` would still be unhandled.

## Micro-Parsons

**Problem:** Given this program's imports, class, and `main` method, reorder the fragments below into the body of `main`. The body tries to open `pit_notes.txt` and print its first line. If the file doesn't exist, it prints a fallback message instead of crashing.

```java
import java.io.*;
import java.util.*;

public class PitNotes
{
    public static void main(String[] args)
    {
        // ⟵ reorder the fragments below into this body
    }
}
```

Reorder the fragments below to complete it:

- a. `            System.out.println(scan.nextLine());`
- b. `        catch (FileNotFoundException e)`
- c. `        {`
- d. `        }`
- e. `            Scanner scan = new Scanner(new File("pit_notes.txt"));`
- f. `            System.out.println("No pit notes found - starting fresh");`
- g. `        try`
- h. `        }`
- i. `            scan.close();`
- j. `        {`

**Answer:** g, c, e, a, i, h, b, j, f, d

**Interchangeable:** (c, j) (d, h)

```java
import java.io.*;
import java.util.*;

public class PitNotes
{
    public static void main(String[] args)
    {
        try
        {
            Scanner scan = new Scanner(new File("pit_notes.txt"));
            System.out.println(scan.nextLine());
            scan.close();
        }
        catch (FileNotFoundException e)
        {
            System.out.println("No pit notes found - starting fresh");
        }
    }
}
```

If `pit_notes.txt` is missing, the output is `No pit notes found - starting fresh`. If it exists, the output is its first line.

**Why this order:** `try` (`g`) and its opening brace (`c`) come first, because the code that might throw has to be inside the `try` block. Inside it, the `Scanner` has to be created (`e`) before anything can be read from it (`a`), and it can only be closed (`i`) after the reading is done. Line `e`, the `Scanner` constructor, is the one that can throw `FileNotFoundException`, which is why it sits inside `try`. The `try` block closes (`h`), and the `catch` (`b`) follows it directly. Its body (`j`, `f`, `d`) holds the fallback message, which only runs if opening the file failed. If opening the file fails, the rest of the `try` block (`a`, `i`) is skipped and execution jumps straight to `f`. Note that `c` and `j` (both an eight-space `{`) are identical, and so are `h` and `d` (both an eight-space `}`). One of each pair belongs to `try` and the other to `catch`, so it doesn't matter which copy goes where, as long as each block gets one opening and one closing brace.

## Coding

**Mode:** harness

**Problem:** A turret only accepts target angles from `0.0` to `180.0` degrees, inclusive. Write two
methods.

`checkAngle` throws an `IllegalArgumentException` whose message is exactly
`"Angle out of range: " + degrees` when `degrees` is below `0.0` or above `180.0`, and does nothing
otherwise.

`firstRejection` takes an array of requested angles and calls `checkAngle` on each one, in order.
It returns the **message** of the **first** exception that `checkAngle` throws (use `try`/`catch`
and `getMessage()`). If no request is rejected, it returns `"all accepted"`.

Examples:

- `firstRejection(new double[] {10.0, 240.0, 90.0})` returns `"Angle out of range: 240.0"`
- `firstRejection(new double[] {0.0, 180.0})` returns `"all accepted"`
- `firstRejection(new double[] {-5.0})` returns `"Angle out of range: -5.0"`

**Signature:** `public static String firstRejection(double[] requests)`

**Starter:**

```java
public class Solution
{
    public static void checkAngle(double degrees)
    {
        // TODO: throw IllegalArgumentException when degrees is out of range
    }

    public static String firstRejection(double[] requests)
    {
        // TODO: return the first rejection's message, or "all accepted"
    }
}
```

**Tests:**

| Visible | Arguments | Expected |
|---|---|---|
| yes | `new double[] {10.0, 240.0, 90.0}` | `"Angle out of range: 240.0"` |
| yes | `new double[] {0.0, 180.0}` | `"all accepted"` |
| yes | `new double[] {-5.0}` | `"Angle out of range: -5.0"` |
| no | `new double[] {200.5, 300.0}` | `"Angle out of range: 200.5"` |
| no | `new double[] {90.0, 181.0}` | `"Angle out of range: 181.0"` |
| no | `new double[] {}` | `"all accepted"` |
| no | `new double[] {180.0, 0.0, -0.5, 400.0}` | `"Angle out of range: -0.5"` |

**Solution:**

```java
public class Solution
{
    public static void checkAngle(double degrees)
    {
        if (degrees < 0.0 || degrees > 180.0)
        {
            throw new IllegalArgumentException("Angle out of range: " + degrees);
        }
    }

    public static String firstRejection(double[] requests)
    {
        for (double angle : requests)
        {
            try
            {
                checkAngle(angle);
            }
            catch (IllegalArgumentException e)
            {
                return e.getMessage();
            }
        }
        return "all accepted";
    }
}
```

**Why:** `checkAngle` is the `throw` side: it builds the exception with a message that includes the
bad value. `firstRejection` is the `catch` side: the `try` wraps the call that might throw,
and the `catch` for `IllegalArgumentException` reports `e.getMessage()` instead of ignoring the
problem. Returning from inside the `catch` stops at the first rejection. Without that, the loop
keeps going and ends up reporting a later rejection, which the hidden tests with two bad angles
catch. The `<` and `>` (not `<=` and `>=`) keep `0.0` and `180.0` legal.
