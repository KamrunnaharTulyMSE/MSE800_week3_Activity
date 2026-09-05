def square_decorator(func):
    def wrapper(a, b):
        return func(a, b)
    return wrapper


@square_decorator
def square(a, b):
    print("Square of", a, "=", a * a)
    print("Square of", b, "=", b * b)


# Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

square(num1, num2)