import sys
input = sys.stdin.readline

word = list(input().rstrip())
n = len(word)
a = word.count('a')
res = sys.maxsize

for i in range(n):
    if n < i + a:
        temp = word[i:] + word[:(i + a) % n]
    else:
        temp = word[i:i + a]
    res = min(res, temp.count('b'))

print(res)