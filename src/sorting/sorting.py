# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = l = r = 0

    for i in range(elements):
        if l >= len(arrA):
            merged_arr[i] = arrB[r]
            r += 1
        elif r >= len(arrB):
            merged_arr[i] = arrA[l]
            l += 1
        elif arrA[l] < arrB[r]:
            merged_arr[i] = arrA[l]
            l += 1
        else:
            merged_arr[i] = arrB[r]
            r += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
        
    if len(arr) > 1:
        middle = (len(arr)) // 2
        left = arr[:middle]
        right = arr[middle:]

        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    left = arr[start:mid]
    right = arr[mid:end + 1]
    print(left, right)
    i = l = r = 0

    for i in range(len(arr)):
        if l >= len(left):
            arr[i] = right[r]
            r += 1
        elif r >= len(right):
            arr[i] = left[l]
            l += 1
        elif left[l] < right[r]:
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if len(arr) > 1:
        m = len(arr) // 2
        return merge_in_place(arr, l, m, r)
    return arr
    

