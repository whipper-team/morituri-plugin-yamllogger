## Status

[![Build Status](https://travis-ci.org/JoeLametta/morituri-yamllogger.svg?branch=master)](https://travis-ci.org/JoeLametta/morituri-yamllogger)

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
--- whipper/morituri/result/logger.py
+++ morituri-yamllogger/yamllogger/logger/yaml.py
@@ -4,2 +3,0 @@
-import morituri
-
@@ -6,0 +5 @@
+from morituri.configure import configure
@@ -10 +9 @@
-class MorituriLogger(result.Logger):
+class YamlLogger(result.Logger):
@@ -28,3 +27 @@
-        # Only implemented in whipper (ripResult.logger)
-        lines.append("Log created by: whipper %s (%s logger)" % (
-                    morituri.__version__, ripResult.logger))
+        lines.append("Log created by: morituri %s" % (configure.version))
@@ -51,3 +47,0 @@
-        # Only implemented in whipper (ripResult.overread)
-        if ripResult.overread:
-            over = "Yes"
```
