# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:23:37 2017

@author: pedrogalera
"""
import numpy as np
from random import shuffle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.show()

# RADIUS OF DISTINCT AGENTS (nm)

XRN1 = 7.95*0.5
TFIIS = 4.66*0.5
CCR4 = 6.5*0.5
RNAPOLII = 15*0.5
GAL1GENE = 523.71*0.5
GAL1MRNA = 523.71*0.5
CELL = 4500*0.5


def euclidean_distance(v1, v2):
    """Returns the euclidean distance between two points"""
    return np.linalg.norm(np.array(v1)-np.array(v2))


def elastic_collision(sphere1, sphere2):
    "Changes the speed of the spheres in an elastic collision"

    m1 = sphere1.get_mass()
    m2 = sphere2.get_mass()
    v1 = sphere1.get_speed()
    v2 = sphere2.get_speed()

    new_speed1 = ((m1-m2)*v1+2*m2*v2)/(m1+m2)
    new_speed2 = ((m2-m1)*v2+2*m1*v1)/(m1+m2)

    sphere1.set_speed(new_speed1)
    sphere2.set_speed(new_speed2)


def boundary_collision(sphere):
    v = sphere.get_speed()
    r = sphere.get_center()
    v_r = (np.dot(v, r)/(np.norm(r)**2)) * r
    speed_after_collision = v - 2 * v_r

    sphere.set_speed(speed_after_collision)


def move_sphere(sphere, timedelta):
    "Moves the sphere according to its speed and the time passed"
    r = sphere.get_center()
    v = sphere.get_speed()

    sphere.set_center(r+v*timedelta)


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

    def plot(self):
        phi = np.linspace(0, 2 * np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        xm = self.get_radius() * np.outer(np.cos(phi), np.sin(theta)) + self.get_center()[0] * np.ones_like(np.outer(np.cos(phi), np.sin(theta)))
        ym = self.get_radius() * np.outer(np.sin(phi), np.sin(theta)) + self.get_center()[1] * np.ones_like(np.outer(np.cos(phi), np.sin(theta)))
        zm = self.get_radius() * np.outer(np.ones(np.size(phi)), np.cos(theta)) + self.get_center()[2] * np.ones_like(np.outer(np.cos(phi), np.sin(theta)))
        ax.plot_surface(xm, ym, zm)


class cell_cinetics_simulator():
    "To simulate a cell"

    def __init__(self, radius, spheres):
        self.cell_center = np.array([0, 0, 0])
        self.cell_radius = CELL
        self.spheres = list(spheres)

    def next_frame(self, timedelta):
        # Boundary collisions
        for sphere in self.spheres:
            if np.norm(sphere.get_center()) + sphere.get_radius > self.cell_radius:
                boundary_collision(sphere)

        # Collision between spheres
        for i, sphere1 in enumerate(self.spheres):
            for sphere2 in self.spheres()[i+1:]:
                if sphere1.intersects(sphere2):
                    elastic_collision(sphere1, sphere2)

        # Move spheres
        for sphere in self.spheres:
            move_sphere(timedelta)

        # Shuffle spheres
        shuffle(self.spheres)

        def save(self):
            pass

        def plot():
            for sphere in self.spheres:
                sphere.plot()









