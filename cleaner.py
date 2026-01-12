import os
import shutil
import argparse
from datetime import datetime

# Get user home
user_home = os.path.expanduser('~')
DEFAULT_PATH = os.path.join(user_home, 'Downloads')

def organize_by_date(path):
    if not os.path.exists(path):
        print(f"Path not found: {path}")
        return

    print(f"Sorting by date in: {path}")

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isdir(file_path):
            continue

        # Get the modification time
        timestamp = os.path.getmtime(file_path)
        date_obj = datetime.fromtimestamp(timestamp)
        
        # Format: YYYY-MM (e.g., "2025-12")
        folder_name = date_obj.strftime('%Y-%m')

        # Create target folder
        target_dir = os.path.join(path, folder_name)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Move file
        try:
            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f"Moved {filename} -> {folder_name}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?', default=DEFAULT_PATH)
    args = parser.parse_args()
    
    organize_by_date(args.path)
    print("Done!")