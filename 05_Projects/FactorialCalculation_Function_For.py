def factorial(sayi):
    factorial = 1
    for i in range(1,sayi+1):
        factorial *= i
    return factorial
        

print(factorial(5))