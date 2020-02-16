from automat import *
import string
class DomolAutomat(Automat):
    def __init__(self, alphabet, state_transitions, start_state, accepting_states, backup, read):
        super().__init__(alphabet, state_transitions, start_state, accepting_states)
        self.backup = backup
        self.read = read 
        self.lexical_formula = ""

    def validate(self, s):
        self.state = self.start_state
        i = 0
        while i < len(s):
            #print(self.state, end=" ")
            #print(self.state_transitions[self.state], end=" ")
            try:
                alph = ""
                Type = "other"
                if self.backup[self.state]:
                    i -= 1
                elif self.read[self.state]:
                    #print(s[i], end="")
                    if s[i] in string.digits:
                        Type = "number"
                    elif s[i] in string.ascii_letters or s[i] in "áéíóöőúüűÁÉÍÓÖŐÚÜŰ":
                        Type = "letter"
                    elif s[i] == "{":
                        Type = "{"
                    elif s[i] == "}":
                        Type = "}"
                    elif s[i] == "(":
                        Type = "("
                    elif s[i] == "*":
                        Type = "*"
                    elif s[i] == ")":
                        Type = ")"
                    elif s[i] == ":":
                        Type = ":"
                    elif s[i] == "=":
                        Type = "="
                    elif s[i] == "<":
                        Type = "<"
                    elif s[i] == ">":
                        Type = ">"
                    elif s[i] == " ":
                        Type = "space"
                    elif s[i] == "$":
                        Type = "$"
                    else:
                        Type = "other"
                    i += 1

                alph = self.findAlph(Type)
                if self.state == 3 and self.state_transitions[self.state][alph] == 1:
                    #print("<azonosító>", end="")
                    self.lexical_formula += "<azonosító>"
                elif self.state == 5 and self.state_transitions[self.state][alph] == 1:
                    #print("<szám>", end="")
                    self.lexical_formula += "<szám>"
                elif self.state == 7 and self.state_transitions[self.state][alph] == 1:
                    #print(f"<{{}} komment>", end="")
                    self.lexical_formula += f"<{{}} komment>"
                elif self.state == 11 and self.state_transitions[self.state][alph] == 1:
                    #print("<() komment>", end="")
                    self.lexical_formula += "<() komment>"
                elif self.state == 13 and self.state_transitions[self.state][alph] == 1:
                    #print("<:= token>", end="")
                    self.lexical_formula += "<:= token>"
                elif self.state == 15 and self.state_transitions[self.state][alph] == 1:
                    #print("<<= token>", end="")
                    self.lexical_formula += "<<= token>"
                elif self.state == 16 and self.state_transitions[self.state][alph] == 1:
                    #print("<<> token>", end="")
                    self.lexical_formula += "<<> token>"
                elif self.state == 18 and self.state_transitions[self.state][alph] == 1:
                    #print("<>= token>", end="")
                    self.lexical_formula += "<>= token>"
                self.state = self.state_transitions[self.state][alph]
                if self.state == 21:
                    #print("<$(program vége) token>")
                    self.lexical_formula += "<$(program vége) token>"
                if self.state == 0:
                    return False
            except ItemNotFound:
                return False
            #print()
        return self.isInAcceptingState()

    def getLexicalFormula(self):
        return self.lexical_formula