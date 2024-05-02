n = int(input())
origin_n = n


i = 2
while True :

    if( n % i == 0):
        print(i)
        n = n/i
    else: i += 1

    if( n == 1 ) or ( i > n):
        break
