
count = 0
dictionary_words = dict()                   # Initializes the dictionary
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue                        # Discards duplicates
        dictionary_words[word] = count      # Value is first time word appears

if 'Python' in dictionary_words:
    print('True')
else:
    print('False')
