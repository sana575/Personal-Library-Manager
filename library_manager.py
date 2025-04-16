import os

# 📂 Function to load library from file
def load_library():
    library = []
    # Check if the file exists
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            for line in file:
                # Strip whitespace and skip empty lines
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                # Split the line into components
                parts = line.split(" | ")
                if len(parts) == 5:  # Ensure the line has exactly 5 parts
                    title, author, year, genre, read_status = parts
                    library.append({
                        "title": title,
                        "author": author,
                        "year": int(year),
                        "genre": genre,
                        "read_status": read_status == "True"
                    })
                else:
                    print(f"⚠️ Skipping invalid line in library.txt: {line}")
    else:
        # Create an empty file if it doesn't exist
        with open("library.txt", "w") as file:
            print("Intialized an empty 'library.txt' file.")
    return library

# 💾 Function to save library to file
def save_library(library):
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{book['read_status']}\n")

# 📚 Function to display all books
def display_all_books(library):
    if not library:
        print("\n📚 Your library is empty. Add some books! 📚\n")
        return
    print("\n📚 Your Library: 📚")
    for idx, book in enumerate(library, start=1):
        read_status = "📖 Read" if book["read_status"] else "❌ Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# ➕ Function to add a book
def add_book(library):
    title = input("📝 Enter the book title: ").strip()
    author = input("🖋️ Enter the author: ").strip()
    year = int(input("📅 Enter the publication year: "))
    genre = input("🎭 Enter the genre: ").strip()
    read_status = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    })
    print("🎉 Book added successfully! 🎉\n")

# ➖ Function to remove a book
def remove_book(library):
    title = input("🗑️ Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("🗑️ Book removed successfully! 🗑️\n")
            return
    print("⚠️ Book not found. ⚠️\n")

# 🔍 Function to search for a book
def search_book(library):
    print("🔍 Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        query = input("📝 Enter the title: ").strip().lower()
        matches = [book for book in library if query in book["title"].lower()]
    elif choice == "2":
        query = input("🖋️ Enter the author: ").strip().lower()
        matches = [book for book in library if query in book["author"].lower()]
    else:
        print("⚠️ Invalid choice. Please try again. ⚠️\n")
        return
    if matches:
        print("\n🔍 Matching Books: 🔍")
        for idx, book in enumerate(matches, start=1):
            read_status = "📖 Read" if book["read_status"] else "❌ Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("⚠️ No matching books found. ⚠️\n")

# 📊 Function to display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("\n📊 No books in the library. Add some books! 📊\n")
        return
    read_books = sum(1 for book in library if book["read_status"])
    percentage_read = (read_books / total_books) * 100
    print(f"\n📊 Total books: {total_books}")
    print(f"📊 Percentage read: {percentage_read:.1f}% 📊\n")

# 🌟 Main function
def main():
    print("🌟 Welcome to your Personal Library Manager! 🌟\n")
    # Load the library and create library.txt if it doesn't exist
    library = load_library()
    while True:
        print("📋 Menu:")
        print("1. ➕ Add a book")
        print("2. ➖ Remove a book")
        print("3. 🔍 Search for a book")
        print("4. 📚 Display all books")
        print("5. 📊 Display statistics")
        print("6. 🚪 Exit")
        choice = input("👉 Enter your choice: ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved to file. Goodbye! 👋\n")
            break
        else:
            print("⚠️ Invalid choice. Please try again. ⚠️\n")

if __name__ == "__main__":
    main()
