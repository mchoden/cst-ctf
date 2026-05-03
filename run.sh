#!/bin/bash
set -e
cd "$(dirname "$0")"
rm -f victim/workshop.db
pip install flask PyJWT --break-system-packages -q 2>/dev/null || pip install flask PyJWT -q 2>/dev/null
echo ""
echo "Security Workshop — Starting servers..."
echo "   Workshop:  http://localhost:5000"
echo "   Internal:  http://localhost:5002"
echo "   Flags:     http://localhost:5000/flags"
echo ""
python victim/app.py &
python internal/app.py &
trap "kill 0" INT TERM
wait
