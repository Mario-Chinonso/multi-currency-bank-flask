# ============================================================================
#               WELCOME TO THE ULTIMATE PYTHON GUIDE FOR BEGINNERS!
# ============================================================================
# Hey there! Welcome to Python. Python is one of the most popular, powerful, 
# and beginner-friendly programming languages in the world. It reads almost 
# like plain English, which makes it perfect for your coding journey.
#
# Because you asked for everything to be in a Python file, ALL explanations 
# and breakdowns are written right here inside these comments. You can run 
# this entire file in any Python environment!
# ============================================================================

# ============================================================================
# PART 1: THE CRITICAL FOUNDATIONS (VARIABLES & DATA TYPES)
# ============================================================================
# In programming, you need a way to store information. We do this using 
# "Variables". Think of a variable like a labeled storage box. 
# Unlike other languages (like C# or Java), Python is smart: it automatically 
# figures out what kind of data you are storing without you explicitly naming the type.

# 1.1 Integers (Whole numbers)
user_age = 21

# 1.2 Floats (Decimal numbers)
account_balance = 95.45

# 1.3 Strings (Text wrapped in single or double quotes)
coder_name = "Future Developer"

# 1.4 Booleans (True or False values - Note the capital T and F)
is_learning_fun = True

# 1.5 Printing to the console/screen
# We use the built-in print() function to see our data.
print("--- PART 1: VARIABLES & PRINTING ---")
print("Hello, World!")
print("Name:", coder_name, "| Age:", user_age)


# ============================================================================
# PART 2: STATEMENTS & CONTROL FLOW (MAKING DECISIONS & LOOPING)
# ============================================================================
# A "statement" is a command that tells Python to execute an action. 
# Control flow statements allow your code to make choices or repeat actions.
# CRITICAL PYTHON RULE: Python uses *Indentation* (4 spaces or a tab) to group
# blocks of code together instead of curly braces `{}`.

print("\n--- PART 2: STATEMENTS & CONTROL FLOW ---")

# 2.1 Conditional Statements (if, elif, else)
# This allows your program to make decisions dynamically based on conditions.
if user_age >= 18:
    print("Decision: You are legally an adult.")
elif user_age == 17:
    print("Decision: Almost an adult! One more year.")
else:
    print("Decision: You are a minor.")

# 2.2 Loops (Repeating Actions)
# The 'for loop' is used when you want to repeat code a specific number of times.
print("For Loop Counting:")
for i in range(1, 4):  # range(1, 4) counts from 1 up to (but not including) 4
    print("  Count is:", i)

# The 'while loop' repeats code as long as a condition remains True.
print("While Loop Action:")
stamina = 3
while stamina > 0:
    print("  Coding hard... Stamina left:", stamina)
    stamina -= 1  # This reduces stamina by 1 every loop. Crucial so the loop ends!


# ============================================================================
# PART 3: FUNCTIONS (REUSABLE CODE BLOCKS)
# ============================================================================
# A "Function" is a block of organized, reusable code used to perform a single, 
# related action. Instead of writing the same 10 lines of code everywhere, 
# you wrap them in a function and "call" it whenever you need it.
#
# Syntax: `def function_name(parameters):`

print("\n--- PART 3: FUNCTIONS ---")

# 3.1 Defining a function that takes arguments (inputs) and returns a value (output)
def calculate_total_price(price, tax_rate):
    """
    This is a docstring. It explains what the function does.
    This function takes a base price and tax, calculates total, and returns it.
    """
    total = price + (price * tax_rate)
    return total

# 3.2 Calling the function
final_bill = calculate_total_price(100.00, 0.05)
print("The calculated total bill is:", final_bill)


# ============================================================================
# PART 4: DATA STRUCTURES & METHODS
# ============================================================================
# Data structures hold collections of data. Python has built-in structures 
# like Lists and Dictionaries. 
# "Methods" are simply special functions that belong exclusively to a specific 
# object or data type. You call them using a dot `.method_name()`

print("\n--- PART 4: DATA STRUCTURES & METHODS ---")

# 4.1 Lists (An ordered, changeable collection of items)
programming_languages = ["Python", "JavaScript", "C#"]

# Using List Methods:
programming_languages.append("Go")          # .append() adds an item to the end
programming_languages.insert(1, "Ruby")      # .insert() adds an item at a specific index
programming_languages.remove("JavaScript")  # .remove() deletes a specific item

print("Modified Python List:", programming_languages)

# 4.2 Dictionaries (Key-Value pairs, like a real dictionary or contact card)
user_profile = {
    "username": "AI_Entrepreneur",
    "level": "Intermediate",
    "xp": 4500
}

# Using Dictionary Methods:
# .keys() retrieves all the labels
print("Dictionary Keys:", list(user_profile.keys()))
# Accessing specific data using its key:
print("User Level is:", user_profile["level"])

# 4.3 String Methods
# Even simple strings have built-in methods!
greeting = "  python programming rocks!  "
print("Clean Upper Text:", greeting.strip().upper()) 
# .strip() removes outer spaces, .upper() converts all characters to uppercase.


# ============================================================================
# PART 5: ERROR HANDLING (THE PRO MINDSET)
# ============================================================================
# Bugs and crashes happen to everyone. Professional programmers prevent their 
# apps from crashing out entirely by wrapping risky code inside a try-except block.

print("\n--- PART 5: ERROR HANDLING ---")

try:
    # Attempting something risky (Dividing by zero is mathematically impossible)
    dangerous_math = 10 / 0
except ZeroDivisionError:
    # Python catches the crash and runs this safe alternative code block instead
    print("System caught an error: You absolutely cannot divide by zero!")


# ============================================================================
# FINAL ADVICE FOR BEGINNERS:
# 1. Code everyday, even if it's just for 15 minutes.
# 2. Don't memorize syntax. Learn the concepts, google/AI the specific commands.
# 3. If your code breaks, read the very bottom line of the error message—it 
#    tells you exactly what went wrong and where.
# ============================================================================