import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
INF = sys.maxsize
cnt = 1

def bfs():
    q = deque([(0, 0)])
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (prices[px][py] + board[nx][ny] < prices[nx][ny]):
                prices[nx][ny] = prices[px][py] + board[nx][ny]
                q.append((nx, ny))

while True:
    n = int(input().rstrip())
    if n == 0: break
    board = [list(map(int, input().rstrip().split())) for _ in range(n)]
    prices = [[INF] * n for _ in range(n)]
    prices[0][0] = board[0][0]
    bfs()
    print(f"Problem {cnt}: {prices[n - 1][n - 1]}")
    cnt += 1