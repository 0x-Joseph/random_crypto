def calc(n):
    a = 0
    for i in range(0, n):
        for j in range(i, n):
            a += 1



for i in (0, 10):
    print('#' + str(i) + str(calc(i)))
