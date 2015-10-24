""" Module responsible for image interpretation. """

import cv2
import Image
from os import listdir, environ
from os.path import isfile, join
import os
import image_capturer as IC
from PIL import Image
from time import sleep
from random import randint
import numpy as np
from structures import Cactus

path = "../resources/templates"
templatesPaths = [f for f in listdir(path) if isfile(join(path, f))]

def process_image(image):
	cactuses = []
	for templatePath in templatesPaths:
		img_rgb = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
		template = cv2.imread(path+"/"+templatePath, 0)
		w, h = template.shape[::-1]

		res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
		threshold = 0.5
		loc = np.where(res >= threshold)
		for pt in zip(*loc[::-1]):
			cactuses.append(Cactus(pt[0], w, h))	
	unique_x = list(set(map(lambda cactus: cactus.x, cactuses)))
	new_cactuses = [ filter(lambda cactus: cactus.x == x, cactuses) for x in unique_x]
	return [reduce(lambda a,b: Cactus(a.x, max(a.width, b.width), max(a.height, b.height)), x) for x in new_cactuses]

if __name__== "__main__":
	browser = IC.open_browser()
	sleep(2)
	while(True):
		image = IC.get_image_from_browser(browser)
		cactuses = process_image(image)
		for cactus in cactuses:
			print cactus,
		print
		#todo rethink performing action & sleep
		IC.perform_action(browser)
		





def test():
    im = Image.open("../resources/canvas1.png")

    pix = im.load()

    for x in xrange(0, im.size[0]):
        line = pix[x, 131]
        if line != (83, 83, 83, 255):
            print x, line
