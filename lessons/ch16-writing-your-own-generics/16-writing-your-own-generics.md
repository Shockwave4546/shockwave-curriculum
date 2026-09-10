# Writing Your Own Generics

**Outline ref:** 16 — Writing Your Own Generics (ORACLE 14.1-5)
**Status:** new — authored lesson (fuller depth than the teaser slide)

`List<String>`, `Map<Integer, Double>`, `ArrayList<TalonFX>` — every collection since Ch.9 has *used* a generic type someone else wrote. This chapter is about writing your own.

## Why Generics Exist

Before generics, a reusable container had to work with the generic `Object` type, requiring an explicit cast every time you got something back out — and nothing stopped the wrong type from going in in the first place:

```java
List list = new ArrayList();         // no generics
list.add("hello");
String s = (String) list.get(0);     // cast required, and could fail at runtime
```

With a type parameter, the compiler enforces correctness *before* the program ever runs, and the cast disappears entirely:

```java
List<String> list = new ArrayList<String>();
list.add("hello");
String s = list.get(0);              // no cast — the compiler already knows it's a String
```

## Writing a Generic Class

A generic class introduces one or more **type parameters** in angle brackets after the class name. Here's a value wrapper — a natural fit for logging a tunable robot value alongside its current setpoint, using a placeholder type instead of committing to `double` or `String` up front:

```java
public class LoggedValue<T>
{
    private T value;

    public void set(T v) { value = v; }
    public T get() { return value; }
}
```

`T` isn't a real type — it's a **type variable**, a placeholder standing in for whatever concrete type gets supplied when the class is actually used:

```java
LoggedValue<Double> setpoint = new LoggedValue<>(); // the "diamond" <> — compiler infers Double from the left side
setpoint.set(3.5);    // OK
setpoint.set("fast"); // compile error — a String doesn't belong in a LoggedValue<Double>
```

By convention, type parameters are single uppercase letters — `T` (Type), `E` (Element, used throughout the collections you already know), `K`/`V` (Key/Value, as in `Map<K, V>`), `N` (Number). This convention exists specifically so a type variable is instantly recognizable and never confused with a real class name.

A generic class can take more than one type parameter, exactly like `Map<K, V>` does:

```java
public class Pair<K, V>
{
    private K key;
    private V value;

    public Pair(K key, V value)
    {
        this.key = key;
        this.value = value;
    }

    public K getKey()   { return key; }
    public V getValue() { return value; }
}

Pair<String, Double> reading = new Pair<>("Front-Left Current", 12.4);
```

## Generic Methods

A single method — even inside an otherwise non-generic class — can introduce its own type parameter, written in angle brackets right before the return type. Its scope is limited to that one method:

```java
public class Util
{
    public static <K, V> boolean sameEntry(Pair<K, V> p1, Pair<K, V> p2)
    {
        return p1.getKey().equals(p2.getKey()) && p1.getValue().equals(p2.getValue());
    }
}
```

Almost always, the compiler figures out the type on its own from how you call it — this is **type inference** — so you can call `Util.sameEntry(p1, p2)` directly, without ever writing the type parameter yourself.

## Bounded Type Parameters

Sometimes a generic type shouldn't accept *just anything* — a method built around numeric comparisons only makes sense for actual numbers. `extends` restricts a type parameter to a specific type (or subtype of it) — here meaning "any subtype of `Number`," which covers `Integer`, `Double`, and the rest:

```java
public static <T extends Number> double clampedValue(T value, double min, double max)
{
    double v = value.doubleValue(); // legal — Number guarantees a doubleValue() method
    if (v < min) return min;
    if (v > max) return max;
    return v;
}
```

Without the `extends Number` bound, `value.doubleValue()` wouldn't compile at all — the compiler would only know `value` is *some* type, with no guarantee it has a `doubleValue()` method to call. The bound is what unlocks calling methods that only `Number` (and its subtypes) actually have.

## Wildcards: A Quick Preview

The `?` wildcard represents an unknown type, mostly useful for parameters and fields where you want to accept "a `List` of anything" without pinning down exactly what. Wildcard variations (upper-bounded, lower-bounded) go beyond what this chapter covers — the short version to remember for now is: `?` is never used when *creating* a generic type (`new Box<?>()` isn't a thing) — only when referring to one you don't need to be specific about.

## Common Pitfalls

- **Forgetting the `<T>` on the class declaration itself.** `public class Box { private T t; }` doesn't compile — `T` has to be introduced with `public class Box<T>` before it can be used anywhere inside the class.
- **Using a primitive as a type argument.** `LoggedValue<double>` doesn't compile — type arguments must be reference types, so use the wrapper (`LoggedValue<Double>`) instead, same rule as `ArrayList` (Lesson 9.2).
- **Calling a bound-specific method without the bound.** `value.doubleValue()` only compiles once `T` is declared `extends Number` — without the bound, the compiler only knows `T` is *some* type, with no guaranteed methods beyond what every `Object` has.

## Key Takeaways

- A generic class introduces type parameters in angle brackets after its name (`class LoggedValue<T>`); the type variable then stands in for a real type anywhere in the class.
- Generic types replace the old cast-from-`Object` pattern with compile-time type safety — a wrong type is now a compile error, not a runtime surprise.
- A generic method can introduce its own type parameter, scoped to just that method; the compiler usually infers the type automatically.
- `<T extends SomeType>` restricts what a type parameter can be, and unlocks calling `SomeType`'s own methods on values of that type.
- The `?` wildcard represents an unknown type for referring to a generic type generically — it's never used when constructing one.

Derived from `other-reference-repo`: `oracle-java-tutorials/generics/01-why-use-generics.md`, `02-generic-types.md`, `03-generic-methods.md`, `04-bounded-type-parameters.md`, `05-wildcards.md` (ORACLE 14.1-5)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 2 ("Writing Your Own Generics")
