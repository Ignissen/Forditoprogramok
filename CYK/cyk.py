

class CYK:
    def __init__(self, rules):
        self.rules = rules

    def validate(self, s):
        cyk_array = self.createMatrix(len(s))
        for i in range(len(s)):
            for j in range(len(self.rules)):
                if s[i] == self.rules[j][1]:
                    cyk_array[len(cyk_array) - 1 - i][i].append(self.rules[j][0])
        
        for k in range(len(cyk_array) - 2, -1, -1):
            print("k=",k)
            j = 0
            for i in range(len(cyk_array) - k, -1, -1):
                print("i=",i)
                print("j=",j)
                for l in range(i + 1, len(cyk_array) - j):
                    print("l=",l)
                    for m in cyk_array[l][j]:
                        for n in cyk_array[k][len(cyk_array[k]) - l]:
                            print("mn=",m+n)
                            for o in range(len(self.rules)):
                                if m+n == self.rules[o][1]:
                                    cyk_array[i][j].append(self.rules[o][0])
                    if cyk_array[i][j] == []:
                        cyk_array[i][j].append("-")
                j += 1
            print(cyk_array)
        
        return "S" in cyk_array[0][0]

    def createMatrix(self, n):
        arr = []
        for i in range(n):
            arr.append([])
            for j in range(n - i):
                arr[i].append([])
        return arr


    