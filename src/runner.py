"""
Starting point of our program.
"""


import util
import structures
import image_capturer
import image_parser
import movement_analyzer
from Queue import Queue
from time import sleep


if __name__ == '__main__':
    browser = util.open_browser()
    util.perform_action(structures.Actions.JUMP, browser)

    # we initialize action queue. We can store multiple actions that will be performed in each frame.
    actions_queue = Queue()

    # we initialize the speed
    speed = util.SPEED

    # in our case the time is the amount of frames that were displayed on the screen
    time = 0
    while True:
        time += 1

        # we store the current board image
        board_image = image_capturer.get_image_from_browser(browser)

        # then retrieve obstacles from given area
        (dino, cactuses, pteros) = image_parser.get_objects_from_image(board_image)

        # calculate our speed
        speed = util.calculate_speed(speed, time, util.ACCELERATION)

        # calculate optimal move and populate the action queue
        movement_analyzer.calculate_next_action(cactuses, pteros, speed, util.convert_dino_height(dino.height),  actions_queue)
        print util.convert_dino_height(dino.height)

        # perform next move
        util.perform_action(actions_queue.get(), browser)

        # sleep the time equal to the time of 1 frame
        sleep(1 / util.FPS)
