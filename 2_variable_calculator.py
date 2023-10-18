while True:

    number1 = float(input("Enter the first number: "))
    # if number1.isdigit():
    # result =
    number2 = float(input("Enter the second number: "))
    operation = int(input("Enter the number of the operation you want to perform: \n 1.Addition \n 2.Subtraction \n "
                          "3.Division \n 4.Multiplication \n Enter selection: "))

    if operation == 1:
        print("Result:", number1 + number2)
    elif operation == 2:
        print("Result:", number1 - number2)
    elif operation == 3:
        print("Result:", number1 / number2)
    else:
        print("Result:", number1 * number2)

    user_input = input("Enter 'e' for exit, 'n' for a new operation: ")
    if user_input == 'e':
        break
