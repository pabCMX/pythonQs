from random import randint

def isPalindrome(num):
    numString = f"{num}"
    index = 1
    palinBool = True
    midString = len(numString)//2
    while index <= midString and palinBool == True:
        for char in numString:
            if char == numString[(len(numString))-index]:
                index+=1
                continue
            else:
                palinBool = False
                break
    return palinBool

def main():
    for i in range(0,10000):
        palinInt = randint(0,100000)
        if isPalindrome(palinInt):
            print(f"{palinInt} is a palindrome.")

if __name__ == "__main__":
    main()