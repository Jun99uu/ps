import sys
input = sys.stdin.readline

n = int(input().rstrip())
res = 0
while 0 < n:
    if n % 5 == 0:
        res += n // 5
        n %= 5
        break
    n -= 3
    res += 1

if n == 0:
    print(res)
else:
    print(-1)