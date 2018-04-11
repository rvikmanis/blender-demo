#!/usr/bin/env bash

/Applications/Blender/blender.app/Contents/MacOS/blender -b tshirt.blend --python render.py
python3 verify_performance.py

echo "See rendered images and performance log in ./output"