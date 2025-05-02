# for i in range(10, 0, -1):
#     print(f"{11 - i} " * i)
f= 1
for i in range(10,0,-1):
    for j in range(i):
        print(f,end=" ")
    f+=1
    print()