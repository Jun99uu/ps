import sys
input = sys.stdin.readline
INF = sys.maxsize

n, k = list(map(int, input().rstrip().split()))
dolls = list(map(int, input().rstrip().split()))

start = 0
end = k
cnt = dolls[start:end + 1].count(1)
res = INF

while end != n:
    if cnt == k:
        res = min(res, end - start + 1)
        if dolls[start] == 1: cnt -= 1
        start += 1
    elif cnt < k:
        end += 1
        if (end < n) and (dolls[end] == 1): cnt += 1
    else:
        if dolls[start] == 1: cnt -= 1
        start += 1

if res == INF:
    print(-1)
else:
    print(res)