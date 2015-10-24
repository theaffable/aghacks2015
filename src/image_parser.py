""" Module responsible for image interpretation. """

import numpy
import cv2
import image_capturer
import util

from os import listdir
from os.path import isfile, join
from PIL import Image
from time import sleep


path = "../resources/templates"
templatesPaths = [f for f in listdir(path) if isfile(join(path, f))]


def get_obstacles_from_image(image):
    hit = 0
    for templatePath in templatesPaths:
        image = numpy.array(image)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(path + "/" + templatePath, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            hit += 1
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # todo offset of trees
    print "amount of trees:", hit
    # cv2.imshow("img", image)
    # TODO IMPLEMENT THE METHOD
    return []


def test():
    im = Image.open("../resources/canvas1.png")

    pix = im.load()

    for x in xrange(0, im.size[0]):
        line = pix[x, 131]
        if line != (83, 83, 83, 255):
            print x, line
