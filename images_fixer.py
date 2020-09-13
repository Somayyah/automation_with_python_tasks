#!/usr/bin/env python3

from PIL import Image
import PIL
import os

dist_dir = "/opt/icons/"
cwd = os.getcwd()
for image in os.listdir(cwd):
        if image.startswith(".") or image == "images_fixer.py":
                continue
        im = Image.open(image)
        if im.mode != "RGB":
                im = im.convert("RGB")
        image_path = os.path.join(dist_dir,image)
        im.rotate(-90).resize((128,128)).save("{}".format(image_path),"JPEG")
