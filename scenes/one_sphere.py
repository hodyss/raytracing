import matplotlib.pyplot as plt

from camera import *
from raytracer import *

# create a scene
scene = Scene()

# create colors
blue = np.array([0,0,1])
white = np.array([1,1,1])

# add the objects and lights
scene.add_object(Sphere(np.array([0,0,3]),1,Material(blue, 0.3, 0.5, 0.8, 50, 0.5)))
scene.add_light(Spotlight(np.array([1,1,0]),white))

# render and save the png image
plt.imsave('one_sphere.png', raytracer_render(Camera(200,200,1), scene), vmin = 0, vmax = 1,  format='png')