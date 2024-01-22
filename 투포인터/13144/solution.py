import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

s, e = 0, 0
dup = set()
res = 0
while (s != n) and (e != n):
    if nums[e] not in dup:
        dup.add(nums[e])
        e += 1
        res += e - s
    else:
        while nums[e] in dup:
            dup.remove(nums[s])
            s += 1

print(res)