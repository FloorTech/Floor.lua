#!/bin/bash
# Run this to install a PIP package(s)!
source venv/bin/activate
pip install $*
deactivate
