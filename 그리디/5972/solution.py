import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, m = list(map(int, input().rstrip().split()))
    graph[u].append((v, m))
    graph[v].append((u, m))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for node in graph[now]:
            if dist + node[1] < distance[node[0]]:
                distance[node[0]] = dist + node[1]
                heapq.heappush(q, (dist + node[1], node[0]))

dijkstra(1)
print(distance[n])