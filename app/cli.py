# app/cli.py

import argparse
from datetime import datetime
from app.utils import add_user, add_transaction, get_transactions

def add_user_command(args):
    user = add_user(args.username, args.password, args.email)
    print(f"User '{user.username}' added successfully.")

def add_transaction_command(args):
    date_obj = datetime.strptime(args.date, '%Y-%m-%d').date()
    transaction = add_transaction(args.user_id, args.amount, date_obj, args.description)
    print(f"Transaction added successfully:\n{transaction}")

def list_transactions_command(args):
    transactions = get_transactions()
    if transactions:
        for transaction in transactions:
            print(f"{transaction.date} - {transaction.description}: ${transaction.amount}")
    else:
        print("No transactions found.")

# Create the command-line interface
parser = argparse.ArgumentParser(description="Personal Finance Tracker CLI")
subparsers = parser.add_subparsers()

# Subcommand: add_user
parser_add_user = subparsers.add_parser('add_user', help="Add a new user")
parser_add_user.add_argument('username', type=str, help="Username")
parser_add_user.add_argument('password', type=str, help="Password")
parser_add_user.add_argument('email', type=str, help="Email")
parser_add_user.set_defaults(func=add_user_command)

# Subcommand: add_transaction
parser_add_transaction = subparsers.add_parser('add_transaction', help="Add a new transaction")
parser_add_transaction.add_argument('user_id', type=int, help="User ID")
parser_add_transaction.add_argument('amount', type=float, help="Transaction amount")
parser_add_transaction.add_argument('date', type=str, help="Transaction date (YYYY-MM-DD)")
parser_add_transaction.add_argument('description', type=str, help="Transaction description")
parser_add_transaction.set_defaults(func=add_transaction_command)

# Subcommand: list_transactions
parser_list_transactions = subparsers.add_parser('list_transactions', help="List all transactions")
parser_list_transactions.set_defaults(func=list_transactions_command)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
