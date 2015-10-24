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

path = "../resources/templates"
templatesPaths = [f for f in listdir(path) if isfile(join(path, f))]

def process_image(image):
	hit = 0
	for templatePath in templatesPaths:
		image = np.array(image)
		img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		template = cv2.imread(path+"/"+templatePath, 0)
		w, h = template.shape[::-1]

		res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
		threshold = 0.8
		loc = np.where(res >= threshold)
		for pt in zip(*loc[::-1]):
			hit += 1
			cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
	
	#todo offset of trees
	print "amount of trees:", hit
	cv2.imshow("img", image)



if __name__== "__main__":
	browser = IC.open_browser()
	while(True):
		image = IC.get_image_from_browser(browser)
		process_image(image)
		#todo rethink performing action & sleep
		IC.perform_action(browser)
		sleep(1)





def test():
    im = Image.open("../resources/canvas1.png")

    pix = im.load()

    for x in xrange(0, im.size[0]):
        line = pix[x, 131]
        if line != (83, 83, 83, 255):
            print x, line