# File Organizer Pro (GUI Edition) 📂

A user-friendly desktop application that automatically organizes your cluttered folders. Built with Python and Tkinter.

## 🚀 Features
- **Graphical Interface:** Simple point-and-click design. No coding knowledge required to use.
- **Smart Sorting:** Instantly sorts files into `Images`, `Documents`, `Installers`, `Archives`, and `Code`.
- **Safety:** Checks for existing folders and handles errors gracefully.

## 🛠️ Built With
- **Python 3.x**
- **Tkinter** (Standard Python GUI Library)
- `shutil` & `os`

## 💻 How to Run

### Prerequisites
You need Python installed.
python --version

Usage
1. Clone the repository:

git clone [https://github.com/YOUR_USERNAME/file-organizer.git](https://github.com/YOUR_USERNAME/file-organizer.git)

2. Run the application:

python cleaner.py

3. A window will appear:

Click "Browse Folder" to select the directory you want to clean (e.g., Downloads or Desktop).

Click "Start Cleaning" to organize the files.

A popup will confirm how many files were moved.

⚙️ Customization
You can modify the DIRECTORIES dictionary in cleaner.py to add your own categories:

Python

DIRECTORIES = {
    'Images': ['.jpg', '.png'],
    'MyCustomFolder': ['.xyz', '.abc'],
}
📄 License
This project is open source and available under the MIT License.
