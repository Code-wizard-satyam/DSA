def insersion_sort(array):
    n = len(array)

    if n <=1:
        return array
    
    
    for i in range (0,n):
        key = array[i]

        j = i-1
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j-=1

        array[j+1] = key

    return array


array = [12,25,11,34,90,22]
result = insersion_sort(array)
print("Sorted array is", result)