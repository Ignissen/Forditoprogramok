from mystack import Stack

class PusdownAutomaton:
    def __init__(self, terminals, nonterminals, stack, state_transitions, start_state, accepting_states):
        self.terminals = terminals
        self.nonterminals = nonterminals
        self.state_transitions = state_transitions
        self.accepting_states = accepting_states
        self.stack = stack
        self.state = self.start_state = start_state

    def validate(self, s=""):
        pass
