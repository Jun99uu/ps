import sys
input = sys.stdin.readline

n, k = list(map(int, input().rstrip().split()))
num = list(map(int, list(input().rstrip())))
stack = []

for i in range(n):
    while stack and (stack[-1] < num[i]) and (0 < k):
        stack.pop()
        k -= 1
    stack.append(num[i])

if k == 0:
    print(''.join(map(str, stack)))
else:
    print(''.join(map(str, stack[:-k])))