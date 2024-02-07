def reverse_words(sentence):
    words = sentence.split()
    print(*reversed(words))

user_input = input()

reverse_words(user_input)