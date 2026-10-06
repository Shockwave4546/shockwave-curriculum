---
outlineRef: "16 — Writing Your Own Generics (ORACLE 14.1-5)"
pairsWith: "[`lessons/ch16-writing-your-own-generics/16-writing-your-own-generics.md`](../../lessons/ch16-writing-your-own-generics/16-writing-your-own-generics.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
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


## Coding

**Mode:** full-program

**Problem:** Write a generic class `Pair<K, V>` and a generic method `Util.sameEntry`. The
fixed `main` uses them with three different type arguments, so nothing may be hard-coded to
`String` or `Double`.

- `Pair<K, V>` holds a key and a value. Its constructor takes `(K key, V value)`, and it has
  `getKey()` (returns a `K`) and `getValue()` (returns a `V`).
- `Util.sameEntry(Pair<K, V> p1, Pair<K, V> p2)` is a static generic method that returns `true`
  when the two pairs have equal keys **and** equal values, and `false` otherwise. Two separate
  `Pair` objects built from the same text and number count as the same entry.

The `main` reads two telemetry readings (a name and a number each) and a slot (an ID number and a
name), then prints three lines. For the input `FL_Current 12.5 FL_Current 12.5 3 Left`:

```text
FL_Current -> 12.5
true
4 LEFT
```

**Starter:**

```java
import java.util.*;

public class Main
{
    // Don't change main
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        Pair<String, Double> a = new Pair<>(in.next(), in.nextDouble());
        Pair<String, Double> b = new Pair<>(in.next(), in.nextDouble());
        Pair<Integer, String> slot = new Pair<>(in.nextInt(), in.next());
        System.out.println(a.getKey() + " -> " + a.getValue());
        System.out.println(Util.sameEntry(a, b));
        int nextId = slot.getKey() + 1;
        System.out.println(nextId + " " + slot.getValue().toUpperCase());
    }
}

// TODO: make Pair generic, with two type parameters
class Pair
{
}

class Util
{
    // TODO: a static generic method sameEntry(Pair<K, V> p1, Pair<K, V> p2)
}
```

**Scenario 1 (visible):**

**Input:**

```text
FL_Current 12.5 FL_Current 12.5 3 Left
```

**Expected output:**

```text
FL_Current -> 12.5
true
4 LEFT
```

**Scenario 2 (visible):**

**Input:**

```text
FL_Current 12.5 FR_Current 12.5 0 Center
```

**Expected output:**

```text
FL_Current -> 12.5
false
1 CENTER
```

**Scenario 3 (hidden):**

**Input:**

```text
Pitch 4.0 Pitch 4.5 9 Right
```

**Expected output:**

```text
Pitch -> 4.0
false
10 RIGHT
```

**Scenario 4 (hidden):**

**Input:**

```text
BusVoltage 12.25 BusVoltage 12.25 -1 Front
```

**Expected output:**

```text
BusVoltage -> 12.25
true
0 FRONT
```

**Scenario 5 (hidden):**

**Input:**

```text
Gyro 1000.5 Gyro 1000.5 41 Back
```

**Expected output:**

```text
Gyro -> 1000.5
true
42 BACK
```

**Solution:**

```java
import java.util.*;

public class Main
{
    // Don't change main
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        Pair<String, Double> a = new Pair<>(in.next(), in.nextDouble());
        Pair<String, Double> b = new Pair<>(in.next(), in.nextDouble());
        Pair<Integer, String> slot = new Pair<>(in.nextInt(), in.next());
        System.out.println(a.getKey() + " -> " + a.getValue());
        System.out.println(Util.sameEntry(a, b));
        int nextId = slot.getKey() + 1;
        System.out.println(nextId + " " + slot.getValue().toUpperCase());
    }
}

class Pair<K, V>
{
    private K key;
    private V value;

    public Pair(K key, V value)
    {
        this.key = key;
        this.value = value;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }
}

class Util
{
    public static <K, V> boolean sameEntry(Pair<K, V> p1, Pair<K, V> p2)
    {
        return p1.getKey().equals(p2.getKey()) && p1.getValue().equals(p2.getValue());
    }
}
```

**Why:** `class Pair<K, V>` introduces the two type variables, and the fields, constructor
parameters, and getter return types all use them. That is what lets `slot.getKey() + 1` compile in
`main`: `getKey()` returns an `Integer` there, not an `Object`. `sameEntry` declares its own
`<K, V>` right before the return type, and compares with `.equals`, because `==` on two separate
`String` or `Double` objects compares references and would report `false` for two entries that
read the same.
