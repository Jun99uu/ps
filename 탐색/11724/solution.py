import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = 0

for _ in range(m):
    u, v = list(map(int, input().rstrip().split()))
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(node)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        res += 1

print(res)