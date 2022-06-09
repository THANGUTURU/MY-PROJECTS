# the program of factorial using recursive functions

def factorial(x):
    if x == 1 or  x==0:
        return 1
    else:
        return (x * factorial(x-1))

number=int(input("enter the number="))
print("The factorial of", number, "is", factorial(number))
