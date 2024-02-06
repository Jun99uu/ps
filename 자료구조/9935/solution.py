import sys
input = sys.stdin.readline

string = list(input().rstrip())
bomb = list(input().rstrip())
bl = len(bomb)

stack = []
for letter in string:
    stack.append(letter)
    if stack[-bl:] == bomb:
        for _ in range(bl):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))

