from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# MySQL Configuration
app.config['MYSQL_HOST'] = os.getenv('DB_HOST', 'localhost')
app.config['MYSQL_PORT'] = int(os.getenv('DB_PORT', 3307))
app.config['MYSQL_USER'] = os.getenv('DB_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DB_NAME', 'contact_book')

mysql = MySQL(app)

# Test database connection on startup
def test_db_connection():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print(f"Host: {app.config['MYSQL_HOST']}")
        print(f"Port: {app.config['MYSQL_PORT']}")
        print(f"User: {app.config['MYSQL_USER']}")
        print(f"Database: {app.config['MYSQL_DB']}")
        return False

@app.route('/')
def index():
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM contacts ORDER BY name")
        contacts = cursor.fetchall()
        cursor.close()
        return render_template('index.html', contacts=contacts)
    except Exception as e:
        flash(f'Database error: {str(e)}', 'error')
        return render_template('index.html', contacts=[])

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email', '')
    
    if name and phone:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
        mysql.connection.commit()
        cursor.close()
        flash('Contact added successfully!', 'success')
    else:
        flash('Please enter both name and phone number', 'error')
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_contact():
    contact_id = request.form.get('contact_id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email', '')
    
    if contact_id and name and phone:
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s", 
                    (name, phone, email, contact_id))
        mysql.connection.commit()
        cursor.close()
        flash('Contact updated successfully!', 'success')
    else:
        flash('Please fill in all required fields', 'error')
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_contact():
    contact_id = request.form.get('contact_id')
    if contact_id:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
        mysql.connection.commit()
        cursor.close()
        flash('Contact deleted successfully!', 'success')
    else:
        flash('No contact selected', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        test_db_connection()
    app.run(host='0.0.0.0', port=5000, debug=True)
