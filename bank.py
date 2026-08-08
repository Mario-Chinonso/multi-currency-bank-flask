def bank_action():

 opening_balance = 20000
 while True:
   
  amount_to_withdraw = float(input("Enter the amount you want to withdraw: "))
  if amount_to_withdraw > opening_balance:
         print("Insufficient fund! ⛔")
         break
  elif amount_to_withdraw <= opening_balance:
       print("Successful Transaction!")
       closing_balance = opening_balance - amount_to_withdraw
       opening_balance = closing_balance
       print("Your balance is ", opening_balance)
       choice_to_continue = input("Do you want to proceed(y/n): ")
       if choice_to_continue == 'y' and opening_balance > 1000:
         print("Welcome, ", user_name, ". \nBalance: ", opening_balance)
         choice = float(input("1. Withdraw\n2. Deposit money\n"))
         if choice == 1:
          continue
         elif choice == 2:
            print("Welcome, ", user_name)
            amount_to_deposit = float(input("Enter the amount you want to deposit: "))
            new_opening_balance = amount_to_deposit + opening_balance
            opening_balance = new_opening_balance
            code_to_check_balance = "*989*7#"
            print("Succesful Deposition!\nTo check your balance enter: ", code_to_check_balance)
            code = input("Enter the code: ")
            if code == code_to_check_balance:
               print("Your balance is: ", new_opening_balance)

            
       elif opening_balance == 1000:
         print("Low funds 🫙. You've reached your daily limit.")
         break
       elif opening_balance == 0:
         print("Sorry, you can't continue. You've exhausted your balance.")
         break
       if choice_to_continue == 'n':
         break
def new_bank_action():
 opening_balance = 20000
 opening_balance = amount_to_deposit + opening_balance
 while True:
   
  amount_to_withdraw = float(input("Enter the amount you want to withdraw: "))
  if amount_to_withdraw > opening_balance:
         print("Insufficient fund! ⛔")
         break
  elif amount_to_withdraw <= opening_balance:
       print("Successful Transaction!")
       closing_balance = opening_balance - amount_to_withdraw
       opening_balance = closing_balance
       print("Your balance is ", opening_balance)
       choice_to_continue = input("Do you want to proceed(y/n): ")
       if choice_to_continue == 'y' and opening_balance > 1000:
         continue
       elif opening_balance <= 1000:
         print("Low funds 🫙. You've reached your daily limit.")
         break
       elif opening_balance == 0:
         print("Sorry, you can't continue. You've exhausted your balance.")
         break
       if choice_to_continue == 'n':
         break
def deposit_money():
  print("Welcome, ", user_name)
  amount_to_deposit = float(input("Enter the amount you want to deposit: "))
  new_opening_balance_2 = amount_to_deposit + new_opening_balance
  code_to_check_balance = "*989*7#"
  print("Succesful Deposition!\nTo check your balance enter: ", code_to_check_balance)
  code = input("Enter the code: ")
  if code == code_to_check_balance:
        print("Your balance is: ", new_opening_balance_2)

       
import sqlite3 as sql

connection = sql.connect("database.db")

cursor = connection.cursor()
password = "2011"
opening_balance = 20000
username = str(input("Username: "))
password = str(input("Password: "))
user_name = username

cursor.execute("""
SELECT *
FROM Users
WHERE Username = ?
AND Password = ?
""", (username, password))


user = cursor.fetchone()

if user:
    print("Welcome, ", user_name, ". \nBalance: ", opening_balance)
    choice = float(input("1. Withdraw\n2. Deposit money\n"))
    if choice == 1:
       bank_action()
    if choice == 2:
       print("Welcome, ", user_name)
       amount_to_deposit = float(input("Enter the amount you want to deposit: "))
       new_opening_balance = amount_to_deposit + opening_balance
       code_to_check_balance = "*989*7#"
       print("Succesful Deposition!\nTo check your balance enter: ", code_to_check_balance)
       code = input("Enter the code: ")
       if code == code_to_check_balance:
          print("Your balance is: ", new_opening_balance)
          choice_to_continue = input("Do you want to proceed(y/n): ")
          if choice_to_continue == 'y':
           print("Welcome, ", user_name, ". \nBalance: ", new_opening_balance)
           choice = float(input("1. Withdraw\n2. Deposit money\n"))
           if choice == 1:
              new_bank_action()
           if choice == 2:
              deposit_money()
          elif choice_to_continue == 'n':
             print()
       

else:
   print("Error")

# print("Welcome, ", user_name, ". \nBalance: ", opening_balance)
# choice = float(input("1. Withdraw\n2. Deposit money\n"))
# if choice == 1:
#   password_check = input("Enter your Password:\n")
#   if password_check == password: 
#     bank_action()
#   elif password_check != password:
#       print("❌ Wrong Password!")
#       password_check_again = input("Try again:\n")
#       if password_check_again == password:
#         bank_action()    # break

# if choice == 2:
#      print("Welcome, ", user_name)
#      amount_to_deposit = float(input("Enter the amount you want to deposit: "))
#      new_opening_balance = amount_to_deposit + opening_balance
#      code_to_check_balance = "*989*7#"
#      print("Succesful Deposition!\nTo check your balance enter: ", code_to_check_balance)
#      code = input("Enter the code: ")
#      if code == code_to_check_balance:
#         print("Your balance is: ", new_opening_balance)
#         print("Welcome, ", user_name, ". \nBalance: ", new_opening_balance)
#         choice = float(input("1. Withdraw\n2. Deposit money\n"))
#         if choice == 1:
#            new_bank_action()
#         if choice == 2: 
#            deposit_money()
           
           
           
           

 


