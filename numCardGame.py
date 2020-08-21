TC = int(input())
ans = []
for tc in range(1, TC+1):
    k = "#" + str(tc) + " "
    N, M = map(int, input().split())

    result = 0
    for i in range(N):
        data = list(map(int, input().split()))
        
        min_value = min(data)

        result = max(result, min_value)
    k += str(result)
    ans.append(k)
for e in ans:
    print(e)