"""
Given a sentence, reverse the order of its words without 
affecting the order of letters within the given word.

Example 1:
input: "Reverse this string"
output: string this Reverse"

Example 2:
input: "   MULTIPLE SPACES   "
output: "SPACES MULTIPLE"

Example 3:
input: "I have 3 cats and a dog"
output: "dog 1 and cats 3 have I"
"""

# trim the string
# reverse the entire string
# creates 2 pointers (start, end)
# start iterating
# when end points to a space, reverse the word (start, end - 1)
# set start and end to the start index of the next word


def clean_string_and_reverse(sentence):
    """clean string of extra spaces"""
    sentence = sentence.strip()
    result = ""
    is_prev_space = False

    for char in sentence:
        if char != " ":
            result += char
            is_prev_space = False
        else:
            if not is_prev_space:
                result += char
            is_prev_space = True

    return result[::-1]


def reverse_words(sentence):
    """returns the reverse word"""
    sentence = clean_string_and_reverse(sentence)

    sentence = list(sentence)
    start = 0

    for end in range(0, len(sentence) + 1):
        if end == len(sentence) or sentence[end] == " ":
            start_word = start
            end_word = end - 1
            while start_word <= end_word:
                sentence[start_word], sentence[end_word] = sentence[end_word], sentence[start_word]
                start_word += 1
                end_word -= 1
            start = end + 1
    return "".join(sentence)


print(reverse_words("we love python"))
