def selection_sort(arr):
    size =len(arr)
    min_index = 0
    start = 0

    for passes in range(size):
        print("Pass: ", passes)
        for j in range(start, size-1):
            if arr[j] < arr[min_index]:
                min_index = j
                print("Minimun Number:", arr[min_index])

            arr[start], arr[min_index] = arr[min_index], arr[start]
            print("Arr: ", arr)
        start += (passes + 1)


unordered_list = [4,2,3,1,5,7,6]
result = selection_sort(unordered_list)

print("The ordered list is" , result)