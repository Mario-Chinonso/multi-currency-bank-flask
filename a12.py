"""
Beginner study guide for the file ai2.py.

This file explains the main Python ideas in a simple way.
It is designed for a beginner who wants to understand the whole code slowly.
"""

# =============================
# 1. Python basics
# =============================

print("Lesson 1: Variables")
name = "Ali"
age = 15
print("My name is", name)
print("My age is", age)

print("\nLesson 2: Strings")
message = "Hello world"
print(message)
print(message.lower())
print(message.upper())

print("\nLesson 3: Numbers")
number1 = 10
number2 = 3
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)

# =============================
# 2. Functions
# =============================

print("\nLesson 4: Functions")

def greet(person_name: str) -> str:
    """Return a friendly message."""
    return f"Hello {person_name}"

print(greet("Sara"))

# =============================
# 3. Important Python keywords explained
# =============================

print("\nLesson 5: Key words and meaning")
keywords = {
    "import": "Brings code from another module or library.",
    "from": "Imports something from a specific module.",
    "def": "Defines a new function.",
    "return": "Sends a value back from a function.",
    "if": "Runs code only if a condition is true.",
    "elif": "Another condition check if the first if is false.",
    "else": "Runs when all previous conditions are false.",
    "try": "Tries some code and prepares for errors.",
    "except": "Handles an error that happens in try.",
    "for": "Loops over a list or collection.",
    "while": "Loops while a condition is true.",
    "with": "Makes sure a file or resource is closed properly.",
}

for keyword, meaning in keywords.items():
    print(f"- {keyword}: {meaning}")

# =============================
# 4. How ai2.py works step by step
# =============================

print("\nLesson 6: How the main code works")

steps = [
    "1. The program starts from the main block at the bottom.",
    "2. It asks for a sentence you want to practice.",
    "3. It records your voice for a short time.",
    "4. It tries to understand your speech using a local model.",
    "5. It compares your text with the expected sentence.",
    "6. It prints a score and a friendly message.",
]

for step in steps:
    print(step)

# =============================
# 5. A tiny practice version of the idea
# =============================

print("\nLesson 7: Mini practice example")

expected = "你好，世界"
recognized = "你好，世界"

if expected == recognized:
    print("Great! Your text matches.")
else:
    print("Try again.")

# =============================
# 6. A beginner curriculum plan
# =============================

print("\nLesson 8: 12-day study curriculum")

curriculum = [
    "Day 1: Learn print(), variables, and strings.",
    "Day 2: Learn input() and how to store user text.",
    "Day 3: Learn if, elif, and else.",
    "Day 4: Learn functions with def and return.",
    "Day 5: Learn loops with for and while.",
    "Day 6: Learn lists and dictionaries.",
    "Day 7: Learn try and except for errors.",
    "Day 8: Learn file handling and paths.",
    "Day 9: Learn how imports work in Python.",
    "Day 10: Study ai2.py line by line.",
    "Day 11: Build a smaller version of the project.",
    "Day 12: Add your own ideas and improve the code.",
]

for day in curriculum:
    print(day)

# =============================
# 7. Practice tasks
# =============================

print("\nLesson 9: Practice tasks")
practice_tasks = [
    "1. Write a function that adds two numbers.",
    "2. Write an if statement that checks if a word is long.",
    "3. Make a loop that prints 1 to 5.",
    "4. Create a small program that compares two sentences.",
]

for task in practice_tasks:
    print(task)

print("\nYou are ready to study ai2.py step by step.")
