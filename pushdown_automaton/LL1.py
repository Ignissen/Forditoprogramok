from mystack import Stack

stack = Stack(["z0"])

#S->aS|bAc
#A->bAc|d

i = 0
be = "abdc"
stack.push("S")
while i < len(be):
    if stack.peep() == "z0":
        break
    if stack.peep() == "S" and be[i] == "a":
        stack.pop()
        stack.push("aS")
        i += 1
    elif stack.peep() == "S" and be[i] == "b":
        stack.pop()
        stack.push("bAc")
        i += 1
    elif stack.peep() == "A" and be[i] == "b":
        stack.pop()
        stack.push("bAc")
        i += 1
    elif stack.peep() == "A" and be[i] == "d":
        stack.pop()
        stack.push("d")
        i += 1
    elif stack.peep() == "a" and be[i] == "a":
        stack.pop()
        i -= 1
    elif stack.peep() == "b" and be[i] == "b":
        stack.pop()
        i -= 1
    elif stack.peep() == "c" and be[i] == "c":
        stack.pop()
        i -= 1
    elif stack.peep() == "d" and be[i] == "d":
        stack.pop()
        i -= 1
    else:
        print("Error")
        break
    print(stack.stack, stack.peep(), be[i], sep="\t")
    
