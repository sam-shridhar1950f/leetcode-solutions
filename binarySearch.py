import math

# Binary Search
array = [1,2,3,4,5,6]
target = 3





def binarySearch(array, target):
    var = 0
    left_pointer = 0
    right_pointer = len(array) - 1
    while(right_pointer >= left_pointer):
        mid = math.floor(left_pointer+(right_pointer-left_pointer)/2)

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1

        var += 1
        print(var) ## Counting
    return -1

result = binarySearch(array, target)

if result != -1:
    print('Element is present at index %d'%result)
else:
    print('Element is not present in the array')

