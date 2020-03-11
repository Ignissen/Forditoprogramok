import sys
from cyk import CYK


if len(sys.argv) == 2:
    s = input("Elemzendő string: ")
elif len(sys.argv) == 3:
    s = sys.argv[2]
else:
    print("""Usage: \n
             python main.py rules.txt [string to analyze]
             """)
    sys.exit(0)

try:
    with open(sys.argv[1],"r") as fin:
        rules = fin.read().splitlines()
        for i in range(len(rules)):
            rules[i] = rules[i].split(sep=" ")
        
except FileNotFoundError:
    print("File not found: " + sys.argv[1])

asd = CYK(rules)
print(asd.validate(s))
for a in asd.cyk_array:
    print(a)
