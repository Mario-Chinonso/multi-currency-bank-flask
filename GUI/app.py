# from flask import Flask, render_template
# import sqlite3 as sql

# connection = sql.connect("database.db")

# cursor = connection.cursor()

# cursor.execute("""
#         SELECT Username, Balance
#         FROM Users
#         WHERE UserID = 12
# """)
# user = cursor.fetchone()


# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template(
#         "index.html",
#         username = user[0],
#         balance = user[1]
#         )

# app.run(debug=True)