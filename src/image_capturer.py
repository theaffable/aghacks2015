from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from io import BytesIO
from PIL import Image

#open browser
browser = webdriver.Chrome('D:/Aghacks/chromedriver')
# must wait some time for loading
browser.get('http://www.9gag.com')


script = "return document.getElementsByTagName('canvas')[0].toDataURL()"

#get image from browser
for x in xrange(4):
	sleep(0.033)
	raw_image = browser.execute_script(script)
	raw_image = raw_image[raw_image.find(',')+1:]
	img = Image.open(BytesIO(raw_image.decode('base64')))
	#img.show()

# for T-REx action in browser
elem = browser.find_element_by_tag_name('canvas') # Find the search box
webdriver.ActionChains(browser).move_to_element(elem).key_up(Keys.UP).perform()
