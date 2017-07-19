# class: Ray
# these objects represents ray, pointing from a given point to a given direction
# @param starting_point: a 1x3 array which is the starting point of the ray
# @param direction: a 1x3 array which is the direction of the ray
# the direction does not need to be normalised since the algorithm normalise it when used
class Ray:
    def __init__(self, starting_point, direction):
        self.starting_point = starting_point
        self.direction = direction
