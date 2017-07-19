import matplotlib.pyplot as plt
from camera import *
from raytracer import *

# create the scene
scene = Scene()
# create colors
blue = np.array([0,0,1])
red = np.array([1,0,0])
white = np.array([1,1,1])
#add the objects and light
scene.add_object(Sphere(np.array([0,0,3]),0.8,Material(blue, 0.3, 0.5, 0.8, 50, 0.5)))
scene.add_object(Sphere(np.array([0.5,0.5,2]),0.3,Material(red, 0.3, 0.5, 0.8, 50, 0.5)))
scene.add_light(Spotlight(np.array([1,1,0]),white))

# render and create the png image
plt.imsave('shadow.png', raytracer_render(Camera(200,200,1), scene), vmin = 0, vmax = 1,  format='png')