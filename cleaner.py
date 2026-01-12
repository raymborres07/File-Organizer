import os
import shutil

# --- CONFIGURATION ---

# 1. Get the user's home directory automatically
# On Windows, this returns "C:\Users\YourName"
# On Mac/Linux, this returns "/home/username"
user_home = os.path.expanduser('~')

# 2. Join it with the "Downloads" folder
DOWNLOADS_PATH = os.path.join(user_home, 'Downloads')

# 3. Define which extensions go where
DIRECTORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp', '.tiff', '.ico'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.ppt', '.xlsx', '.xls', '.csv'],
    'Installers': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.iso'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio_Video': ['.mp3', '.wav', '.mp4', '.mkv', '.mov', '.avi', '.flv'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.h', '.m', '.json', '.java']
}

# --- FUNCTION DEFINITION ---

def clean_folder(path):
    # Check if path exists
    if not os.path.exists(path):
        print(f"Error: The path {path} does not exist.")
        return
    
    print(f"Scanning directory: {path}...")

    # Loop through all files in the directory
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Skip if it's a directory (we only want to move files)
        if os.path.isdir(file_path):
            continue

        # Get the extension
        _, extension = os.path.splitext(filename)
        
        # Convert to lowercase to handle .JPG vs .jpg
        extension = extension.lower()

        # Check which folder this extension belongs to
        destination_folder = None
        for folder_name, extensions_list in DIRECTORIES.items():
            if extension in extensions_list:
                destination_folder = folder_name
                break

        # If we found a match, move the file
        if destination_folder:
            # Create the sub-folder path
            target_dir = os.path.join(path, destination_folder)
            
            # Create the folder if it doesn't exist yet
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                print(f"Created new folder: {destination_folder}")

            # Move the file
            try:
                shutil.move(file_path, os.path.join(target_dir, filename))
                print(f"Moved: {filename} -> {destination_folder}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

# --- EXECUTION ---

if __name__ == "__main__":
    clean_folder(DOWNLOADS_PATH)
    print("Done!")