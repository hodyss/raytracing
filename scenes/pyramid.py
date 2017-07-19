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
azur = np.array([0.4, 0.6, 0.8])

half_white = np.array([0.5, 0.5, 0.5])
smooth_white = np.array([0.3, 0.3, 0.3])

# create the objects
S0 = Sphere([-2, -2, 9], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S1 = Sphere([-1, -2, 9], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S2 = Sphere([0, -2, 9], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S3 = Sphere([-1.5, -2, 8], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S4 = Sphere([-0.5, -2, 8], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S5 = Sphere([0.5, -2, 8], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S6 = Sphere([-1, -2, 7], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S7 = Sphere([0, -2, 7], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S8 = Sphere([1, -2, 7], 0.5, Material(red, 0.1, 0.8, 0.8, 10, 0.4))
S9 = Sphere([0.5, -2+1/np.sqrt(2), 7.5], 0.5, Material(blue, 0.1, 0.8, 0.8, 10, 0.4))
S10 = Sphere([-0.5, -2+1/np.sqrt(2), 7.5], 0.5, Material(blue, 0.1, 0.8, 0.8, 10, 0.4))
S11 = Sphere([0, -2+1/np.sqrt(2), 8.5], 0.5, Material(blue, 0.1, 0.8, 0.8, 10, 0.4))
S12 = Sphere([-1, -2+1/np.sqrt(2), 8.5], 0.5, Material(blue, 0.1, 0.8, 0.8, 10, 0.4))
S13 = Sphere([-0.125, -2+2/np.sqrt(2), 8], 0.5, Material(green, 0.1, 0.8, 0.8, 10, 0.4))
T1 = Triangle(np.array([0, -2.5, 100]), np.array([-40, -2.5, -20]), np.array([40, -2.5, -20]), Material(yellow, 0.1, 0.9, 0.9, 5, 0.2))
T2 = Triangle(np.array([30, 20, 30]), np.array([-30, 20, 30]), np.array([0, -100, 30]), Material(azur, 0.1, 0.9, 0.9, 5, 0.2))

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
scene.add_object(S6)
scene.add_object(S7)
scene.add_object(S8)
scene.add_object(S9)
scene.add_object(S10)
scene.add_object(S11)
scene.add_object(S12)
scene.add_object(S13)
scene.add_object(T1)
scene.add_object(T2)
scene.add_light(L0)
scene.add_light(L1)
scene.add_light(L2)

# configure the multiprocessing
pool = Pool(processes = 2)
result = pool.apply_async(raytracer_render, (Camera(800,800,2), scene))

# render and save the image
if __name__ == "__main__":
    plt.imsave('pyramid3.png', result.get(timeout=3600), vmin=0, vmax=1, format='png')