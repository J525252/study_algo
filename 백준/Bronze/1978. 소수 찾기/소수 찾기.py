N = int(input())
num_list = list(map(int, input().split()))

cnt = 0  #소수 갯수
for n in num_list:
    t = 1
    if( n == 1):
        continue

    for d in range(2, n):
        if( n%d ==0):
            t = 0
    if( t == 1):
        cnt += 1

print(cnt)