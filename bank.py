def bank_action():
 while True:
  opening_balance = get_balance(username)
  amount_to_withdraw = float(input("Enter the amount you want to withdraw: "))
  if amount_to_withdraw > opening_balance:
         print("Insufficient fund! ⛔")
         break
  elif amount_to_withdraw <= opening_balance:
       print("Successful Transaction!")
       closing_balance = opening_balance - amount_to_withdraw
       opening_balance = closing_balance
       save_balance(user_name, opening_balance)
       print("Your balance is ", opening_balance)
       choice_to_continue = input("Do you want to proceed(y/n): ")
       if choice_to_continue == 'y' and opening_balance > 1000:
         print("Welcome, ", user_name, ". \nBalance: ", opening_balance)
         choice = float(input("1. Withdraw\n2. Deposit money\n"))
         if choice == 1:
          continue
         elif choice == 2:
           deposit_money()
           choice_to_continue = input("Do you want to proceed(y/n): ")
           if choice_to_continue == 'y':
              continue
           else:
              break
       elif opening_balance == 1000:
         print("Low funds 🫙. You've reached your daily limit.")
         break
       elif opening_balance == 0:
         print("Sorry, you can't continue. You've exhausted your balance.")
         break
       elif choice_to_continue == 'n':
         print("Bye, ", user_name,".👋")
         break
def deposit_money():
  opening_balance = get_balance(username)
  print("Welcome, ", user_name, "\nBalance: ", opening_balance)
  amount_to_deposit = float(input("Enter the amount you want to deposit: "))
  opening_balance = amount_to_deposit + opening_balance
  save_balance(user_name, opening_balance)   
  code_to_check_balance = "*989*7#"
  print("Succesful Deposition!\nTo check your balance enter: ", code_to_check_balance)
  code = input("Enter the code: ")
  if code == code_to_check_balance:
        print("Your balance is: ", opening_balance)
  choice_to_continue = input("Do you want to proceed(y/n): ")
  if choice_to_continue == 'y':
     choice = float(input("1. Withdraw\n2. Deposit money\n"))
     if choice == 1:
        bank_action()
     elif choice == 2:
        deposit_money()
  elif choice_to_continue == 'n':
       print("Bye, ", user_name,".👋")
def get_balance(username):
   cursor.execute("""
      SELECT Balance
      FROM Users
      WHERE Username = ?
   
   """,(username,))
   row = cursor.fetchone()
   return row[0] if row else None
def save_balance(username, new_balance):
   cursor.execute("""
      UPDATE Users
      SET Balance = ?
      WHERE Username = ?
 """,(new_balance, username))
   connection.commit()
def change_pwd():
   change_pwd_question = float(input("Welcome, user. To change your password, answer the following:\n1. What's your Balance: "))
   change_pwd_question_2 = input("2. Your Username: ")
   balance = get_balance(change_pwd_question_2)
   
   cursor.execute("""
         SELECT Username
         FROM Users
         WHERE Balance = ?
      """, (balance,))
   user = cursor.fetchone()
   user_name = user[0]
   if change_pwd_question == balance and change_pwd_question_2 == user_name:
      new_pwd = input("New password: ")
      hashed = bcrypt.hashpw(
         new_pwd.encode(),
         bcrypt.gensalt()
      )
      cursor.execute("""
            UPDATE Users
            SET Password = ?
            WHERE Username = ?
      """,(hashed, user_name))
      connection.commit()
      print("Your password have been changed successfuly! ✅")
   else:
      print("Error!")
import sqlite3 as sql
import bcrypt
connection = sql.connect("database.db")
cursor = connection.cursor()

print("Welcome, to Opay Terminal app.")
choose = float(input("1. Log in.\n2. Register.\n3. Reset password\n"))
if choose == 1:
  username = str(input("Username: "))
  password = str(input("Password: "))
  user_name = username

  cursor.execute("""
      SELECT Username, Balance, Password
      FROM Users
      WHERE Username = ?
      OR Password = ?
    """, (username, password))

  user = cursor.fetchone()

  if user:
      stored_bash = user[2]
      if bcrypt.checkpw(password.encode(), stored_bash):
        opening_balance = get_balance(username)
        print("Welcome, ", user_name, ". \nBalance: ", opening_balance)
        choice = float(input("1. Withdraw\n2. Deposit money\n"))
        if choice == 1:
           bank_action()
        if choice == 2:
           deposit_money()
      else:
         print("Wrong password!")

  else:
     print("Error")

elif choose == 2:
   username = input("Choose a Username: ")
   password = input("Choose a Password: ")
   confirm = input("Confirm password: ")
   if password != confirm:
      print("Password does not match.")
   else:
      cursor.execute("""
          SELECT *
          FROM Users
          WHERE Username = ?
        """, (username,))
      existing_user = cursor.fetchone()
      hashed = bcrypt.hashpw(
         confirm.encode(),
         bcrypt.gensalt()
      )
      if existing_user:
         print("Username already exists.Please try another username")
      else:
         cursor.execute("""
            INSERT INTO Users
            (Username, Password)
            VALUES(?, ?)
          """, (username, hashed))
         connection.commit()
         code_to_continue = "#opay~yt63#"
         choice_to_continue= input("Your account has been registered.\nEnter '#opay~yt63#' to start using opay now!\nPlus 💵 20000 free, to start off with.\nEnter the code: ")
         user_name = username
         if choice_to_continue == code_to_continue:
            opening_balance = get_balance(username)
            print("Welcome, ", user_name, "\nBalance: ", opening_balance)
            choice = float(input("1. Withdraw\n2. Deposit money\n"))
            if choice == 1:
               bank_action()
            elif choice == 2:
               deposit_money()
elif choose == 3:
   change_pwd()
                
connection.close()
      
  
   

# print("Welcome, ", user_name, ". \nBalance: ", opening_balance)
# Your account has been registered.\n
          # Enter '#opay~yt63#' to start using opay now!\n 
          # + 💵20000 free, to start off with.
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
           
           
           
           

 


