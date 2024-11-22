operand1 = operand2 = None
operator = None

def main():
    global operand1, operand2, operator
    ask_user_input()
    result = calculate(operand1, operator, operand2)
    display_result(operand1, operator, operand2, result)

def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = float(input("Enter the first operand: "))

    # Get the operator from the user
    global operator
    operator = input("Enter an operator (+, -, *, /): ")

    # Get second operand from the user
    global operand2
    operand2 = float(input("Enter the second operand: "))

def calculate(operand1, operator, operand2):
    match operator:
        case '+':
            result = operand1 + operand2
        case '-':
            result = operand1 - operand2
        case '*':
            result = operand1 * operand2
        case '/':
            if operand2 == 0:
                print("Error: Division by zero is undefined.")
                return
            else:
                result = operand1 / operand2
        case _:
            print("Invalid operator.")
            return
    return result

def display_result(operand1, operator, operand2, result):
    print(operand1,operator, operand2,"=", result)

# Call the main function to run the program
main()