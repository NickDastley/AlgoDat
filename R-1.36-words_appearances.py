# P-1.36 Write a Python program that inputs a list of words,
# separated by whitespace, and outputs how many times each word appears in the list.
# You need not worry about efficiency at this point, however,
# as this topic is something that will be addressed later in this book.

def calculate_word_appearances(string_of_words):
    splitted = string_of_words.split(' ')
    unique_words = {}

    for word in splitted:
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1
    print(unique_words)

calculate_word_appearances("Ich Ich hab hab nie nie nie nie nie Döner gegessen")