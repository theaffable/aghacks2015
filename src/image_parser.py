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
	hit = 0
	cactuses = []
	for templatePath in templatesPaths:
		print image
		#nparr = np.fromstring(image, np.uint8)
		#image = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
		#
		#image = np.array(image)
		#image = cv2.imdecode(image, cv2.CV_LOAD_IMAGE_COLOR)
		# 
		open_cv_image = np.array(image) 
		# Convert RGB to BGR 
		image = open_cv_image[:, :, ::-1].copy() 
		#
		img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		template = cv2.imread(path+"/"+templatePath, 0)
		w, h = template.shape[::-1]

		res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
		threshold = 0.8
		loc = np.where(res >= threshold)
		for pt in zip(*loc[::-1]):
			hit += 1
			cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
			cactuses.append(Cactus(pt[0], w, h))
	cv2.imwrite(path+"/out/"+str(randint(1, 1000)) + ".png", image)	

		
	
	#todo offset of trees
	print "amount of trees:", hit
	return cactuses



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
		sleep(1)
		





def test():
    im = Image.open("../resources/canvas1.png")

    pix = im.load()

    for x in xrange(0, im.size[0]):
        line = pix[x, 131]
        if line != (83, 83, 83, 255):
            print x, line
