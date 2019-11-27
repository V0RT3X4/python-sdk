#!/bin/bash

mkdir -p ./_build/pydocmd/examples
python docs/autogen.py
pydocmd build
