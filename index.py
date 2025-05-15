# Simple Expense Tracker
expenses = []

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Try again.")
        return
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Date: {exp['date']} | Category: {exp['category']} | Amount: ${exp['amount']:.2f} | Description: {exp['description']}")
    print()

def total_by_category():
    if not expenses:
        print("\nNo expenses to summarize.\n")
        return

    category = input("Enter category to total: ")
    total = sum(exp["amount"] for exp in expenses if exp["category"].lower() == category.lower())
    print(f"Total expenses for '{category}': ${total:.2f}\n")

def delete_expense():
    if not expenses:
        print("\nNo expenses to delete.\n")
        return

    view_expenses()
    try:
        idx = int(input("Enter entry number to delete: "))
        if 1 <= idx <= len(expenses):
            deleted = expenses.pop(idx - 1)
            print(f"Deleted: {deleted['description']} - ${deleted['amount']:.2f}\n")
        else:
            print("Invalid entry number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("===== Expense Tracker Menu =====")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
