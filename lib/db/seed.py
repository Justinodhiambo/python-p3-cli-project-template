from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, Expense

engine = create_engine('sqlite:///budget.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def seed_database():
    categories = ["Food", "Transportation", "Utilities"]
    for category_name in categories:
        category = Category(name=category_name)
        session.add(category)
    session.commit()

if __name__ == "__main__":
    seed_database()
