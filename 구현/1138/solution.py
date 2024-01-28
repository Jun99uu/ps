import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
res = []

for i in range(n - 1, -1, -1):
    length = len(res)
    if nums[i] == 0:
        res = [i + 1] + res
    elif nums[i] < length:
        res = res[:nums[i]] + [i + 1] + res[nums[i]:]
    else:
        res.append(i + 1)

print(*res)