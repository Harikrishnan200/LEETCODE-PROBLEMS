#  Custom Sort Strings Based on Length, Then Lexicographically

# Problem: Given a list of strings, sort them by length first, and if two strings have the same length, sort them lexicographically.

# input = ['apple', 'banana', 'kiwi', 'orange', 'grape', 'pear']
# output = ['kiwi', 'pear', 'apple', 'grape', 'banana', 'orange']

from functools import cmp_to_key
def custom_sort(input_list):
    def compare(x, y):
        """
        Custom comparator to determine the order of strings.
        Compare by length first, then lexicographically
        """
        if len(x) < len(y):
            return -1  # x should come before y
        elif len(y) < len(x):
            return 1  # y should come before x
        else:
            if x < y:
                return -1
            elif y < x:
                return 1
            else:
                return 0


    sorted_list = sorted(input_list, key=cmp_to_key(compare))
    return sorted_list

input_list = ['apple', 'banana', 'kiwi', 'orange', 'grape', 'pear']
print("Custom Sorted List:", custom_sort(input_list))
# Output
# Custom Sorted List: ['kiwi', 'pear', 'apple', 'grape', 'banana', 'orange']