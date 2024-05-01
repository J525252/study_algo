
n = int(input())

stand = 55      #1+2+3+...+9+10
count = 0

for i in range(n//100 +1 ):
    if( n < 0) :
        break

    count += 10
    n -= stand + 100*i

n = (-1)*n
for j in range( 10):
    if( n == 0):
        break
    elif ( n <= 10*(i+1) -j):
        count -= 1
        break
    else :
        n -= 10*(i+1) -j
        count -= 1

print(count)

