q = int(input())

for i in range(q):
    res = 0
    sco = 0
    str = input()
    for char in str:
        if char == "O":
            sco += 1
            res += sco
        else:
            sco = 0

    print(res)
