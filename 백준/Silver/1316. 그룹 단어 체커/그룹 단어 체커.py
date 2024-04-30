def solve():
    n = int(input())
    count = n
    for i in range(n):
        s = input()
        j = 0
        out = 0
        while (j < len(s) - 1):
            r = s.count(s[j])
            for k in range(1, r):
                if (s[j] != s[j + k]):
                    out += 1
            if (out != 0):
                count -= 1
                break
            j += r
    print(count)


solve()