def bubble_sort(arr):
    size = len(arr)

    for passes in range(size-1):
        end = size - passes -1
        for j in range(0, end):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


unordered_list = [8,6,9,5,2]
ordered_list = bubble_sort(unordered_list)

print("Our shorted list is ", ordered_list)
