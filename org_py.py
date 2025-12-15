import os
import shutil

# Path where your files are located
BASE_PATH = r"C:\Users\suhas_t9klwz0\Downloads\company"

# Loop through all files in the directory
for file in os.listdir(BASE_PATH):
    # Check if file is like 1.py, 2.py, etc.
    if file.endswith(".py") and file[:-3].isdigit():
        number = int(file[:-3])

        # Create folder name Q01, Q02, ...
        folder_name = f"Q{number:02d}"
        folder_path = os.path.join(BASE_PATH, folder_name)

        # Create folder if not exists
        os.makedirs(folder_path, exist_ok=True)

        # Source file path
        source_file = os.path.join(BASE_PATH, file)

        # Destination file path (rename to solution.py)
        destination_file = os.path.join(folder_path, "solution.py")

        # Move and rename the file
        shutil.move(source_file, destination_file)

print("✅ All files organized successfully!")
