def calc(n):
    a = 0
    for i in range(0, n):
        for j in range(i, n):
            a += 1
    return a


for i in range(0, 11):
    print('#' + str(i) + ' ...... ' + str(calc(i)))