import mysql.connector
from flask import Flask, jsonify, url_for, render_template, request, redirect


#instance of flask
app = Flask(__name__, template_folder='./')


#initializing mysql connection
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=331,
    database='google'
)
db_cursor = db_connection.cursor()


#fetch data from table
db_cursor.execute("SELECT * FROM products")
products=db_cursor.fetchall()

#close database connection
db_cursor.close()
db_connection.close()

#initialize root directory
@app.route('/', methods=["GET"])
def hello():
    products_link = url_for('get_products')
    return f'Welcome to products list. Click <a href="{products_link}">here</a> to view the product' 


@app.route('/products', methods=['GET'])
def get_products():
    home_link=url_for('hello')
    return render_template('products.html', products= products, home=home_link)


@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    if product_id == 0:
        submitted_product_id = request.args.get('product_id')

        try:
            if submitted_product_id:
                submitted_product_id = int(submitted_product_id)
                # Redirect to the URL with the correct product_id in the path
                return redirect(url_for('get_product', product_id=submitted_product_id))
            else:
                return jsonify({"error": "Product ID is missing"}), 400
        except ValueError:
            return jsonify({"error": "Invalid product ID"}), 400
    else:
        # Handle the case where product_id is not 0
        # Fetch the product details and return a response
        product = next((p for p in products if p[0] == product_id), None)
        if product is not None:
            product_dict = {
                "product_id": product[0],
                "name": product[1],
                "price": product[2],
                "description": product[3]
            }
            return jsonify(product_dict), 200
        else:
            return jsonify({"error": "Product not found"}), 404




if __name__ == '__main__':
    app.run(debug=True)
