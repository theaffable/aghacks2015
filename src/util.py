"""
Module containing all of the utility functions.
We will need this module only if canvas-through-websocket won't work.
"""

from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from structures import Actions
from os import environ


# constants
MIN_JUMP_HEIGHT = 35
TIME_IN_AIR = 40        # time spent in the air with the basic jump force
DINO_WIDTH = 20

ACCELERATION = 0.0004
MAX_SPEED = 13
SPEED = 6
FPS = 60.0
BROWSER_OPEN_TIME = 3


def calculate_speed(previous_speed, time, acceleration):
    if time == 0:
        return SPEED

    # we must check if current speed is not higher than MAX_SPEED
    current_speed = previous_speed + time * acceleration
    if current_speed > MAX_SPEED:
        return MAX_SPEED

    return current_speed


def perform_action(action, browser):
    """
    Performs given action inside the browser.
    """
    elem = browser.find_element_by_tag_name('canvas')   # Find the search box

    if action == Actions.JUMP:
        webdriver.ActionChains(browser).move_to_element(elem).key_up(Keys.UP).perform()
    elif action == Actions.DUCK:
        webdriver.ActionChains(browser).move_to_element(elem).key_up(Keys.DOWN).perform()
    else:
        pass    # if is equal to Moves.Wait we don't have to do anything


def open_browser():
    browser = webdriver.Chrome(CHROME_DRIVER_DIR)
    # must wait some time for loading
    sleep(BROWSER_OPEN_TIME)
    browser.get('http://9gag.com')
    return browser
