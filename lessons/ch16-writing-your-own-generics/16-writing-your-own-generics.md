---
outlineRef: "16 — Writing Your Own Generics (ORACLE 14.1-5)"
status: "new — authored lesson (fuller depth than the teaser slide)"
---

# Writing Your Own Generics

`List<String>`, `Map<Integer, Double>`, `ArrayList<Double>` — every collection since Ch.9 has *used* a generic type someone else wrote. This chapter is about writing your own.

## Why Generics Exist

Before generics, a reusable container had to work with the generic `Object` type, requiring an explicit cast every time you got something back out — and nothing stopped the wrong type from going in in the first place:

```java
List list = new ArrayList();         // no generics
list.add("hello");
String s = (String) list.get(0);     // cast required, and could fail at runtime
```

The `(String)` is a **cast**: it forces the compiler to treat the value as that type. If the object handed back weren't actually a `String`, this line would compile fine and then throw `ClassCastException` at runtime instead of failing to compile.

With a type parameter, the compiler enforces correctness *before* the program ever runs, and the cast disappears entirely:

```java
List<String> list = new ArrayList<String>();
list.add("hello");
// no cast — the compiler already knows it's a String
String s = list.get(0);
```

## Writing a Generic Class

A generic class introduces one or more **type parameters** in angle brackets after the class name. Here's a value wrapper — a natural fit for logging one tunable robot value (a setpoint, a gain, a mode name) without having to commit to `double` or `String` up front, using a placeholder type instead:

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
// the "diamond" <> — compiler infers Double from the left side
LoggedValue<Double> setpoint = new LoggedValue<>();
setpoint.set(3.5);    // OK
// compile error — a String doesn't belong in a LoggedValue<Double>
setpoint.set("fast");
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

A quick primer before this section's example: `Number` is a Java class — like `Object`, the ultimate parent of every class in Java (Ch.17 covers what that relationship means for classes you write yourself) — that `Integer`, `Double`, and the other numeric wrapper classes all `extends`. That's what makes "any subtype of `Number`" a meaningful thing to say, and it's the same "is a more specific kind of" relationship Ch.17 covers in full.

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

## What Generics Can't Do

Generics only exist at compile time — the compiler checks everything, then largely erases the type information before the program runs (this is called **type erasure**). That limits what a generic class can do with its own type parameter:

- No `new T()` — the compiler doesn't know at runtime which constructor to call.
- No `new T[10]` — creating an array of the type parameter doesn't compile, for the same reason.
- No `static` field or method of type `T` — a type parameter belongs to each individual object, not to the class itself.

Skipping the type argument entirely (`List list = new ArrayList();`, this lesson's very first snippet) is called a **raw type** — it compiles, but with an "unchecked" warning, not a hard error. Java kept raw types working only so pre-generics code (written before Java 5) wouldn't break; never write one on purpose in new code.

## Common Pitfalls

- **Forgetting the `<T>` on the class declaration itself.** `public class Box { private T t; }` doesn't compile — `T` has to be introduced with `public class Box<T>` before it can be used anywhere inside the class.
- **Using a primitive as a type argument.** `LoggedValue<double>` doesn't compile — type arguments must be reference types, so use the wrapper (`LoggedValue<Double>`) instead, same rule as `ArrayList` (Lesson 9.2).
- **Calling a bound-specific method without the bound.** `value.doubleValue()` only compiles once `T` is declared `extends Number` — without the bound, the compiler only knows `T` is *some* type, with no guaranteed methods beyond what every `Object` has.
- **Expecting `new T()`, `new T[]`, or a `static T` to work.** Type erasure means none of them compile — see "What Generics Can't Do" above.

## Key Takeaways

- A generic class introduces type parameters in angle brackets after its name (`class LoggedValue<T>`); the type variable then stands in for a real type anywhere in the class.
- Generic types replace the old cast-from-`Object` pattern with compile-time type safety — a wrong type is now a compile error, not a runtime surprise.
- A generic method can introduce its own type parameter, scoped to just that method; the compiler usually infers the type automatically.
- `<T extends SomeType>` restricts what a type parameter can be, and unlocks calling `SomeType`'s own methods on values of that type.
- Type erasure means a generic class can't `new T()`, `new T[]`, or use `T` statically; skipping the type argument entirely compiles as a raw type, with an unchecked warning.
- The `?` wildcard represents an unknown type for referring to a generic type generically — it's never used when constructing one.

Derived from `other-reference-repo`: `oracle-java-tutorials/generics/01-why-use-generics.md`, `02-generic-types.md`, `03-generic-methods.md`, `04-bounded-type-parameters.md`, `05-wildcards.md` (ORACLE 14.1-5)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 2 ("Writing Your Own Generics")
