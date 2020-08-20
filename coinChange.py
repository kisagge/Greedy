n = int(input())
cnt = 0

lst = [500, 100, 50, 10]

for coin in lst:
    cnt += n // coin
    n %= coin

print(cnt)