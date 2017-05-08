# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:46:23 2017

@author: pedrogalera
"""

import numpy as np


class id_generator(object):
    """Generator to create universal distinct ids."""

    def incremental_loop():
        n = 0
        while True:
            yield n
            n += 1

    i = incremental_loop()

    def __call__(self):
        return str(next(self.i))


def euclidean_distance(v1, v2):
    """Returns the euclidean distance between two points."""
    return np.linalg.norm(np.array(v1)-np.array(v2))


def elastic_collision(sphere1, sphere2):
    "Changes the speed of the spheres in an elastic collision."
    m1 = sphere1.get_mass()
    m2 = sphere2.get_mass()
    v1 = sphere1.get_speed()
    v2 = sphere2.get_speed()

    new_speed1 = ((m1-m2)*v1+2*m2*v2)/(m1+m2)
    new_speed2 = ((m2-m1)*v2+2*m1*v1)/(m1+m2)

    sphere1.set_speed(new_speed1)
    sphere2.set_speed(new_speed2)


def boundary_collision(sphere):
    """Update the speed of a given sphere colliding with a spheric wall
    centered on the origin.
    """
    v = sphere.get_speed()
    r = sphere.get_center()
    v_r = (np.dot(v, r)/(np.linalg.norm(r)**2)) * r
    speed_after_collision = v - 2 * v_r

    sphere.set_speed(speed_after_collision)


def move_sphere(sphere, timedelta):
    "Moves the sphere according to its speed and the time passed."
    r = sphere.get_center()
    v = sphere.get_speed()

    sphere.set_center(r+v*timedelta)


def time_space_precision(list_of_spheres, alpha):
    """Given a system configuration, calculates the interval of time that
    minimizes the error in the colision.
    """
    r = min([sphere.get_radius() for sphere in list_of_spheres])
    v = max([np.linalg.norm(sphere.get_speed()) for sphere in list_of_spheres])
    return alpha * r * 0.5 / v
