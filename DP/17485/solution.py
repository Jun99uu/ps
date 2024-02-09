import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = list(map(int, input().rstrip().split()))
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    dp[0][j] = [board[0][j]] * 3

for i in range(1, n):
    for j in range(m):
        if j != 0:
            dp[i][j][2] = board[i][j] + min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1])
        if j != m - 1:
            dp[i][j][0] = board[i][j] + min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2])
        dp[i][j][1] = board[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])

print(min([el for row in dp[-1] for el in row]))