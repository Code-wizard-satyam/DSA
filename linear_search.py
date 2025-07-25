def linear_search(arr, trgt):
    index = -1
    for i in arr:
        index+=1
        if i == trgt:
            return index
    return index


lis = [13, 35, 63, 70, 23]
target = 70

print(linear_search(lis, target))