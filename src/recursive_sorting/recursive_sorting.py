# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    i = 0
    j = 0
    lenA = len(arrA)
    lenB = len(arrB)
    arr = []
    # TO-DO
    while ((i<lenA) and (j<lenB)):
        if arrA[i] < arrB[j]:
            arr.append(arrA[i])
            i = i + 1
        else:
            arr.append(arrB[j])
            j = j + 1
    
    while(i < lenA):
        arr.append(arrA[i])
        i = i + 1

    while(j < lenB):
        arr.append(arrB[j])
        j = j + 1
    return arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:] 

        return merge(merge_sort(left), merge_sort(right))
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
