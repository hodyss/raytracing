import numpy as np
from scene import *


# class: Intersection
# these objects gather all the information needed about the intersection between a ray and an object
# @param position: a 1x3 array which contain the coordinates of the intersection
# @param normal: a 1x3 normalised array which is the normal to the surface of the object at the intersection point
# @param object: the object which was intersected by the ray. It is a sphere or a triangle which belongs to the scene.
class Intersection:
    def __init__(self, position, normal, object):
        self.position = position
        self.normal = normal
        self.object = object


# function: intersect find if there is an intersection between the object and the ray
# if there is, it returns the intersection found
# it uses geometry and vectors to calculate if there is an intersection
# @param object: object from the Sphere class or the Triangle class
# @param ray: object from the Ray class
# @return: returns None if there is no intersection, or an object from the Intersection class if there is
def intersect(object, ray):
    # different algorithms depending on the type of the object
    # if it is a sphere:
    if type(object) is Sphere:
        # name the key elements:
        O = ray.starting_point
        C = object.center
        D = ray.direction
        # normalise:
        I = D / np.sqrt(D.dot(D))
        CO = O - C
        # calculate the projection of the vector between C and O onto the direction of the ray
        # it should be < 0 if the intersection exists, since the ray is a half-line and so doesn't go backward
        L_CO = I.dot(CO)
        # the following comments are geometrical explanations of the calculations, they can be skipped
        # to find the intersection, we have to resolve the following quadratic formula in x:
        # x ** 2 + 2*I.dot(CO) * x + CO.dot(CO) - object.rayon ** 2 = 0
        # where x is the distance between the intersection point P and O on the ray line: P = O + x * I
        #
        # this equation is obtained by writing that P belongs to the ray and the sphere:
        # (O + x * I - C)*(O + x * I - C) = object.rayon ** 2 (sphere equation)
        #
        # we need to calculate the discriminant Discr = 4 * L_CO ** 2 - 4 * ( CO.dot(CO) - object.rayon ** 2 )
        # and find its sign in order to know if there is a solution
        # we will focus to Delta = Discr / 4
        #
        # Delta represents the difference between the square of the sphere radius (object.rayon ** 2)
        # and the distance between the sphere center and the ray (CO.dot(CO) - L_CO ** 2, according to Pythagoras)
        Delta = L_CO ** 2 - CO.dot(CO) + object.rayon ** 2
        # if it is < 0, it means the distance center - ray is greater than the radius, so there is no intersection
        if Delta < 0:
            return None
        # else, is Delta = 0, it means the ray intersects the edge of the sphere, at only one point
        elif Delta == 0:
            # if L_CO < 0, then the intersection exists
            # the criteria is L_CO <= 10 ** -6 to prevent the ray from intersecting the object it is coming from
            # when it is a ray reflected over several object in the trace_ray function (raytracer.py)
            if L_CO <= 10 ** -6:
                # the intersection point is on the half-line described by the ray
                # we can use the equation of a line through O directed by the vector I
                P = O - L_CO * I
                # the normal of the intersection is obtained by normalising the radius vector
                # from the center of the sphere to the intersection
                N = (P - C) / np.sqrt((P - C).dot(P - C))
                return Intersection(P, N, object)
            # if L_CO > 0, the intersection would be "behind" the beginning of the ray, so it doesn't exist
            else:
                return None
        # else, Delta > 0, which mean the ray goes through the sphere and intersect it two times
        # we have to find out which intersection is the first one (and so the one which is really seen)
        else:
            # we only need to find the distance d1 and d2 between the intersections and O
            # then we just have to take the smaller number between d1 and d2 to find the first intersection
            # d1 and d2 are the roots of the quadratic formula we saw before
            # if the smaller distance is positive, it is the one of first intersection
            # once again, it has to be big enough to be sure the ray doesn't intersect the object it is coming from
            if - L_CO - np.sqrt(Delta) >= 10 ** -6:
                d = - L_CO - np.sqrt(Delta)
                # calculate the intersection point P:
                P = O + d * I
                # and the normal of the intersection:
                N = (P - C) / np.sqrt((P - C).dot(P - C))
                return Intersection(P, N, object)
            # else, it means the smaller distance is negative or too small: it is not an intersection
            # if the bigger distance is positive and big enough, it is the distance to the intersection point
            elif - L_CO + np.sqrt(Delta) >= 10 ** -6:
                d = - L_CO + np.sqrt(Delta)
                P = O + d * I
                N = (C - P) / np.sqrt((P - C).dot(P - C))
                return Intersection(P, N, object)
            # else, it means both distances are negative or too small
            # the sphere is behind the starting point or is the object the ray is coming from
            # there is no intersection in that case
            else:
                return None
    # in that second part, we will deal with triangles
    # it is quite the same geometrical ideas, so the explanations will be shorter
    if type(object) is Triangle:
        A = object.v0
        B = object.v1
        C = object.v2
        O = ray.starting_point
        D = ray.direction
        I = D / np.sqrt(D.dot(D))
        AB = B - A
        AC = C - A
        # the following cross product gives a vector normal to the plan of the triangle
        crossp = np.cross(AB, AC)
        # calculate det, the projection of the triangle normal onto the ray direction:
        det = crossp.dot(D)
        if abs(det) < 10 ** -6:
            # D is parallel to the triangle: no intersection
            return None
        prenormal = -det * crossp
        # it gives the orientation of the triangle normal as opposed to the one of the ray
        N = prenormal / np.sqrt(prenormal.dot(prenormal))
        # calculate d, the distance between the starting point of the ray and the intersection:
        d = ((A - O).dot(N)) / (I.dot(N))
        if d < 10 ** -6:
            # the intersection is behind the starting point
            return None
        P = O + d * I
        for i in range(3):
            if np.cross(A - B, P - B).dot(np.cross(C - B, P - B)) > 0:
                # BP is not between BA and BC: P is out of the triangle
                return None
            A, B, C = B, C, A
            # permutation of the triangle vertices for the calculation
        return Intersection(P, N, object)
