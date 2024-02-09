import sys
input = sys.stdin.readline

n, c = list(map(int, input().rstrip().split()))
home = sorted(int(input().rstrip()) for _ in range(n))
start, end = 1, home[-1] - home[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    prev, temp = home[0], 1
    for cur in home[1:]:
        if mid <= (cur - prev):
            prev = cur
            temp += 1
    if temp >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)