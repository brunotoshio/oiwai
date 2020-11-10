#!/usr/bin/env bash

pipenv run flake8

pipenv run coverage erase ; pipenv run pytest ; pipenv run coverage html

pipenv run python -m http.server --directory htmlcov --bind 127.0.0.1 8800
