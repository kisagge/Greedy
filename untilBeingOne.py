TC = int(input())
ans = []
for tc in range(1, TC+1):
    k = "#" + str(tc) + " "
    N, K = map(int, input().split())

    result = 0

    while True:
        # (N==K 로 나누어 떨어지는 수 )가 될 때까지 1씩 빼기
        tg = (N // K) * K
        result += N - tg
        N = tg
        if N < K:
            break
        result += 1
        N //= K
    result += (N - 1)
    k += str(result)
    ans.append(k)
for e in ans:
    print(e)