word = input()

word_length = len(word)
number_of_stars = word_length - 4

first_two_characters = word[:2]
last_two_characters = word[word_length - 2:]

result = first_two_characters + "*" * number_of_stars + last_two_characters
print(result)
