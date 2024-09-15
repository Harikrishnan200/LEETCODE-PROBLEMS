# def count_white_spaces(arr):
#     count = 0
#     for i in range(len(arr)-1):
#         if arr[i] == " ":
#             count += 1
#     return count
# print(count_white_spaces("h ari krish nan"))


# TWO POINTER APPROACH

def count_white_spaces(arr):
    count = 0
    left,right = 0,len(arr)-1
    while left <= right:
        if arr[left] == " ":
            count += 1
        if arr[right] == " " and left != right:      # sam ple
            count += 1
        left += 1
        right -= 1
    return count

print(count_white_spaces("s am pl e"))