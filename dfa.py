# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:02:32 2017

@author: pedrogalera
"""

class DFA(object):
    """This class represent an instance of a particular deterministic finite
    automaton. It has all some of the most useful methods to create, modify, 
    and work with DFAs.
    """
    
    def __init__(self, states, inputs, transition_functions, initial_state):
        """A deterministic finite automaton is univoquely defined by a set of 
        possible states, a set of inputs that can be proccessed, a transition 
        function that maps the cartesian product of the set of states and the 
        set of inputs to the set of inputs, and initial state.
        """
        
        self.states = states
        self.inputs = inputs
        self.transition_functions = transition_functions
        self.initial_state = initial_state
        self.current_state = initial_state
    
#    def current_state(self):
#        """This method returns the current state of the authomata. """
#        return self.current_state or self.initial_state
        
    def next_state(self, given_input):
        """This method produces a change of state on the automaton for a given
        input.
        """
        self.current_state = self.transition_function(
            self.current_state,
            given_input
        )
        return self.current_state
