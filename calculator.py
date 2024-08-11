#This is a calculator that performs calculations or reads from a text file
while True:
    user_input=input("1. Perform calculation\n2. Read from text file \n3. Exit")
    file = None
    if user_input=='1':
       #Getting user input for calculation
        while True:
            try:
                num1 = int(input("Please enter a number: "))
                break
            # This exception covers when the user didn't enter a valid number
            except ValueError:
                print("Ooops! That is not a valid number, please try again!")
        while True:
            try:
                operator = input("Please enter an operator: ")

                if operator in ["+", "-", "x", "/"]:
                    break
                else:
                    # This exception covers the option of when a an invalid operator is entered
                    raise Exception
            except Exception as error:

                print("That is not a valid operator, please try again.", error)

        while True:
            try:
                num2 = int(input("Please enter a number: "))

                result=0
                #Different operations
                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "x":
                    result = num1 * num2
                elif operator == "/":
                    result = num1 / num2
                print(result)

                file_name = "CalculatorFile"
                # Open text file to add new calculation
                with open(file_name, 'a+') as file:
                    file.write(f'{num1} {operator} {num2} = {result} \n')
                    break
            except ValueError:
                print("Ooops! That is not a valid number, please try again!")
            except ZeroDivisionError:
                print("You cannot have a division with zero, please try again!")

    #Enter the file name
    elif user_input=='2':
        file_name = input("Please enter a file name")
        try:
            with open(file_name, 'r') as file:
                print(file.read())

        except FileNotFoundError as error:
            print("The file that you are trying to open does not exist.")

    elif user_input == "3":
        print("Program ended")
        break
    else:
        print("Invalid input")
