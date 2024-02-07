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

n, m = int(input().rstrip()), int(input().rstrip())
parent = [i for i in range(n + 1)]
for i in range(n):
    link = list(map(int, input().rstrip().split()))
    for j in range(n):
        if link[j] == 1:
            union(i + 1, j + 1)

plan = list(map(int, input().rstrip().split()))
start = parent[plan[0]]
for i in range(1, m):
    if start != parent[plan[i]]:
        print('NO')
        exit()
print('YES')