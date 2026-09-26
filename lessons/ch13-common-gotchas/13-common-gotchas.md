---
outlineRef: "13 — Common Gotchas (no citation — deck-original content)"
status: "new — authored lesson (fuller depth than the teaser slide)"
---

# Common Gotchas

This chapter is a quick-reference checklist, not new material — each item below is taught in full elsewhere in this curriculum. Its job is to put the most common real mistakes side by side, since they tend to resurface long after the lesson that first covered them. **Note:** this list is expected to grow once real code-review and exercise practice surfaces more of the mistakes people actually make — it currently only covers what the original deck flagged.

## == vs. .equals()

`==` compares primitives (`int`, `double`, `boolean`) by value, which is correct and sufficient for them. For objects — including `String` — `==` instead checks whether two variables point at the *exact same object in memory*, which is almost never what you actually want to ask:

```java
String a = new String("BlueAlliance-Left");
String b = new String("BlueAlliance-Left");
System.out.println(a == b);        // false — two different objects, same text
System.out.println(a.equals(b));   // true — compares the actual characters
```

Use `.equals()` — or a purpose-built comparison method like `.equalsIgnoreCase()`, `.compareTo()`, or `.contains()` — for any object type, including boxed numbers like `Integer` and `Double`. See Lesson 6.1 for the full explanation.

A few `==` special cases worth knowing by heart:

- **`double ==`.** Even without boxing, `0.1 + 0.2 == 0.3` is `false` — floating-point math rarely lands on an exact value. Compare with a tolerance instead (`Math.abs(a - b) < 0.0001`), as covered in Lesson 2.4.
- **`Integer ==`.** Java caches small boxed `Integer` values (`-128` to `127`), so `Integer x = 100, y = 100; x == y` happens to be `true` — but `Integer p = 1000, q = 1000; p == q` is `false`. Never rely on this; always use `.equals()` for boxed numbers.
- **Enums are the exception.** `==` *is* safe (and preferred) for comparing enum constants (Lesson 11) — there's only ever one object per constant, so `==` and `.equals()` always agree.

## Integer Division

Dividing two `int`s produces an `int` — the fractional part is silently discarded (truncated), not rounded:

```java
int result = 5 / 2;       // 2, not 2.5 — the .5 is thrown away, not rounded
double result2 = 5.0 / 2.0; // 2.5 — at least one operand must be a floating-point type
```

This bites often when averaging (`total / count` where both are `int`) — cast at least one operand to `double` first. See Lesson 2.4 for casting rules in full.

## NullPointerException

Calling a method or accessing a field on a variable that's `null` (declared but never assigned a real object) throws `NullPointerException` — one of the most common runtime crashes in any Java program, robot code included:

```java
Drivetrain drivetrain = null; // explicitly assigned null — no real object yet
drivetrain.stop();            // NullPointerException — nothing to call stop() on
```

(A *local* variable left truly unassigned — just `Drivetrain drivetrain;` with no `= null` — is a different, compile-time error: Java refuses to compile code that reads it before it's given a value, reporting "variable drivetrain might not have been initialized." Only a *field* defaults to `null` automatically.)

The fix is always the same shape: make sure every object is actually constructed (`new Drivetrain(...)`) before anything calls a method on it, and check for `null` explicitly at any point where a value might legitimately be missing (e.g., a `HashMap.get()` that found no match — see Lesson 9.3).

## Off-by-One

Arrays (and `ArrayList`) are indexed starting at `0` — the last valid index is always `length - 1` (or `size() - 1`), never `length` itself:

```java
int[] canBusIds = new int[10]; // valid indices: 0 through 9
// ArrayIndexOutOfBoundsException — 10 is one past the end
System.out.println(canBusIds[10]);
```

This is the single most common loop-bound mistake — writing `i <= array.length` instead of `i < array.length`. See Lesson 9.1 (arrays) and 9.2 (ArrayList) for the full indexing rules.

## Ignoring a Return Value

Methods like `String.toUpperCase()`, `.trim()`, and `.replace()` don't modify the object they're called on — `String` is immutable — they *return* a new value. Calling one and throwing away the result does nothing:

```java
String teamName = "shockwave";
teamName.toUpperCase();               // return value discarded — teamName is unchanged
teamName = teamName.toUpperCase();    // correct — reassign the result
```

See Lesson 6.1 for the full list of String methods that work this way.

## switch Fall-Through

A colon-style `switch` (Lesson 5.12) keeps running into the *next* `case` once one matches, unless a `break` stops it — forgetting one is a classic bug:

```java
switch (day)
{
    case 1:
        System.out.println("Mon");
    case 2:                          // day == 2 starts here...
        System.out.println("Tue");
    case 3:                          // ...and falls through to here too
        System.out.println("Wed");
        break;
    default:
        System.out.println("other");
}
// day == 2 prints both "Tue" and "Wed" — not just "Tue"
```

Arrow-style `case ->` (also Lesson 5.12) never falls through, which is why this course defaults to it.

## Common Pitfalls

- **Treating this chapter as the complete list of Java mistakes.** It isn't — it's the handful the original deck happened to flag. Real practice will surface plenty more (this chapter is expected to grow).
- **Fixing the symptom instead of the cause.** E.g., wrapping a `NullPointerException` in a `try`/`catch` (Lesson 12) instead of fixing why the object was never constructed in the first place.

## Key Takeaways

- Use `==` for primitives, `.equals()` for objects (Lesson 6.1) — except enums, where `==` is safe. Watch `double ==` and the `Integer` cache.
- `int / int` truncates; make at least one operand a floating-point type to keep the fractional part (Lesson 2.4).
- `NullPointerException` means something was used before it was actually constructed — always initialize before use (Lessons 4.4–4.6, 9.1).
- Valid indices run from `0` to `length - 1` (or `size() - 1`) — never `length` itself (Lessons 9.1, 9.2).
- A discarded `String` method return value does nothing; a colon-style `switch` without `break` falls through to the next `case`.
- This is a living checklist, not a finished one — expect it to grow as more real gotchas surface through practice.

Derived from `mechacoder-test`: `src/lessons/java-1.js`, slide 13 ("Common Gotchas") — original deck content, no external citation
