# ----------------------------------------------------------
#        Quick 'n' dirty 565-to-png file converter
#
# File:        565_to_png.py
# Author:      Jille
# Revision:    1
# Purpose:     Converting Arcade1Up menu screens (.565 and .load) to png
# Comments:    Usage: 565_to_png.py <path to .565 files> <output folder>
# Credits:     Using convert_to_png from xC0000005 
#              (https://github.com/xC0000005/Arcade1UpTools)
# Changelog:   v1: Initial version
# ----------------------------------------------------------

import fnmatch
import os
import sys

if sys.version_info[0] < 3:
    sys.exit("You need to run this with Python 3")

try:
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
except ImportError:
    print("  You are missing the PIL module!\n"
          "  install it by running:\n"
          "  pip install image")
    input("\nPress Enter to exit...")
    sys.exit(1)

if len(sys.argv) != 3:
    print("usage: 565_to_png.py <path to .565 files> <output folder>")
    input("\nPress Enter to exit...")
    sys.exit(1)

out_dir = sys.argv[2]
path = sys.argv[1]
if not os.path.exists(out_dir):
    os.makedirs(out_dir)


def convert_to_png(source, target):
    raw_file = open(source, "rb")
    img = Image.new('RGBA', (640, 480))
    raw_bytes = bytearray(raw_file.read())
    byte_index = 0
    for y in range(0, 480):
        for x in range(0, 640):
            pixel_value = (raw_bytes[byte_index + 2], raw_bytes[byte_index + 1], raw_bytes[byte_index + 0],
                           255)  # raw_bytes[byte_index + 3])
            img.putpixel((x, y), pixel_value)
            byte_index = byte_index + 4
    img.save(target, "PNG")
    raw_file.close()


counter = 0
for filename_full in os.listdir(path):
    if (fnmatch.fnmatch(filename_full, '*.565')) | (fnmatch.fnmatch(filename_full, '*.load')):
        filename, extension = os.path.splitext(filename_full)
        output = out_dir + "\\" + filename_full + ".png"
        filepath = path + filename_full
        print("Converting %s to %s" % (filename_full, output))
        convert_to_png(filepath, output)
        counter = counter + 1

print("\n%s files converted." % (counter))
