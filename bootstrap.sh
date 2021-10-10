#!/usr/bin/env bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}" || exit

pip install pip-tools

python -m venv .venv
source .venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install pip-tools
pip install -r requirements.txt