while True:
    operator = input("Enter an Operator from /, +, - and *")

    # Check if the operator is valid
    if operator not in ['+', '-', '*', '/']:
        print(f"{operator} isn't a valid operator! Please try again.")
    else:
        # If the operator is valid, proceed with number input
        while True:
            try:
                num_1 = float(input("Enter Your first number!: "))
                num_2 = float(input("Enter Your second number!: "))
                break  # Break the loop if both inputs are valid numbers
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        # Perform the calculation based on the operator
        if operator == "*":
            print(f"Your result is: {num_1 * num_2}")
        elif operator == "+":
            print(f"Your result is: {num_1 + num_2}")
        elif operator == "-":
            print(f"Your result is: {num_1 - num_2}")
        elif operator == "/":
            # Check for division by zero
            if num_2 != 0:
                print(f"Your result is: {round(num_1 / num_2, 2)}")
            else:
                print("Error: Cannot divide by zero!")

        # Prompt to restart with validation
        while True:
            restart = input("Do you want to restart the program? (yes/no): ")
            if restart.lower() in ['yes', 'no']:
                break  # Break the loop if a valid input is provided
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        if restart.lower() != 'yes':
            break