
from sqlalchemy.orm import sessionmaker
from .models import Base, Category, Expense
from datetime import datetime

engine = create_engine('sqlite:///budget.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_expense(name, amount):
    category_id = int(input("Enter category ID: "))
    expense = Expense(name=name, amount=amount, category_id=category_id)
    session.add(expense)
    session.commit()
    print("Expense added successfully.")

def list_expenses():
    expenses = session.query(Expense).all()
    for expense in expenses:
        print(f"{expense.name}: ${expense.amount}")

def calculate_total_expenses():
    expenses = session.query(Expense).all()
    total = sum(expense.amount for expense in expenses)
    return total
