import argparse
import requests

BASE_URL = "http://127.0.0.1:5000"

def list_menu():
    r = requests.get(f"{BASE_URL}/menu")
    print(r.json())

def create_order(args):
    data = {
        "name": args.name,
        "address": args.address,
        "pizza_id": args.pizza_id
    }
    r = requests.post(f"{BASE_URL}/order", json=data)
    print(r.json())

def check_order(args):
    r = requests.get(f"{BASE_URL}/order/{args.order_id}")
    print(r.json())

def cancel_order(args):
    headers = {}
    if args.token:
        headers["Authorization"] = f"Bearer {args.token}"
    r = requests.delete(f"{BASE_URL}/order/{args.order_id}", headers=headers)
    print("Order cancelled." if r.status_code == 204 else r.text)

def add_pizza(args):
    headers = {"Authorization": f"Bearer {args.token}"}
    data = {"name": args.name, "price": args.price}
    r = requests.post(f"{BASE_URL}/menu", json=data, headers=headers)
    print(r.status_code)
    print(r.text)

def delete_pizza(args):
    headers = {"Authorization": f"Bearer {args.token}"}
    r = requests.delete(f"{BASE_URL}/menu/{args.pizza_id}", headers=headers)
    print("Pizza deleted." if r.status_code == 204 else r.text)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

subparsers.add_parser("list-menu").set_defaults(func=lambda args: list_menu())

order_parser = subparsers.add_parser("create-order")
order_parser.add_argument("--name")
order_parser.add_argument("--address")
order_parser.add_argument("--pizza_id")
order_parser.set_defaults(func=create_order)

check_parser = subparsers.add_parser("check-order")
check_parser.add_argument("--order_id")
check_parser.set_defaults(func=check_order)

cancel_parser = subparsers.add_parser("cancel-order")
cancel_parser.add_argument("--order_id")
cancel_parser.add_argument("--token", default=None)
cancel_parser.set_defaults(func=cancel_order)

add_parser = subparsers.add_parser("add-pizza")
add_parser.add_argument("--name")
add_parser.add_argument("--price", type=float)
add_parser.add_argument("--token")
add_parser.set_defaults(func=add_pizza)

del_parser = subparsers.add_parser("delete-pizza")
del_parser.add_argument("--pizza_id")
del_parser.add_argument("--token")
del_parser.set_defaults(func=delete_pizza)

args = parser.parse_args()
args.func(args)
