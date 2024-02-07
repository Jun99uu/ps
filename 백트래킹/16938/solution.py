import sys
input = sys.stdin.readline

n, l, r, x = list(map(int, input().rstrip().split()))
a = list(map(int, input().rstrip().split()))
a.sort()
res = 0

def bt(idx, cur, nv, xv):
    global res
    if (l <= cur <= r) and (x <= xv - nv):
        res += 1
    for i in range(idx + 1, n):
        bt(i, cur + a[i], nv, a[i])

for i in range(n):
    bt(i, a[i], a[i], a[i])

print(res)