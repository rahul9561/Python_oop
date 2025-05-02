for i in range(10):
    ascii_val = ord('A') + i
    letter = chr(ascii_val)
    print(f"{letter} " * (10 - i))