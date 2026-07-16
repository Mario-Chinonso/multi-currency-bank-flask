# new.py
# This file explains the `elif` keyword in Python using simple real-life examples.

# `elif` means "else if".
# It is used when you want to check multiple conditions one after another.
# It is helpful when only one condition should be chosen from many.

# Real-life example:
# Imagine a traffic light.
# If the light is green, you go.
# If it is yellow, you slow down.
# If it is red, you stop.
# In Python, we can write this with `if`, `elif`, and `else`.

light = "yellow"

if light == "green":
    print("Go!")
elif light == "yellow":
    print("Slow down!")
else:
    print("Stop!")

# Another real-life example:
# Suppose you are choosing what to wear based on the weather.
# We use `elif` to check different weather types.

weather = "rainy"

if weather == "sunny":
    print("Wear sunglasses.")
elif weather == "rainy":
    print("Take an umbrella.")
elif weather == "cloudy":
    print("Wear a light jacket.")
else:
    print("Wear normal clothes.")

# Explanation for beginners:
# `elif` is like saying:
# "If the first condition is not true, then check this next one."
# It helps avoid writing many separate `if` statements.

# Example with marks:
# A school system might give grades based on marks.

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Important note:
# Python checks the conditions from top to bottom.
# As soon as one condition is true, it stops checking the rest.
# That is why `elif` is useful for choosing one correct path.
