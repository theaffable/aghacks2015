""" Module responsible for image interpretation. """

import Image

im = Image.open("../resources/canvas1.png")

pix = im.load()

for x in xrange(0, im.size[0]):
    line = pix[x, 131]
    if line != (83, 83, 83, 255):
        print x, line
