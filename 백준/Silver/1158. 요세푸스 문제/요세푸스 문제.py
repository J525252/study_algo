N, K = map(int, input().split())

people = [i for i in range(1, N+1) ]
idx = 0

print('<', end = "")
while True:
    if( len(people) == 1):
        print(f'{people[-1]}>')
        break


    idx += (K - 1)
    if (idx >= len(people) ):
        idx = idx % len(people)

    print(people[idx], end = ", ")
    people.pop(idx)


