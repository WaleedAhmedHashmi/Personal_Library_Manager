import json

def load_library(filename):
    try:
        with open("filename", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library(filename, library):
    with open("filename", "w") as file:
        json.dump(library, file)

def display_menu():
    print("Menu")
    print("Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    return input("Enter your choice: ")

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == 'yes'
    library.append({
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    })
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"Book removed successfully!")
            return
    print("Book not found!")

def search_book(library):
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    if choice == '1':
        title = input("Enter the title: ")
        for book in library:
            if book['title'].lower() == title.lower():
                print(f"Matching Books:\n1. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
                return
    elif choice == '2':
        author = input("Enter the author: ")
        for book in library:
            if book['author'].lower() == author.lower():
                print(f"Matching Books:\n1. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
                return
    print("No matching books found!")

def display_all_books(library):
    print("Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

def main():
    filename = 'library.json'
    library = load_library(filename)

    while True:
        choice = display_menu()
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(filename, library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()