import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
res = [0] * n

for i in range(n - 1):
    temp = -sys.maxsize
    for j in range(i + 1, n):
        if temp < (nums[j] - nums[i]) / (j - i):
            res[i] += 1
            res[j] += 1
            temp = (nums[j] - nums[i]) / (j - i)

print(max(res))