def min_max_elements(arr):
    if len(arr) == 0:
        return "Array is empty"

    min_ele = arr[0]
    max_ele = arr[0]

    for num in arr:
        if num < min_ele:
            min_ele = num
        if num > max_ele:
            max_ele = num

    return [min_ele, max_ele]

arr = [1, 2, 3, 5, -1]
print(min_max_elements(arr))
