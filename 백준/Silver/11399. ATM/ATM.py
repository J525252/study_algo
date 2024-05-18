N  = int(input())

time_list = list( map(int, input().split()) )
time_list.sort()

time = [t for t in time_list] 

for i in range( 1, len(time_list)):   ## time = 인당 인출하는데 필요한 시간
    time[i] = time[i-1] + time_list[i]
print( sum(time) )