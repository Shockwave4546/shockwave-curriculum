---
outlineRef: "13 — Common Gotchas (no citation — deck-original content)"
pairsWith: "[`lessons/ch13-common-gotchas/13-common-gotchas.md`](../../lessons/ch13-common-gotchas/13-common-gotchas.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Common Gotchas — Worked Example

## Problem

After 4 qualification matches, the scouting sheet shows the robot earned 38 climb points in total. Compute the average climb points per match for the pick-list meeting. This example works through the **integer division** gotcha: the obvious code compiles, runs, and quietly gives the wrong answer.

## Step 1: Plan It First

1. Store the total points and the number of matches.
2. Divide to get the average, and check whether the result is actually right.
3. If it's wrong, find out why and fix it.

The right answer, worked out by hand first: 38 ÷ 4 = **9.5**.

## Step 2: The Obvious First Try

```java
int totalClimbPoints = 38; // over 4 qualification matches
int matchesPlayed = 4;

double firstTry = totalClimbPoints / matchesPlayed;
System.out.println("First try:  " + firstTry);
```

```
First try:  9.0
```

Storing the result in a `double` didn't help. Java evaluates the right-hand side first: `totalClimbPoints / matchesPlayed` is `int / int`, so the answer is an `int` (`9`). The `.5` is thrown away, not rounded. Only after that is the `9` widened to `9.0` to fit the `double` variable, and by then the fraction is already gone.

## Step 3: A Tempting Fix That Still Doesn't Work

Casting to `double` sounds like the fix, but *where* the cast goes matters:

```java
double secondTry = (double) (totalClimbPoints / matchesPlayed);
System.out.println("Second try: " + secondTry);
```

```
Second try: 9.0
```

The parentheses force the division to happen first, still as `int / int`, so it still produces `9`. The cast then turns that `9` into `9.0`. The fraction was lost before the cast ever ran.

## Step 4: The Fix, Casting Before Dividing

```java
double average = (double) totalClimbPoints / matchesPlayed;
System.out.println("Correct:    " + average);
```

```
Correct:    9.5
```

Now the cast applies to `totalClimbPoints` alone, turning `38` into `38.0` *before* the division. `double / int` is floating-point division, so the `.5` survives. Only one operand needs to be a `double`.

## The Full Program

```java
public class ClimbAverage
{
    public static void main(String[] args)
    {
        int totalClimbPoints = 38; // over 4 qualification matches
        int matchesPlayed = 4;

        double firstTry = totalClimbPoints / matchesPlayed;
        System.out.println("First try:  " + firstTry);

        double secondTry = (double) (totalClimbPoints / matchesPlayed);
        System.out.println("Second try: " + secondTry);

        double average = (double) totalClimbPoints / matchesPlayed;
        System.out.println("Correct:    " + average);
    }
}
```

```
First try:  9.0
Second try: 9.0
Correct:    9.5
```

## Recap

- `int / int` always produces an `int`. The fractional part is cut off, not rounded, and no error or warning appears.
- Storing that result in a `double` doesn't bring the fraction back. The division already happened as whole numbers.
- Casting the result of the division (`(double) (a / b)`) is too late. Cast one operand *before* dividing (`(double) a / b`).
- Averages are where this bites most often, so always check an average against a hand-worked answer (Lesson 2.4 has the full casting rules).
