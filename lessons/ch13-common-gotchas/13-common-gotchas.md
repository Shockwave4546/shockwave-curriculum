# Common Gotchas

**Outline ref:** 13 — Common Gotchas (no citation — deck-original content)
**Status:** new — authored lesson (fuller depth than the teaser slide)

This chapter is a quick-reference checklist, not new material — each item below is taught in full elsewhere in this curriculum. Its job is to put the most common real mistakes side by side, since they tend to resurface long after the lesson that first covered them. **Note:** this list is expected to grow once real code-review and exercise practice surfaces more of the mistakes people actually make — it currently only covers what the original deck flagged.

## == vs. .equals()

`==` compares primitives (`int`, `double`, `boolean`) by value, which is correct and sufficient for them. For objects — including `String` — `==` instead checks whether two variables point at the *exact same object in memory*, which is almost never what you actually want to ask:

```java
String a = new String("BlueAlliance-Left");
String b = new String("BlueAlliance-Left");
a == b;        // false — two different objects, even with identical text
a.equals(b);   // true — compares the actual characters
```

Use `.equals()` (or `.equals()`-style comparisons) for any object type, including boxed numbers like `Integer` and `Double`. See Lesson 6.1 for the full explanation.

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
Drivetrain drivetrain; // declared, but never assigned — currently null
drivetrain.stop();      // NullPointerException — nothing to call stop() on
```

The fix is always the same shape: make sure every object is actually constructed (`new Drivetrain(...)`) before anything calls a method on it, and check for `null` explicitly at any point where a value might legitimately be missing (e.g., a `HashMap.get()` that found no match — see Lesson 9.3).

## Off-by-One

Arrays (and `ArrayList`) are indexed starting at `0` — the last valid index is always `length - 1` (or `size() - 1`), never `length` itself:

```java
int[] canBusIds = new int[10]; // valid indices: 0 through 9
canBusIds[10]; // ArrayIndexOutOfBoundsException — 10 is one past the end
```

This is the single most common loop-bound mistake — writing `i <= array.length` instead of `i < array.length`. See Lesson 9.1 (arrays) and 9.2 (ArrayList) for the full indexing rules.

## Common Pitfalls

- **Treating this chapter as the complete list of Java mistakes.** It isn't — it's the handful the original deck happened to flag. Real practice will surface plenty more (this chapter is expected to grow).
- **Fixing the symptom instead of the cause.** E.g., wrapping a `NullPointerException` in a `try`/`catch` (Lesson 12) instead of fixing why the object was never constructed in the first place.

## Key Takeaways

- Use `==` for primitives, `.equals()` for objects (Lesson 6.1).
- `int / int` truncates; make at least one operand a floating-point type to keep the fractional part (Lesson 2.4).
- `NullPointerException` means something was used before it was actually constructed — always initialize before use (Lessons 4.4–4.6, 9.1).
- Valid indices run from `0` to `length - 1` (or `size() - 1`) — never `length` itself (Lessons 9.1, 9.2).
- This is a living checklist, not a finished one — expect it to grow as more real gotchas surface through practice.

Derived from `mechacoder-test`: `src/lessons/java-1.js`, slide 13 ("Common Gotchas") — original deck content, no external citation
