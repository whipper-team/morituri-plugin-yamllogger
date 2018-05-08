## Status

[![Build Status](https://travis-ci.com/JoeLametta/morituri-yamllogger.svg?branch=master)](https://travis-ci.com/JoeLametta/morituri-yamllogger)

## Logger information

This logger was created in order to benefit morituri users. It provides whipper's improved logger structure in a way that's compatible with morituri.

## Using instructions (valid only for morituri)

To use this plugin:

* build it:

    ```bash
    git clone https://github.com/JoeLametta/morituri-yamllogger.git
    cd morituri-yamllogger
    python2 setup.py bdist_egg
    ```

* copy it to your plugin directory:

    ```bash
    mkdir -p $HOME/.morituri/plugins
    cp dist/morituri_*egg $HOME/.morituri/plugins
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

Yamllogger tries to stay very close to whipper's internal logger. Here you can find the diff report between the two:

```diff
--- whipper/whipper/result/logger.py
+++ morituri-yamllogger/yamllogger/logger/yaml.py
@@ -4 +4,3 @@
-import whipper
+from morituri.common import common
+from morituri.configure import configure
+from morituri.result import result
@@ -6,2 +7,0 @@
-from whipper.common import common
-from whipper.result import result
@@ -9,2 +9 @@
-
-class WhipperLogger(result.Logger):
+class YamlLogger(result.Logger):
@@ -28,2 +27,2 @@
-        lines.append("Log created by: whipper %s (internal logger)" %
-                     whipper.__version__)
+        lines.append("Log created by: morituri %s (yaml logger)" %
+                     configure.version)
@@ -48,6 +47,2 @@
-        # Currently unsupported by the official cdparanoia package
-        over = "No"
-        # Only implemented in whipper (ripResult.overread)
-        if ripResult.overread:
-            over = "Yes"
-        lines.append("  Overread into lead-out: %s" % over)
+        # Unsupported by the official cdparanoia package and morituri
+        lines.append("  Overread into lead-out: not supported in morituri")
@@ -57,5 +52,2 @@
-        if ripResult.isCdr:
-            isCdr = "Yes"
-        else:
-            isCdr = "No"
-        lines.append("  CD-R detected: %s" % isCdr)
+        # CD-R Detection (only implemented in whipper)
+        lines.append("  CD-R detected: not supported in morituri")
@@ -178,7 +170,2 @@
-        # Pre-emphasis status
-        # Only implemented in whipper (trackResult.pre_emphasis)
-        if trackResult.pre_emphasis:
-            preEmph = "Yes"
-        else:
-            preEmph = "No"
-        lines.append("    Pre-emphasis: %s" % preEmph)
+        # Pre-emphasis status (only implemented in whipper)
+        lines.append("    Pre-emphasis: not supported in morituri")
@@ -205,23 +192,21 @@
-        for v in ('v1', 'v2'):
-            if trackResult.AR[v]['DBCRC']:
-                lines.append("    AccurateRip %s:" % v)
-                self._inARDatabase += 1
-                if trackResult.AR[v]['CRC'] == trackResult.AR[v]['DBCRC']:
-                    lines.append("      Result: Found, exact match")
-                    self._accuratelyRipped += 1
-                else:
-                    lines.append("      Result: Found, NO exact match")
-                lines.append(
-                    "      Confidence: %d" % trackResult.AR[v]['DBConfidence']
-                )
-                lines.append(
-                    "      Local CRC: %s" % trackResult.AR[v]['CRC'].upper()
-                )
-                lines.append(
-                    "      Remote CRC: %s" % trackResult.AR[v]['DBCRC'].upper()
-                )
-            elif trackResult.number != 0:
-                lines.append("    AccurateRip %s:" % v)
-                lines.append(
-                    "      Result: Track not present in AccurateRip database"
-                )
+        # There's no support for AccurateRip v2 in morituri
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
+            lines.append("      Result: not supported in morituri")
+        elif trackResult.number != 0:
+            lines.append("    AccurateRip v1:")
+            lines.append("      Result: Track not present in "
+                         "AccurateRip database")
+            lines.append("    AccurateRip v2:")
+            lines.append("      Result: not supported in morituri")
```
