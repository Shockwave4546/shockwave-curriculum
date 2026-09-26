BEATS = [
    {
        "screen": '''<div class="scr-title">
      <div class="scr-eyebrow">Ch. 9 &middot; Storing Data</div>
      <h1>Using Text Files</h1>
      <p class="scr-sub">Reading data that outlives the program &mdash; and doesn't have to be hardcoded.</p>
    </div>''',
        "speak": "Everything we've stored so far has lived only while the program runs. A file's data persists even after the program stops, which makes it perfect for configuration, or for data too large, or too changeable, to hardcode directly into your source. A robot might load its table of autonomous starting positions from a file instead.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">import</span> java.io.*;
<span class="k">import</span> java.util.*;

<span class="t">File</span> configFile = <span class="k">new</span> <span class="t">File</span>(<span class="s">"auto_config.csv"</span>); <span class="c">// just a name &mdash; this line can't fail</span>
<span class="t">Scanner</span> scan = <span class="k">new</span> <span class="t">Scanner</span>(configFile); <span class="c">// this line can throw FileNotFoundException</span></code></pre>''',
        "speak": "Two classes handle this. File represents the file itself, really just a filename, and building one never fails even if the file doesn't actually exist. Scanner is what actually reads from it, and that's the line that can throw if the file can't be found. Those two import star lines pull in every class from that whole package at once, java dot io star for File and IO Exception, java dot util star for Scanner, instead of naming each class individually.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">public static void</span> main(<span class="t">String</span>[] args) <span class="k">throws</span> <span class="t">IOException</span>
{
    <span class="t">File</span> configFile = <span class="k">new</span> <span class="t">File</span>(<span class="s">"auto_config.csv"</span>);
    <span class="t">Scanner</span> scan = <span class="k">new</span> <span class="t">Scanner</span>(configFile);
    <span class="c">// ...</span>
    scan.close();
}</code></pre>''',
        "speak": "Since opening a file can fail, a wrong name, a missing file, Java forces you to acknowledge that. The simplest way is adding throws IO Exception to the method's own header. If the file genuinely can't be found, the program terminates with a clear error instead of silently continuing on with no data at all. Chapter 12 covers try and catch, the alternative to throws, including a form that can close the scanner for you automatically.",
    },
    {
        "screen": '''<pre class="code"><code><span class="k">while</span> (scan.hasNextLine())
{
    <span class="t">String</span> line = scan.nextLine();
    <span class="c">// process this line</span>
}
scan.close(); <span class="c">// always close when done</span></code></pre>''',
        "speak": "has Next Line stays true as long as there's another line left to read, so pairing it with a while loop is the standard way to read an entire file, one line at a time, until it runs out. And always close the scanner once you're done, a small habit that prevents a real resource leak in a program that opens many files over time.",
    },
    {
        "screen": '''<pre class="code"><code><span class="c">// One line of auto_config.csv: "3-Piece-Left,14.2,BlueAlliance"</span>
<span class="t">String</span> line = scan.nextLine();
<span class="t">String</span>[] fields = line.split(<span class="s">","</span>);
<span class="t">String</span> routeName = fields[<span class="n">0</span>];       <span class="c">// "3-Piece-Left"</span>
<span class="k">double</span> routeTime = Double.parseDouble(fields[<span class="n">1</span>]); <span class="c">// "14.2" -&gt; 14.2</span>
<span class="t">String</span> alliance = fields[<span class="n">2</span>];        <span class="c">// "BlueAlliance"</span></code></pre>''',
        "speak": "A CSV file, comma separated values, packs several fields into one line. String's split method, given a comma, breaks that line into a String array around every comma. Grab each field out by index, and convert the numeric one back into an actual double with Double dot parse Double, since split always hands you back plain text. Integer dot parse Int and Double dot parse Double belong to the wrapper classes, Lesson 9.2 covers those in full.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt; configLines = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">String</span>&gt;();
<span class="k">while</span> (scan.hasNextLine())
{
    configLines.add(scan.nextLine());
}</code></pre>''',
        "speak": "If you already know the line count, an array works fine. But usually you don't, and that's exactly when array list earns its keep, no need to know the size up front, just add every line as you read it.",
    },
    {
        "screen": '''<pre class="code"><code><span class="t">ArrayList</span>&lt;<span class="t">AutoRoute</span>&gt; routes = <span class="k">new</span> <span class="t">ArrayList</span>&lt;<span class="t">AutoRoute</span>&gt;();
<span class="k">while</span> (scan.hasNextLine())
{
    <span class="t">String</span>[] fields = scan.nextLine().split(<span class="s">","</span>);
    routes.add(<span class="k">new</span> AutoRoute(fields[<span class="n">0</span>], Double.parseDouble(fields[<span class="n">1</span>]), fields[<span class="n">2</span>]));
}</code></pre>''',
        "speak": "And once the data has real structure, it's cleaner to stop working with raw String arrays entirely, and instead define a class matching the file's columns, building one real object per row. Same has-a, one-object-per-record idea from Chapter 7, just now driven by whatever's actually sitting in the file.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Common Pitfalls</h2><ul>
      <li><span class="check">!</span>Forgetting throws IOException (or a try/catch) &mdash; Java won't compile file-reading code without it.</li>
      <li><span class="check">!</span>Forgetting to close() the scanner &mdash; a small leak that adds up.</li>
      <li><span class="check">!</span>Trying to parse a header row as data &mdash; call nextLine() once before the loop starts, not inside it.</li>
      <li><span class="check">!</span>Assuming a relative filename resolves next to the source file &mdash; it resolves from wherever the program runs.</li>
    </ul></div>''',
        "speak": "Four pitfalls. Java simply won't compile file-reading code unless you've acknowledged that opening the file might fail, throws IO Exception, or a try and catch, is required. Don't forget to close the scanner, it's a small leak, but it adds up in any program that opens many files. Don't try to parse a header row as if it were real data, call next Line once before the loop even starts to throw it away, rather than checking for it on every single pass. And don't assume a relative filename resolves next to your source file, it resolves relative to wherever the program is actually run from.",
    },
    {
        "screen": '''<div class="scr-recap"><h2 class="scr-h2">Recap</h2><ul>
      <li><span class="check">&#10003;</span>File just represents a filename and never throws; Scanner is what can throw when it opens that file.</li>
      <li><span class="check">&#10003;</span>hasNextLine() with a while loop is the standard whole-file read pattern.</li>
      <li><span class="check">&#10003;</span>String.split(",") breaks a CSV line into fields; parseInt/parseDouble convert them to numbers.</li>
      <li><span class="check">&#10003;</span>Reading rows into custom objects beats raw split arrays once the data has real structure.</li>
    </ul></div>''',
        "speak": "So, to recap. File just represents a filename and never throws, Scanner is what can actually throw once it tries to open that file, and Java makes you explicitly acknowledge that. has Next Line paired with a while loop is the standard pattern for reading an entire file. String's split method, given a comma, breaks a CSV line into its fields, and parse Int and parse Double convert those fields into real numbers. And once your data has real structure, reading each row into a custom object beats working with raw split arrays. That wraps up Chapter 9, and everything Chapters 6 through 9 set out to cover. Nice work, see you next chapter.",
    },
]
