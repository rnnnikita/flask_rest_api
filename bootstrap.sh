#!/usr/bin/env bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}" || exit

python -m venv .venv
source .venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt