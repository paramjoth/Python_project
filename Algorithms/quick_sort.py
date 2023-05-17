# best and avg time complexity: O(n * log(n))
# worst time complexity: O(n *2)

def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    p = arr[right]
    j = right - 1
    while i < j:
        while i < right and arr[i] < p:
            i += 1
        while j > left and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > p:
        arr[i], arr[right] = arr[right], arr[i]

    return i

my_array = [2, 5, 8, 1, 24, 92, 14, 8]
quick_sort(my_array, 0, len(my_array)-1)
print(my_array)
