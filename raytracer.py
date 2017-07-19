from light import *


# function: trace_ray finds whether the ray intersects an object or not
# if not, it returns a black pixel
# if it intersects one or several objects, the function finds the closest intersection
# then it uses the Phong model and reflexions from other objects to calculate the color of the pixel
#
# @param ray: object from the Ray class
# @param scene: object from the Scene class
# @param k: a counter which indicates how many times the function has been called for calculating a reflection
# we consider that a ray of light which has been reflected more than 20 times will not have any impact on the
# final intensity. So the recursion stops when k > 20.
# @return: returns a 1x3 array which indicates the final color of the pixel
def trace_ray(ray, scene, k=0):
    # initialize the research of an intersection
    closest_intersection = None
    d_closest_intersection = float('inf')
    # the recursion base case:
    # we have consider enough reflexions
    if k > 20:
        return np.array([0, 0, 0])
    # look if there is an intersection for every object of the scene
    for object in scene.objects:
        i = intersect(object, ray)
        # if there is an intersection
        if i != None:
            d = i.position - ray.starting_point
            # and if it is closest than the previous one
            if np.sqrt(d.dot(d)) < d_closest_intersection:
                # then say that it is the current closest intersection
                d_closest_intersection = np.sqrt(d.dot(d))
                closest_intersection = i
    # if there is no intersection at all
    if closest_intersection == None:
        # the pixel is black
        return np.array([0, 0, 0])
    # else, there is an object which reflects light
    r = closest_intersection.object.material.reflection
    D = ray.direction
    P = closest_intersection.position
    n = closest_intersection.normal
    # determine the direction of reflection, which is the symmetric of the ray under the normal n
    D = D - 2 * (D.dot(n)) * n
    f_ray = Ray(P, D / np.sqrt(D.dot(D)))
    # a part of the light comes from the light sources (Phong model)
    # the other part car come from the reflected light of another object coming from the direction of reflexion D
    # and the relative proportion is given by the reflection coefficient
    return (1 - r) * phong_illuminate(scene, closest_intersection, ray.starting_point) + r * trace_ray(f_ray, scene,
                                                                                                       k + 1)


# function: raytracer_render render the scene and creates the 3D image
# it uses the trace_ray function for every pixel of the image
# @param camera: object from the Camera class
# @param scene: object from the Scene class
# @return: returns a nrows x ncols array of 1x3 arrays
# each 1x3 array contains the RGB components of the pixel color
def raytracer_render(camera, scene):
    # define the dimensions of the picture
    nrows = camera.image_nrows
    ncols = camera.image_ncols
    # initialise the picture as a black one
    rendering = np.zeros((nrows, ncols, 3))
    # run through the picture to color every pixel
    # begin with the rows to fit with the numpy array format
    for i in range(nrows):
        # then run through the columns
        for j in range(ncols):
            # and calculate the color of the pixel
            rendering[i][j] = np.clip(trace_ray(camera.ray_at(i, j), scene), 0, 1)
    return rendering
