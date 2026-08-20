from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3 as sql
import bcrypt



app = Flask(__name__)

app.secret_key = "maduka_learning_flask_secret_key_123"

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    conn = sql.connect('database.db')
    cur = conn.cursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        initial_deposit = float(request.form['initial_deposit'])
        age = int(request.form['age'])
        country = request.form['country']
        free_initial_deposit = initial_deposit + 20000
        
        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )
        cur.execute("""
            SELECT *
            FROM Users
            WHERE Username = ?
            """, (username, ))
        existing_user = cur.fetchone()
        if existing_user:
            conn.close()
            return render_template('signup.html', error = 'Username already exists!')
        else:
            # 1. First Insert: Users table
            cur.execute("""
                INSERT INTO Users(Username, Password, Balance)
                VALUES(?, ?, ?)
            """, (username, hashed, free_initial_deposit))
            # 2. Get the generated UserID
            new_user_id = cur.lastrowid
            # 3. Second Insert: User_Info table using the Foreign Key
            cur.execute("""
                INSERT INTO User_Info(ID, Age, Country)
                VALUES (?, ?, ?)
            """, (new_user_id, age, country))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
    conn.close()
    return render_template('signup.html')

@app.route("/error_page")
def error_page():
    return render_template('error_page.html')

@app.route("/dashboard")
def dashboard():
    # 1. Check if user is loggen in
    if 'username' not in session:
        return redirect(url_for('login'))
    # 2. Retrieve logged-in username from session
    username = session['username']

    # 3. Query the database for this specific user's info
    conn = sql.connect('database.db')
    cur = conn.cursor()


    cur.execute("""
        SELECT Username, Age, Country, Balance
        FROM Users
        JOIN User_Info
        ON User_Info.ID = Users.UserID
        WHERE Username = ?
        """, (username,))
    user_info = cur.fetchone()
    conn.close()
    if user_info:
        user_balance = user_info[3]
        user_country = user_info[2]
        user_age = user_info[1]
    else:
        # Fallbacks if columns/user are missing
        user_balance, user_country, user_age = 0.0, "N/A", 0

    # 4. Pass the database values to the template    
    return render_template(
        'dashboard.html',
        balance = user_balance,
        username_1 = username,
        age = user_age,
        country = user_country

                           )

@app.route("/login", methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute("""
            SELECT Password, Username
            FROM Users
            WHERE Username = ?
        """, (username, ))
        user = cur.fetchone()
        conn.close()
        stored_hash = user[0]
        if bcrypt.checkpw(password.encode(), stored_hash):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('error_page'))
    elif request.method == 'GET':
        print("Hello, Using Get")
    else:
        return render_template('error_page.html')
    return render_template('login.html')


@app.route('/deposit', methods = ['GET', 'POST'])
def deposit():
    conn = sql.connect('database.db')

    cur = conn.cursor()

    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']

    if request.method == 'POST':
        amount = float(request.form['amount'])
        cur.execute("""
                SELECT Balance
                FROM Users
                WHERE Username = ?

            """, (username, ))
        row = cur.fetchone()
        user_balance = row[0]

        new_balance = user_balance + amount

        cur.execute("""
            UPDATE Users
            SET Balance = ?
            WHERE Username = ?
        """, (new_balance, username))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    cur.execute("""
            SELECT Balance
            FROM Users
            WHERE Username = ?

            """, (username, ))
    row = cur.fetchone()
    user_balance = row[0]
    conn.close()
    return  render_template('deposit.html', balance = user_balance)


@app.route('/withdraw', methods = ['GET', 'POST'])
def withdraw():
    conn = sql.connect('database.db')

    cur = conn.cursor()


    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    if request.method == 'POST':
        amount = float(request.form['amount'])

        cur.execute("""
            SELECT Balance
            FROM Users
            WHERE Username = ?
        """, (username, ))
        row = cur.fetchone()
        balance = row[0]
        if amount <= balance:

             new_balance = balance - amount
             cur.execute("""
            UPDATE Users
            SET Balance = ?
            WHERE Username = ?
            """, (new_balance, username))
             conn.commit()
             conn.close()
             return redirect(url_for('dashboard'))
        elif amount > balance:
            return render_template(
                'withdraw.html', 
                balance = balance,
                error = 'Insuficient Funds!'
                                   )
        else:
            return redirect(url_for('dashboard'))

    cur.execute("""
        SELECT Balance
        FROM Users
        WHERE Username = ?
        """, (username, ))
    row = cur.fetchone()
    user_balance = row[0]
    conn.close()
    return render_template('withdraw.html', balance = user_balance)




if __name__ == '__main__':
    app.run(port=3000, debug=True)

