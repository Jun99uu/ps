import sys
input = sys.stdin.readline

gather = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}

while True:
    pwd = input().rstrip()
    if pwd == 'end': exit()
    letters = []
    g_check, c_check, s_check = False, True, True
    for letter in pwd:
        if letter in gather:
            g_check = True
        if len(letters) < 1:
            letters.append(letter)
            continue
        if (letter == letters[-1]) and not (letter == 'e' or letter == 'o'):
            s_check = False
            break
        if len(letters) < 2:
            letters.append(letter)
            continue
        if (letters[-2] not in gather) and (letters[-1] not in gather) and (letter not in gather):
            c_check = False
            break
        if (letters[-2] in gather) and (letters[-1] in gather) and (letter in gather):
            c_check = False
            break
        letters.append(letter)
    if g_check and c_check and s_check:
        print(f"<{pwd}> is acceptable.")
    else:
        print(f"<{pwd}> is not acceptable.")