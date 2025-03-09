import os
from datetime import datetime

def rename_files(folder_path):
    try:
        files = os.listdir(folder_path)
        for index, file in enumerate(files):
            old_path = os.path.join(folder_path, file)
            
            # Skip if it's not a file
            if not os.path.isfile(old_path):
                continue
            
            # Generate a new file name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_extension = os.path.splitext(file)[1]
            new_name = f"renamed_{index}_{timestamp}{file_extension}"
            new_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    folder_to_rename = "C:/Users/Musti/Documents/TestFiles"  # Change to your folder path
    rename_files(folder_to_rename)
