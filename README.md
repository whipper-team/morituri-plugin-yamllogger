## Status
[![Build Status](https://travis-ci.org/JoeLametta/morituri-yamllogger.svg?branch=master)](https://travis-ci.org/JoeLametta/morituri-yamllogger)

## Using

To use this plugin:

* build it:

        git clone git://github.com/JoeLametta/morituri-yamllogger.git
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
