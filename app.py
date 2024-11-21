from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Path to CSV file
csv_path = 'Road_Accidents.csv'

# Initialize the database
def init_db():
    conn = sqlite3.connect('accidents.db')
    cursor = conn.cursor()
    
    # Create table for road accidents data if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accidents (
            Reference_Number TEXT PRIMARY KEY,
            State TEXT,
            Area_Name TEXT,
            Traffic_Rules_Violation TEXT,
            Vechile_Load TEXT,
            Time INTEGER,
            Road_Class TEXT,
            Road_Surface TEXT,
            Lighting_Conditions TEXT,
            Weather_Conditions TEXT,
            Person_Type TEXT,
            Sex TEXT,
            Age INTEGER,
            Type_of_Vehicle TEXT,
            Label INTEGER
        )
    ''')
    
    # Create table for user authentication if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Read CSV data
    df = pd.read_csv(csv_path)
    
    # Insert data into the database
    df.to_sql('accidents', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

# Initialize the database on startup
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        state = request.form.get('state')
        area_name = request.form.get('area_name')
        time = request.form.get('time')
        vehicle_load = request.form.get('vehicle_load')

        # Fetch accident record based on user input
        conn = sqlite3.connect('accidents.db')
        cursor = conn.cursor()
        query = '''
            SELECT * FROM accidents
            WHERE State = ? AND Time = ? AND Vechile_Load = ?
        '''
        cursor.execute(query, (state, time, vehicle_load))
        accident_record = cursor.fetchone()
        conn.close()

        # Redirect to the result page if record is found
        if accident_record:
            columns = ['Reference_Number', 'State', 'Area_Name', 'Traffic_Rules_Violation', 'Vechile_Load', 'Time', 'Road_Class', 'Road_Surface', 'Lighting_Conditions', 'Weather_Conditions', 'Person_Type', 'Sex', 'Age', 'Type_of_Vehicle', 'Label']
            result = dict(zip(columns, accident_record))
            return render_template('result.html', result=result)
        else:
            return "No accident record found."

    return render_template('index.html', result="Welcome, " + session['username'] + "!")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Hash the password and insert the new user
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        conn = sqlite3.connect('accidents.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Username already exists!"
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check credentials
        conn = sqlite3.connect('accidents.db')
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Invalid username or password!"
    
    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
