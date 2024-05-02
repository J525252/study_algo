hour, minut = map(int, input().split())
time = int(input())
minut += time

while True:

    if( 0 <= minut < 60):
        print( hour, minut)
        break

    minut -= 60
    hour += 1

    if( hour >= 24):
        hour -= 24

