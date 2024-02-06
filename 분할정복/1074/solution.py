import sys
input = sys.stdin.readline

n, r, c = list(map(int, input().rstrip().split()))
stand = [[0, 1], [2, 3]]
res = 0

while n != 1:
    line = 2 ** (n - 1)
    frame = 2 ** (2 * n - 2)
    if r < line: # 1사분면은 변함 없음
        if c >= line: # 2사분면
            c -= line
            res += frame
    else:
        if c < line: # 3사분면
            r -= line
            res += (frame * 2)
        else: # 4사분면
            r -= line
            c -= line
            res += (frame * 3)
    n -= 1

res += stand[r][c]
print(res)