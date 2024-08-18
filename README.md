# Expense Tracke CLI

## Description
The Expense Tracker CLI is a Python-based command-line tool designed to help users track their expenses. It leverages the `rich` library to provide a user-friendly interface for adding, viewing, and managing expenses. The tool supports various features such as categorizing expenses, generating reports, and more.

It is inspired from the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) project featured in the [Backend Roadmap](https://roadmap.sh/backend) from [roadmap.sh](https://roadmap.sh/).

## Features
- **Add Expenses**: Easily add new expenses with details such as amount, category, and description.
- **Delete Expenses**: 
- **View Expenses**: Display a list of all recorded expenses.
- **Categorize Expenses**: Organize expenses into different categories for better tracking.
- **Generate Reports**: Create summary reports of expenses over a specified period.

## Prerequisites
- Python 3.6+
- Git

## Installation
1. **Clone the Repository**:
   ``` python
   git clone https://github.com/siamonas/expense-tracker-cli.git
   cd expense-tracker-cli ```
2. Create and Activate a Virtual Environment
   ```sh
   python -m venv venv

   # On Windows:
   .\venv\Scripts\activate

   # On macOS and Linux:
   source venv/bin/activate
3. Install Dependencies
   ```sh
   pip install -r requirements.txt
  
## Usage
1. Run the application
   ```sh
   python expense-tracker-cli -h # Show help
   python expense-tracker add --description "Lunch" --amount 20 # Add an expense
   python expense-tracker add --description "Dinner" --amount 10 # Add another expense
   python expense-tracker list # List all expenses 
   python expense-tracker summary # Show summary of expenses
   python expense-teacker summary --month 8 # Show summary of expenses for specific month
   python expense-tracker delete --id 1 # Delete an expense by ID
