
n = int(input())   # 명령어 갯수

stack = []
count = 0
printresult = []

for i in range(n):
    command= input()
    if( command[:4] == "push"):  #push X: 정수 X를 스택에 넣는 명령어
        stack.append(int(command[5:]))
        count += 1
    elif( command == "pop"):  #스택에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
        if(count == 0):        # 만약 스택에 들어있는 정수가 없는경우 : -1출력
            printresult.append("-1")
        else:
            printresult.append(str(stack[0]))
            stack.pop(0)
            count -= 1
    elif( command == "size"):   #스택에 들어있는 정수의 개수를 출력
        printresult.append(str(count))
    elif ( command == "empty"):
        if(count == 0):          #스택이 비어있으면 1출력
            printresult.append("1")
        else:
            printresult.append("0") # 아니면 0출력
    elif( command == "front"):   # 큐의 가장 앞에 있는 정수를 출력
        if( count == 0):        # 만약 큐에 들어있는 정수가 없는 경우에는 -1
            printresult.append("-1")
        else:
            printresult.append(str(stack[0]))
    elif( command == "back"): #큐의 가장 뒤에 있는 정수를 출력
        if( count == 0 ):       #먄약 큐에 들어있는 정수가 없는 경우에는 -1
            printresult.append("-1")
        else:
            printresult.append(str(stack[-1]))

print('\n'.join(printresult))