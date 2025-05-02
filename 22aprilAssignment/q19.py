for i in range(10):
    o = ord('A') + i
    c = chr(o)
    print(f"{c} " * (10 - i))