from multiprocessing import Pool

import matplotlib.pyplot as plt

from camera import *
from raytracer import *

# create scene
scene = Scene()

# create colors
blue = np.array([0,0,1])
white = np.array([1,1,1])

# add objects and lights
scene.add_object(Triangle(np.array([-1,-1,1]), np.array([0,1,1]),np.array([1,0,1]),Material(blue, 0.3, 0.5, 0.8, 50, 0.5)))
scene.add_light(Spotlight(np.array([1,1,0]),white))

# configure the multiprocessing
pool = Pool(processes = 2)
result = pool.apply_async(raytracer_render, (Camera(200,200,1), scene))

# render and save the image
plt.imsave('one_triangle.png', result.get(timeout=10), vmin = 0, vmax = 1,  format='png')