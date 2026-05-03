#!/bin/bash
set -e
cd "$(dirname "$0")/.."
rm -f victim/workshop.db
echo "Starting Security Workshop servers..."
python victim/app.py &
python internal/app.py &
wait
