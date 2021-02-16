# Flaky API

## How to run

This project uses pipenv, which can be installed by following [these instructions](https://docs.pipenv.org/#install-pipenv-today).

### Install dependencies

To install the project's dependencies, run `pipenv install`

### Run it

To run the script, `pipenv run python main.py`

### Run the tests

`pipenv run python -m unittest`

## Comments

The images get downloaded to a folder named `output` at the root of the project.

Since the given endpoint fails intermittently, each page request is retried up to 5 times. If we couldn't get a successful response at this point we give up and note that on the standard output. Even if a subset of the desired pages fail, we still attempt to download the images for the rest of them.