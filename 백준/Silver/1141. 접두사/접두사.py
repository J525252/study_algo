N = int(input())

s = [ input() for _ in range(N) ]

for i in range(N):
    for j in range(N):

        if( i == j):
            continue

        elif( len(s[i]) > len(s[j]) ):
            continue
        elif( s[j][: len(s[i] )] == s[i] ):
            s[i] = ',,,,,,'

print(len(s) - s.count(',,,,,,') )
