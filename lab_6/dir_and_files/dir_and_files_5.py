def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"The list has been successfully written to the file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

output_file_path = "output.txt"
my_list = ["Item 1", "Item 2", "Item 3", "Item 4"]

write_list_to_file(output_file_path, my_list)