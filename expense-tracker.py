import argparse
from commands.add import add_expense
from commands.list import list_expenses
from commands.summary import show_summary
from commands.delete import delete_expense

# Create the top-level parser
parser = argparse.ArgumentParser(description='Expense Tracker CLI')
subparsers = parser.add_subparsers(dest='command', help='Sub-commands')

# Create the parser for the "add" command
parser_add = subparsers.add_parser('add', help='Add a new expense')
parser_add.add_argument('--categort', required=True, type=str, help='Category of the expense')
parser_add.add_argument('--description', required=True, type=str, help='Description of the expense')
parser_add.add_argument('--amount', required=True, type=float, help='Amount of the expense')

# Create the parser for the "list" command
parser_list = subparsers.add_parser('list', help='List all expenses')

# Create the parser for the "summary" command
parser_summary = subparsers.add_parser('summary', help='Show summary of expenses')
parser_summary.add_argument("--month", type=int, choices=range(1, 13), help="Month (1-12) to filter expenses")

# Create the parser for the "delete" command
parser_delete = subparsers.add_parser('delete', help='Delete an expense')
parser_delete.add_argument('--id', required=True, type=int, help='ID of the expense to delete')

# Parse the arguments
args = parser.parse_args()

match args.command:
    case 'add':
        add_expense(args.description, args.amount)
    case 'list':
        list_expenses()
    case 'summary':
        show_summary(args.month)
    case 'delete':
        delete_expense(args.id)
    case _:
        parser.print_help()