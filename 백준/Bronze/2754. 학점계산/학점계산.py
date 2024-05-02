
s = input()

score = 4.3
alph = 'ABCD'

if( s == 'F'):
    score = 0.0

else:
    score = score - alph.index(s[0])

    if( s[1] == '0'):
        score -= 0.3
    elif ( s[1] == '-'):
        score -= 0.6

print(round(score, 1))

