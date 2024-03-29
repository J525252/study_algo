n = int(input())

stack = []
count = 0
printresult = []

for i in range(n):
    command= input()
    if( command[:4] == "push"):
        stack.append(int(command[5:]))
        count += 1
    elif( command == "pop"):
        if(count == 0):
            printresult.append("-1")
        else:
            printresult.append(str(stack[-1]))
            stack.pop()
            count -= 1
    elif( command == "size"):
        printresult.append(str(count))
    elif ( command == "empty"):
        if(count == 0):
            printresult.append("1")
        else:
            printresult.append("0")
    elif ( command == "top"):
        if( count == 0):
            printresult.append("-1")
        else:
            printresult.append(str(stack[-1]))


print('\n'.join(printresult))