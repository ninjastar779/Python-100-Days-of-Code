def factorial(n):
    global productAns
    if n == 0:
        return 1
    else:
        productAns = n * factorial(n - 1)
        return productAns
    

n = int(input("Enter a number: "))
print(factorial(n))