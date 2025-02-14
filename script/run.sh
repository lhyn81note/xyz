#!/bin/bash

shopt -s expand_aliases

if [ -z "$1" ]; then
    echo "dev/build?"
    exit 0
fi

if [ "$1" == "dev" ]; then
    echo "========== Dev ==========="
    for dir in view/*/; do
        folder_name=$(basename "$dir")
        rm -f "${dir}_view.py"
        pyside6-uic "${dir}view.ui" -o "${dir}_view.py"
    done
    python app.py
fi

if [ "$1" == "build" ]; then
    echo "========== Build ==========="
    rm -rf build
    rm -rf dist
    pyinstaller build.spec
    mkdir -p dist/res
    cp -r res dist/res
    cp setting.py dist
fi

exit 0