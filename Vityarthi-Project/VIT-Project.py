print("Name : Saumya Sopan Bari")
print("Registration no. : 25MIM10064")
print("----------------------------------------------")

def add_expense(expenses):
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount. Enter a number.")

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    note = input("Enter note/description: ")

    expenses.append({
        "amount": amount,
        "date": date,
        "category": category,
        "note": note
    })
    print("Expense added.\n")


def show_expenses(expenses):
    if not expenses:
        print("No expenses.\n")
        return

    print(f"{'No.':<4} {'Date':<12} {'Category':<15} {'Amount':<10} {'Note'}")
    print("-" * 70)
    for i, e in enumerate(expenses, start=1):
        print(f"{i:<4} {e['date']:<12} {e['category']:<15} {e['amount']:<10} {e['note']}")
    print()


def total_spent(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: {total}\n")


def total_by_category(expenses):
    cat = input("Enter category to check: ")
    total = sum(e["amount"] for e in expenses if e["category"].lower() == cat.lower())
    print(f"Total spent in {cat}: {total}\n")


def show_stats(expenses):
    if not expenses:
        print("No expenses.\n")
        return

    amounts = [e["amount"] for e in expenses]
    print(f"Maximum expense: {max(amounts)}")
    print(f"Minimum expense: {min(amounts)}")
    print(f"Average expense: {sum(amounts) / len(amounts):.2f}\n")


def delete_expense(expenses):
    show_expenses(expenses)
    if not expenses:
        return

    try:
        idx = int(input("Enter expense number to delete: "))
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            print(f"Deleted expense: {removed}")
        else:
            print("Invalid expense number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def edit_expense(expenses):
    show_expenses(expenses)
    if not expenses:
        return

    try:
        idx = int(input("Enter expense number to edit: "))
        if 1 <= idx <= len(expenses):
            expense = expenses[idx - 1]

            print("Leave input blank to keep current value.")
            new_amount = input(f"Enter new amount ({expense['amount']}): ")
            if new_amount:
                try:
                    expense['amount'] = float(new_amount)
                except ValueError:
                    print("Invalid amount entered, keeping original.")

            new_date = input(f"Enter new date ({expense['date']}): ")
            if new_date:
                expense['date'] = new_date

            new_category = input(f"Enter new category ({expense['category']}): ")
            if new_category:
                expense['category'] = new_category

            new_note = input(f"Enter new note ({expense['note']}): ")
            if new_note:
                expense['note'] = new_note

            print("Expense updated.\n")
        else:
            print("Invalid expense number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    expenses = []
    while True:
        print("==== PERSONAL EXPENSE TRACKER ====")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Show total spent")
        print("4. Show total by category")
        print("5. Show stats (max/min/avg)")
        print("6. Delete an expense")
        print("7. Edit an expense")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_spent(expenses)
        elif choice == "4":
            total_by_category(expenses)
        elif choice == "5":
            show_stats(expenses)
        elif choice == "6":
            delete_expense(expenses)
        elif choice == "7":
            edit_expense(expenses)
        elif choice == "0":
            print("------------------- Have a Nice Day ------------------------")
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
