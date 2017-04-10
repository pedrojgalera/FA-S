# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:02:32 2017

@author: pedrogalera
"""
class FA(object):
    """This class represent an instance of a particular deterministic finite
    automaton. It has all some of the most useful methods to create, modify, 
    and work with DFAs.
    """
    
    def __init__(self, states=set(), inputs=set(), transition_function={}, 
                 initial_state=None):
        """A deterministic finite automaton is univoquely defined by a set of 
        possible states, a set of inputs that can be proccessed, a transition 
        function that maps the cartesian product of the set of states and the 
        set of inputs to the set of inputs, and initial state.
        """
        
        self.states = states
        self.inputs = inputs
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.current_state = initial_state
    
#    def current_state(self):
#        """This method returns the current state of the authomata. """
#        return self.current_state or self.initial_state

    def _add_new_states(self, *args):
        """Adds new states to the finite automaton. """        
        for state in args:        
            self.states.add(state)
    
    def _add_new_inputs(self, *args):
        """Adds new inputs to the finite automaton. """
        for new_input in args:
            self.inputs.add(new_input)
        
    def _modify_transition_function(self, state_input_tuple, state):
        """Add or modify the transition function """
        domain_state, domain_input = state_input_tuple
        if domain_state in self.states and domain_input in self.inputs:
            self.transition_function[state_input_tuple] = state
#            TODO: decir error si hay error
                
    def perform_transition(self, given_input):
        """This method performs the change of state given an input. """
        try:
            self.current_state = self.transition_function[(
                self.current_state,
                given_input
            )]
        except:
            raise("The state \'{}\' cannot proccess the input \'{}\'".format(
                self.current_state,
                given_input
            ))
            
