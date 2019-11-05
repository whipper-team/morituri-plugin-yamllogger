## Status

[![License](https://img.shields.io/github/license/whipper-team/morituri-plugin-yamllogger.svg)](https://github.com/whipper-team/morituri-plugin-yamllogger/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/whipper-team/morituri-plugin-yamllogger.svg?branch=master)](https://travis-ci.com/whipper-team/morituri-plugin-yamllogger)
[![GitHub (pre-)release](https://img.shields.io/github/release/whipper-team/morituri-plugin-yamllogger/all.svg)](https://github.com/whipper-team/morituri-plugin-yamllogger/releases/latest)

**NOTICE: UNMANTAINED**

## Logger information

This logger was created in order to benefit morituri users. It provides [whipper](https://github.com/whipper-team/whipper)'s improved logger structure (in YAML format) in a way that's compatible with morituri.

## Instructions

To use this plugin:

* build it:

    ```bash
    git clone https://github.com/whipper-team/morituri-plugin-yamllogger.git
    cd morituri-plugin-yamllogger
    python2 setup.py bdist_egg
    ```

* copy it to your plugin directory:

    ```bash
    mkdir -p "$HOME/.morituri/plugins"
    cp dist/morituri_*egg "$HOME/.morituri/plugins"
    ```

* verify that it gets recognized:

    ```bash
    rip cd rip --help
    ```

  You should see 'yaml' as a possible logger.

* use it:

    ```bash
    rip cd rip --logger=yaml
    ```

## Developers

To use the plugin while developing uninstalled:

```bash
python2 setup.py develop --install-dir=path/to/checkout/of/morituri
```

Yamllogger tries to stay very close to whipper's internal logger. Here you can find a diff report between the two:

```diff
--- a/whipper/whipper/result/logger.py
+++ b/morituri-plugin-yamllogger/yamllogger/logger/yaml.py
@@ -0,0 +1 @@
+import yamllogger
@@ -4,4 +5,3 @@ import hashlib
-import whipper
-
-from whipper.common import common
-from whipper.result import result
+from morituri.common import common
+from morituri.configure import configure
+from morituri.result import result
@@ -10 +10 @@ from whipper.result import result
-class WhipperLogger(result.Logger):
+class YamlLogger(result.Logger):
@@ -28,2 +28,2 @@ class WhipperLogger(result.Logger):
-        lines.append("Log created by: whipper %s (internal logger)" %
-                     whipper.__version__)
+        lines.append("Log created by: morituri %s (yaml logger %s)" % (
+                     configure.version, yamllogger.__version__))
@@ -50,6 +50,4 @@ class WhipperLogger(result.Logger):
-        # Currently unsupported by the official cdparanoia package
-        over = "No"
-        # Only implemented in whipper (ripResult.overread)
-        if ripResult.overread:
-            over = "Yes"
-        lines.append("  Overread into lead-out: %s" % over)
+        # Unsupported by both the official cdparanoia package and morituri
+        # Feature implemented in whipper
+        lines.append("  Overread into lead-out: No "
+                     "(unsupported in morituri)")
@@ -59,5 +57,2 @@ class WhipperLogger(result.Logger):
-        if ripResult.isCdr:
-            isCdr = "Yes"
-        else:
-            isCdr = "No"
-        lines.append("  CD-R detected: %s" % isCdr)
+        # CD-R Detection (only implemented in whipper)
+        lines.append("  CD-R detected: Unknown (unsupported in morituri)")
@@ -68,2 +63,2 @@ class WhipperLogger(result.Logger):
-        lines.append("  Release: %s - %s" %
-                     (ripResult.artist, ripResult.title))
+        lines.append("  Release: %s - %s" % (
+                     ripResult.artist, ripResult.title))
@@ -118,4 +113 @@ class WhipperLogger(result.Logger):
-            track_lines, ARDB_entry, ARDB_match = self.trackLog(t)
-            self._inARDatabase += int(ARDB_entry)
-            self._accuratelyRipped += int(ARDB_match)
-            lines.extend(track_lines)
+            lines.extend(self.trackLog(t))
@@ -179 +171 @@ class WhipperLogger(result.Logger):
-        peak = trackResult.peak / 32768.0
+        peak = trackResult.peak
@@ -182,7 +174,2 @@ class WhipperLogger(result.Logger):
-        # Pre-emphasis status
-        # Only implemented in whipper (trackResult.pre_emphasis)
-        if trackResult.pre_emphasis:
-            preEmph = "Yes"
-        else:
-            preEmph = "No"
-        lines.append("    Pre-emphasis: %s" % preEmph)
+        # Pre-emphasis status (only implemented in whipper)
+        lines.append("    Pre-emphasis: Unknown (unsupported in morituri)")
@@ -209,25 +196,22 @@ class WhipperLogger(result.Logger):
-        ARDB_entry = 0
-        ARDB_match = 0
-        for v in ("v1", "v2"):
-            if trackResult.AR[v]["DBCRC"]:
-                lines.append("    AccurateRip %s:" % v)
-                ARDB_entry += 1
-                if trackResult.AR[v]["CRC"] == trackResult.AR[v]["DBCRC"]:
-                    lines.append("      Result: Found, exact match")
-                    ARDB_match += 1
-                else:
-                    lines.append("      Result: Found, NO exact match")
-                lines.append(
-                    "      Confidence: %d" % trackResult.AR[v]["DBConfidence"]
-                )
-                lines.append(
-                    "      Local CRC: %s" % trackResult.AR[v]["CRC"].upper()
-                )
-                lines.append(
-                    "      Remote CRC: %s" % trackResult.AR[v]["DBCRC"].upper()
-                )
-            elif trackResult.number != 0:
-                lines.append("    AccurateRip %s:" % v)
-                lines.append(
-                    "      Result: Track not present in AccurateRip database"
-                )
+        # There's no support for AccurateRip v2 in morituri
+        # AccurateRip v2 is supported in whipper
+        if trackResult.accurip:
+            lines.append("    AccurateRip v1:")
+            self._inARDatabase += 1
+            if trackResult.ARCRC == trackResult.ARDBCRC:
+                lines.append("      Result: Found, exact match")
+                self._accuratelyRipped += 1
+            else:
+                lines.append("      Result: Found, NO exact match")
+            lines.append("      Confidence: %d" %
+                         trackResult.ARDBConfidence)
+            lines.append("      Local CRC: %08X" % trackResult.ARCRC)
+            lines.append("      Remote CRC: %08X" % trackResult.ARDBCRC)
+            lines.append("    AccurateRip v2:")
+            lines.append("      Result: Unknown (unsupported in morituri)")
+        elif trackResult.number != 0:
+            lines.append("    AccurateRip v1:")
+            lines.append("      Result: Track not present in "
+                         "AccurateRip database")
+            lines.append("    AccurateRip v2:")
+            lines.append("      Result: Unknown (unsupported in morituri)")
@@ -241 +225 @@ class WhipperLogger(result.Logger):
-        return lines, bool(ARDB_entry), bool(ARDB_match)
+        return lines
```
