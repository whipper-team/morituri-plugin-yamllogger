from setuptools import setup

setup(
    name="morituri-yamllogger",
    version="0.1.0",
    description="""morituri YAML style logger""",
    author="JoeLametta",
    packages=[
        'yamllogger',
        'yamllogger.logger'],
    entry_points="""
  [morituri.logger]
  yaml = yamllogger.logger.yaml:YamlLogger
  """)
