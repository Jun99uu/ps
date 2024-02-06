import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(n)]
num_type = set(nums)
res = 1

for type in num_type:
    arr = [num for num in nums if num != type]
    temp = 1
    for i in range(1, len(arr)):
       if arr[i] != arr[i - 1]:
           res = max(res, temp)
           temp = 1
       else:
           temp += 1
    res = max(res, temp)

print(res)