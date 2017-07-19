import sys
sys.path.append('..')

from multiprocessing import Pool

from camera import *
from raytracer import *
import numpy as np
import matplotlib.pyplot as plt

# create the scene
scene = Scene()

# create the colors
red = np.array([1, 0, 0])
green = np.array([0, 1, 0])
blue = np.array([0, 0, 1])
yellow = np.array([1, 1, 0])
violet = np.array([1, 0, 0.5])
grey = np.array([0.8, 0.8, 0.8])
azur = np.array([0.3, 0.5, 0.8])

half_white = np.array([0.5, 0.5, 0.5])
smooth_white = np.array([0.3, 0.3, 0.3])

# create the objects
S0 = Sphere([1, 0, 3], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S1 = Sphere([-1, 0, 3], 0.5, Material(green, 0.1, 0.8, 0.8, 10, 0.4))
S2 = Sphere([0, -1, 3], 0.5, Material(blue, 0.1, 0.8, 0.8, 10, 0.4))
S3 = Sphere([0, 1, 3], 0.5, Material(yellow, 0.1, 0.8, 0.8, 10, 0.4))
S4 = Sphere([0, 0, 3], 0.3, Material(violet, 0.2, 0.8, 0.8, 10, 0.4))
S5 = Sphere([0, 0, 15], 10, Material(grey, 0.2, 0.8, 0.8, 10, 0.4))
T = Triangle(np.array([0, 5, 50]), np.array([-30, -2, -1]), np.array([30, -2, -1]), Material(azur, 0.1, 0.9, 0.9, 5, 0.2))

# create the lights
L0 = Spotlight(np.array([1, 1, 0]), half_white)
L1 = Spotlight(np.array([-1, 1, 0]), half_white)
L2 = Spotlight(np.array([0, 1, 0]), smooth_white)

# add objects and lights
scene.add_object(S0)
scene.add_object(S1)
scene.add_object(S2)
scene.add_object(S3)
scene.add_object(S4)
scene.add_object(S5)
scene.add_object(T)
scene.add_light(L0)
scene.add_light(L1)
scene.add_light(L2)

# configure the multiprocessing
pool = Pool(processes = 2)
result = pool.apply_async(raytracer_render, (Camera(400,400,1), scene))

# render and save the image
if __name__ == "__main__":
    plt.imsave('final_scene.png', result.get(timeout=3600), vmin=0, vmax=1, format='png')