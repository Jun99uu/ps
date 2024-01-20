import sys
input = sys.stdin.readline

n, record, p = list(map(int, input().rstrip().split()))

if n == 0:
    print(1)
    exit()

rank = list(map(int, input().rstrip().split()))

if (n == p) and (rank[-1] >= record):
    print(-1)
else:
    res = n + 1
    for i in range(n):
        if rank[i] <= record:
            res = i + 1
            break
    print(res)