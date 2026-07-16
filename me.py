# Advanced Calculator
# This script creates a menu-based calculator with several advanced operations.
# It uses functions, loops, conditionals, and error handling.

import math

# `def` is used to define a function.
# Functions help organize code and make it reusable.
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # `if` checks whether the denominator is zero.
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def square_root(a):
    # `if` is used again to prevent invalid math operations.
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)


def percentage(a, b):
    # This computes what percentage one number is of another.
    return (a * b) / 100


def advanced_calculator():
    # `while True` creates an endless loop until the user exits.
    while True:
        print("\nAdvanced Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()

        # `if`, `elif`, and `else` decide which operation to perform.
        if choice == "9":
            print("Goodbye!")
            break

        # `try` and `except` handle errors safely.
        try:
            if choice in {"1", "2", "3", "4", "5", "6"}:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    result = add(num1, num2)
                elif choice == "2":
                    result = subtract(num1, num2)
                elif choice == "3":
                    result = multiply(num1, num2)
                elif choice == "4":
                    result = divide(num1, num2)
                elif choice == "5":
                    result = power(num1, num2)
                elif choice == "6":
                    result = modulus(num1, num2)

                print("Result:", result)

            elif choice == "7":
                num = float(input("Enter a number: "))
                result = square_root(num)
                print("Result:", result)

            elif choice == "8":
                total = float(input("Enter the total value: "))
                percent = float(input("Enter the percentage: "))
                result = percentage(total, percent)
                print("Result:", result)

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            # `except` catches incorrect input, such as letters instead of numbers.
            print("Input error:", error)
        except ZeroDivisionError as error:
            # This handles division by zero safely.
            print("Math error:", error)

        # `input()` asks the user whether they want to continue.
        again = input("Do you want to continue? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


# `if __name__ == "__main__":` runs the program only when this file is executed directly.
if __name__ == "__main__":
    advanced_calculator()
