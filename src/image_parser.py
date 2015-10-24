""" Module responsible for image interpretation. """

import cv2
import numpy
from os import listdir
from os.path import isfile, join
from structures import Cactus


path = "../resources/templates"
templatesPaths = [f for f in listdir(path) if isfile(join(path, f))]


def get_obstacles_from_image(image):
    cactuses = []
    for templatePath in templatesPaths:
        img_rgb = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(path+"/"+templatePath, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.4
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cactuses.append(Cactus(pt[0], w, h))
    unique_x = list(set(map(lambda cactus: cactus.x, cactuses)))
    new_cactuses = [filter(lambda cactus: cactus.x == x, cactuses) for x in unique_x]
    return sorted([reduce(lambda a, b: Cactus(a.x, max(a.width, b.width), max(a.height, b.height)), x) for x in new_cactuses], lambda a, b: a.x - b.x)
