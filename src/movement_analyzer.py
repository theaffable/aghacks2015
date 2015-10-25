""" Module used to analyze given data and calculate movements. """


import util
import structures


def calculate_next_action(diff, last_x, next_obstacle):
    """
    Function determines next optimal move for given state of the board.
    The state of the board is defined by the list of obstacles and current speed of the character.
    """

    speed = diff * util.FPS

    if type(next_obstacle) == structures.Cactus:
        #print next_obstacle - last_x  #-> [150....400]
        print next_obstacle.x, last_x
        print (1-(next_obstacle.x - last_x)/450.0)*35
        if (last_x>70) and (speed/util.FPS > last_x-115-(1 - next_obstacle.width/55.0)*10-(1-(next_obstacle.x - last_x)/600.0)*35):   #-180 sprobuje wyskoczyc mozliwie wczesnie!
            return structures.Actions.JUMP
        return structures.Actions.WAIT
    elif type(next_obstacle) == structures.Pterodactyl:
        print next_obstacle.height
        if next_obstacle.height > 60:
            return structures.Actions.DUCK
        return structures.Actions.JUMP


def merge_obstacles(obstacles, delta):
    """
    Merges obstacles contained in the given list. Merging is performed if two or more obstacles are next to each other.
    Returns new list where len(obstacles) >= len(result_list).
    """
    if obstacles:
        return sorted(obstacles, lambda a, b: a.x - b.x)
        #return [reduce(lambda o1, o2: structures.Cactus(o1.x, o2.x + o2.width - o1.x, o1.height if o1.height > o2.height else o2.height) if o1.x + o1.width + delta >= o2.x else o1, sorted(obstacles, lambda a, b: a.x - b.x))] 
    return []


def get_nearest_obstacle_x(obstacles):
    """
    Returns the first obstacle in the list if it exists. If not it returns None.
    """
    obstacles = filter(lambda a: a.x>70, obstacles)
    if obstacles:
        return obstacles[0].x
    return 600

