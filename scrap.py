def x(y,z):
    sum=y+z
    product=y*z
    return sum,product

def main():
    sum,product = x(2.0,4)
    print (f"{sum:.3f} is the sum, and {product}")

if __name__ == "__main__":
    main()