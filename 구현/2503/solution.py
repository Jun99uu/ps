import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input().rstrip())
candi = set(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    cur, s, b = list(map(int, input().rstrip().split()))
    cur = tuple(map(int, list(str(cur))))
    temp = set()
    for num in candi:
        ts, tb = 0, 0
        for i in range(3):
            if num[i] == cur[i]: ts += 1
            elif num[i] in cur: tb += 1
        if (ts == s) and (tb == b):
            temp.add(num)
    candi = temp

print(len(candi))