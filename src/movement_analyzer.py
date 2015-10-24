""" Module used to analyze given data and calculate movements. """


import util
import structures


def calculate_next_action(cactuses, pteros, current_speed, current_height, actions_queue):
    """
    Function determines next optimal move for given state of the board.
    The state of the board is defined by the list of obstacles and current speed of the character.
    """
    cactuses = merge_obstacles(cactuses, delta=30)
    nearest_cactus = get_nearest_obstacle(cactuses)

    # if the nearest obstacle is None it means that there are no obstacles on the board, we can do nothing
    if nearest_cactus is None:
        if actions_queue.empty():
            actions_queue.put(structures.Actions.WAIT)
        return

    jump_distance = calculate_jump_distance(current_speed)
    if nearest_cactus.x + nearest_cactus.width / 2.0 - util.DINO_WIDTH < (jump_distance / 1.5):
        actions_queue.put(structures.Actions.JUMP)
        return

    actions_queue.put(structures.Actions.WAIT)


def calculate_jump_distance(current_speed):
    return current_speed * util.TIME_IN_AIR + (util.ACCELERATION*util.TIME_IN_AIR*util.TIME_IN_AIR)/2.0


def merge_obstacles(obstacles, delta):
    """
    Merges obstacles contained in the given list. Merging is performed if two or more obstacles are next to each other.
    Returns new list where len(obstacles) >= len(result_list).
    """
    if obstacles:
    #return sorted(obstacles, lambda a, b: a.x - b.x)
        return [reduce(lambda o1, o2: structures.Cactus(o1.x, o2.x + o2.width - o1.x, o1.height if o1.height > o2.height else o2.height) if o1.x + o1.width + delta >= o2.x else o1, sorted(obstacles, lambda a, b: a.x - b.x))] 
    return []


def get_nearest_obstacle(obstacles):
    """
    Returns the first obstacle in the list if it exists. If not it returns None.
    """
    if obstacles:
        return obstacles[0]
    return None

