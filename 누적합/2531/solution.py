import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rstrip().split())
table = [int(input()) for _ in range(n)]
res = 0

for i in range(n):
    if i + k > n:
        tmp = len(set(table[i:n] + table[:(i+k) % n] + [c]))
    else:
        tmp = len(set(table[i:i+k] + [c]))
    if res < tmp:
        res = tmp

print(res)