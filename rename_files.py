import os
from datetime import datetime

def rename_files(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist. Please check the path.")
        return

    try:
        files = os.listdir(folder_path)
        
        if not files:
            print("Warning: No files found in the folder.")
            return
        
        for index, file in enumerate(files):
            old_path = os.path.join(folder_path, file)

            # Skip directories
            if not os.path.isfile(old_path):
                continue

            # Generate a new file name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_extension = os.path.splitext(file)[1]
            new_name = f"renamed_{index}_{timestamp}{file_extension}"
            new_path = os.path.join(folder_path, new_name)

            # Rename the file
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {file} -> {new_name}")
            except PermissionError:
                print(f"Error: Permission denied for {file}. It might be open in another program.")
            except Exception as e:
                print(f"Error renaming {file}: {e}")

    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' was not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    folder_to_rename = "C:/Users/Musti/Documents/TestFiles"  # Change to your folder path
    rename_files(folder_to_rename)
