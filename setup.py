from setuptools import setup
from yamllogger import __version__ as plugin_version

setup(
    name="morituri-plugin-yamllogger",
    version=plugin_version,
    description="A plugin for whipper which provides YAML style log reports",
    author="JoeLametta",
    maintainer="JoeLametta",
    license="ISC License",
    url="https://github.com/whipper-team/whipper-plugin-yamllogger",
    packages=['yamllogger', 'yamllogger.logger'],
    entry_points={
        "morituri.logger": [
            "yaml = yamllogger.logger.yaml:YamlLogger"
        ]
    }
)
