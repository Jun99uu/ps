import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = list(map(int, input().rstrip().split()))
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
dy = [-1, 0, 1]

res = INF

def dfs(px, py, pd, cur):
    global res
    if px == n - 1:
        res = min(res, cur)
        return
    for i in range(3):
        ny = py + dy[i]
        if (i != pd) and (0 <= ny < m):
            dfs(px + 1, ny, i, cur + board[px + 1][ny])

for i in range(m):
    dfs(0, i, -1, board[0][i])

print(res)