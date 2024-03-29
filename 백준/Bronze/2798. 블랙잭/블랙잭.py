N, M = map(int, input().split())
num_list = list( map(int, input().split()))

sum_list = []
for i in range(len(num_list) - 2 ):
    for j in range( i+1, len(num_list) - 1):
        for k in range( j+1, len(num_list) ):
            sum_list.append(num_list[i] + num_list[j] + num_list[k])

dif_list = [ M-s if(M - s >= 0) else M  for s in sum_list]

print( sum_list[ dif_list.index( min(dif_list) ) ] )