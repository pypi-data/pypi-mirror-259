[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Introduction 
This repo tracks the evidi_fabric package which is intended to collect useful helper when working with fabric

# Linting with Ruff

We have used the default Ruff setup, but this can be edited in the pyproject.toml file.

Running checks:

```
ruff check .                        # Lint all files in the current directory (and any subdirectories).
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories).
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`.
ruff check path/to/code/to/file.py  # Lint `file.py`.
ruff check @arguments.txt           # Lint using an input file, treating its contents as newline-delimited command-line arguments.
```

Add the --fix flag to automatically apply the suggestions.

```poetry run ruff check evidi_fabric/ --fix```

Unsafe fixes will not be applied unless you do --unsafe-fixes

```poetry run ruff check evidi_fabric/ --fix --unsafe-fixes```

# Formatting with Ruff

We also use ruff as a formatter.

Running format:

```
ruff format .                        # Format all files in the current directory (and any subdirectories).
ruff format path/to/code/            # Format all files in `/path/to/code` (and any subdirectories).
ruff format path/to/code/*.py        # Format all `.py` files in `/path/to/code`.
ruff format path/to/code/to/file.py  # Format `file.py`.
ruff format @arguments.txt           # Format using an input file, treating its contents as newline-delimited command-line arguments.
```
In our repo:

```
poetry run ruff format .
``` 

The idea is to run ruff format before you comit you code, and then the linting will run automatically after creating a PR.

# Build and Publish to test

One time config:
```poetry config repositories.test-pypi https://test.pypi.org/legacy/```

For fast patch, build and publish, you can use the following command:

```poetry version patch && poetry build && python3 -m twine upload --repository testpypi dist/*```

and for faster upload simply run the below, to only upload the newest version

```poetry run python -m update_package --test```

To upgrade your local repositories to use the test version of the package, run:

```python3 -m pip install --index-url https://test.pypi.org/simple/ evidi_fabric```


# Build and Publish

For fast patch, build and publish, you can use the following command:

```poetry version patch && poetry build && python3 -m twine upload dist/*```

and for faster upload simply run the below, to only upload the newest version

```poetry run python -m update_package```

To upgrade your local repositories with the latest version of the package with pip, run:

```pip install --upgrade evidi_fabric```


## find a specific line of code in all scripts:
run below in a bash terminal
```./helpers/find_file_with_line_of_code.sh "TEXT YOU WANT TO FIND"```