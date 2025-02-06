# Pyramid sum ( UST )

#input: arr = [1,2,3]
# output: 8 



def pyramid_sum(arr):
    while len(arr) > 1:
        temp = []
        for i in range(len(arr)-1):
            temp.append(arr[i]+arr[i+1])
        arr = temp
    return arr[0]

print(pyramid_sum([1,2,3]))