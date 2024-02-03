def sum(arr):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr.pop()

    return arr.pop() + sum(arr);

print("----------- SUM -------------")
print(sum([1, 4, 5]))
print(sum([3, 4, 5]))
print(sum([1]))
print(sum([]))
print("-----------------------------")
print()

def count(arr):
    if not arr:
        return 0
    
    arr.pop()
    return 1 + count(arr)


print("---------- COUNT ------------")
print(count([]))
print(count([1, 3, 5]))
print(count([1, 3, 5, 7, 8]))
print("-----------------------------")
print()

def find_higher(arr):
    if (len(arr)) == 0:
        return None
    elif (len(arr)) == 1:
        return arr[0]
    else:
        max_num = find_higher(arr[1:])
        return arr[0] if arr[0] > max_num else max_num

print("---------- COUNT ------------")
print(find_higher([]))
print(find_higher([1, 3, 5]))
print(find_higher([1, 3, 5, 7, 8]))
print("-----------------------------")
print()
