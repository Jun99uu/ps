import sys, heapq
input = sys.stdin.readline

n = int(input().rstrip())
q = []

for _ in range(n):
    nums = list(map(int, input().rstrip().split()))
    for num in nums:
        if len(q) < n:
            heapq.heappush(q, num)
        else:
            if q[0] < num:
                heapq.heappop(q)
                heapq.heappush(q, num)

print(q[0])