import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
temp = [list(map(int, input().rstrip().split())) for _ in range(n)]
board = [[0] * n for _ in range(n)]
dist = [[0] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
uni = 0
res = sys.maxsize

for i in range(n):
    for j in range(n):
        if (temp[i][j] == 1) and (board[i][j] == 0):
            q = deque([(i, j)])
            uni += 1
            board[i][j] = uni
            while q:
                px, py = q.popleft()
                for d in range(4):
                    nx, ny = px + dx[d], py + dy[d]
                    if (0 <= nx < n) and (0 <= ny < n) and (temp[nx][ny] == 1) and (board[nx][ny] == 0):
                        board[nx][ny] = uni
                        q.append((nx, ny))

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            q = deque([(i, j)])
            start = board[i][j]
            while q:
                px, py = q.popleft()
                for d in range(4):
                    nx, ny = px + dx[d], py + dy[d]
                    if (0 <= nx < n) and (0 <= ny < n) and (board[nx][ny] == 0) and (
                            dist[nx][ny] == 0 or dist[px][py] + 1 < dist[nx][ny]):
                        dist[nx][ny] = dist[px][py] + 1
                        q.append((nx, ny))
                    elif (0 <= nx < n) and (0 <= ny < n) and (board[nx][ny] != 0) and (board[nx][ny] != start):
                        res = min(res, dist[px][py])

print(res)