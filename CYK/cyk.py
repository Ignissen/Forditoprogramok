

class CYK:
    def __init__(self, rules):
        self.rules = rules
        self.cyk_array = []

    def validate(self, s):
        self.cyk_array = self.createMatrix(len(s))
        for i in range(len(s)):
            for j in range(len(self.rules)):
                if s[i] == self.rules[j][1]:
                    self.cyk_array[len(self.cyk_array) - 1 - i][i].append(self.rules[j][0])
        
        for k in range(len(self.cyk_array) - 2, -1, -1):
            print(k)
            j = 0
            for i in range(len(self.cyk_array) - k, -1, -1):
                for l in range(i + 1, len(self.cyk_array) - j):
                    for m in self.cyk_array[l][j]:
                        for n in self.cyk_array[i][len(self.cyk_array[i]) - (l - i)]:
                            print("mn=",m+n)
                            for o in range(len(self.rules)):
                                if m+n == self.rules[o][1]:
                                    self.cyk_array[i][j].append(self.rules[o][0])
                    if self.cyk_array[i][j] == []:
                        self.cyk_array[i][j].append("-")
                    
                j += 1
        
        return "S" in self.cyk_array[0][0]

    def createMatrix(self, n):
        arr = []
        for i in range(n):
            arr.append([])
            for j in range(n - i):
                arr[i].append([])
        return arr


    