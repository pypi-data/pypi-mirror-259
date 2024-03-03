#!/bin/bash


python -m build

pip install --force-reinstall dist/logos-0.0.1-py3-none-any.whl
