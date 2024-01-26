import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())
blocks = defaultdict(int)
m, ml, mh = 0, 0, 0
for _ in range(n):
    l, h = list(map(int, input().rstrip().split()))
    blocks[l] = h
    if mh < h:
        mh = h
        ml = l
    m = max(m, l)

res = 0
temp = 0

for i in range(ml + 1):
    if temp < blocks[i]:
        temp = blocks[i]
    res += temp

temp = 0
for i in range(m, ml, -1):
    if temp < blocks[i]:
        temp = blocks[i]
    res += temp

print(res)