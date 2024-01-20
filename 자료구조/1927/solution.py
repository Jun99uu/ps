import sys, heapq
input = sys.stdin.readline

q = []

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    if n == 0:
        if not q: print(0)
        else: print(heapq.heappop(q))
    else:
        heapq.heappush(q, n)