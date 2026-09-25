---
outlineRef: "16 — Writing Your Own Generics (ORACLE 14.1-5)"
pairsWith: "[`lessons/ch16-writing-your-own-generics/16-writing-your-own-generics.md`](../../lessons/ch16-writing-your-own-generics/16-writing-your-own-generics.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
---

# Writing Your Own Generics — Exercises

## Multiple Choice

**Question:** A teammate wants a generic method that accepts any number type (`Integer`, `Double`, and so on) and returns it as a `double` by calling `value.doubleValue()` inside the body. Which method header compiles, with the body `return value.doubleValue();`?

**Options:**

- A. `public static <T> double toDouble(T value)`
- B. `public static <T extends Number> double toDouble(T value)`
- C. `public static double toDouble(T value)`
- D. `public static <T> double toDouble(T extends Number value)`

**Answer:** B

**Why:** `<T extends Number>` introduces the type variable `T` and restricts it to `Number` and its subtypes. Because of that bound, the compiler knows every possible `T` has a `doubleValue()` method, so `value.doubleValue()` compiles.

- A is wrong because `<T>` has no bound, so the compiler only knows `value` is *some* type. It has no guarantee of a `doubleValue()` method, and the call fails with "cannot find symbol."
- C is wrong because `T` is never introduced. There's no `<T>` before the return type, so `T` isn't a known type at all and the header itself doesn't compile.
- D is wrong because the bound belongs where the type parameter is declared (`<T extends Number>`), not in the parameter list. `T extends Number value` is a syntax error.

## Micro-Parsons

**Problem:** These lines, once correctly ordered, form a complete program: a generic `Tunable<T>` class that can hold a tuning value of any type, plus a `main` method that uses it to store a `Double` gain of `0.05` and print it. The program should print `0.05`. Put the class's field and methods above `main`.

Reorder the fragments below into a working program:

- a. `        kP.set(0.05);`
- b. `    public T get() { return value; }`
- c. `{`
- d. `        System.out.println(kP.get());`
- e. `    public static void main(String[] args)`
- f. `}`
- g. `    private T value;`
- h. `        Tunable<Double> kP = new Tunable<>();`
- i. `public class Tunable<T>`
- j. `    }`
- k. `    public void set(T v) { value = v; }`
- l. `    {`

**Answer:** i, c, g, k, b, e, l, h, a, d, j, f

**Interchangeable:** (g, k, b)

```java
public class Tunable<T>
{
    private T value;
    public void set(T v) { value = v; }
    public T get() { return value; }

    public static void main(String[] args)
    {
        Tunable<Double> kP = new Tunable<>();
        kP.set(0.05);
        System.out.println(kP.get());
    }
}
```

**Why this order:** The class line (`i`) comes first, since it introduces `T`, and its opening brace (`c`) follows. Inside the class, the field (`g`) and the two methods (`k`, `b`) can go in any order among themselves: Java doesn't care whether a field is declared above or below the methods that use it. Putting the field first is just the usual convention. `main` (`e`) and its opening brace (`l`) come next. Inside `main`, the `Tunable<Double>` has to be created (`h`) before anything can be stored in it. The value must be `set` (`a`) before `get` (`d`) can print it, or `get()` would print `null`. The braces close in reverse: `main`'s body (`j`), then the class's body (`f`).
