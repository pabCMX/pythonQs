from random import randint

coins = []
iterations = 1000
TsOnly = 0
HsOnly = 0
mixedHT = 0
for i in range (0,iterations):
    for j in range(0, 2):
        flipCheck = bool(randint(0,1))
        if flipCheck:
            coins.append("H")
        else:
            coins.append("T")

    if coins[0] == "H":
        if coins[1] == "T":
            mixedHT += 1
        else:
            HsOnly += 1
    elif coins[1] == "H":
        mixedHT += 1
    else:
        TsOnly += 1
    coins = []

TsOnlyPcnt = (TsOnly/iterations)*100
HsOnlyPcnt = (HsOnly/iterations)*100
mixedHTPcnt = (mixedHT/iterations)*100

msg = (
    f'Total heads only pairs:\t {HsOnly:4}\n'
    f'Total tails only pairs:\t {TsOnly:4}\n'
    f'Total mixed pairs:\t {mixedHT:4}\n'
    f'Total heads only %:\t {HsOnlyPcnt:4.2f}%\n'
    f'Total tails only %:\t {TsOnlyPcnt:4.2f}%\n'
    f'Total mixed %:\t\t {mixedHTPcnt:4.2f}%\n'
)
print(msg)