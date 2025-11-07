#using modulus

for i in range(0,101):
    if i%2 == 0:
        print(f"{i} even")
    else:
        print(f"{i} odd")

#no modulus

for i in range (0,101):
    noDecimal = (int(i/2) == i/2)

    if noDecimal:
        print(f"{i} even")
    else:
        print(f"{i} odd")

#no if/else/switch

for i in range (0,101):
    noDecimal = (int(i/2) == i/2)

    while noDecimal:
        print(f"{i} even")
        break
    while not noDecimal:
        print(f"{i} odd")
        break