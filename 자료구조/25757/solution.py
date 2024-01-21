import sys
input = sys.stdin.readline

n, game = list(input().rstrip().split())
players = set([input().rstrip() for _ in range(int(n))])

gaming = {
    'Y': 1,
    'F': 2,
    'O': 3
}

print(len(players) // gaming[game])