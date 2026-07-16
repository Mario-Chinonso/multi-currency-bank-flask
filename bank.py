import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import jupyter as jt


user_name = "Ugwu Bernard"
password = "2011"
opening_balance = 20000



# while True:
 
#  print("Welcome, ", user_name, ". \nBalance: ", opening_balance)
#  amount_to_withdraw = float(input("Enter the amount you want to withdraw: "))
#  if amount_to_withdraw > opening_balance:
#     print("Insufficient fund!⛔")
#     break
#  elif amount_to_withdraw <= opening_balance:
#    print("Successful transaction.")
#    closing_balance = opening_balance - amount_to_withdraw
#    opening_balance = closing_balance
#    print("Your balance is: ",closing_balance)
#    choice_to_continue = input("do you want to continue(y/n): ")
#    if choice_to_continue == "y" and closing_balance > 1000:
#      continue
#    elif closing_balance <= 1000:
#      print("Low funds🫙. You've reached your daily limit.")
#      break
      
#    else:
#       print("Sorry, you can't continue.You have exhausted your balance")
#       break
 
# def simple_interest(p, r, t):
#   return (p * r * t) / 100


# print("The simple instrest of Principal 💲8000, rate 90 and time of 5 years is: ",simple_interest(8000, 9, 5))
 
   
def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b


