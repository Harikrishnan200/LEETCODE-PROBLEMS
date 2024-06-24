# Find the largest index of largest string in an Array of size n.

class Solution:
    def __init__(self):
        self.lengths = []

    def largestString(self, input_list: list):
        for string in input_list:
            length = len(string)
            self.lengths.append(length)

    def print_sorted_lengths(self):
        max_length = max(self.lengths)  # to find the maximum length
        max_index = self.lengths.index(max_length)  # to find the index of the maximum length
        print("Index of the longest string':", max_index+1)

# Example usage:
input_list = ["ab", "abc","hellohowareyou", "qbcd","hellohai"]
sol = Solution()
sol.largestString(input_list)
sol.print_sorted_lengths()


# Output: Index of the longest string: 3

# The time complexity of the code is O(N) where N is the number of strings in the input list. The space complexity of the code is O(1) as we are using a constant amount of space to store the lengths of the strings.


# Another method 
# Optimized code

def find_largest_string(arr):
    if not arr:
        return None  # Return None if the array is empty
    
    largest_str = arr[0]  # Initialize largest_str with the first string
    max_length = len(arr[0])  # Initialize max_length with the length of the first string
    
    for s in arr[1:]:  # Start iterating from the second string in the array
        current_length = len(s)
        if current_length > max_length:
            max_length = current_length
            largest_str = s
    
    return largest_str

# Example usage:
arr = ["apple", "banana", "kiwi", "orange"]
largest_string = find_largest_string(arr)
print("Largest string:", largest_string)  # Output: Largest string: banana


# The time complexity of the code is O(N) where N is the number of strings in the input array. The space complexity of the code is O(1) as we are using a constant amount of space to store the largest string and its length.
