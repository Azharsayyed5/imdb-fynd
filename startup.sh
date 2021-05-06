#!/bin/sh
echo Starting uvicron web server
uvicorn src.main.app:app --host 0.0.0.0 --port 8000 --debug --workers 3