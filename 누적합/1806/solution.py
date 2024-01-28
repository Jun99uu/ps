import sys
input = sys.stdin.readline
INF = sys.maxsize

n, s = list(map(int, input().rstrip().split()))
prefix = [0] + list(map(int, input().rstrip().split()))
for i in range(1, n + 1):
    prefix[i] += prefix[i - 1]
res = INF

st, en = 0, 1
while True:
    if (en == n) and ((prefix[en] - prefix[st]) < s):
        break
    if s <= (prefix[en] - prefix[st]):
        res = min(res, en - st)
        st += 1
    else:
        en += 1

if res == INF:
    print(0)
else:
    print(res)