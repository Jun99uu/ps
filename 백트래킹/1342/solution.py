import sys
from collections import Counter
input = sys.stdin.readline

word = list(input().rstrip())
length = len(word)
letters = Counter(word)
res = set()

def bt(prev, cur):
    if len(cur) == length:
        res.add(cur)
        return
    for letter in letters:
        if (prev == letter) or (letters[letter] == 0): continue
        letters[letter] -= 1
        bt(letter, cur + letter)
        letters[letter] += 1

bt('-', '')

print(len(res))