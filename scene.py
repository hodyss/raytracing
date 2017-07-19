# class: Sphere
# these objects represent spheres in the scene
# they are defined by their center, their radius and their material
# @param center: a 1x3 array which indicates the position of the center
# @param rayon: a positive real number which is the radius of the sphere
# @param materiel: object from the Material class
class Sphere:
    def __init__(self, center, rayon, material):
        self.center = center
        self.rayon = rayon
        self.material = material


# class: Scene
# an object which contains every element of the scene to render: objects and lights
# @attribute objects: a list of the different objects present in the scene
# here, objects are from the Sphere class or the Triangle class
# @attribute lights: a list of the different lights present in the scene
# lights are objects from the Spotlight class
class Scene:
    def __init__(self):
        self.objects = []
        self.lights = []

    # method add_object: add the given object to the attribute objects
    # @argument o: the given object to add
    def add_object(self, o):
        self.objects.append(o)

    # method add_light: add the given light to the attribute lights
    # @argument l: the given light to add
    def add_light(self, l):
        self.lights.append(l)


# class: Material
# each object contain all the properties of the material which constitute objects (Sphere or Triangle)
# @param color: a 1x3 array which contains the RGB components of the color of the material
# @param ambiant: a real number between 0 and 1
# it is the ambiant reflection constant of the material, in the Phong model
# @param diffuse: a real number between 0 and 1
# it is the diffuse reflection constant of the material, in the Phong model
# @param specular: a real number between 0 and 1
# it is the specular reflection constant of the material, in the Phong model
# @param shininess: a real number greater or equal to 1 (generally between 1 and 50)
# it is the shininess constant of the material, in the Phong model
# @param reflection: a real number between 0 and 1
# it represents the proportion of light which is reflected from other objects by this material
class Material:
    def __init__(self, color, ambiant, diffuse, specular, shininess, reflection):
        self.color = color
        self.ambiant = ambiant
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.reflection = reflection


# class: triangle
# represents triangles in the scene
# @param v0: a 1x3 array which contains the coordinates of the first point which defines a triangle
# @param v1: a 1x3 array which contains the coordinates of the second point which defines a triangle
# @param v2: a 1x3 array which contains the coordinates of the third point which defines a triangle
# @param material: object from the Material class
class Triangle:
    def __init__(self, v0, v1, v2, material):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.material = material
