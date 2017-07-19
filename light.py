from intersection import *
from ray import *


# class: Spotlight
# these objects represent the lights of the scene
# lights are punctual
# @param position: a 1x3 array which indicates the position of the light
# @param color: a 1x3 array which contains real numbers between 0 and 1
# 0 stands for black and 1 stands for the maximum intensity of the component in the RGB model
class Spotlight:
    def __init__(self, position, color):
        self.position = position
        self.color = color


# function: phong_illuminate calculates the color of the pixel studied
# it uses the phong model for every light source and sum the intensities
# description of the phong model can be found in the report
#
# arguments:
# @param scene: object from the Scene class.
# Its attributes are the different objects and lights of the scene.
# @param intersection: object from the Intersection class.
# Its attributes give the coordinates and the normal (both 1x3 array) of the intersection
# @param viewer: a 1x3 array giving the position of the viewer (a.k.a the camera)
# @return: returns a 1x3 array representing the three RGB components of the pixel color
def phong_illuminate(scene, intersection, viewer):
    # name useful constants
    ka = intersection.object.material.ambiant
    kd = intersection.object.material.diffuse
    ks = intersection.object.material.specular
    sh = intersection.object.material.shininess
    M = intersection.position
    N = intersection.normal
    V = (viewer - M) / np.sqrt((viewer - M).dot(viewer - M))
    # initialize the color
    C = np.zeros(3)
    # sum the intensity from each light
    # pick a light
    for light in scene.lights:
        # calculate the normal vector from the intersection to the light
        L = (light.position - M) / np.sqrt((light.position - M).dot(light.position - M))
        # if the light isn't hidden by another object or the object itself
        if shadow_test(light, scene, intersection) == False and N.dot(L) > 0:
            # calculate the direction of reflexion towards the viewer
            # then calculate the intensity reflected
            # then add the contribution of the light to the final color
            R = 2 * L.dot(N) * N - L
            I = ka + kd * L.dot(N) + ks * (R.dot(V)) ** sh
            C += I * intersection.object.material.color * light.color
    return C


# function: shadow_test determines if there is an object between the light and the intersection studied
# if it is the case, it means this object prevents the light from reflecting on the intersection
#
# arguments:
# @param light: object from the Spotlight class
# @param scene: object from the Scene class
# @param intersection: object from the Intersection class
# @return: return a boolean
# True if there is a shadow
# False otherwise
def shadow_test(light, scene, intersection):
    O = light.position
    I = intersection.position
    OI = I - O
    ray = Ray(O, OI / OI.dot(OI))
    for object in scene.objects:
        # we don't consider the object of the intersection itself
        if object != intersection.object:
            j = intersect(object, ray)
            # if there is an intersection with another object
            if j != None:
                OJ = j.position - O
                di = OI.dot(ray.direction)
                dj = OJ.dot(ray.direction)
                # and if the other object is between the light and the intersection
                if dj < di:
                    # then there is a shadow
                    return True
    return False
