class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, isbn):
        if isbn not in self.books:
            self.books[isbn] = {'title': title, 'author': author}
            print(f"Book '{title}' added to the library.")
        else:
            print(f"Book with ISBN {isbn} already exists in the library.")

    def search_book(self, keyword):
        matching_books = []
        for isbn, book in self.books.items():
            if keyword in book['title'] or keyword in book['author']:
                matching_books.append((isbn, book))
        return matching_books

    def display_books(self):
        print("Library Catalog:")
        for isbn, book in self.books.items():
            print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a book")
        print("2. Search for a book")
        print("3. Display all books")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == "2":
            keyword = input("Enter a keyword to search for a book: ")
            results = library.search_book(keyword)
            if results:
                print("Matching books:")
                for isbn, book in results:
                    print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}")
            else:
                print("No matching books found.")
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
