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
