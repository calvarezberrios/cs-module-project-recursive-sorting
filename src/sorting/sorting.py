# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = l = r = 0

    while l < len(arrA) and r < len(arrB):
        if arrA[l] < arrB[r]:
            merged_arr[i] = arrA[l]
            l += 1
        else:
            merged_arr[i] = arrB[r]
            r += 1
        i += 1

    while l < len(arrA):
        merged_arr[i] = arrA[l]
        l += 1
        i += 1

    while r < len(arrB):
        merged_arr[i] = arrB[r]
        r += 1
        i += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    
    
    if len(arr) > 1:
        middle = (len(arr)) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)
        arr = merge(left, right)

    return arr

print(merge_sort([5,3,1,4,2,0,9,8,7,6]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

