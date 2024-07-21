import math
a, b, v = map(int, input().split())

v =  v - a
day = 1 + math.ceil( v/(a-b))


print(day)
