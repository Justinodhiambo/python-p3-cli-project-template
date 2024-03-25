from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Category, Expense


engine = create_engine('sqlite:///budget.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def display_menu():
    print("\nBudget Manager CLI\n")
    print("1. Manage Categories")
    print("2. Manage Expenses")
    print("3. Exit")

def manage_categories():
    while True:
        print("\nManage Categories\n")
        print("1. Create Category")
        print("2. Delete Category")
        print("3. View All Categories")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter category name: ")
            category = Category(name=name)
            session.add(category)
            session.commit()
            print("Category created successfully.")
        elif choice == '2':
            category_id = int(input("Enter category ID to delete: "))
            category = session.query(Category).filter_by(id=category_id).first()
            if category:
                session.delete(category)
                session.commit()
                print("Category deleted successfully.")
            else:
                print("Category not found.")
        elif choice == '3':
            categories = session.query(Category).all()
            if categories:
                for category in categories:
                    print(category)
            else:
                print("No categories found.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_expenses():
    while True:
        print("\nManage Expenses\n")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View All Expenses")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            category_id = int(input("Enter category ID: "))
            expense = Expense.create(session, name, amount, category_id)
            print(f"Expense '{expense.name}' added successfully.")
        elif choice == '2':
            expense_id = int(input("Enter expense ID to delete: "))
            Expense.delete(session, expense_id)
            print("Expense deleted successfully.")
        elif choice == '3':
            expenses = Expense.get_all(session)
            if expenses:
                for expense in expenses:
                    print(f"{expense.id}: {expense.name} - {expense.formatted_amount} ({expense.category.name})")
            else:
                print("No expenses found.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            manage_categories()
        elif choice == '2':
            manage_expenses()
        elif choice == '3':
            print("Exiting Budget Manager CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
