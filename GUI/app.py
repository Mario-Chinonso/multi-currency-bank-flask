from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3 as sql
import bcrypt
import random



app = Flask(__name__)

app.secret_key = "maduka_learning_flask_secret_key_123"

# Global exchange rates
USD_RATE = 1370.37
CNY_RATE = 201.7386
CND_RATE = 963.76
def update_exchange_rates():
    global USD_RATE, CNY_RATE, CND_RATE
    try:
        # Fetch latest exchange rates relative to USD
        response = requests.get("https://open.er-api.com/v6/latest/USD", timeout=5)
        data = response.json()
        
        if data.get("result") == "success":
            rates = data.get("rates", {})
            
            # 1. Direct USD to NGN rate
            usd_to_ngn = rates.get("NGN")
            if usd_to_ngn:
                USD_RATE = usd_to_ngn

            # 2. CNY to NGN rate (NGN per 1 CNY)
            cny_to_usd = rates.get("CNY")
            if cny_to_usd and cny_to_usd > 0:
                CNY_RATE = USD_RATE / cny_to_usd

            # 3. CAD (CND) to NGN rate (NGN per 1 CAD)
            cad_to_usd = rates.get("CAD")
            if cad_to_usd and cad_to_usd > 0:
                CND_RATE = USD_RATE / cad_to_usd

            print(f"[+] Exchange rates updated: USD={USD_RATE:.2f}, CNY={CNY_RATE:.2f}, CND={CND_RATE:.2f}")
    except Exception as e:
        print(f"[-] Failed to fetch live exchange rates: {e}. Using fallback rates.")
# Fetch rates when starting the server
update_exchange_rates()
@app.context_processor
def inject_exchange_rates():
    return {
        'USD_RATE': round(USD_RATE, 2),
        'CNY_RATE': round(CNY_RATE, 2),
        'CND_RATE': round(CND_RATE, 2)
    }

@app.route('/')
def home():
    return render_template('home.html')

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
    flash('Wrong password or username', 'danger')
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
        flash('You do not have an account', 'danger')
        return redirect(url_for('login'))
    

    # 4. Pass the database values to the template    
    return render_template(
        'dashboard.html',
        balance = user_balance,
        username_1 = username,
        age = user_age,
        country = user_country,
        usd_rate = USD_RATE,
        cny_rate = CNY_RATE,
        cnd_rate = CND_RATE
                        )

@app.route("/login", methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute("""
            SELECT Password, Username, UserID
            FROM Users
            WHERE Username = ?
        """, (username, ))
        user = cur.fetchone()
        conn.close()
        stored_hash = user[0]
        user_id = user[2]
        if bcrypt.checkpw(password.encode(), stored_hash):
            session['username'] = username
            session['user_id'] = user_id
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
    username = session.get('username')

    if request.method == 'POST':
        raw_amount = float(request.form.get('amount', 0))
        currency = request.form.get('currency', 'NGN')
        
        # Convert to Naira
        if currency == 'USD':
            amount_in_naira = raw_amount * USD_RATE
        elif currency == 'CNY':
            amount_in_naira = raw_amount * CNY_RATE
        elif currency == 'CND':
            amount_in_naira = raw_amount * CND_RATE
        else:
            amount_in_naira = raw_amount
        
        # Database Update
        cur.execute("""
                SELECT Balance
                FROM Users
                WHERE Username = ?
            """, (username, ))
        row = cur.fetchone()
        user_balance = row[0]

        new_balance = user_balance + amount_in_naira

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


    if 'username' not in session: # What does this line mean using IT terminologies
        return redirect(url_for('login'))

    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        raw_amount = float(request.form.get('amount', 0))
        currency = request.form.get('currency', 'NGN')

        if currency == 'USD':
            amount_in_naira = raw_amount * USD_RATE
        elif currency == 'CNY':
            amount_in_naira = raw_amount * CNY_RATE
        elif currency == 'CND':
            amount_in_naira = raw_amount * CND_RATE
        else:
            amount_in_naira = raw_amount

        cur.execute("""
            SELECT Balance
            FROM Users
            WHERE Username = ?
        """, (username, ))
        row = cur.fetchone()
        balance = row[0]
        if amount_in_naira <= balance:
             new_balance = balance - amount_in_naira
             cur.execute("""
                 UPDATE Users
                 SET Balance = ?
                 WHERE Username = ?
            """, (new_balance, username))
             conn.commit()
             conn.close()
             return redirect(url_for('dashboard'))
        elif amount_in_naira > balance:
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

@app.route('/reset_pwd', methods = ['GET', 'POST'])
def reset_pwd():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session.get('username')
    if  not username:
        return redirect( url_for('login'))
    conn = sql.connect('database.db')
    cur = conn.cursor()

    if request.method == 'POST':
        current_pwd = request.form.get('current_pwd', 'admin')
        new_pwd = request.form.get('new_pwd', 'admin')
        confirm_pwd = request.form.get('confirm_pwd', 'admin')

        cur.execute("""
            SELECT Password, Username
            FROM Users
            WHERE Username = ?
            """, (username, ))
        user = cur.fetchone()
        stored_hash = user[0]
        if user and bcrypt.checkpw(current_pwd.encode(), stored_hash):
            hashed = bcrypt.hashpw(
                new_pwd.encode(),
                bcrypt.gensalt()
            )
            if confirm_pwd != new_pwd:
                return render_template('reset_pwd.html', error='Passwords do not match')
            cur.execute("""
                    UPDATE Users
                    SET Password = ?
                    WHERE Username = ?
            """, (hashed, username))
            conn.commit()
            conn.close()
            return redirect( url_for('dashboard'))
        else:
            conn.close()
            return render_template(
                'reset_pwd.html',
                error = 'Username or Password does not exists'
                )
    return render_template('reset_pwd.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash("You've successfully logged out.", "info")
    return redirect(url_for('login'))
def generate_account_number(conn: sql.Connection) -> str:
    """Generates a unique 10-digit random account number.

    Ensures the number starts with a non-zero digit and doesn't already exist
    in the database.
    """
    cur = conn.cursor()
    while True:
        # Generates a random integer between 1000000000 and 9999999999
        acc_num = str(random.randint(1000000000, 9999999999))

        # Check if this account number already exists
        cur.execute(
            "SELECT 1 FROM Account_Number WHERE Number = ?", (acc_num,)
        )
        if not cur.fetchone():
            return acc_num
@app.route('/transfer', methods= ['GET', 'POST'])
def transfer():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session.get('username')
    user_id = session.get('user_id')
    if username is None:
        return redirect(url_for('login'))
    if not user_id or not username:
        return redirect(url_for('login'))
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute(
        'SELECT Users.Balance, Account_Number.Number FROM Users JOIN Account_Number ON Account_Number.Number = Users.UserID WHERE Users.UserID = ? AND Users.Username = ?',
        (user_id, username)
    )
    balance = cur.fetchone()[0]
    sender_username = cur.fetchone()[1]
    if request.method == 'POST':
        conn = sql.connect('database.db')
        cur = conn.cursor()
        acc_no = request.form.get('account_number')
        currency = request.form.get('currency')
        raw_amount = float(request.form.get('amount'))

        cur.execute(
            'SELECT Users.UserID, Users.Balance, Account_Number.Number FROM Users JOIN Account_Number' \
            'ON Account_Number.Number = Users.UserID WHERE Account_Number.Number = ?',
            (acc_no, )
        )
        info = cur.fetchone()
        if info:
            if currency == 'USD':
                new_amount = raw_amount * USD_RATE
            elif currency == 'CND':
                new_amount = raw_amount * CND_RATE
            elif currency == 'CNY':
                new_amount = raw_amount * CNY_RATE
            else:
                new_amount = raw_amount
            

    return render_template('transfer.html', balance = balance)

if __name__ == '__main__':
    app.run(port=3000, debug=True)

