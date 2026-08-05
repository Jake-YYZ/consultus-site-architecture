#!/bin/bash
# Double-click this in Finder to build the site and open it in your browser.
cd "$(dirname "$0")" || exit 1
echo "Building the site (this takes about 20 seconds)..."
python3 build.py --all --clean || { echo "Build failed."; read -r -p "Press return to close."; exit 1; }
echo
echo "Opening http://localhost:8099/ ..."
( sleep 2; open "http://localhost:8099/" ) &
python3 serve.py 8099
