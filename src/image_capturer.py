from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from io import BytesIO
from PIL import Image
from time import sleep
import os


def open_browser():
    browser = webdriver.Chrome(os.environ["CHROME_DRIVER"])
    # must wait some time for loading
    sleep(3)
    browser.get('http://www.9gag.com')
    return browser


def get_image_from_browser(browser):
    script = "return document.getElementsByTagName('canvas')[0].toDataURL()"

    raw_image = browser.execute_script(script)
    raw_image = raw_image[raw_image.find(',')+1:]
    image = Image.open(BytesIO(raw_image.decode('base64')))
    return image


def perform_action(browser):
    # TODO move to another file
    # for T-REx action in browser
    elem = browser.find_element_by_tag_name('canvas') # Find the search box
    webdriver.ActionChains(browser).move_to_element(elem).key_up(Keys.UP).perform()
