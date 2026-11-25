
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    comparisons = 0
    result = -1

    while low <= high:
        mid = (low + high) // 2
        value = nums[mid]

        comparisons += 1

        if value == target:
            result = mid
            high = mid - 1

        else:
            comparisons += 1

            if value < target:
                low = mid + 1
            else:
                high = mid - 1

    return result, comparisons


# Testing the function
numbers = [2, 4, 6, 6, 6, 8, 10]

print(binary_search(numbers, 6))
print(binary_search(numbers, 8))
print(binary_search(numbers, 5))



def rle_encode(text):
    if text == "":
        return ""
    
    result = ""
    i = 0

    while i < len(text):
        count = 1


