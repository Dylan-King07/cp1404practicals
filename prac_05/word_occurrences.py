"""
Word Occurrences
Estimated time: 30 minutes
Actual time: 40 minutes
"""

string_input = input("Text: ")
split_string = string_input.split()

count_words = {}
for word in split_string:
    occurrence_of_words = count_words.get(word, 0)
    count_words[word] = occurrence_of_words + 1

longest_word = max(len(word) for word in count_words)

for word in sorted(count_words):
    print(f"{word:{longest_word}} : {count_words[word]}")
