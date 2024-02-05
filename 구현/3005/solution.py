import sys
input = sys.stdin.readline

r, c = list(map(int, input().rstrip().split()))
puzzle = [list(input().rstrip()) for _ in range(r)]
res = []

for row in puzzle:
    res.extend([word for word in ''.join(row).split('#') if len(word) > 1])

for col in list(zip(*puzzle)):
    res.extend([word for word in ''.join(col).split('#') if len(word) > 1])

print(sorted(res)[0])