#sum all ints from 0 thru 1000

x = int(input("Enter the smaller number: "))
y = int(input("Enter the bigger number: ")) + 1
sum = 0

for i in range (x, y):
    sum += i
print (sum)
