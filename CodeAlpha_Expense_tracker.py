class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        self.expenses.append({"description": description, "amount": amount, "category": category})

    def view_expenses(self):
        print("\nExpense List:")
        for expense in self.expenses:
            print(f"{expense['description']}: ${expense['amount']} ({expense['category']})")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal expenses: ${total}")

    def category_expenses(self):
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            category_totals[category] = category_totals.get(category, 0) + amount
        
        print("\nCategory-wise Expenses:")
        for category, total in category_totals.items():
            print(f"{category}: ${total}")

    def summary(self):
        self.total_expenses()
        self.category_expenses()


def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category-wise Expenses")
        print("5. Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            tracker.add_expense(description, amount, category)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            tracker.category_expenses()
        elif choice == '5':
            tracker.summary()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
