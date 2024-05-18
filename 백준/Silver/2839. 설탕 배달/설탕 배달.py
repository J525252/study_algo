n = int(input())

cnt = 0
if( n < 5) and ( n != 3):
    cnt = -1

else:
    num = n //3
    for i in range(num +1):
        if( n % 5 == 0) or ( n == 0):
            cnt += n//5
            break
        n -= 3
        cnt += 1
    else:
        cnt = -1
print(cnt)

