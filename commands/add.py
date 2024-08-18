from .utils import read_expenses, write_expenses
from datetime import datetime
from rich import print

def add_expense(description, amount):
    if amount <= 0:
        print("Amount must be [bold green]greater[/bold green] than 0.")
        return
    
    try:
        amount = float(amount)
        if round(amount, 2) != amount:
            raise ValueError("Amount must have at most two decimal places.")
    except ValueError as e:
        print(f"[bold red]{e}[/bold red]")
        return

    expenses = read_expenses()

    if len(expenses) == 0:
        expense_id = 1
    else:
        expense_id = expenses[-1]['id'] + 1

    expenses.append({
        'id': expense_id,
        'date': datetime.now().isoformat(), 
        'description': description, 
        'amount': amount
        })
    
    write_expenses(expenses)
    print(f"Expense [bold green]added[/bold green] successfully (ID: {expense_id})")