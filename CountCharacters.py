def count_characters(s):
    chars = {}
    for i in s:
        i = i.lower()
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1

    print(chars)

count_characters("Malayalam")


# output:
#{'m': 2, 'a': 4, 'l': 2, 'y': 1}