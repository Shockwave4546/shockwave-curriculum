---
outlineRef: "12 — Exceptions & try/catch (ORACLE 11.1-16)"
pairsWith: "[`lessons/ch12-exceptions-and-try-catch/12-exceptions-and-try-catch.md`](../../lessons/ch12-exceptions-and-try-catch/12-exceptions-and-try-catch.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
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
