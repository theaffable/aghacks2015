""" Module responsible for image interpretation. """

import cv2
import numpy
from os import listdir
from os.path import isfile, join
from structures import Cactus, Pterodactyl, Dino


cactusPath = "../resources/templates/cactus"
pteroPath = "../resources/templates/ptero"
dinoPath = "../resources/templates/dino"
cactusPaths = [f for f in listdir(cactusPath) if isfile(join(cactusPath, f))]
pteroPaths = [f for f in listdir(pteroPath) if isfile(join(pteroPath, f))]
dinoPaths = [f for f in listdir(dinoPath) if isfile(join(dinoPath, f))]


def match_cactuses(image, file_names, path):
    objects = []
    for templatePath in file_names:
        img_rgb = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(path+"/"+templatePath, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.4
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            objects.append(Cactus(pt[0], w, h))
    unique_x = list(set(map(lambda cactus: cactus.x, objects)))
    new_cactuses = [filter(lambda cactus: cactus.x == x, objects) for x in unique_x]
    return [reduce(lambda a, b: Cactus(a.x, max(a.width, b.width), max(a.height, b.height)), x) for x in new_cactuses]


def match_pteros(image, file_names, path):
    objects = []
    for templatePath in file_names:
        img_rgb = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(path+"/"+templatePath, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.4
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            objects.append(Pterodactyl(pt[0], w, h))
    unique_x = list(set(map(lambda ptero: ptero.x, objects)))
    new_pteros = [filter(lambda ptero: ptero.x == x, objects) for x in unique_x]
    return [reduce(lambda a, b: Pterodactyl(a.x, max(a.width, b.width), max(a.height, b.height)), x) for x in new_pteros]


def match_dino(image, file_names, path):
    objects = []
    for templatePath in file_names:
        img_rgb = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(path+"/"+templatePath, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.4
        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            objects.append(Dino(h))
    unique_x = list(set(map(lambda dino: dino.x, objects)))
    return [reduce(lambda a, b: Dino(max(a.height, b.height)), x) for x in unique_x]


def get_objects_from_image(image):
    cactuses = match_cactuses(image, cactusPaths, cactusPath)
    pteros = match_pteros(image, pteroPaths, pteroPath)
    dino = match_dino(image, dinoPaths, dinoPath)
    return (dino, cactuses, pteros)
