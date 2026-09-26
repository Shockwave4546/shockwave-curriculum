---
outlineRef: "12 — Exceptions & try/catch (ORACLE 11.1-16)"
status: "new — authored lesson (fuller depth than the teaser slide)"
---

# Exceptions & try/catch

## What an Exception Is

An **exception** is an "exceptional event" — something that disrupts a program's normal flow while it runs (a file that doesn't exist, an array index that's out of range, dividing by zero). When an error occurs, the method creates an **exception object** describing what went wrong and hands it to the Java runtime — this is called **throwing** the exception.

The runtime then searches back up the **call stack** (the chain of methods that led to this point) looking for an **exception handler** — a block of code able to deal with that type of exception. The first matching handler it finds is said to **catch** the exception. If nothing on the whole call stack can handle it, the runtime terminates the program: on a robot, an uncaught exception in `periodic()` is exactly what turns the Driver Station's "Robot Code" indicator red.

## try / catch

A `try` block wraps code that might throw; a `catch` block that follows it handles a specific exception type if one occurs:

```java
try
{
    config = loadFromFile("tuning.json");
}
catch (IOException e)
{
    // Recover: fall back to defaults
    config = Config.defaults();
    reportWarning("Using default tuning");
}
```

If `loadFromFile` throws an `IOException`, execution jumps straight into the matching `catch` block — the rest of the `try` block is skipped. If no exception occurs, the `catch` block never runs at all.

A `try` can have multiple `catch` blocks, checked in order, for handling different exception types differently:

```java
try
{
    camera = new UsbCamera("Camera 1", 0);
}
catch (VideoException e)
{
    reportWarning("Camera unavailable — skipping vision this match");
}
catch (NullPointerException e)
{
    reportWarning("Camera name was null");
}
```

`VideoException` is *unchecked* — it extends `RuntimeException` — so catching it here is optional, not compiler-required. Catching it anyway lets the robot keep running with vision disabled instead of crashing outright.

Two `catch` blocks for exception types that share no inheritance relationship can be combined into one with `|` (multi-catch), when they should be handled identically:

```java
catch (VideoException | NullPointerException e)
{
    reportWarning("Camera unavailable — skipping vision this match");
}
```

Order matters when the types *do* relate: a `catch` for a more general type (like `Exception`) must come *after* every more specific `catch` for one of its subclasses — putting the general one first makes the specific one unreachable, which is a compile error ("exception X has already been caught").

## finally

An optional `finally` block, after all the `catch` blocks, always runs — whether an exception was thrown or not, and even if the `catch` block itself returns early. It's the right place for cleanup that must happen no matter what (closing a file, releasing a resource):

```java
Scanner scan = null;
try
{
    scan = new Scanner(new File("auto_config.csv"));
    // ... read the file ...
}
catch (FileNotFoundException e)
{
    reportWarning("Missing auto_config.csv — using default route");
}
finally
{
    if (scan != null)
    {
        scan.close(); // runs whether the try succeeded, failed, or even returned early
    }
}
```

## try-with-resources

The `finally`-based cleanup above is exactly the case **try-with-resources** exists to replace. Any resource that implements `AutoCloseable` (like `Scanner`) can be declared inside parentheses right after `try`; Java then calls its `close()` automatically, in every case, without a `finally` block at all:

```java
try (Scanner scan = new Scanner(new File("auto_config.csv")))
{
    // ... read the file ...
}
catch (FileNotFoundException e)
{
    reportWarning("Missing auto_config.csv — using default route");
}
```

`scan` is closed the moment the `try` block ends — normally or via an exception — and it only exists inside that `try`. Prefer this form over a manual `finally` whenever the resource type supports it.

## Checked vs. Unchecked Exceptions

Java splits exceptions into two kinds, and the difference matters for what the compiler demands of you:

- **Checked exceptions** (like `IOException`) — the compiler forces you to either `catch` them or declare them with a `throws` clause. They represent problems a caller could reasonably be expected to recover from.
- **Unchecked exceptions** (`RuntimeException`, `Error`, and their subclasses — `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ArithmeticException`) — the compiler does not require handling them at all, though you're always allowed to. `RuntimeException` subclasses almost always represent a genuine programming bug (a null you forgot to check, an index you miscalculated) rather than something the caller can meaningfully recover from at runtime; `Error` and its subclasses represent serious JVM-level failures ordinary code doesn't catch or throw.

Guideline from the language's own designers: *if a client can reasonably be expected to recover from a problem, make it checked; if a client can't do anything useful about it, make it unchecked.* CSA covers unchecked-exception concepts (NullPointerException, ArrayIndexOutOfBoundsException) as topics in their own right, without teaching the `try`/`catch` mechanism itself — the AP exam doesn't test it.

## The `throws` Clause

If a method doesn't want to handle a checked exception itself, it can instead declare that it might throw one, pushing the decision up to whoever calls it. `PrintWriter`/`FileWriter` write text to a file — the counterpart to `Scanner`, which Lesson 9.8 uses to read one:

```java
public void writeList() throws IOException
{
    try (PrintWriter out = new PrintWriter(new FileWriter("OutFile.txt")))
    {
        // ...
    }
}
```

`throws` goes after the parameter list, before the method body's opening brace. Unchecked exceptions never need to appear in a `throws` clause (though nothing stops you from listing one). Note the `try`-with-resources here too: without it, an exception thrown between opening `out` and calling `out.close()` would skip the close and leak the file handle.

## The `throw` Statement

Any code — yours, a library's, or the Java runtime itself — can trigger an exception with the `throw` statement, given any object that's a `Throwable` (or a subclass):

```java
public void setTargetAngle(double degrees)
{
    if (degrees < 0 || degrees > 180)
    {
        throw new IllegalArgumentException("Angle out of range: " + degrees);
    }
    this.targetAngle = degrees;
}
```

Every exception type in Java descends from `Throwable` — each one is a **subclass** of it (built on top of it, inheriting its behavior; Ch.17 covers what that means in full). Its two direct children are `Error` (serious JVM-level failures — not something ordinary code catches or throws) and `Exception` (everything an ordinary program throws and catches), and `RuntimeException` is the branch of `Exception` reserved for unchecked exceptions.

## Reading What Went Wrong

Every exception carries a message, and a caught one doesn't have to be handled blind:

```java
catch (IllegalArgumentException e)
{
    reportWarning("Rejected: " + e.getMessage()); // "Angle out of range: 240.0"
}
```

`e.getMessage()` returns the text passed to the exception's constructor (`"Angle out of range: " + degrees` above) — use it in a log message instead of guessing what failed. An *uncaught* exception prints a **stack trace**: the exception type and message, followed by the chain of method calls (most recent first) that led to it —

```
java.lang.IllegalArgumentException: Angle out of range: 240.0
    at Arm.setTargetAngle(Arm.java:107)
    at Robot.teleopPeriodic(Robot.java:42)
```

— which is exactly what shows up when robot code crashes: read from the top down, the first line is the problem, and the first `at` line naming your own class (not a library's) is usually where to start looking.

Writing your **own** exception types (for errors specific to your robot code, not covered by a built-in class) needs `extends`, which isn't taught until Ch.17 — Lesson 17.2 covers it.

## Common Pitfalls

- **Catch-and-ignore.** An empty `catch` block silently swallows a real problem — at minimum, log or report it (`reportWarning(...)` above), even if there's nothing more to do.
- **Catching to "fix" a bug instead of fixing it.** Wrapping buggy code in `try`/`catch` to suppress a `NullPointerException` hides the actual mistake instead of correcting it — reserve catching for genuinely recoverable situations (a missing file, an unreachable camera), not programming errors.
- **Forgetting `finally` runs even on an early `return` inside `try`/`catch`.** Cleanup code that must always run belongs in `finally`, not duplicated at the end of every branch.

## Key Takeaways

- Throwing an exception creates an object describing the problem and hands it to the runtime, which searches the call stack for a matching handler; an unhandled exception crashes the program (a red "Robot Code" indicator, on a robot).
- `try` wraps risky code; one or more `catch` blocks (in order, general after specific, or combined with `|`) handle specific exception types; an optional `finally` block always runs, for cleanup — or use try-with-resources for anything `AutoCloseable`.
- Checked exceptions (like `IOException`) must be caught or declared with `throws`; unchecked exceptions (`RuntimeException`, `Error`, and their subclasses) don't require either, since they usually signal a real bug rather than a recoverable situation.
- `throw someObject;` triggers an exception yourself, given any `Throwable`.
- `e.getMessage()` reports what went wrong; an uncaught exception prints a stack trace, read top-down.
- Never catch-and-ignore — recover meaningfully, or at least report the problem.

Derived from `other-reference-repo`: `oracle-java-tutorials/exceptions/01-what-is-an-exception.md`, `03-catching-and-handling-exceptions.md`, `09-specifying-the-exceptions-thrown-by-a-method.md`, `10-how-to-throw-exceptions.md`, `13-unchecked-exceptions-the-controversy.md` (ORACLE 11.1-16)
**Deck context:** mechacoder-test/src/lessons/java-1.js, slide 11 ("Exceptions & try/catch")
