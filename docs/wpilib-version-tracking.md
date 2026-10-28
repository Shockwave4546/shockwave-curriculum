# WPILib version tracking

What the course uses that isn't in the WPILib release our checker runs yet. Re-check this list every
time WPILib publishes a new 2027 release, then update Piston and remove the notes below.

## Current versions (as of 10-28-2026)

- **Newest WPILib release:** 2027.0.0-alpha-7 (09-01-2026).
- **Checker (local Piston):** the same alpha-7 jars, in `~/piston-data/packages/java/25.0.1/wpilib/`.
- **Course content:** Ch.25 was written from allwpilib `main`, so it can be ahead of the release.

## Ahead of the release

| API | In `main` since | Used in | Note to remove when released |
|---|---|---|---|
| `whenExited(...)` (Commands v3) | 09-13-2026, [wpilibsuite/allwpilib#9402](https://github.com/wpilibsuite/allwpilib/pull/9402) | Lessons 25.2, 25.3, 25.7; Examples 25.2, 25.6, 25.7; Exercise 25.2 (Micro-Parsons) | "Version note" under "Cleaning Up When a Command Ends" in Lesson 25.2 |

No Coding exercise uses `whenExited`, so nothing a student runs in the checker fails today. The
Micro-Parsons checks for 25.2 (`tools/parsons_orders/ch19-28/`) swap in `whenCanceled` to compile
against alpha-7; remove that replacement once the jar has `whenExited`.

## When a new release ships

1. Check each row above against the release's API docs.
2. Update the Piston WPILib jars to the new release (see `tools/piston/`).
3. Remove the matching notes and the harness replacement, then delete the row.
