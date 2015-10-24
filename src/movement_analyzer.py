""" Module used to analyze given data and calculate movements. """


import util


def calculate_next_move(obstacles, current_speed):
    """
    Function determines next optimal move for given state of the board.
    The state of the board is defined by the list of obstacles and current speed of the character.
    """
    pass


def calculate_jump_distance(current_speed):
    return current_speed * util.TIME_IN_AIR


def merge_obstacles(obstacles):
    """
    Merges obstacles contained in the given list. Merging is performed if two or more obstacles are next to each other.
    Returns new list where len(obstacles) >= len(result_list).
    """
    # TODO implement
    # TODO create test cases
    return obstacles

