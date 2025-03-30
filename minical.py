
def calculator():
    """
    A simple calculator that performs basic arthmetic operations.
    It takes two numbers and an operator as an input from the user and return the result."""
    a = int(input("Enter first number: "))
    op = input("Enter operator like + - / *: ")
    b = int(input("Enter second number: "))

    if op == '+':
        print("Result :", a + b)

    elif op == '-':
        print("Result :", a - b)

    elif op == '*':
        print("Result :" ,a * b)
    
    elif op == '/':
        print("Result :", a / b)
    
    else:
        raise ValueError("Invalid operator. Supported operators are: + - * /")
    


calculator()



