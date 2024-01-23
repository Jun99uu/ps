import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    word = defaultdict(list)
    for idx, value in enumerate(list(input().rstrip())):
        word[value].append(idx)
    k = int(input().rstrip())
    res = []
    for idx in word.values():
        for i in range(len(idx) - k + 1):
            res.append(idx[i + k - 1] - idx[i] + 1)
    if res:
        print(min(res), max(res))
    else:
        print(-1)