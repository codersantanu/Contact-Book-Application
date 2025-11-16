from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_this'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'santanu@2006AI'
app.config['MYSQL_DB'] = 'contact_book'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM contacts ORDER BY name")
    contacts = cursor.fetchall()
    cursor.close()
    return render_template('index.html', contacts=contacts)

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
    app.run(host='0.0.0.0', port=5000,debug=True)
