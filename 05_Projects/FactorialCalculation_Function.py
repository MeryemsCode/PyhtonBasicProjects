def factorial(sayi):
    factorial = 1
    if (sayi == 0 or sayi == 1):
        print("Factorial:",factorial)
    else:
        while (sayi >= 1):
            factorial = factorial * sayi
            sayi -= 1
        print("Factorial:",factorial)

factorial(5)
