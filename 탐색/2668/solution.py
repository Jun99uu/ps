import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [0] + [int(input().rstrip()) for _ in range(n)]
res = []

def dfs(cur):
    global start
    visited[cur] = True
    next = graph[cur]
    if not visited[next]:
        dfs(next)
    elif visited[next] and (next == start):
        res.append(next)
        return

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    start = i
    dfs(i)

print(len(res))
print(*sorted(res), sep='\n')