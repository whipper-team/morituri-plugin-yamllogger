from setuptools import setup, find_packages

setup(
    name="morituri-yamllogger",
    version="0.0.1",
    description="""morituri YAML style logger""",
    author="JoeLametta",
    packages=[
        'yamllogger',
        'yamllogger.logger'],
    entry_points="""
  [morituri.logger]
  yaml = yamllogger.logger.yaml:YamlLogger
  """)
