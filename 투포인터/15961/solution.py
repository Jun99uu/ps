import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = list(map(int, input().rstrip().split()))
dishes = [int(input().rstrip()) for _ in range(n)]

start, end = 0, k
res = 0
dtype = defaultdict(int)
for i in range(0, k):
    dtype[dishes[i]] += 1
dtype[c] += 1

while start != n:
    res = max(res, len(dtype))
    dtype[dishes[start]] -= 1
    dtype[dishes[end % n]] += 1
    if dtype[dishes[start]] == 0:
        dtype.pop(dishes[start])
    start += 1
    end += 1

print(res)