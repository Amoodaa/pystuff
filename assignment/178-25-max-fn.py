def max(list):
    list.sort()
    max_item = list[0]
    for num in list:
        if max_item < num:
            max_item = num
    return max_item


print(max([-1, 1, 3, 4, 18, 9, -5]))
