

class Stack:
    def __init__(self, stack=[]):
        self.stack = stack
    
    def push(self, value):
        if len(value) == 1:
            self.stack.append(value)
        else:
            for c in value:
                self.stack.append(c)
    
    def peep(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()