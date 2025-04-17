# 📚 Personal Library Manager

Welcome to the **Personal Library Manager**, a Python-based application designed to help you organize and track your personal book collection. Effortlessly manage your library with features to add, remove, search, and analyze your books. 🚀

---

## ✨ Features

- **➕ Add Books**: Store detailed information about each book in your library.
- **➖ Remove Books**: Easily delete books that you no longer own or want to track.
- **🔍 Search Books**: Find books by their title or author quickly.
- **📖 Display All Books**: View an organized list of your entire collection.
- **📊 Statistics**: Get insightful stats like total books and percentage of books read.
- **📂 Persistent Storage**: Save your library to a file and access it anytime.

---

## 🔧 Requirements

- **Python**: Version 3.7 or higher

---

## 🚀 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/sana575/personal-library-manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd personal-library-manager
   ```

3. Verify Python installation:

   ```bash
   python --version
   ```

---

## 🌟 Usage

1. Run the application:

   ```bash
   python library_manager.py
   ```

2. Follow the menu options:

   - Add books
   - Remove books
   - Search for books
   - Display your collection
   - View statistics

---

## 📂 File Structure

- **library\_manager.py**: Main application containing all functionality.
- **library.txt**: Data file where your library details are stored.

---

## ⚙️ Imported Libraries

- **`os`**: Used to check if files exist and to handle file paths.
- **`json`**: Facilitates reading and writing of library data in JSON format.

---

## 🌟 Functions Overview

### **File Management**

- **`load_library()`**: Loads the library from `library.txt`. Initializes an empty file if not found.
- **`save_library(library)`**: Saves the current library to `library.txt` persistently.

### **Library Management**

- **`add_book(library)`**: Prompts user to input book details and adds them to the library.
- **`remove_book(library)`**: Removes a book based on its title.
- **`search_book(library)`**: Searches for books by title or author and displays matching results.
- **`display_all_books(library)`**: Displays the complete list of books along with their details.
- **`display_statistics(library)`**: Shows the total number of books and the percentage of books read.

### **Main Function**

- **`main()`**: Runs the program and provides an interactive menu for users to manage their library.

---

---

## 👩‍💻 Author

- **Name**: Sana Ishaq
- **GitHub**: [sana575](https://github.com/sana575)

---

## 🙏 Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request. Let's make this project even better. 🌟

---

## 📜 License

This project is open-source and available under the MIT License.

