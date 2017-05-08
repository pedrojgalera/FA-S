# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:02:32 2017

@author: pedrogalera
"""


class finiteAutomaton(object):
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
        if initial_state in states:
            self.initial_state = initial_state
            self.current_state = initial_state
        else:
            raise('initial state must be a valid state of the automaton')

    def __call__(self, *args, **kwargs):
        self.perform_transition(*args, **kwargs)

    def _add_new_states(self, *args):
        """Adds new statesFA to the finite automaton."""
        for state in args:
            self.states.add(state)

    def _add_new_inputs(self, *args):
        """Adds new inputs to the finite automaton."""
        for new_input in args:
            self.inputs.add(new_input)

    def _modify_transition_function(self, state_input_tuple, state):
        """Add or modify the transition function."""
        domain_state, domain_input = state_input_tuple
        if domain_state in self.states and domain_input in self.inputs:
            self.transition_function[state_input_tuple] = state
        else:
            raise Exception("""Transition function must be defined in the
            specific domain of the states and inputs""")

    def perform_transition(self, given_input):
        """This method performs the change of state given an input."""
        try:
            self.current_state = self.transition_function[(
                self.current_state,
                given_input
            )]
        except:
            raise Exception(
                "The current state {} cannot proccess the input {}".
                format(self.current_state, given_input))


class extendedFiniteAutomaton(object):
    pass


class molecularFiniteAutomaton(object):
    pass


states = ['s1', 's2', 's3']
inputs = ['a', 'b', 'c', 'e1', 'e2']
transition_function = {
    ('s1', 'a'): 's2',
    ('s2', 'e1'): 's1',
    ('s2', 'b'): 's3',
    ('s3', 'e2'): 's2',
    ('s3', 'c'): 's1',
}
ex = finiteAutomaton(set(states), set(inputs), transition_function, 's1')

#biostates = ['G+PC', 'G', 'GP', 'GX', 'BLOQUEO']
#bioinputs = [
#    'se adiere polimerasa',
#    'se adiere polimerasa con Ccr4',
#    'se']
