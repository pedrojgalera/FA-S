# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:23:37 2017

@author: pedrogalera
"""
import csv
import numpy as np
from random import shuffle
from utils import boundary_collision, elastic_collision, new_number


class cell_cinetics_simulator(object):
    "To simulate a cell"

    def __init__(self, cell_radius, nucleus_radius, spheres):
        self.cell_center = np.array([0, 0, 0])
        self.cell_radius = cell_radius
        self.nucleus_radius = nucleus_radius
        self.spheres = list(spheres)
        self.time = 0
        self.file = 'sim'+str(new_number())

    def set_in_random_position(self, sphere):
        "Set the spheres randomly inside the cell. "
        phi = np.random.uniform(0, 2 * np.pi)
        theta = np.random.uniform(0, np.pi)
        radius = np.random.uniform(0, self.cell_radius - sphere.get_radius())
        x = radius * np.cos(phi) * np.sin(theta)
        y = radius * np.sin(phi) * np.sin(theta)
        z = radius * np.cos(theta)
        sphere.set_center([x, y, z])

    def initialize_positions(self):
        "Hay que afinar esto"
        for sphere in self.spheres:
            self.set_in_random_position(sphere)

    def initialize_speeds(self):
        mean = [0, 0, 0]
        cov = [[100, 0, 0], [0, 100, 0], [0, 0, 100]]
        for sphere in self.spheres:
            sphere.set_speed(np.random.multivariate_normal(mean, cov))

    def next_frame(self, timedelta):
#        collisions = 0
        # Boundary collisions
        for sphere in self.spheres:

            if sphere.farthest_distance_to_origin() > self.cell_radius:
                boundary_collision(sphere)
#                collisions += 1

        # Collision between spheres

        for i, sphere1 in enumerate(self.spheres):
            for sphere2 in self.spheres[i+1:]:
                if sphere1.intersects(sphere2):
                    elastic_collision(sphere1, sphere2)
#                    collisions += 1

        # Move spheres
        for sphere in self.spheres:
            sphere.move(timedelta)

        # Shuffle spheres
        shuffle(self.spheres)
#        print('collisions: '+str(collisions))

    def save(self):
        time = self.time
        data = []
        for sphere in self.spheres:
            data.append([sphere.id,
                         sphere.name,
                         sphere.get_center(),
                         sphere.get_radius()])
        with open('./data/{}.csv'.format(self.file), 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([time]+data)

    def run(self):
        self.initialize_positions()
        self.initialize_speeds()
        while self.time < 10000:
            self.next_frame(1)
            self.time += 1
            self.save()
#            print(self.time)
