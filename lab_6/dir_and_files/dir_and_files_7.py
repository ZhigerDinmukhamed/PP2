import shutil

def copy_file(source_file, destination_file):
    try:
        shutil.copy(source_file, destination_file)
        print(f"Contents of '{source_file}' successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: One or both of the files do not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file_path = "source.txt"
destination_file_path = "destination.txt"

copy_file(source_file_path, destination_file_path)