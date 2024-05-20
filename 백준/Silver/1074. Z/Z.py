N, r, c = map(int, input().split())


cnt = 0
while True:
    if( N == 1):
        if( r == 0) and ( c == 0):
            cnt += 0
        elif( r == 0) and ( c== 1):
            cnt += 1
        elif( r == 1) and ( c == 0):
            cnt += 2
        elif( r == 1) and (c == 1):
            cnt += 3
        break

    mid = 2 ** (N - 1) - 1

    if( r > mid):
        cnt += ( mid+1 )*(mid+1)*2
        r -= (mid+1)

    if( c > mid):
        cnt += (mid+1)*(mid+1)
        c -= (mid+1)

    N -= 1

print(cnt)


