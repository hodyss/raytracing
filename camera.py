from ray import *
import numpy as np


# class: Camera
# represent the viewer eyes
# it is arbitrarily positioned at the origin ([0,0,0])
# @param image_nrows: a positive integer which is the number lines of the picture
# @param image_ncols: a positive integer which is the number of columns of the picture
# @param focal_length: a positive real_number which is the distance between the camera and the screen
class Camera:
    def __init__(self, image_nrows, image_ncols, focal_length):
        self.image_nrows = image_nrows
        self.image_ncols = image_ncols
        self.focal_length = focal_length

    # methode ray_at: create a ray pointing at the indicated pixel, from the camera
    # @param row: positive integer which is the line of the pixel
    # @param col: positive integer which is the column of the pixel
    # @return: object from the Ray class
    def ray_at(self, row, col):
        return Ray(np.array([0, 0, 0]),
                   np.array([1 - 2 * col / self.image_ncols, 1 - 2 * row / self.image_nrows, self.focal_length]))
