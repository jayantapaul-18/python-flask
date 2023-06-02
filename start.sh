#! /bin/bash
echo "python3 -m venv .venv"
python3 -m venv .venv
echo ". .venv/bin/activate"
. .venv/bin/activate
echo "export FLASK_APP=server.py"
export FLASK_APP=server.py
echo "flask run"
flask run