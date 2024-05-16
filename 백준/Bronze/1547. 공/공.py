m = int(input())

index = 1
for i in range(m):
    a,b = map(int,input().split())

    if( a == index):
        index = b
    elif ( b == index):
        index = a

print(index)
