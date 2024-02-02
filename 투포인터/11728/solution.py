import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

ai = 0
bi = 0
res = []

while (ai != n) and (bi != m):
    if a[ai] < b[bi]:
        res.append(a[ai])
        ai += 1
    else:
        res.append(b[bi])
        bi += 1

res += a[ai:] + b[bi:]
print(*res, sep=' ')