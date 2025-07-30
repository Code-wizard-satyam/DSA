def selection_sort(arr):
    n =len(arr)
    for i in range(n-1):
        min_index = i

        for j in range(i+1,n):
            if (arr[j] < arr[min_index]):
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

unordered_list = [4,2,3,1,5,7,6]
result = selection_sort(unordered_list)

print("The ordered list is" , result)