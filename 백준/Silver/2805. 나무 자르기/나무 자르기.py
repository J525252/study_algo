N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

low, high = 0, max(tree_list)
while True:
    mid = (low + high) // 2

    if( low > high ):
        print(mid)
        break
        
    parts = [ (tree - mid)  for tree in tree_list if(tree-mid) > 0]  ## 얻은 나무들 길이 list
    if( sum(parts) == M):
        print(mid)
        break
    elif( sum(parts) > M ): ## 얻은 나무가 원하는 나무(M)보다 클때
        low = mid + 1
    elif( sum(parts) < M ):
        high = mid - 1

