
#checking for trivial division by the primes under 100
from reprlib import recursive_repr


def trivialDivide(num):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    primeBool = True
    while primeBool:
        for i in primes:
            if num%i==0:
                primeBool = False
                break
    return primeBool
def Factor2(num,r):
    r+=1

#checking for strong probable primes using the fermat test:
def base2ModTest(num):
    d = 0
    while d%2 == 0:
        d, r = Factor2(num, r)

# A Jacobi Symbol is a measure of whether given (D/n) if 
# 0: D%n=0
# 1: D%n!=0 but there exists x such that D%n=x^2
#-1: D%n!=0 and no such x exists
# 
def jacobiSym(num):
    D=5
    jSym = 
    primeBool=True
    while jSym != -1:

        if D < 0:
            D=(D*-1)+2
        else:
            D=(D+2)*-1
        if D/num == 0:
            primeBool=False
            break
    q=(1-D)/4
    return D, q, primeBool
            


def lucasTest(num, D, q):
    i=1
    P = 1
    Uk=1
    U2k=1
    Vk=1
    V2k=1-2q**2
    k = 2
    deltaNum = num - (D/num)
    while d%2==0:
        d=deltaNum/2**i
        i+=1
    while k < num+1:
        tempUk=U2k
        tempVk=V2k
        U2k = Uk * Vk
        V2k = (Vk**2+D*Uk**2)/2
        Uk = tempUk
        Vk = tempVk
        k*=2
    while k <= num+1:
        tempUk=U2k
        tempVk=V2k
        if (P*Uk+Vk)%2 == 0:
            U2k = int((P*Uk+Vk)/2)
        else:
            U2k = int((P*Uk+Vk+num)/2)
        if (D*Uk+P*Vk)%2 == 0:
            V2k = int((D*Uk+P*Vk)/2)
        else:
            V2k = int((D*Uk+P*Vk+num)/2)
        Uk=tempUk
        Vk=tempVk
        k+=1
        # implement a binary expansion of num, or just leave it here and assume
        # it will be done soon enough given num <= 2,000,000
        


def primesearch(low,high):
    primes = []
    for i in range(low,high):
        if not trivialDivide(i):
            break
        if not base2ModTest(i):
            break
        D,q,primeBool=jacobiSym(i)
        if not primeBool:
            break
        if not lucasTest(i,D,q):
            break
        else:
            primes.append(i)
    return primes            

def main():
    low = 2
    high = 2000000
    sum = 0
    primes = primesearch(low, high)
    for i in primes:
        sum+=i
    print("The sum of all primes between {low} and {high} is {sum}.")