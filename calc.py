def calculator() -> None:
    num1: float = float(input("Enter first value :"))
    num2: float = float(input("Enter second value :"))
    print("""Select operation :
          1 for Addition
          2 for Subtraction
          3 for Multiplication
          4 for Division""")
    choice: str = input("Enter here :")
    print(choice)
    if choice in ['1', '2', '3', '4']:
        if choice == "1":
            print(addition(num1, num2))
        elif choice == "2":
            print(subtraction(num1, num2))
        elif choice == "3":
            print(multiplication(num1, num2))
        elif choice == "4":
            print(division(num1, num2))
        else:
            print("invalid input")


def addition(a, b):
    # print("Add")
    return a + b


def subtraction(a, b):
    # print("Sub")
    return a - b


def multiplication(a, b):
    # print("Mul")
    return a * b


def division(a, b):
    # print("Div")
    return a / b


calculator()
