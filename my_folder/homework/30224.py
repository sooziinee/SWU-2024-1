a = int(input())

if a % 7 != 0 and "7" not in str(a):
    print("0")
elif a % 7 == 0 and "7" not in str(a):
    print("1")
elif a % 7 != 0 and "7" in str(a):
    print("2")
elif a % 7 == 0 and "7" in str(a):
    print("3")
