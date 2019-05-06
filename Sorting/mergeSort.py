"""

Implementation of merge sort

"""

def mergeSort(arr):

    n = len(arr)

    if n > 1:

        # spit
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        # sort
        mergeSort(left)
        mergeSort(right)

        """
        # merge
        i1 = 0
        i2 = 0
        for i in range(0, n):

            if i2 >= len(right) or (i1 < len(left) and left[i1] < right[i2]):
                arr[i] = left[i1]
                i1 = i1 + 1
            else:
                arr[i] = right[i2]
                i2 = i2 + 1
        """

        # Merge part 2:
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


a = [1,5,3,2,0]
alist = [54,26,93,17,77,31,44,55,20]

mergeSort(alist)
mergeSort(a)

print(alist)
print(a)
