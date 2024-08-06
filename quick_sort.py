def quicksort(arr):
    
    if (len(arr) <= 1):
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    arr = [ 3, 4, 9, 1, 2, 88, 34, 78]
    print(quicksort(arr))