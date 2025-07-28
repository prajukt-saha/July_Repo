def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  
    return -1  

my_list = [10, 23, 45, 70, 11, 15]
search_target = 70

result = linear_search(my_list, search_target)

if result != -1:
    print(f"Element {search_target} found at index: {result}")
else:
    print(f"Element {search_target} not found in the list.")

search_target_not_present = 99
result_not_present = linear_search(my_list, search_target_not_present)

if result_not_present != -1:
    print(f"Element {search_target_not_present} found at index: {result_not_present}")
else:
    print(f"Element {search_target_not_present} not found in the list.")