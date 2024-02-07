from itertools import permutations
def print_permutations(input_string):
    # Generate all permutations of the input string and print each one
    for permute in permutations(input_string):
        for char in permute:
            print(char, end='')
        print()

# Take input from the user
user_input = input("Enter a string: ")

# Call the print_permutations function
print_permutations(user_input)