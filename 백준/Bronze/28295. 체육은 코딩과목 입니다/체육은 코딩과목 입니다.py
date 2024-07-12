
pos = 0

for _ in range(10):
    n = int(input())

    if( n == 1 ) :
        pos += 1
    elif ( n == 2) :
        pos += 2
    elif ( n == 3 ) :
        pos -= 1

    pos += 4
    pos = pos % 4


if( pos == 0):
    print('N')
elif( pos == 1):
    print('E')
elif( pos == 2):
    print('S')
elif( pos == 3):
    print('W')

