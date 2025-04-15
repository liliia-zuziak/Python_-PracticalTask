# Pizza Ordering CLI & API

This Python-based system lets users place pizza orders via a REST API and command-line interface.  
Admins can manage the pizza menu using a secure token. User registration and order tracking are supported.

---

## Server Setup

### Run the Flask server

```bash
python3 server.py
```

---

## API Endpoints

### Register a User

```bash
curl -X POST http://127.0.0.1:5000/register \
-H "Content-Type: application/json" \
-d '{"name": "Alina", "address": "Dnipro, vul. Polia, 18"}'
```

---

### List Menu

```bash
curl http://127.0.0.1:5000/menu
```

---

### Add Pizza (Admin Only)

```bash
curl -X POST http://127.0.0.1:5000/menu \
-H "Authorization: Bearer supersecrettoken" \
-H "Content-Type: application/json" \
-d '{"name": "Margherita", "price": 115}'
```

---

### Delete Pizza

```bash
curl -X DELETE http://127.0.0.1:5000/menu/<pizza_id> \
-H "Authorization: Bearer supersecrettoken"
```

---

### Create Order

```bash
curl -X POST http://127.0.0.1:5000/order \
-H "Content-Type: application/json" \
-d '{"name": "Olena", "address": "Odesa, vul. Derybasivska, 5", "pizza_id": "<pizza_id>"}'
```

---

### Check Order Status

```bash
curl http://127.0.0.1:5000/order/<order_id>
```

---

### Cancel Order

```bash
# For customer
curl -X DELETE http://127.0.0.1:5000/order/<order_id>

# For admin
curl -X DELETE http://127.0.0.1:5000/order/<order_id> \
-H "Authorization: Bearer supersecrettoken"
```

---

## CLI Commands

### List Menu

```bash
python3 cli.py list-menu
```

---

### Add Pizza (Admin)

```bash
python3 cli.py add-pizza --name "Four Cheese" --price 140 --token supersecrettoken
```

---

### Delete Pizza (Admin)

```bash
python3 cli.py delete-pizza --pizza_id <id> --token supersecrettoken
```

---

### Create Order

```bash
python3 cli.py create-order --name "Andrii" --address "Kharkiv, vul. Sumska, 30" --pizza_id <id>
```

---

### Check Order

```bash
python3 cli.py check-order --order_id <id>
```

---

### Cancel Order

```bash
# For customer
python3 cli.py cancel-order --order_id <id>

# For admin
python3 cli.py cancel-order --order_id <id> --token supersecrettoken
```

---


