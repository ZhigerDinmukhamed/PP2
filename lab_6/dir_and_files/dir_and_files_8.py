import os

def delete_file(file_path):
    try:
        # Check if the path exists
        if os.path.exists(file_path):
            print(f"The file '{file_path}' exists.")

            # Check if the file is readable
            if os.access(file_path, os.R_OK):
                print(f"The file '{file_path}' is readable.")

                # Check if the file is writable
                if os.access(file_path, os.W_OK):
                    print(f"The file '{file_path}' is writable.")

                    # Delete the file
                    os.remove(file_path)
                    print(f"The file '{file_path}' has been deleted.")
                else:
                    print(f"The file '{file_path}' is not writable.")
            else:
                print(f"The file '{file_path}' is not readable.")
        else:
            print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_to_delete = "path/to/your/file.txt"
delete_file(file_to_delete)