import sys
input = sys.stdin.readline

n = int(input().rstrip())
scores = list(map(int, input().rstrip().split()))
gap = sys.maxsize
res = (0, 0)

start = 0
end = n - 1
while start < end:
    cur = scores[start] + scores[end]
    if abs(cur) < gap:
        gap = abs(cur)
        res = (scores[start], scores[end])
    if cur == 0:
        break
    elif cur > 0:
        end -= 1
    elif cur < 0:
        start += 1

print(*res)