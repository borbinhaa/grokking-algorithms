def binary_search(search_list, search_item):
    left  = 0
    right = len(search_list) - 1

    while left <= right:
        middle = (left + right) // 2
        item = search_list[int(middle)]

        if item == search_item:
            return middle
        if item > search_item:
            right = middle - 1
        else:
            left = middle + 1
    return None

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]

    print(binary_search(my_list, 3))
    print(binary_search(my_list, 9))
    print(binary_search(my_list, 4))