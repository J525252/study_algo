while True:
    num = int(input())
    num_reverse = []

    if( num == 0) :
        break;

    num_spell = list( str(num))
    for i in range( 1, len(num_spell) +1):
        num_reverse.append(num_spell[-i])

    for i in range( len(num_spell) ):
        if( num_reverse[i] != num_spell[i]):
            print("no")
            break;
    else:
        print("yes")