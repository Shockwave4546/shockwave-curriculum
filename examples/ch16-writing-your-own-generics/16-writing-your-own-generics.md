---
outlineRef: "16 — Writing Your Own Generics (ORACLE 14.1-5)"
pairsWith: "[`lessons/ch16-writing-your-own-generics/16-writing-your-own-generics.md`](../../lessons/ch16-writing-your-own-generics/16-writing-your-own-generics.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Writing Your Own Generics — Worked Example

## Problem

The dashboard should show both the current value and the previous value for several robot readings, so drivers can spot a sudden jump. The arm angle is a `Double`, and the drive mode is a `String`. Write one reusable class that remembers "current and previous" for a value of *any* type. Then write a method that computes how much a *numeric* reading changed, one that only accepts number readings.

## Step 1: Plan It First

1. One class that works for any value type means a generic class with a type parameter `T`.
2. The class holds two values of that same type (current and previous). Updating it moves current into previous, then stores the new value as current.
3. "How much did it change" only makes sense for numbers, so the method needs a bounded type parameter: `T extends Number`.

## Step 2: Why Not Just Write Two Classes?

Without generics, this would need a `DoubleReading` class for the arm angle and a separate `StringReading` class for the drive mode, with identical logic and only the field types different. Every future reading type would need yet another copy. With a type parameter, one class covers all of them, and the compiler still checks that each reading only ever holds its own type.

## Step 3: Write the Generic Class

```java
public class LatestReading<T>
{
    private T current;
    private T previous;

    public LatestReading(T initial)
    {
        current = initial;
        previous = initial;
    }

    public void update(T newValue)
    {
        previous = current;
        current = newValue;
    }

    public T getCurrent()  { return current; }
    public T getPrevious() { return previous; }
}
```

The `<T>` after the class name introduces the type variable. Without it, `T` wouldn't compile anywhere inside the class. After that, `T` stands in for the real type everywhere: both fields, the constructor parameter, `update`'s parameter, and both getters' return types. The constructor sets both fields to the starting value, so `getPrevious()` never returns `null` before the first `update`.

## Step 4: Use It With Two Different Types

```java
LatestReading<Double> armAngle = new LatestReading<>(42.0);
armAngle.update(45.5);
System.out.println(armAngle.getPrevious() + " -> " + armAngle.getCurrent()); // 42.0 -> 45.5

LatestReading<String> driveMode = new LatestReading<>("Field-Relative");
driveMode.update("Robot-Relative");
System.out.println("Switched from " + driveMode.getPrevious()); // Switched from Field-Relative
```

The diamond `<>` lets the compiler infer `Double` (and then `String`) from the left side. The type argument is `Double`, not `double`, because type arguments must be reference types. `42.0` and `45.5` are autoboxed automatically, the same as with `ArrayList<Double>`.

Because `armAngle` is a `LatestReading<Double>`, the compiler rejects the wrong type before the program ever runs:

```java
armAngle.update("fast"); // compile error — a String doesn't belong in a LatestReading<Double>
```

## Step 5: The Bounded Method — Only Numbers Allowed

```java
public class ReadingMath
{
    public static <T extends Number> double change(LatestReading<T> reading)
    {
        return reading.getCurrent().doubleValue() - reading.getPrevious().doubleValue();
    }
}
```

`<T extends Number>` goes right before the return type, and it belongs to this one method only. The bound is what makes `.doubleValue()` legal. With a plain `<T>`, the compiler would only know `T` is *some* type, and `getCurrent().doubleValue()` would fail with "cannot find symbol."

```java
System.out.println(ReadingMath.change(armAngle)); // 3.5

LatestReading<Integer> piecesScored = new LatestReading<>(3);
piecesScored.update(5);
System.out.println(ReadingMath.change(piecesScored)); // 2.0
```

Type inference works out `T` from the argument, so the call is just `ReadingMath.change(armAngle)`. `Integer` works too, since it's also a subtype of `Number`. The result is `2.0`, not `2`, because the method returns a `double`.

The drive-mode reading is correctly rejected:

```java
ReadingMath.change(driveMode); // compile error — String isn't a subtype of Number
```

## Recap

- `public class LatestReading<T>` introduces a type variable that stands in for a real type everywhere inside the class: fields, parameters, and return types.
- One generic class replaces a separate copy per type, and the compiler still rejects the wrong type at compile time.
- The diamond `<>` lets the compiler infer the type argument. Type arguments must be wrapper types like `Double`/`Integer`, never primitives.
- A generic method declares its own type parameter before its return type, and the compiler infers it from the arguments.
- `<T extends Number>` limits the method to number types and is what makes calling `doubleValue()` legal.
