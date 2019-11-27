#!/bin/bash

rm -rf ./_build
rm -rf ./mkdocs.yml
mkdir -p ./_build/pydocmd/examples
python docs/autogen.py
pydocmd serve
