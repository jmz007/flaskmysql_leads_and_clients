from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
mysql = connectToMySQL('jmzleadgen')

@app.route('/', methods=['GET'])
def index():
    mysql = connectToMySQL('jmzleadgen')
    all_customers = mysql.query_db("SELECT * FROM customers")
    print("Fetched all customers", all_customers)
    return render_template('index.html', customers = all_customers)

@app.route('/adjust_date', methods=['POST'])
def create():
    mysql = connectToMySQL('jmzleadgen')
    query = "INSERT INTO customers (first_name, last_name, leads ) VALUES (%(first_name)s, %(last_name)s, %leads)s);"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'leads': request.form['leads.']
           }
    calenderset = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)