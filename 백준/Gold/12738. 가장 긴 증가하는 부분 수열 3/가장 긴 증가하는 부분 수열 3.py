n = int(input())
v = list(map(int, input().split()))

dp = [v[0]]
for i in range(1, n):
    if dp[-1] < v[i]:
        dp.append(v[i])
        continue
    pos = 0
    left, right = 0, len(dp) - 1
    while left <= right:
        mid = (left + right) // 2
        if dp[mid] < v[i]:
            pos = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    dp[pos] = v[i]

print(len(dp))

