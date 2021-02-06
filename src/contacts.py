from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Pametros de conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Andres24'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

#Definicion de sesion
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    #return ('Hello')
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    #return 'add contact'    
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

    print(fullname)
    print(phone)
    print(email)

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
    mysql.connection.commit()
    flash('Contact added succesfully')
    #return 'received'
    return redirect(url_for('Index'))


@app.route('/edit_contact')
def edit_contact():
    return 'edit contact'

@app.route('/delete_contact')
def delete_contact():
    return 'borra contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)