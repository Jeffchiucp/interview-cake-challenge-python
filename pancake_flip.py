def flip(arr, i):
    # reverse arr[0...i]
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1


def pancake_sort(arr):
    # the main function that complete sorting
    # start from the array and one by one reduce the current size
    output = []
    curr_size = len(arr) - 1
    # find the index of the maxmium element inside the arr[0..curr_size -1]
    while curr_size > 0:
        mi = findMaxUpTo(arr, curr_size)
        if mi != curr_size:
            flip(arr, mi)
            # once I flip it
            # now move the maximum number to the end by reversing current array
            flip(arr, curr_size)
        curr_size -= 1
    return arr


def findMaxUpTo(arr, rightBound):
    best_index = 0
    max_val = None
    for i in range(rightBound + 1):
        if arr[i] > max_val:
            best_index = i
            max_val = arr[i]
    return best_index


"""
input:  arr = [1, 5, 4, 3, 2]
              [1, 4, 3, 2, 5]

               ^           ^
output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output


"""
arr2 = [1, 5, 4, 3, 2]
test1 = arr2
print(pancake_sort(test1))



"""
# Python3 program to
# sort array using
# pancake sort

# Reverses arr[0..i] */
def flip(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1


# Returns index of the maximum
# element in arr[0..n-1] */
def findMax(arr, n):
    mi = 0
    for i in range(0, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi


# The main function that
# sorts given array
# using flip operations
def pancakeSort(arr, n):
    # Start from the complete
    # array and one by one
    # reduce current size
    # by one
    curr_size = n
    while curr_size > 1:
        # Find index of the maximum
        # element in
        # arr[0..curr_size-1]
        mi = findMax(arr, curr_size)

        # Move the maximum element
        # to end of current array
        # if it's not already at
        # the end
        if mi != curr_size - 1:
            # To move at the end,
            # first move maximum
            # number to beginning
            flip(arr, mi)

            # Now move the maximum
            # number to end by
            # reversing current array
            flip(arr, curr_size - 1)
        curr_size -= 1

"""