"""
Lesson-plan style explanation of ai2.py.
Each section teaches one small idea.
"""

# ==========================
# Lesson 1: What this program does
# ==========================
print("Lesson 1: What this program does")
print("This program helps you practice pronunciation.")
print("It records your voice and compares it with a sentence you want to say.")

# ==========================
# Lesson 2: Variables
# ==========================
print("\nLesson 2: Variables")
expected = "你好，世界"
print("expected stores the sentence we want to practice:", expected)

# ==========================
# Lesson 3: Strings
# ==========================
print("\nLesson 3: Strings")
message = "Hello"
print("A string is text.")
print("Example:", message)

# ==========================
# Lesson 4: Functions
# ==========================
print("\nLesson 4: Functions")

def greet(name):
    return "Hello " + name

print(greet("Ali"))
print("Functions help us reuse code.")

# ==========================
# Lesson 5: If statements
# ==========================
print("\nLesson 5: If statements")
score = 90
if score >= 85:
    print("Great job!")
else:
    print("Keep practicing.")

# ==========================
# Lesson 6: Try and except
# ==========================
print("\nLesson 6: Try and except")
try:
    number = int("10")
    print("This worked:", number)
except Exception:
    print("This failed, so we handled the error.")

# ==========================
# Lesson 7: Importing tools
# ==========================
print("\nLesson 7: Importing tools")
import math
print("We can use ready-made Python tools.")
print("Example:", math.sqrt(16))

# ==========================
# Lesson 8: Recording audio
# ==========================
print("\nLesson 8: Recording audio")
print("This part of the program uses the microphone.")
print("It saves the sound into a WAV file.")

# ==========================
# Lesson 9: Transcription
# ==========================
print("\nLesson 9: Transcription")
print("This part tries to understand the words in the recording.")
print("It uses a local speech model when available.")

# ==========================
# Lesson 10: Comparing text
# ==========================
print("\nLesson 10: Comparing text")
expected_text = "你好"
recognized_text = "你好"
if expected_text == recognized_text:
    print("The texts match.")
else:
    print("They are different.")

# ==========================
# Lesson 11: Giving a score
# ==========================
print("\nLesson 11: Giving a score")
print("The program compares the expected and recognized text.")
print("Then it gives a score out of 100.")

# ==========================
# Lesson 12: Running the program
# ==========================
print("\nLesson 12: Running the program")
print("To run the full app, use this command:")
print("c:/Users/Dell/Coding/Python/.venv/Scripts/python.exe ai2.py")

print("\nThat is the lesson plan for understanding ai2.py.")
