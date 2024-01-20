import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
emblem = [list(input().rstrip().split()) for _ in range(n)]

def binary(score):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if int(emblem[mid][1]) < score:
            start = mid + 1
        else:
            end = mid - 1
    return emblem[start][0]

for _ in range(m):
    print(binary(int(input().rstrip())))