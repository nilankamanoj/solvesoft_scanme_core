#!/bin/bash
source venv/bin/activate
export FLASK_ENV=development
export FALSK_APP=app.py
python -m flask run --host=0.0.0.0
