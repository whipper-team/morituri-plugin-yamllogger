from setuptools import setup, find_packages

setup(
    name="morituri-whatlogger",
    version="0.0.1",
    description="""morituri YAML style logger for What.CD""",
    author="JoeLametta",
    packages=[
        'whatlogger',
        'whatlogger.logger'],
    entry_points="""
  [morituri.logger]
  what = whatlogger.logger.whatcd:WhatLogger
  """)
