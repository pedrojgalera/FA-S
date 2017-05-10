# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:49:35 2017

@author: pedrogalera
"""
from simulator import cell_cinetics_simulator
from sphere import create_collection_of_agents

# NUMBER OF AGENTS
NUMBER_OF_XRN1 = 200
NUMBER_OF_CCR4 = 200
NUMBER_OF_TFIIS = 20
NUMBER_OF_POLII = 3


# RADIUS OF DISTINCT AGENTS (nm)
XRN1_RADIUS = 7.95*0.5
TFIIS_RADIUS = 4.66*0.5
CCR4_RADIUS = 6.5*0.5
RNAPOLII_RADIUS = 15*0.5
GAL1GENE_RADIUS = 523.71*0.5
GAL1MRNA_RADIUS = 523.71*0.5
CELL_RADIUS = 4500*0.5


# CREATING AGENTS
def create_agents():
    xrn1_agents = create_collection_of_agents(
                NUMBER_OF_XRN1, 'xrn1', XRN1_RADIUS)
    ccr4_agents = create_collection_of_agents(
                NUMBER_OF_CCR4, 'ccr4', CCR4_RADIUS)
    tfiis_agents = create_collection_of_agents(
                NUMBER_OF_TFIIS, 'tfIIs', TFIIS_RADIUS)
    polII_agents = create_collection_of_agents(
                NUMBER_OF_POLII, 'polII', RNAPOLII_RADIUS)

    return xrn1_agents, ccr4_agents, tfiis_agents, polII_agents

ccs = cell_cinetics_simulator(CELL_RADIUS, GAL1GENE_RADIUS, sum(create_agents(),[]))

while True:
    a = cell_cinetics_simulator(CELL_RADIUS, GAL1GENE_RADIUS, sum(create_agents(),[]))
    a.run()
