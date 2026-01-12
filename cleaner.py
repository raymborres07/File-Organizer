import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# --- CONFIGURATION (Same as before) ---
DIRECTORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp', '.tiff', '.ico'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.ppt', '.xlsx', '.xls', '.csv'],
    'Installers': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.iso'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio_Video': ['.mp3', '.wav', '.mp4', '.mkv', '.mov', '.avi', '.flv'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.h', '.m', '.json', '.java']
}

def clean_folder(path):
    if not path:
        return
    
    count = 0
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        destination_folder = None
        for folder_name, extensions_list in DIRECTORIES.items():
            if extension in extensions_list:
                destination_folder = folder_name
                break

        if destination_folder:
            target_dir = os.path.join(path, destination_folder)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            try:
                shutil.move(file_path, os.path.join(target_dir, filename))
                count += 1
            except Exception as e:
                print(f"Error: {e}")
    
    return count

# --- GUI LOGIC ---
def select_folder():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=f"Selected: {path}")
        run_button.config(state="normal", command=lambda: execute_clean(path))

def execute_clean(path):
    moved_files = clean_folder(path)
    messagebox.showinfo("Success", f"Done! Organized {moved_files} files.")

# --- MAIN WINDOW ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Organizer Pro")
    root.geometry("400x200")

    tk.Label(root, text="Select a folder to organize:", font=("Arial", 12)).pack(pady=10)
    
    path_label = tk.Label(root, text="No folder selected", fg="gray")
    path_label.pack(pady=5)

    btn_browse = tk.Button(root, text="Browse Folder", command=select_folder)
    btn_browse.pack(pady=5)

    run_button = tk.Button(root, text="Start Cleaning", state="disabled", bg="#4CAF50", fg="white")
    run_button.pack(pady=20)

    root.mainloop()