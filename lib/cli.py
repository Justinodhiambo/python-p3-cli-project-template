from helpers import add_expense, list_expenses, calculate_total_expenses
import sys

def main():
    print("Welcome to Budget Manager!")
    while True:
        print("\nSelect an option:")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Calculate total expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            add_expense(name, amount)
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            total = calculate_total_expenses()
            print(f"Total expenses: ${total}")
        elif choice == "4":
            print("Exiting Budget Manager. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
