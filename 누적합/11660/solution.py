import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
pre = [[0] * (n + 1)] + [[0] + list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        pre[i][j] += pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = list(map(int, input().rstrip().split()))
    print(pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1])