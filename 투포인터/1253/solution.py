import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = sorted(list(map(int, input().rstrip().split())))
res = 0

def find_sum(target, arr):
    s, e = 0, len(arr) - 1
    while s < e:
        tmp = arr[s] + arr[e]
        if tmp == target:
            return True
        elif tmp < target:
            s += 1
        else:
            e -= 1
    return False

for i in range(n):
    if find_sum(nums[i], nums[:i] + nums[i+1:]):
        res += 1

print(res)