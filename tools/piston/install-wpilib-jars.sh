#!/usr/bin/env bash
# Installs the WPILib 2027 jars that Ch.25 (Commands v3) exercises compile against into
# Piston's Java 25 package, and puts them on that package's CLASSPATH.
#
# Why: Ch.25 exercises are compile-only (see docs/exercise-authoring-conventions.md), so the
# student's code must see the real org.wpilib.command3 API at compile time. Running commands
# is NOT supported: the Scheduler also needs the third-party `quickbuf` library, which has
# not been approved for this project.
#
# What it does (idempotent, safe to re-run):
#   1. downloads the jars from WPILib's Maven server and verifies each against Maven's SHA-1
#   2. with sudo, copies them to <piston-data>/packages/java/<version>/wpilib/
#   3. with sudo, adds a CLASSPATH line to that package's `environment` and `.env` files
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

echo "== Done. Check it:"
echo "   curl -s -X POST localhost:2000/api/v2/execute -H 'Content-Type: application/json' \\"
echo "     -d '{\"language\":\"java\",\"version\":\"$JAVA_PKG\",\"files\":[{\"name\":\"Main\",\"content\":\"import org.wpilib.command3.Command; public class Main { public static void main(String[] a){ System.out.println(Command.class.getName()); } }\"}]}'"
