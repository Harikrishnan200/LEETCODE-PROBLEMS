# Given a large string, return a list of small strings
# Example : 
# Input : "This is a large string"
# Output : ['This', 'is', 'a', 'large', 'string']

def split_words(str):
    words = []
    current_word = ""
    for char in str:
        if char != " ":
            current_word += char
        else:
            if current_word:   # if the current_word is not empty
                words.append(current_word)
                current_word = ""

    if current_word:     # append the last current_word
        words.append(current_word)

    return words

print(split_words("hai hello hi"))



# Simple solution

text = "hai hello hi"
word_list = text.split()
print(word_list)  # Output: ['hai', 'hello', 'hi']
