def solve():
    n = int(input())
    printresult = []

    for i in range(n):
        s = input()
        if (s.count('(') != s.count(')')):
            printresult.append("NO")
        else:
            countx = 0
            county = 0
            no = 0

            for j in range(len(s)):
                if (s[j] == '('):
                    countx += 1
                else:
                    county += 1

                if (countx < county):
                    no = 1

            if (no == 1):
                printresult.append("NO")
            else:
                printresult.append("YES")

    print('\n'.join(printresult))
    
    
solve()