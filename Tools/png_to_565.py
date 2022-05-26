# ----------------------------------------------------------
#           Quick 'n' dirty png-to-565 file converter
#
# File:        png_to_565.py
# Author:      Jille
# Revision:    1
# Purpose:     
# Comments:    Usage: png_to_565.py <path to .png files> <output folder>
# Credits:     
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


def convert_to_565(source, target):
    input_png = Image.open(source).convert('RGBA')
    output_565 = open(target, 'wb')
    # split rgba channels
    b, g, r, a = input_png.split()
    # set alpha channel to 0
    a = a.point(lambda i: i * 0)
    input_png = Image.merge("RGBA", (r, g, b, a))
    image_bytes = input_png.tobytes('raw')
    output_565.seek(0)
    output_565.write(image_bytes)
    output_565.close()


counter = 0

for filename_full in os.listdir(path):
    if (fnmatch.fnmatch(filename_full, '*.png')):
        filename, extension = os.path.splitext(filename_full)
        output = out_dir + "\\" + filename
        filepath = path + filename_full
        print("Converting %s to %s" % (filename_full, output))
        convert_to_565(filepath, output)
        counter = counter + 1

print("\n%s files converted." % (counter))
