for r in range(10):
    for c in range(r + 1):
        a = ord('A') + c
        l = chr(a)
        print(l, end=" ")
    print()