library = []

def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print("Book added successfully!")

def issue_book():
    book = input("Enter book name to issue: ")
    if book in library:
        library.remove(book)
        print("Book issued successfully!")
    else:
        print("Book not available!")

def return_book():
    book = input("Enter book name to return: ")
    library.append(book)
    print("Book returned successfully!")

def search_book():
    book = input("Enter book name to search: ")
    if book in library:
        print("Book is available in the library")
    else:
        print("Book not found")

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
