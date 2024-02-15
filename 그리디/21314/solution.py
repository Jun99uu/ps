import sys
input = sys.stdin.readline

nums = list(input().rstrip())

def minn():
    stack = []
    res = ''
    for num in nums:
        if num == 'K':
            if len(stack): res += str(10 ** (len(stack) - 1))
            res += '5'
            stack = []
        else:
            stack.append(num)
    if len(stack): res += str(10 ** (len(stack) - 1))
    return res

def maxx():
    stack = []
    res = ''
    for num in nums:
        if num == 'K':
            res += str(5 * (10 ** len(stack)))
            stack = []
        else:
            stack.append(num)
    for _ in stack:
        res += '1'
    return res

print(maxx())
print(minn())