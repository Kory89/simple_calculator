

def calculator():
    operation = input("Please select an operation(+,-,*,/):")
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if operation == '/' and num2 == 0:
        return "Cannot divide by zero."

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "invalid Calculator."
print(calculator())