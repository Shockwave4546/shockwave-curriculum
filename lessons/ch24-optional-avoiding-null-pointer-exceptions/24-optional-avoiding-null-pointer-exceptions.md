# Optional: Avoiding Null Pointer Exceptions

**Outline ref:** 24 — Optional: Avoiding Null Pointer Exceptions (ORACLE 16.1) — renamed from "Optional: Maybe a Value" to disambiguate from optional method parameters; the deck's actual slide heading is unchanged
**Status:** new — authored lesson (fuller depth than the teaser slide)

## The Null Problem

Returning `null` to mean "there's no value here" is one of the most common sources of bugs in any Java program — Tony Hoare, who introduced the null reference in 1965, later called it his "billion-dollar mistake." The trouble is that `null` is invisible in a method's signature: nothing about `Pose2d getVisionPose()` warns a caller that it might come back `null`, so it's easy to forget the check and get a `NullPointerException` (Ch.12/13) instead.

The classic FRC case: a vision pose estimator can only report a robot position if a camera actually sees an AprilTag *this frame* — plenty of frames, it can't. Returning `null` on those frames leaves every caller responsible for remembering to check first.

## Optional: Making "Might Be Absent" Part of the Type

`java.util.Optional<T>` is a container that either holds a value, or is explicitly **empty** — and unlike `null`, that possibility is written directly into the method's return type:

```java
public Optional<Pose2d> getPose()
{
    if (!hasTargetThisFrame())
    {
        return Optional.empty();       // explicitly "no value" — not null
    }
    return Optional.of(currentPose);   // wraps a real, non-null value
}
```

Just by reading `Optional<Pose2d> getPose()`'s signature, a caller already knows the pose might not be there this frame — the type itself documents it, instead of relying on a comment or tribal knowledge.

## Creating an Optional

```java
Optional<Pose2d> empty = Optional.empty();           // definitely no value
Optional<Pose2d> present = Optional.of(currentPose);  // wraps a value — throws immediately if currentPose is null
Optional<Pose2d> maybe = Optional.ofNullable(currentPose); // empty if currentPose is null, present otherwise
```

`Optional.of(...)` is a deliberate safety check: if you accidentally pass it a `null`, it throws right away — better to fail loudly at the source than to silently wrap a `null` and have it surface as a confusing failure somewhere else later.

## Handling Both Cases Honestly

```java
Optional<Pose2d> visionPose = vision.getPose();

// Run logic only when a value exists
visionPose.ifPresent(pose -> estimator.addVisionMeasurement(pose, timestamp));

// Or supply a fallback value for the empty case
Pose2d pose = visionPose.orElse(lastKnownPose);

// Or throw a specific exception if a value was truly required
Pose2d requiredPose = visionPose.orElseThrow(IllegalStateException::new);
```

`ifPresent` runs a lambda (Lesson 19.1) only if a value is actually there — nothing happens otherwise. `orElse` supplies a fallback value for the empty case. `orElseThrow` is for the rarer case where an empty `Optional` really does mean something has gone wrong, and continuing anyway wouldn't make sense.

## The One Pitfall That Defeats the Whole Point

`Optional` has an `isPresent()` check and a `get()` method that returns the wrapped value — but calling `get()` without checking `isPresent()` first throws `NoSuchElementException` on an empty `Optional`, which is exactly the same class of crash `Optional` exists to prevent, just under a different exception name:

```java
Pose2d pose = visionPose.get(); // never do this blind — this is a NullPointerException with extra steps
```

Even the safer `isPresent()` + `get()` pairing is discouraged — it's really just a nested-null-check in disguise. `ifPresent`, `orElse`, and `orElseThrow` all handle both cases directly, without ever needing to call bare `get()`.

## Filtering and Transforming (a Brief Look)

Beyond the core methods above, `Optional` supports `filter` (keep the value only if it matches a condition, otherwise become empty) and `map` (transform the value, if present, into something else) — useful for chaining a couple of extra checks without falling back into nested `if` statements:

```java
visionPose
    .filter(pose -> pose.getX() >= 0)         // only proceed if the pose has a valid X coordinate
    .ifPresent(pose -> estimator.addVisionMeasurement(pose, timestamp));
```

These compose well for simple cases; genuinely complex chains of `Optional` transformations are a more advanced topic than this curriculum covers in depth.

## Common Pitfalls

- **Calling `.get()` without checking first.** This throws on an empty `Optional`, defeating the entire purpose of using one.
- **Using `Optional` for every field or parameter, out of habit.** It's meant for genuinely optional *results* (especially return values) — not a blanket replacement for every reference type in a program.
- **Passing a `null` to `Optional.of(...)`.** That throws immediately — use `Optional.ofNullable(...)` instead when the value genuinely might be `null`.

## Key Takeaways

- `Optional<T>` makes "this might not have a value" visible directly in a method's return type, instead of relying on an invisible, easy-to-forget `null` check.
- Create one with `Optional.empty()`, `Optional.of(value)` (throws if `value` is null), or `Optional.ofNullable(value)` (safe either way).
- Handle both cases with `ifPresent(...)`, `orElse(fallback)`, or `orElseThrow(...)` — never call bare `.get()` without checking first.
- `filter` and `map` let you chain a couple of extra conditions/transformations without falling back into nested `if` checks.

Derived from `other-reference-repo`: `oracle-java-tutorials/optional/java8-optional.md` (ORACLE 16.1)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 9b ("Optional: Maybe a Value") — vision pose estimator example
