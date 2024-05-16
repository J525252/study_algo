N=int(input())
yon=[]

for i in range(N):
    input_str=input()
    op=0
    cl=0
    a=True

    for char in input_str:
        if char=='(':
            op +=1
        elif char==')':
            cl +=1
            if cl>op:
                a=False
                break

    if a and op==cl:
        yon.append('YES')
    else:
        yon.append('NO')


print('\n'.join(yon) )