a = 0
b = 0

v = {"a", "e", "i", "o", "u"}

s = input()

for i in s:
    if i in v:
        a += 1
    if i == "y":
        b += 1

print(f"{a} {a+b}")
