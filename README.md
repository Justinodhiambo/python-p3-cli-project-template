Budget Manager CLI Application

Overview

This project is a CLI application designed to help users manage their budgets effectively. It allows users to track expenses, categorize spending, and calculate total expenses.

Files

cli.py

This file contains the main entry point for the CLI application. It handles user interaction and command-line interface.

models.py

The models.py file defines SQLAlchemy models for managing budget-related data. It includes classes representing entities such as expenses and categories.

seed.py

The seed.py file is a script used to seed the database with initial data. It populates the database tables with sample data for testing purposes.

helpers.py

This file contains helper functions used throughout the application. It includes functions for adding expenses, listing expenses, calculating total expenses, and other utility functions.

Setup

To run the Budget Manager CLI application:
* Clone the repository to your local machine.
* Navigate to the project directory.
* Set up a virtual environment using Pipenv install Activate the virtual environment: pipenv shell Run the CLI application: python cli.py
