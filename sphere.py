# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:44:41 2017

@author: pedrogalera
"""
import numpy as np
from utils import euclidean_distance


class sphere(object):
    """The geometrical model of a n-dimensional sphere."""

    def __init__(self, center, radius, speed=None):
        """To define an sphere it is only neccesary the coordinates of the
        center and the radius of the sphere.
        """
        self.center = np.array(center)
        self.radius = radius
        self.speed = np.array(speed) if speed else np.zeros_like(self.center)

    def get_center(self):
        "Returns the center of the sphere."
        return self.center

    def get_radius(self):
        "Returns the radius of the sphere."
        return self.radius

    def get_mass(self):
        "Return a mass value computed from the radius."
        return (4 * np.pi * (self.get_radius()**3)) / 3

    def get_speed(self):
        "Return the speed of the sphere."
        return self.speed

    def set_center(self, new_center):
        "Sets a new center for the sphere"
        self.center = np.array(new_center)

    def set_radius(self, new_radius):
        "Sets a new radius for the sphere"
        self.radius = new_radius

    def set_speed(self, new_speed):
        "Sets a new speed for the sphere"
        self.speed = np.array(new_speed)

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

    def farthest_distance_to_origin(self):
        """Returns the distance from the origin to the farthest point of the
        sphere.
        """
        return np.linalg.norm(self.get_center()) + self.get_radius()

    def plot(self, ax):
        phi = np.linspace(0, 2 * np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        xm = self.get_radius() * np.outer(np.cos(phi), np.sin(theta)) + self.get_center()[0] * np.ones_like(np.outer(np.cos(phi), np.sin(theta)))
        ym = self.get_radius() * np.outer(np.sin(phi), np.sin(theta)) + self.get_center()[1] * np.ones_like(np.outer(np.cos(phi), np.sin(theta)))
        zm = self.get_radius() * np.outer(np.ones(np.size(phi)), np.cos(theta)) + self.get_center()[2] * np.ones_like(np.outer(np.cos(phi), np.sin(theta)))
        ax.plot_surface(xm, ym, zm)