#!/bin/bash
# pip3 install virtualenv
# virtualenv ./.venv
python -m venv ./.venv
source ./.venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
deactivate