## Status

[![Build Status](https://travis-ci.com/whipper-team/morituri-plugin-yamllogger.svg?branch=master)](https://travis-ci.com/whipper-team/morituri-plugin-yamllogger)

## Logger information

This logger was created in order to benefit morituri users. It provides whipper's improved logger structure in a way that's compatible with morituri.

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

Yamllogger tries to stay very close to whipper's internal logger. Here you can find a diff report between the two:

```diff
--- whipper/whipper/result/logger.py
+++ morituri-plugin-yamllogger/yamllogger/logger/yaml.py
@@ -1,13 +1,12 @@
 import time
 import hashlib
 
-import whipper
+from morituri.common import common
+from morituri.configure import configure
+from morituri.result import result
 
-from whipper.common import common
-from whipper.result import result
 
-
-class WhipperLogger(result.Logger):
+class YamlLogger(result.Logger):
 
     _accuratelyRipped = 0
     _inARDatabase = 0
@@ -25,8 +24,8 @@
         lines = []
 
         # Ripper version
-        lines.append("Log created by: whipper %s (internal logger)" %
-                     whipper.__version__)
+        lines.append("Log created by: morituri %s (yaml logger)" %
+                     configure.version)
 
         # Rip date
         date = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch)).strip()
@@ -47,20 +46,15 @@
             defeat = "No"
         lines.append("  Defeat audio cache: %s" % defeat)
         lines.append("  Read offset correction: %+d" % ripResult.offset)
-        # Currently unsupported by the official cdparanoia package
-        over = "No"
-        # Only implemented in whipper (ripResult.overread)
-        if ripResult.overread:
-            over = "Yes"
-        lines.append("  Overread into lead-out: %s" % over)
+        # Unsupported by both the official cdparanoia package and morituri
+        # Feature implemented in whipper
+        lines.append("  Overread into lead-out: No "
+                     "(not supported in morituri)")
         # Next one fully works only using the patched cdparanoia package
         # lines.append("Fill up missing offset samples with silence: Yes")
         lines.append("  Gap detection: cdrdao %s" % ripResult.cdrdaoVersion)
-        if ripResult.isCdr:
-            isCdr = "Yes"
-        else:
-            isCdr = "No"
-        lines.append("  CD-R detected: %s" % isCdr)
+        # CD-R Detection (only implemented in whipper)
+        lines.append("  CD-R detected: Unknown (not supported in morituri)")
         lines.append("")
 
         # CD metadata
@@ -174,16 +168,11 @@
             lines.append("    Pre-gap length: %s" % common.framesToMSF(pregap))
 
         # Peak level
-        peak = trackResult.peak / 32768.0
+        peak = trackResult.peak
         lines.append("    Peak level: %.6f" % peak)
 
-        # Pre-emphasis status
-        # Only implemented in whipper (trackResult.pre_emphasis)
-        if trackResult.pre_emphasis:
-            preEmph = "Yes"
-        else:
-            preEmph = "No"
-        lines.append("    Pre-emphasis: %s" % preEmph)
+        # Pre-emphasis status (only implemented in whipper)
+        lines.append("    Pre-emphasis: Unknown (not supported in morituri)")
 
         # Extraction speed
         if trackResult.copyspeed:
@@ -204,29 +193,28 @@
             lines.append("    Copy CRC: %08X" % trackResult.copycrc)
 
         # AccurateRip track status
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
+            lines.append("      Result: not supported in morituri")
+        elif trackResult.number != 0:
+            lines.append("    AccurateRip v1:")
+            lines.append("      Result: Track not present in "
+                         "AccurateRip database")
+            lines.append("    AccurateRip v2:")
+            lines.append("      Result: Unknown (not supported in morituri)")
 
         # Check if Test & Copy CRCs are equal
         if trackResult.testcrc == trackResult.copycrc:
```
