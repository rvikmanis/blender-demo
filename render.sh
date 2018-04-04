#!/usr/bin/env bash
export COLOR_R=$1
export COLOR_G=$2
export COLOR_B=$3

BLENDER_PATH=/Applications/Blender/blender.app/Contents/MacOS/blender

${BLENDER_PATH} -b ./cube.blend -P generate_image.py
