import sys
input = sys.stdin.readline

n, m, h = list(map(int, input().rstrip().split()))
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
milks = []
hx, hy = 0, 0
res = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            hx, hy = i, j
        elif board[i][j] == 2:
            milks.append((i, j))

def bt(px, py, hp, cnt):
    global res
    for nx, ny in milks:
        if board[nx][ny] == 2:
            dist = abs(nx - px) + abs(ny - py)
            if dist <= hp:
                board[nx][ny] = 0
                bt(nx, ny, hp - dist + h, cnt + 1)
                board[nx][ny] = 2
    hdist = abs(hx - px) + abs(hy - py)
    if hdist <= hp:
        res = max(res, cnt)

bt(hx, hy, m, 0)
print(res)