---
outlineRef: "26 — Architecture Takeaways (DRY/YAGNI/SOLID) (no citation — deck-original content; neither WPILib nor T5817 teach these as named general principles)"
pairsWith: "[`lessons/ch26-architecture-takeaways/26-architecture-takeaways.md`](../../lessons/ch26-architecture-takeaways/26-architecture-takeaways.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Architecture Takeaways — Worked Example

## Problem

A teammate's climber code reports three settings, and all three happen to be `0.5`: the winch speed while extending, the winch speed while retracting, and the brightness of the climber's status light. The drive coach wants the winch sped up to `0.6` in both directions — but the status light should stay exactly as bright as it is. Refactor the code so it follows DRY, without forcing unrelated values together.

## Step 1: Start From the Repeated Version

```java
public class Climber
{
    public static void main(String[] args)
    {
        System.out.println("Extending at speed " + 0.5);
        System.out.println("Retracting at speed " + 0.5);
        System.out.println("Status light brightness " + 0.5);
    }
}
```

Prints:

```
Extending at speed 0.5
Retracting at speed 0.5
Status light brightness 0.5
```

The same literal `0.5` appears three times. To make the coach's change, someone has to find every copy and decide which ones to edit — and missing one (say, updating extend but not retract) would leave the winch running at two different speeds, with nothing to warn anyone.

## Step 2: Ask *Why* Each Value Is `0.5`

DRY is about duplicated *knowledge*, not duplicated characters. Before merging anything, check what each `0.5` actually means:

- Extending speed and retracting speed are the **same fact** — "how fast the winch runs." The coach's request changes both together, so they should come from one source.
- Status light brightness is a **different fact** that just happens to have the same value today. The coach's request should *not* change it.

This is the lesson's first Common Pitfall in action: forcing all three into one shared constant because they look the same would tie the light's brightness to the winch speed — an awkward, accidental dependency between two things that should stay separate.

## Step 3: One Named Constant per Real Fact

Use `public static final` constants (Ch.7.4, and the same `Constants` style as Ch.25.7) — one for each distinct fact:

```java
public class Climber
{
    public static final double WINCH_SPEED = 0.5;
    public static final double LED_BRIGHTNESS = 0.5;

    public static void main(String[] args)
    {
        System.out.println("Extending at speed " + WINCH_SPEED);
        System.out.println("Retracting at speed " + WINCH_SPEED);
        System.out.println("Status light brightness " + LED_BRIGHTNESS);
    }
}
```

The output is identical to Step 1 — refactoring for DRY changes where a value lives, not what the program does.

## Step 4: Make the Coach's Change — in One Place

Now the requested change is a single edit:

```java
public static final double WINCH_SPEED = 0.6;
```

With everything else left exactly as in Step 3, it prints:

```
Extending at speed 0.6
Retracting at speed 0.6
Status light brightness 0.5
```

Both winch directions moved together because they share one source of truth, and the light stayed put because it has its own. Neither outcome depended on anyone remembering to hunt down every copy.

## Recap

- DRY means one source of truth for each piece of knowledge — here, one named constant per real setting.
- Before merging duplicated values, ask whether they're the same fact or just the same number today; only the same fact belongs in one shared constant.
- A DRY refactor shouldn't change behavior on its own — it changes how many places a future edit has to touch (ideally, one).
