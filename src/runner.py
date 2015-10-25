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

    last_pos = 600
    sleep(4)

    # we initialize the speed
    speed = util.SPEED

    # in our case the time is the amount of frames that were displayed on the screen
    time = 0
    while True:
        time += 1

        # we store the current board image
        board_image = image_capturer.get_image_from_browser(browser)

        # then retrieve obstacles from given area
        cactuses, pteros = image_parser.get_objects_from_image(board_image)
        if pteros:
            print "PTERODAKTYL ------------------------------------------------", len(pteros)

        obstacles = sorted(cactuses + pteros, lambda a, b: a.x - b.x)
        tmp = movement_analyzer.get_nearest_obstacle_x(obstacles)
        diff = last_pos - tmp
        last_pos = tmp

        next_obstacle = obstacles[1] if len(obstacles) > 1 else structures.Obstacle(600)

        action = movement_analyzer.calculate_next_action(diff, tmp, next_obstacle)
        util.perform_action(action, browser)
        sleep(1/util.FPS)
