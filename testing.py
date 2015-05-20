def count_words(text, words):
    return [w in text.lower() for w in words]

#These "asserts" using only for self-checking and not necessary for auto-testing
print(sum(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})))