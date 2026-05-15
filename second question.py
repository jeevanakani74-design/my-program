# Add Book
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print("Book added:", title)


# Borrow Book
def borrow_book(catalog, borrowed_books, book_id):

    if book_id not in catalog:
        print("Book not found")

    elif book_id in borrowed_books:
        print("Book already borrowed")

    else:
        borrowed_books.append(book_id)
        print("Book borrowed")


# Return Book
def return_book(borrowed_books, book_id):

    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book returned")

    else:
        print("Book was not borrowed")


# Register Member
def register_member(members, member_id):
    members.add(member_id)
    print("Member registered:", member_id)


# Show Available Books
def show_available(catalog, borrowed_books):

    print("\nAvailable Books:")

    for book_id, details in catalog.items():

        if book_id not in borrowed_books:

            title, author, year = details

            print(f"{book_id} - {title} by {author} ({year})")


# Main Function
def main():

    catalog = {}
    borrowed_books = []
    members = set()

    # Adding Books
    add_book(catalog, 1, "Python Basics", "John", 2020)
    add_book(catalog, 2, "C Programming", "David", 2018)
    add_book(catalog, 3, "Data Science", "Smith", 2022)
    add_book(catalog, 4, "Machine Learning", "James", 2021)

    # Register Members
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 101)   # Duplicate ignored by set

    # Borrow Books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    # Return One Book
    return_book(borrowed_books, 1)

    # Show Available Books
    show_available(catalog, borrowed_books)


# Run Program
main()
