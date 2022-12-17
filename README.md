<h1 align="center">Python Packaging Tutorial</h1>
<p align="center">
A quick tour of how to set up a Python package
</p>

---

> This is a work in progress (the guide part at least, the code here is probably in it's final form)

## Introduction
In this tutorial, you will be introduced to (some very opinionated views involving) the concept of Python packages, 
class objects, configuration objects, YAML configuration files, the Click library (CLI interfaces), 
the creation of a `setup.py` file, and Python package management. 

## Disclaimer
This is just how I usually start a project. Even then, it's only if the project requires CLI, configuration management, 
and levels of abstraction for ease of use.
(particularly if it's something that will be used by others or executed autonomously)


The target audience is those who want a flexible template for projects that meet the criteria mentioned above.

## Table of Contents

1. [Project Layout](./docs/1.%20Project%20Layout.md)
2. [Using Classes](./docs/2.%20Using%20classes.md)
3. [Importing Packages](./docs/3.%20Importing%20Packages.md)
4. [Configuration Objects](./docs/4.%20Configuration%20objects.md)
5. [Ingesting YAML](./docs/5.%20Ingesting%20YAML.md)
6. [CLI Interfaces](./docs/6.%20CLI%20interfaces.md)
7. [Python setuptools](./docs/7.%20Python%20setuptools.md)
8. [Implementation](./docs/8.%20Implementation.md)

## Author
[Cam Ratchford](https://github.com/camratchford)

## License
[CC0 1.0 Universal](./LICENSE)