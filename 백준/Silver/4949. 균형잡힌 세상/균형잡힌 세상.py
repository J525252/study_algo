brake = '([)]'
while True:
    s = input()
    stack = [0]
    if( s == '.'):
        break
    if( ( s.count("(") + s.count("[") ) != ( s.count(")") + s.count("]") )):
        print('no')
        continue

    for si in s :
        if (si == "(") or (si == "["):
            stack.append(si)
        elif (si == ")") and (stack[-1] == "("):
            stack.pop()
        elif (si == "]") and (stack[-1] == "["):
            stack.pop()
        elif (brake.find(si) != -1):
            print('no')
            break
    else:
        print('yes')

