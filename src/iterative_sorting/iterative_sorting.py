# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        for j in range (i+1, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j
        if cur_index != i:
            arr[i], arr[cur_index] = arr[cur_index], arr[i]
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range (0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr