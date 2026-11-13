from models import Book, Magazine, DVD, Member, LibraryItem


# Create three library items
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 15)
dvd = DVD("Python Course", 3, 120)


# Create two members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)


# 1. Borrowing and error handling

try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())

    bob.borrow(book)

except ValueError as e:
    print("Could not borrow:", e)


# 2. Borrow limit error

try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())

    bob.borrow(dvd)

except ValueError as e:
    print("Could not borrow:", e)


# 3. Returning an item not borrowed

try:
    bob.return_item(book)

except ValueError as e:
    print("Could not return:", e)


# 4. Return item and calculate late fee

fee = alice.return_item(book, days_late=3)
print("Alice returned:", book.title)
print("Late fee: Rs", fee)


# 5. Polymorphism

print("\nLate Fees for 3 Days:")

items = [book, magazine, dvd]

for item in items:
    print(item.describe(), "-> Rs", item.late_fee(3))


# 6. Borrowed items

print("\nAlice's Borrowed Items:", alice.borrowed_titles())
print("Bob's Borrowed Items:", bob.borrowed_titles())


# 7. Encapsulation

print("\nAvailability:", book.is_available())

try:
    print(book.__available)

except AttributeError:
    print("Private attribute cannot be accessed directly")


# 8. Total items

print("Total items created:", LibraryItem.total_items)