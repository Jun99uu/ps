import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

n, m = list(map(int, input().rstrip().split()))
graph = []
nodes = []
walls = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = INF

for i in range(n):
    row = list(map(int, input().rstrip().split()))
    for j in range(n):
        if row[j] == 2:
            nodes.append((i, j))
        elif row[j] == 1:
            walls.append((i, j))
    graph.append(row)

def bfs(frame):
    global res
    q = deque([])
    temp = 0
    for node in frame:
        q.append(node)
        times[node[0]][node[1]] = 0
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (graph[nx][ny] != 1) and (times[px][py] + 1 < times[nx][ny]):
                times[nx][ny] = times[px][py] + 1
                temp = max(temp, times[nx][ny])
                q.append((nx, ny))
    flag = False
    for i in range(n):
        for j in range(n):
            if (i, j) in walls: continue
            if times[i][j] == INF:
                flag = True
                break
    if not flag:
        res = min(res, temp)

for frame in combinations(nodes, m):
    times = [[INF] * n for _ in range(n)]
    bfs(frame)

if res == INF:
    print(-1)
else:
    print(res)