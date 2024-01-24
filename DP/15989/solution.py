import sys
input = sys.stdin.readline

end = 10001
dp = [1] * end

for i in range(2, end):
    dp[i] += dp[i - 2]
for i in range(3, end):
    dp[i] += dp[i - 3]

for _ in range(int(input().rstrip())):
    print(dp[int(input().rstrip())])