# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:23:37 2017

@author: pedrogalera
"""
import numpy as np


def euclidean_distance(v1, v2):
    """Returns the euclidean distance between two points"""
    return np.linalg.norm(np.array(v1)-np.array(v2))


class sphere(object):
    """The geometrical model of a n-dimensional sphere."""

    def __init__(self, center, radius):
        """To define an sphere it is only neccesary the coordinates of the
        center and the radius of the sphere.
        """
        self.center = np.array(center)
        self.radius = radius

    def get_center(self):
        "Returns the center of the sphere."
        return self.center

    def get_radius(self):
        "Returns the radius of the sphere."
        return self.radius

    def get_mass(self):
        "Return a mass value computed from the radius"
        return (4 * np.pi * (self.get_radius()**3)) / 3

    def set_center(self, new_center):
        "Sets a new center for the sphere"
        self.center = np.array(new_center)

    def set_radius(self, new_radius):
        "Sets a new radius for the sphere"
        self.radius = new_radius

    def contains(self, point):
        """Given a point returns true if it is inside the sphere,
        false otherwise.
        """
        return np.linalg.norm(self.center-np.array(point)) <= self.get_radius()

    def intersects(self, other_sphere):
        """Returns true if the sphere is intersecting with another sphere,
        false otherwise.
        """
        d = euclidean_distance(self.get_center(), other_sphere.get_center())
        return d <= self.get_radius() + other_sphere.get_radius()
