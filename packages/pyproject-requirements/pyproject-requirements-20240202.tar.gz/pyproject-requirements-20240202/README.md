# pip-requirements

Install requirements/dependencies specified in a pyproject.toml using pip.

## Features

- Installs required, optional and/or all dependencies.
- Detects and works with pip in installed in virtual environments.

## Quick Start

1. Install pip-requirements:

   ```shell
   pip install pip-requirements
   ```

2. Install all dependencies of your pyproject.toml 

   ```shell
   # use `--optional name` to limit to optional named dependency section
   # use `--required` to install required dependencies
   pip-requirements install --all path/to/pyproject.toml 
   ```

## Why

- This only exists because it's not builtin to pip.

- Using requirements.txt files is primitive and redundant compared to the expressiveness
  of pyproject.toml files..

We should have something like:

```shell
pip install --optional=name --required --all path/to/pyproject.toml
```

Or:

```shell
pip requirements install --all path/to/pyproject.toml
```


## Links

- [Source](https://hg.sr.ht/~metacompany/pip-requirements) (Source Hut)

