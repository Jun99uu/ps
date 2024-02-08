import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
visited = [False] * n
res = 0

def bt(arr):
    global res
    if len(arr) == n:
        temp = 0
        for i in range(n - 1):
            temp += abs(arr[i] - arr[i + 1])
        res = max(res, temp)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(nums[i])
            bt(arr)
            visited[i] = False
            arr.pop()

bt([])
print(res)

