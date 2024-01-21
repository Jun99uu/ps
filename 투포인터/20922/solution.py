import sys
input = sys.stdin.readline

n, k = list(map(int, input().rstrip().split()))
nums = list(map(int, input().rstrip().split()))
num_dict = {}

s, e = 0, 0
res = 0
while e != n:
    num_dict[nums[e]] = num_dict.get(nums[e], 0) + 1
    if num_dict.get(nums[e], 0) > k:
        res = max(res, e - s)
        while (s <= e) and (num_dict.get(nums[e], 0) > k):
            num_dict[nums[s]] -= 1
            s += 1
    e += 1

print(max(res, e - s))