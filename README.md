# Campus Library Management System

## Project Description
This is a Python-based Campus Library Management System.
It manages books, magazines, and DVDs using Object-Oriented Programming.

## Features
- Abstract parent class LibraryItem.
- Book, Magazine, and DVD child classes.
- Borrowing and returning items.
- Private item availability and borrowed list.
- Late fee calculation.
- Exception handling.
- Polymorphism and encapsulation.

## Technologies Used
- Python 3.12+
- Object-Oriented Programming

## How to Run
Run the following command:

python main.py

## Reflection Questions

### 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is abstract because it provides common features for all library items. If DVD does not implement late_fee(), Python raises a TypeError when we try to create a DVD object.

### 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Accessing item.__available directly raises an AttributeError. We use is_available() to safely check availability without directly accessing the private attribute.

### 3. What is the difference between LibraryItem.total_items and self.title?

LibraryItem.total_items is a class attribute shared by all library items. self.title is an instance attribute that stores the title of a particular item.

## Author
Ratnesh