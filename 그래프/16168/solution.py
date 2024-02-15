import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(v + 1)]
parent = [i for i in range(v + 1)]
for _ in range(e):
    a, b = list(map(int, input().rstrip().split()))
    if find(a) != find(b): union(a, b)
    graph[a].append(b)
    graph[b].append(a)


# 모두 연결되어있고, 차수 규칙에 맞아야함
temp = find(parent[1])
if not all(find(el) == temp for el in parent[1:]): # 연결되지 않은 경우
    print('NO')
    exit()
nodes = [len(node) % 2 for node in graph[1:]]
if all(el == 0 for el in nodes) or (nodes.count(1) == 2): # 차수 규칙
    print('YES')
else:
    print('NO')