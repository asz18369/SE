from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# 建立MySQL連線
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    port="3306",
    SSL="enable with TLS_AES_256_GCM_SHA384",
    database="final_project"
)

# 路由 - 顯示客戶列表


@app.route('/customers')
def show_customers():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Customers")
    customers = cursor.fetchall()
    return render_template('customers.html', customers=customers)

# 路由 - 顯示添加客戶的頁面


@app.route('/add_customer_page')
def show_add_customer_page():
    return render_template('add_customer.html')

# 路由 - 處理添加客戶的請求

@app.route('/add_customer', methods=['POST'])
def add_customer():
    cursor = db.cursor()
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    family_members = request.form['family_members']
    query = "INSERT INTO Customers (name, address, phone, family_members) VALUES (%s, %s, %s, %s)"
    values = (name, address, phone, family_members)
    cursor.execute(query, values)
    db.commit()
    return 'Customer added successfully!'

# 路由 - 顯示業務員列表


@app.route('/salespersons')
def show_salespersons():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Salespersons")
    salespersons = cursor.fetchall()
    return render_template('salespersons.html', salespersons=salespersons)

# 路由 - 顯示按摩椅列表


@app.route('/massagechairs')
def show_chairs():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM MassageChairs")
    chairs = cursor.fetchall()
    return render_template('chairs.html', chairs=chairs)

# 路由 - 顯示操作列表


@app.route('/operations')
def show_operations():
    cursor = db.cursor()
    cursor.execute("SELECT Operations.operation_id, MassageChairs.style, Operations.quantity, Operations.status FROM Operations JOIN MassageChairs ON Operations.chair_id = MassageChairs.chair_id")
    operations = cursor.fetchall()
    return render_template('operations.html', operations=operations)

# 路由 - 顯示添加業務員的頁面


@app.route('/add_salesperson_page')
def show_add_salesperson_page():
    return render_template('add_salesperson.html')

# 路由 - 處理添加業務員的請求


@app.route('/add_salesperson', methods=['POST'])
def add_salesperson():
    cursor = db.cursor()
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    query = "INSERT INTO Salespersons (name, address, phone) VALUES (%s, %s, %s)"
    values = (name, address, phone)
    cursor.execute(query, values)
    db.commit()
    return 'Salesperson added successfully!'

# 路由 - 顯示添加按摩椅的頁面


@app.route('/add_chair_page')
def show_add_chair_page():
    return render_template('add_chair.html')

# 路由 - 處理添加按摩椅的請求


@app.route('/add_chair', methods=['POST'])
def add_chair():
    cursor = db.cursor()
    style = request.form['style']
    price = request.form['price']
    quantity = request.form['quantity']
    query = "INSERT INTO MassageChairs (style, price, quantity) VALUES (%s, %s, %s)"
    values = (style, price, quantity)
    cursor.execute(query, values)
    db.commit()
    return 'Massage chair added successfully!'

# 路由 - 顯示添加操作的頁面


@app.route('/add_operation_page')
def show_add_operation_page():
    return render_template('add_operation.html')

# 路由 - 處理添加操作的請求


@app.route('/add_operation', methods=['POST'])
def add_operation():
    cursor = db.cursor()
    chair_id = request.form['chair_id']
    quantity = request.form['quantity']
    status = request.form['status']
    query = "INSERT INTO Operations (chair_id, quantity, status) VALUES (%s, %s, %s)"
    values = (chair_id, quantity, status)
    cursor.execute(query, values)
    db.commit()
    return 'Operation added successfully!'


if __name__ == '__main__':
    app.run()
