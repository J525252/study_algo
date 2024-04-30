N = int(input())

num = [ int(input() ) for _ in range(N) ]

## O(n^2)
for i in range(N):
    for j in range(i, N):
        if( num[i] > num[j] ):
            num[i], num[j] = num[j], num[i]

for n in num:
    print(n)