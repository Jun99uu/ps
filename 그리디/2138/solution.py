import sys
input = sys.stdin.readline

n = int(input().rstrip())
bef = list(map(int, list(input().rstrip())))
obj = list(map(int, list(input().rstrip())))
res = []

def change(temp):
    cur = bef[:]
    for i in range(1, n):
        if cur[i - 1] != obj[i - 1]:
            temp += 1
            for j in range(i - 1, i + 2):
                if j < n: cur[j] = 1 - cur[j]
    if cur == obj:
        return temp
    return sys.maxsize

res.append(change(0))

bef[0] = 1 - bef[0]
bef[1] = 1 - bef[1]
res.append(change(1))
ans = min(res)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)