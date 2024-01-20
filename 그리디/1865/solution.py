import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellman(start):
    distance[start] = 0
    for i in range(n):
        for s, e, t in graph:
            dist = distance[s] + t
            if dist < distance[e]:
                if i == n - 1:
                    return True
                distance[e] = dist
    return False

for _ in range(int(input().rstrip())):
    n, m, w = list(map(int, input().rstrip().split()))
    graph = []
    distance = [INF] * (n + 1)
    for _ in range(m): # 도로 -> 양방향
        s, e, t = list(map(int, input().rstrip().split()))
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(w): # 웜홀 -> 단방향
        s, e, t = list(map(int, input().rstrip().split()))
        graph.append((s, e, -t))
    if bellman(1):
        print('YES')
    else:
        print('NO')