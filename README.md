## Status
[![Build Status](https://travis-ci.org/JoeLametta/morituri-yamllogger.svg?branch=master)](https://travis-ci.org/JoeLametta/morituri-yamllogger)

## Logger information

This logger was created in order to benefit morituri users. It provides whipper's improved logger structure in a way that's compatible with morituri.
Yamllogger can be used with whipper too but, in this case, it won't provide any benefit at all so I consider this use case as unsupported.

## Using instructions (valid only for morituri)

To use this plugin:

* build it:

        git clone https://github.com/JoeLametta/morituri-yamllogger.git
        cd morituri-yamllogger
        python2 setup.py bdist_egg

* copy it to your plugin directory:

        mkdir -p $HOME/.morituri/plugins
        cp dist/morituri_*egg $HOME/.morituri/plugins

* verify that it gets recognized:

        rip cd rip --help

   You should see 'yaml' as a possible logger.

* use it:

        rip cd rip --logger=yaml


## Developers

To use the plugin while developing uninstalled:

    python2 setup.py develop --install-dir=path/to/checkout/of/morituri

This plugin tries to stay very close to whipper's internal logger. Here you can find the diff report between the two:

```diff
--- whipper/morituri/result/logger.py
+++ morituri-yamllogger/yamllogger/logger/yaml.py
@@ -9 +9 @@
-class MorituriLogger(result.Logger):
+class YamlLogger(result.Logger):
@@ -27,3 +27,6 @@
-        # Only implemented in whipper (ripResult.logger)
-        lines.append("Log created by: whipper %s (%s logger)" % (
-                    configure.version, ripResult.logger))
+        try:
+            # Only implemented in whipper (ripResult.logger)
+            lines.append("Log created by: whipper %s (%s logger)" % (
+                        configure.version, ripResult.logger))
+        except NameError:
+            lines.append("Log created by: morituri %s" % (configure.version))
@@ -50,3 +53,6 @@
-        # Only implemented in whipper (ripResult.overread)
-        if ripResult.overread:
-            over = "Yes"
+        try:
+            # Only implemented in whipper (ripResult.overread)
+            if ripResult.overread:
+                over = "Yes"
+        except NameError:
+            pass
```
