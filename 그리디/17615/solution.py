import sys
input = sys.stdin.readline

n = int(input().rstrip())
balls = input().rstrip()

red = balls.count('R')
blue = n - red

res = min(red, blue)

cont = 1
for i in range(1, n):
    if balls[i] == balls[i - 1]:
        cont += 1
    else:
        break

if balls[0] == 'R':
    res = min(res, red - cont)
else:
    res = min(res, blue - cont)

cont = 1
for i in range(n - 2, -1, -1):
    if balls[i] == balls[i + 1]:
        cont += 1
    else:
        break

if balls[-1] == 'R':
    res = min(res, red - cont)
else:
    res = min(res, blue - cont)

print(res)