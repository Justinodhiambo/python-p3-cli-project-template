from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="expenses")

    @property
    def formatted_amount(self):
        return f"${self.amount:.2f}"

    @classmethod
    def create(cls, session, name, amount, category_id):
        expense = cls(name=name, amount=amount, category_id=category_id)
        session.add(expense)
        session.commit()
        return expense

    @classmethod
    def delete(cls, session, expense_id):
        expense = session.query(cls).filter_by(id=expense_id).first()
        if expense:
            session.delete(expense)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, expense_id):
        return session.query(cls).filter_by(id=expense_id).first()

Category.expenses = relationship("Expense", back_populates="category")
