import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

def bt(arr):
    global res
    if len(s) == len(arr):
        if s == arr:
            print(1)
            exit()
        return
    if arr[-1] == 'A':
        bt(arr[:-1])
    if arr[0] == 'B':
        bt(arr[::-1][:-1])

bt(t)
print(0)