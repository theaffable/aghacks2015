""" Module used to analyze given data and calculate movements. """


import util
import structures


def calculate_next_move(obstacles, current_speed):
    """
    Function determines next optimal move for given state of the board.
    The state of the board is defined by the list of obstacles and current speed of the character.
    """
    obstacles = merge_obstacles(obstacles)
    nearest_obstacle = get_nearest_obstacle(obstacles)

    # if the nearest obstacle is None it means that there are no obstacles on the board, we can do nothing
    if nearest_obstacle is None:
        return structures.Moves.WAIT

    jump_distance = calculate_jump_distance(current_speed)
    if nearest_obstacle.x - util.DINO_WIDTH < jump_distance / 2.0:
        return structures.Moves.JUMP

    return structures.Moves.WAIT


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


def get_nearest_obstacle(obstacles):
    """
    Returns the first obstacle in the list if it exists. If not it returns None.
    """
    if len(obstacles) >= 1:
        return obstacles[0]
    return None

