def binary_search(arr, x):
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        mid_value = arr[mid]
        
        if mid_value == x:
            print("Found")
            return mid_value
        elif mid_value < x:
            low = mid + 1
        else:
            high = mid - 1
    
    print("Not Found")
    return -1
    

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 88, 99, 101, 122, 177]
    print(binary_search(arr, 121))