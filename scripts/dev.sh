#!/bin/bash
# Please run `./setup.sh` before this one!
source venv/bin/activate
python3 src/main.py $*
deactivate
