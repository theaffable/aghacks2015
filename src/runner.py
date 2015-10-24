"""
Starting point of our program.
"""


import util
import structures
import image_capturer
import image_parser
import movement_analyzer
from time import sleep


if __name__ == '__main__':
    browser = util.open_browser()
    util.perform_action(structures.Actions.JUMP, browser)

    # in our case the time is the amount of frames that were displayed on the screen
    time = 0
    while True:
        time += 1

        # we store the current board image
        board_image = image_capturer.get_image_from_browser(browser)

        # then retrieve obstacles from given area
        obstacles = image_parser.get_obstacles_from_image(board_image)

        # calculate our speed
        speed = util.calculate_speed(time, util.ACCELERATION)

        # calculate optimal move
        action = movement_analyzer.calculate_next_action(obstacles, speed)

        # perform next move
        util.perform_action(action, browser)

        # sleep the time equal to the time of 1 frame
        sleep(1 / util.FPS)
