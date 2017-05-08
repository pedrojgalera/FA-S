# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:49:35 2017

@author: pedrogalera
"""
from simulator import cell_cinetics_simulator
from sphere import sphere


# RADIUS OF DISTINCT AGENTS (nm)

XRN1 = 7.95*0.5
TFIIS = 4.66*0.5
CCR4 = 6.5*0.5
RNAPOLII = 15*0.5
GAL1GENE = 523.71*0.5
GAL1MRNA = 523.71*0.5
CELL = 4500*0.5

SPHERES = [sphere([300*i, -300*i, 300*i], 250) for i in range(50)]
BIG_CELL = cell_cinetics_simulator(CELL, SPHERES)
