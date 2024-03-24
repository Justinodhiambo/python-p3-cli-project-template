# Directory: lib/db/models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    expenses = relationship('Expense', back_populates='category')

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category', back_populates='expenses')
