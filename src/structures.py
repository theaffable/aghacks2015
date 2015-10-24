""" Module with all structures used throughout the program. """


class Rectangle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Dino(object):
    def __init__(self, height):
        self.height = height


class Obstacle(object):
    """ Class used to represent obstacles. Each of those obstacles has it's own location on X axis. """
    def __init__(self, x):
        self.x = x


class Cactus(Obstacle):
    """
    Class that represents a cactus obstacle seen in the game. Cactus inherits X axis location from Obstacle class
    and adds it's own fields - width and height.
    """
    def __init__(self, x, width, height):
        super(Cactus, self).__init__(x)
        self.width = width
        self.height = height

    def __str__(self):
        return "Cactus(%d, %d, %d)" % (self.x, self.width, self.height)


class Pterodactyl(Obstacle):
    """
    Class that represents a pterodactyl obstacle seen later in the game. Inherits X axis location from Obstacle class
    and adds Y axis location.
    """
    def __init__(self, x, width, height):
        super(Pterodactyl, self).__init__(x)
        self.width = width
        self.height = height


class Actions(object):
    """
    Enum class that represents possible moves for our character.
    """
    WAIT = 0
    JUMP = 1
    DUCK = 2

