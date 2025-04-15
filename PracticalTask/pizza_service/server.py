from flask import Flask, request, jsonify, abort
import uuid
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

MENU_FILE = 'data/menu.json'
ORDERS_FILE = 'data/orders.json'
USERS_FILE = 'data/users.json'

def load_data(file_path, default):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return default

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


@app.route('/menu', methods=['GET'])
def list_menu():
    menu = load_data(MENU_FILE, [])
    return jsonify(menu)

@app.route('/menu', methods=['POST'])
def add_pizza():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if token != ADMIN_TOKEN:
        abort(401, description="Unauthorized")
    data = request.json
    menu = load_data(MENU_FILE, [])
    pizza = {
        "id": str(uuid.uuid4()),
        "name": data["name"],
        "price": data["price"]
    }
    menu.append(pizza)
    save_data(MENU_FILE, menu)
    return jsonify(pizza), 201

@app.route('/menu/<pizza_id>', methods=['DELETE'])
def delete_pizza(pizza_id):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if token != ADMIN_TOKEN:
        abort(401, description="Unauthorized")
    menu = load_data(MENU_FILE, [])
    menu = [p for p in menu if p['id'] != pizza_id]
    save_data(MENU_FILE, menu)
    return '', 204


@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    orders = load_data(ORDERS_FILE, [])
    order = {
        "id": str(uuid.uuid4()),
        "name": data["name"],
        "address": data["address"],
        "pizza_id": data["pizza_id"],
        "status": "pending"
    }
    orders.append(order)
    save_data(ORDERS_FILE, orders)
    return jsonify(order), 201

@app.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    orders = load_data(ORDERS_FILE, [])
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        abort(404, description="Order not found")
    return jsonify(order)

@app.route('/order/<order_id>', methods=['DELETE'])
def cancel_order(order_id):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    orders = load_data(ORDERS_FILE, [])
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        abort(404, description="Order not found")

    is_admin = token == ADMIN_TOKEN
    if not is_admin and order['status'] == 'ready_to_be_delivered':
        abort(400, description="Order already prepared and cannot be cancelled")

    orders = [o for o in orders if o['id'] != order_id]
    save_data(ORDERS_FILE, orders)
    return '', 204


@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if not data.get("name") or not data.get("address"):
        abort(400, description="Missing name or address")

    users = load_data(USERS_FILE, [])
    existing = next((u for u in users if u["name"] == data["name"]), None)
    if existing:
        abort(400, description="User already exists")

    user = {
        "id": str(uuid.uuid4()),
        "name": data["name"],
        "address": data["address"]
    }
    users.append(user)
    save_data(USERS_FILE, users)
    return jsonify(user), 201

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)
