from turtle import pos


def sub(int1, int2):
    partialQ = int1 - int2
    return partialQ

def divWRemain(int1, int2, count, posneg=1):
    if int1 < 0:
        int1 *= -1
        posneg=-1
    elif int2 < 0:
        int2 *= -1
        posneg=-1
    if int1 <= int2:
        return int1, 0, posneg
    int1 = sub(int1,int2)
    rem, count, posneg = divWRemain(int1, int2, count, posneg)
    count += 1
    return rem, count, posneg

def main():
    i1=int(input("Input an integer: "))
    i2=int(input("Input another integer to divide by: "))
    rem, count, posneg = divWRemain(i1, i2, 0)
    count*=posneg
    print(f"Dividing {i1} by {i2} returns {count} with {rem} remaining.")

if __name__ == "__main__":
    main()