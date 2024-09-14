
#Using Two pointer approach 

def reverse_string(s):
    s_list = list(s)   # string is immutable. SO, we need to convert it to a list

    low = 0
    high = len(s) - 1
    while low < high:
        s_list[low],s_list[high] = s_list[high],s_list[low]
        low += 1
        high -= 1
    return ''.join(s_list)

s = "hello"
print(reverse_string(s))
    