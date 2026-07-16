"""
Beginner-friendly explanation of algorithms and pseudocode.
"""

print("What is an algorithm?")
print("An algorithm is a step-by-step set of instructions used to solve a problem.")
print("It is like a recipe.")
print()

print("Example: Making a cup of tea")
print("1. Boil water")
print("2. Put tea in a cup")
print("3. Pour hot water into the cup")
print("4. Stir")
print("5. Drink")
print()

print("In programming, an algorithm tells the computer exactly what to do.")
print()

print("Example 1: Add two numbers")
print("Algorithm:")
print("1. Start")
print("2. Read the first number")
print("3. Read the second number")
print("4. Add them")
print("5. Show the result")
print()

print("Pseudocode for adding two numbers:")
print("BEGIN")
print("    READ a")
print("    READ b")
print("    sum = a + b")
print("    PRINT sum")
print("END")
print()

# Python example

def add_numbers(a, b):
    return a + b

print("Python example:")
print(add_numbers(3, 5))
print()

print("Example 2: Find the largest number")
print("Algorithm:")
print("1. Compare the first and second numbers")
print("2. Keep the larger one")
print("3. Compare it with the next number")
print("4. Continue until all numbers are checked")
print("5. Show the largest number")
print()

print("Pseudocode for finding the largest number:")
print("BEGIN")
print("    READ numbers")
print("    largest = numbers[0]")
print("    FOR each number in numbers")
print("        IF number > largest")
print("            largest = number")
print("        ENDIF")
print("    ENDFOR")
print("    PRINT largest")
print("END")
print()

# Python example

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print("Python example:")
print(find_largest([4, 9, 2, 7]))
print()

print("What is pseudocode?")
print("Pseudocode is a simple way to describe an algorithm using plain English")
print("or a mix of English and code-like steps.")
print("It is not real programming code, but it helps us plan the solution before writing code.")
print()

print("Why use pseudocode?")
print("- It is easy to read")
print("- It helps you plan your logic")
print("- It is useful before writing real Python code")
print()

print("Quick summary:")
print("- An algorithm is a step-by-step solution to a problem")
print("- Pseudocode is a simple description of that solution")
print("- Python code is the real program that runs")
