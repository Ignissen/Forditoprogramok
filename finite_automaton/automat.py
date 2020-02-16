class ItemNotFound(Exception):
    pass

class Automat:
    def __init__(self, alphabet, state_transitions, start_state, accepting_states):
        self.alphabet = alphabet
        self.state_transitions = state_transitions
        self.start_state = self.state = start_state
        self.accepting_states = accepting_states

    def validate(self, s):
        self.state = self.start_state
        for c in s:
            try:
                alph = self.findAlph(c)
                self.state = self.state_transitions[self.state][alph]
                if self.state == 0:
                    return False
            except ItemNotFound:
                return False
        return self.isInAcceptingState()

    def getState(self):
        return self.state
    
    def findAlph(self, c):
        for i in range(len(self.alphabet)):
            if self.alphabet[i] == c:
                return i
        raise ItemNotFound        
        

    def isInAcceptingState(self):
        return self.state in self.accepting_states