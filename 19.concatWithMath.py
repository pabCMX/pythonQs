from random import randint

def concatNums(primary, secondary):
    i = 10
    quotient = secondary/i
    while quotient > 1:
        i*=10
        quotient = secondary/i
    primary*=i
    concatNums = primary+secondary
    return concatNums

def main():
    i = randint(1, 10000)
    j = randint(1, 10000)
    finalConCat = concatNums(i,j)
    print(f"{i} and {j} concatinated is: {finalConCat}")

if __name__ == "__main__":
    main()

            
    