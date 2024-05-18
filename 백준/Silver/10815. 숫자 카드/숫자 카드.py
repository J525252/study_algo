import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split() ) )
N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split() ) )

for m in M_list:
    high, low = N-1, 0
    while True:
        if( high < low ):
            print(0, end = " ")
            break

        mid = int( (high + low ) / 2 )

        if (m == N_list[mid]):
            print(1, end = " ")
            break

        elif (m < N_list[mid]):
            high = mid-1
        elif (m > N_list[mid]):
            low = mid+1

