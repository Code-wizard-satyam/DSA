def bubble_sort(arr):
    size = len(arr)

    for passes in range(size):
        for j in range(0, size-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


unordered_list = [24,87,97,45,67,98,22,24,56]
ordered_list = bubble_sort(unordered_list)

print("Our shorted list is ", ordered_list)
