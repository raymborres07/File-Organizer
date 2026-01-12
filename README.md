# Automated File Organizer 📂

A robust Python automation script designed to declutter your directories by organizing files into categorized sub-folders based on their extensions.

## 🚀 Features
- **Smart Sorting:** Automatically moves files into categories like `Images`, `Documents`, `Installers`, `Archives`, and `Code`.
- **Cross-Platform:** Works seamlessly on Windows, macOS, and Linux.
- **CLI Support:** Run it on your default "Downloads" folder or specify any target directory via the command line.
- **Safety First:** Skips directories to prevent recursive moving errors and checks for duplicate filenames.

## 🛠️ Built With
- **Python 3.x**
- `os` (Path manipulation)
- `shutil` (File operations)
- `argparse` (Command-line argument parsing)

## 📂 Project Structure
```text
file-organizer/
│
├── cleaner.py        # The main automation script
├── README.md         # Project documentation
├── LICENSE           # MIT License
└── .gitignore        # Git configuration

💻 How to Run
Prerequisites
Ensure you have Python installed on your system.

Bash

python --version
Installation
Clone the repository:

Bash

git clone [https://github.com/YOUR_USERNAME/file-organizer.git](https://github.com/YOUR_USERNAME/file-organizer.git)
Navigate to the project folder:

Bash

cd file-organizer
Usage
Option 1: The Default Mode Running the script without arguments will automatically clean your Downloads folder.

Bash

python cleaner.py
Option 2: The Custom Mode You can specify any folder path you want to organize by adding it after the filename.

Windows Example:

Bash

python cleaner.py "C:\Users\YourName\Desktop"
Mac/Linux Example:

Bash

python cleaner.py /home/username/Desktop
⚙️ Customization
You can easily add new file types or categories. Open cleaner.py and modify the DIRECTORIES dictionary:

Python

DIRECTORIES = {
    'Images': ['.jpg', '.png', '.gif'],
    'MyNewCategory': ['.xyz', '.abc'],  # Add your own here!
    # ...
}
🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

📄 License
This project is open source and available under the MIT License.


### Final Step for the Portfolio
Once you save this file, push the update to GitHub to finalize your documentation:

```bash
git add README.md
git commit -m "Docs: Updated README with CLI usage instructions"
git push