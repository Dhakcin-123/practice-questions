with open('sample.txt', 'w') as file:
    file.write("This is a sample text file. It contains some words for testing.")

with open('sample.txt', 'r') as file:
    content = file.read()

words = content.split()
word_count = len(words)

print("The number of words in the file is:", word_count)