import string


fout = open("case.txt", "w")
for c in string.ascii_letters:
    print("s[i] == '"+ c +"' || ", file=fout, end=" ")
fout.close()