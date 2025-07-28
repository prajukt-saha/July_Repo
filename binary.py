def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    arr = [1, 3, 5, 7, 9, 11, 13]
    key = int(input("Enter element to search: "))
    result = binary_search(arr, key)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

if __name__ == "__main__":
    main()
