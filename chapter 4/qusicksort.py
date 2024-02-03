def quicksort(arr):
    if (len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([]))
print(quicksort([2]))
print(quicksort([2, 5, 3, 10, 9]))
print(quicksort([2, 5, 3, 10, 9, 3]))