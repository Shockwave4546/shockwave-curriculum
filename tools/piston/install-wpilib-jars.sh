#!/usr/bin/env bash
# Installs the WPILib 2027 jars that Ch.25 (Commands v3) exercises compile against into
# Piston's Java 25 package, and puts them on that package's CLASSPATH.
#
# Why: the Ch.25 exercises build and RUN real Commands v3 objects (see "Ch.25: construct and
# inspect" in docs/exercise-authoring-conventions.md), so student code must see the real
# org.wpilib.command3 API, and the scheduler has to run without a robot. That takes:
#   - the 8 WPILib jars (WPILib's Maven server),
#   - quickbuf-runtime 1.4 (Maven Central): the Scheduler's protobuf runtime (approved by Joe
#     2026-10-06; WPILib's own build pins the same version),
#   - command3-test-support.jar: ~40 lines of OUR code (tools/piston/command3-test-support/) that
#     replaces the two things that need WPILib's native hardware library, the Driver Station
#     opmode lookup and the robot clock, with a fixed opmode and a clock that only moves when told
#     (TestSupport.init() / TestSupport.advance(seconds)),
#   - two JVM flags (`--add-opens`) that the scheduler's coroutines need,
#   - CPU-saving JVM flags: Piston kills a run at 3 CPU-seconds, and a default JVM spends about
#     2.1 CPU-seconds on even a 0.8 s scheduler run (parallel GC and JIT threads), so a few students
#     at once pushed nearly every run over the limit. SerialGC + C1-only roughly halves the CPU time.
#
# What it does (idempotent, safe to re-run):
#   1. downloads the jars and verifies each against the repository's published SHA-1
#   2. builds command3-test-support.jar with Piston's own JDK
#   3. with sudo, copies all jars to <piston-data>/packages/java/<version>/wpilib/
#   4. with sudo, adds a CLASSPATH line to that package's `environment` and `.env` files
#   5. with sudo, sets the JVM flags on that package's `run` script (it is read on every job)
# Restart Piston afterwards (`sudo podman restart piston_api`) so it re-reads `.env`.
#
# Usage:  bash tools/piston/install-wpilib-jars.sh [--dry-run]
#   PISTON_DATA   Piston data dir on the host (default ~/piston-data)
#   JAVA_PKG      Piston Java package version  (default 25.0.1)
set -euo pipefail

WPILIB_VERSION="2027.0.0-alpha-7"          # alpha: the API can still change before the final release
MAVEN="https://frcmaven.wpi.edu/artifactory/release/org/wpilib"
# path-under-MAVEN   (artifact name is the last path component)
ARTIFACTS=(
  commandsv3-java
  wpilibj/wpilibj-java
  wpimath/wpimath-java
  wpiunits/wpiunits-java
  wpiutil/wpiutil-java
  hal/hal-java
  ntcore/ntcore-java
  datalog/datalog-java
)

QUICKBUF_URL="https://repo1.maven.org/maven2/us/hebi/quickbuf/quickbuf-runtime/1.4"
QUICKBUF_JAR="quickbuf-runtime-1.4.jar"
JVM_FLAGS="--add-opens java.base/jdk.internal.vm=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED -XX:+UseSerialGC -XX:TieredStopAtLevel=1 -Xshare:auto -Xmx256m -XX:CICompilerCount=1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PISTON_DATA="${PISTON_DATA:-$HOME/piston-data}"
JAVA_PKG="${JAVA_PKG:-25.0.1}"
PKG_DIR="$PISTON_DATA/packages/java/$JAVA_PKG"
IN_CONTAINER_DIR="/piston/packages/java/$JAVA_PKG/wpilib"   # path as seen inside the container
DRY_RUN=false
[ "${1:-}" = "--dry-run" ] && DRY_RUN=true

[ -d "$PKG_DIR" ] || { echo "Piston Java package not found: $PKG_DIR" >&2; exit 1; }

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

echo "== Downloading and verifying ${#ARTIFACTS[@]} jars ($WPILIB_VERSION)"
for path in "${ARTIFACTS[@]}"; do
  name="${path##*/}"
  jar="$name-$WPILIB_VERSION.jar"
  # -L: larger files are served via a redirect to the Maven server's own file storage
  curl -fsSL -o "$WORK/$jar"      "$MAVEN/$path/$WPILIB_VERSION/$jar"
  curl -fsSL -o "$WORK/$jar.sha1" "$MAVEN/$path/$WPILIB_VERSION/$jar.sha1"
  want="$(tr -d ' \n\r' < "$WORK/$jar.sha1" | cut -c1-40)"
  got="$(sha1sum "$WORK/$jar" | cut -d' ' -f1)"
  if [ "$want" != "$got" ]; then echo "CHECKSUM MISMATCH: $jar (want $want, got $got)" >&2; exit 1; fi
  echo "   ok  $jar  $(stat -c%s "$WORK/$jar") bytes"
done

echo "== Downloading and verifying $QUICKBUF_JAR (Maven Central)"
curl -fsSL -o "$WORK/$QUICKBUF_JAR"      "$QUICKBUF_URL/$QUICKBUF_JAR"
curl -fsSL -o "$WORK/$QUICKBUF_JAR.sha1" "$QUICKBUF_URL/$QUICKBUF_JAR.sha1"
want="$(tr -d ' \n\r' < "$WORK/$QUICKBUF_JAR.sha1" | cut -c1-40)"
got="$(sha1sum "$WORK/$QUICKBUF_JAR" | cut -d' ' -f1)"
if [ "$want" != "$got" ]; then echo "CHECKSUM MISMATCH: $QUICKBUF_JAR (want $want, got $got)" >&2; exit 1; fi
echo "   ok  $QUICKBUF_JAR  $(stat -c%s "$WORK/$QUICKBUF_JAR") bytes"

echo "== Building command3-test-support.jar with Piston's own JDK"
JDK_BIN="$PKG_DIR/bin"
CP="$(ls "$WORK"/*.jar | paste -sd:)"
mkdir -p "$WORK/support-classes"
"$JDK_BIN/javac" -cp "$CP" -d "$WORK/support-classes" "$SCRIPT_DIR/command3-test-support/org/wpilib/command3/TestSupport.java"
"$JDK_BIN/jar" cf "$WORK/command3-test-support.jar" -C "$WORK/support-classes" .
echo "   ok  command3-test-support.jar  $(stat -c%s "$WORK/command3-test-support.jar") bytes"

if $DRY_RUN; then
  echo "== Dry run: stopping before any change to $PKG_DIR"
  exit 0
fi

echo "== Installing into $PKG_DIR (needs sudo)"
sudo mkdir -p "$PKG_DIR/wpilib"
sudo cp "$WORK"/*.jar "$PKG_DIR/wpilib/"
sudo chown -R --reference="$PKG_DIR/environment" "$PKG_DIR/wpilib"

CP_LINE="export CLASSPATH=\"$IN_CONTAINER_DIR/*\""
ENV_LINE="CLASSPATH=$IN_CONTAINER_DIR/*"
grep -qxF "$CP_LINE"  "$PKG_DIR/environment" || echo "$CP_LINE"  | sudo tee -a "$PKG_DIR/environment" >/dev/null
grep -qxF "$ENV_LINE" "$PKG_DIR/.env"        || echo "$ENV_LINE" | sudo tee -a "$PKG_DIR/.env"        >/dev/null

RUN_FILE="$PKG_DIR/run"
# Rewrites the `java ... $filename` line each time, so re-running picks up changed flags.
sudo sed -i "s#^java .*\$filename#java $JVM_FLAGS \$filename#" "$RUN_FILE"
grep -q -- "UseSerialGC" "$RUN_FILE" || { echo "Could not set the JVM flags in $RUN_FILE" >&2; exit 1; }

echo "== Done. Restart Piston (sudo podman restart piston_api), then check it:"
echo "   curl -s -X POST localhost:2000/api/v2/execute -H 'Content-Type: application/json' \\"
echo "     -d '{\"language\":\"java\",\"version\":\"$JAVA_PKG\",\"files\":[{\"name\":\"Main\",\"content\":\"import org.wpilib.command3.Command; public class Main { public static void main(String[] a){ System.out.println(Command.class.getName()); } }\"}]}'"
