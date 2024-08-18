from .utils import read_expenses
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import print

def list_expenses():
    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[/bold red]")
        return

    table = Table(title="Expense Summary")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Category", style="yellow")
    table.add_column("Description", style="green")
    table.add_column("Amount", justify="right", style="red")

    for expense in expenses:
        date = datetime.fromisoformat(expense['date']).strftime('%Y-%m-%d')
        amount = f"{expense['amount']:.2f}"
        table.add_row(
            str(expense['id']), 
            date, 
            expense['category'],
            expense['description'],
            f"{amount}")

    console = Console()
    console.print(table)