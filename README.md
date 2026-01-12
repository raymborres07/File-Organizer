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
```bash
python --version

Usage
Clone the repository:

Bash

git clone [https://github.com/YOUR_USERNAME/file-organizer.git](https://github.com/YOUR_USERNAME/file-organizer.git)
Run the application:

Bash

python cleaner.py
A window will appear:

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