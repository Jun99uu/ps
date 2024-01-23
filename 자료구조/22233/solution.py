import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
keywords = set(input().rstrip() for _ in range(n))

for _ in range(m):
    uses = input().rstrip().split(',')
    for use in uses:
        if use in keywords:
            keywords.remove(use)
    print(len(keywords))