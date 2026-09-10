# Exceptions & try/catch

**Outline ref:** 12 — Exceptions & try/catch (ORACLE 11.1-16)
**Status:** new — authored lesson (fuller depth than the teaser slide)

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
catch (IllegalArgumentException e)
{
    reportWarning("Bad camera config — check the port number");
}
```

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

## Checked vs. Unchecked Exceptions

Java splits exceptions into two kinds, and the difference matters for what the compiler demands of you:

- **Checked exceptions** (like `IOException`) — the compiler forces you to either `catch` them or declare them with a `throws` clause. They represent problems a caller could reasonably be expected to recover from.
- **Unchecked exceptions** (`RuntimeException` and its subclasses — `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ArithmeticException`) — the compiler does not require handling them at all, though you're always allowed to. They almost always represent a genuine programming bug (a null you forgot to check, an index you miscalculated) rather than something the caller can meaningfully recover from at runtime.

Guideline from the language's own designers: *if a client can reasonably be expected to recover from a problem, make it checked; if a client can't do anything useful about it, make it unchecked.* This is also why CSA covers unchecked-exception concepts (NullPointerException, ArrayIndexOutOfBoundsException) as topics in their own right, without ever teaching the `try`/`catch` mechanism itself — the AP exam doesn't test it.

## The `throws` Clause

If a method doesn't want to handle a checked exception itself, it can instead declare that it might throw one, pushing the decision up to whoever calls it:

```java
public void writeList() throws IOException
{
    PrintWriter out = new PrintWriter(new FileWriter("OutFile.txt"));
    // ...
    out.close();
}
```

`throws` goes after the parameter list, before the method body's opening brace. Unchecked exceptions never need to appear in a `throws` clause (though nothing stops you from listing one).

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

Every exception type in Java descends from `Throwable`. Its two direct children are `Error` (serious JVM-level failures — not something ordinary code catches or throws) and `Exception` (everything an ordinary program throws and catches), and `RuntimeException` is the branch of `Exception` reserved for unchecked exceptions.

## Common Pitfalls

- **Catch-and-ignore.** An empty `catch` block silently swallows a real problem — at minimum, log or report it (`reportWarning(...)` above), even if there's nothing more to do.
- **Catching to "fix" a bug instead of fixing it.** Wrapping buggy code in `try`/`catch` to suppress a `NullPointerException` hides the actual mistake instead of correcting it — reserve catching for genuinely recoverable situations (a missing file, an unreachable camera), not programming errors.
- **Forgetting `finally` runs even on an early `return` inside `try`/`catch`.** Cleanup code that must always run belongs in `finally`, not duplicated at the end of every branch.

## Key Takeaways

- Throwing an exception creates an object describing the problem and hands it to the runtime, which searches the call stack for a matching handler; an unhandled exception crashes the program (a red "Robot Code" indicator, on a robot).
- `try` wraps risky code; one or more `catch` blocks handle specific exception types; an optional `finally` block always runs, for cleanup.
- Checked exceptions (like `IOException`) must be caught or declared with `throws`; unchecked exceptions (`RuntimeException` and its subclasses) don't require either, since they usually signal a real bug rather than a recoverable situation.
- `throw someObject;` triggers an exception yourself, given any `Throwable`.
- Never catch-and-ignore — recover meaningfully, or at least report the problem.

Derived from `other-reference-repo`: `oracle-java-tutorials/exceptions/01-what-is-an-exception.md`, `03-catching-and-handling-exceptions.md`, `09-specifying-the-exceptions-thrown-by-a-method.md`, `10-how-to-throw-exceptions.md`, `13-unchecked-exceptions-the-controversy.md` (ORACLE 11.1-16)
**Deck context:** mechacoder-test/src/lessons/java-1.js, slide 11 ("Exceptions & try/catch")
