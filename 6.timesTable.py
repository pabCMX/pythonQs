xNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
xArray = []
product = 0

for i in xNumbers:
    for t in yNumbers:
        product = i*t
        xArray.append(product)
    xLine="""|{}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t|\n-------------------------------------------------------------------------------------------------""".format(*xArray)
    xArray.clear()
    print(xLine)