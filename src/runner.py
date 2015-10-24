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

    while True:
        board_image = image_capturer.get_image_from_browser(browser)
        obstacles = image_parser.get_obstacles_from_image(board_image)
	
	tmp = movement_analyzer.get_nearest_obstacle(obstacles)
	diff = last_pos - tmp
	last_pos = tmp
	
	next_obstacle = obstacles[1].x if len(obstacles)>1 else 600

        action = movement_analyzer.calculate_next_action(diff, tmp, next_obstacle)
        util.perform_action(action, browser)
	sleep(1/util.FPS)
