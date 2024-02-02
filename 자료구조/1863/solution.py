import sys
input = sys.stdin.readline

stack = [0]
res = 0

def remove(target):
    global res
    while stack and (target < stack[-1]):
        stack.pop()
    if stack and stack[-1] != target:
        res += 1
    stack.append(target)

for _ in range(int(input().rstrip())):
    x, y = list(map(int, input().rstrip().split()))
    if stack[-1] < y:
        res += 1
        stack.append(y)
    else:
        remove(y)

print(res)