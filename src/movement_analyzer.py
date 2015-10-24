""" Module used to analyze given data and calculate movements. """


import util
import structures


def calculate_next_action(diff, last_x, next_obstacle):
    """
    Function determines next optimal move for given state of the board.
    The state of the board is defined by the list of obstacles and current speed of the character.
    """

    speed = diff/0.01667

    #print next_obstacle - last_x  #-> [150....400]
    print (1-(next_obstacle - last_x)/600.0)*30
    if (last_x > 70) and (speed*0.01667 > last_x-170+(1-(next_obstacle - last_x)/600.0)*40):   #-180 sprobuje wyskoczyc mozliwie wczesnie!
	return structures.Actions.JUMP
    return structures.Actions.WAIT


def calculate_jump_distance(current_speed):
    return current_speed


def merge_obstacles(obstacles, delta):
    """
    Merges obstacles contained in the given list. Merging is performed if two or more obstacles are next to each other.
    Returns new list where len(obstacles) >= len(result_list).
    """
    if obstacles:
    	return sorted(obstacles, lambda a, b: a.x - b.x)
        #return [reduce(lambda o1, o2: structures.Cactus(o1.x, o2.x + o2.width - o1.x, o1.height if o1.height > o2.height else o2.height) if o1.x + o1.width + delta >= o2.x else o1, sorted(obstacles, lambda a, b: a.x - b.x))] 
    return []


def get_nearest_obstacle(obstacles):
    """
    Returns the first obstacle in the list if it exists. If not it returns None.
    """
    if obstacles:
        return obstacles[0].x
    return 600

