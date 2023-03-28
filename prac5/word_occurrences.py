
# Initialize the text
text = input("Text: ")

# Store words in a dictionary
words = {}

# Split the text into individual words
for word in text.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# Find length of longest word
longest_word = 0
for word in words:
    if len(word) > longest_word:
        longest_word = len(word)

# Output the words and their occurrences
for word, count in sorted(words.items()):
    print(f"{word:{longest_word}} : {count}")