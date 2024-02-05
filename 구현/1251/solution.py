import sys
input = sys.stdin.readline

word = list(input().rstrip())
lw = len(word)
res = []

for i in range(1, lw - 1):
    for j in range(i + 1, lw):
       res.append(''.join(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]))

print(sorted(res)[0])