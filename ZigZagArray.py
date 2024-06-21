# Given an array of distinct elements of size N , the task is to rearrange the elements of the array in a zig-zag fashion so that
# the converted array should be in the below form:

# arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n] .

# TC O(N*log N) and SC O(1)

def zigZag(arr,n):
    arr.sort()
    for i in range(1,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]

    return arr

arr = [5,8,2,4,6,1]
length = len(arr)
print(zigZag(arr,length))

# Output: [1, 4, 2, 6, 5, 8]

#Optimized code
# TC O(N) and SC O(1)

def zigZag(arr,n):
    flag = True  # flag = True represents even indexes  arr[0] < arr[1] > arr[2]
    for i in range(n-1):

        if flag is True:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        else:                      # flag = False represents odd indexes
                if arr[i] < arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
        flag = not flag
    return arr


arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
print(zigZag(arr, n))