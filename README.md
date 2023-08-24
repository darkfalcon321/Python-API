# Python-API
This is a basic python API to understand the working of API. A micro web framework *flask* library is used to set up a server and is backed up with a database with the help of *mysql.connector* library.

## Flask Routes
Contains mainly 3 Directories.

### Root Directory
'/' 
The main route which the user would be led to at first. It would contain the link to the other Directories.

### Products Directory
'/products'
It contains the list of all the mock data pre-inputed in the mysql database. There is an HTML textbox given below to search for the details of any product using their product ID. 

### Single Product Directory
'/product/<int:product_id>'
Shows the detail of a single product in json format with the help of *jsonify* library. Based on the product ID inputed in the textbox in the /products route, the user would be redirected to another route where they would be displayed the product information in json format.
#### Example
```
{
  "description": "Best For Gaming",
  "name": "Laptop",
  "price": 200,
  "product_id": 1
}
```
