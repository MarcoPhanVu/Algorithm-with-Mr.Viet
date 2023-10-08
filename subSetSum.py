def maxCrossingSum(arr, left, middle, right):
    # Get elements from the left
    temp_sum = 0
    left_sum = -10000 # first ele might be lower than 0
    
    for i in range(middle, left - 1, -1):
        # print("i: ", i)
        temp_sum += arr[i]
        
        if (temp_sum > left_sum):
            left_sum = temp_sum
            
    
    temp_sum = 0
    right_sum = -100000
    for i in range(middle, right + 1):
        temp_sum += arr[i]
        
        if (temp_sum > right_sum):
            right_sum = temp_sum
            
    return max( left_sum + right_sum - arr[middle], # Right sum already contain arr[middle]
                left_sum,
                right_sum)
    
    
def maxSubArraySum(arr, left, right): 
    # Invalid Range:
    if (left > right): 
        return -10000
    
    if (left == right): 
        return arr[left] 
    
    middle = (left + right) // 2

    return max( maxSubArraySum(arr, left, middle - 1), 
                maxSubArraySum(arr, middle + 1, right), 
                maxCrossingSum(arr, left, middle, right)) 
    
arrA = [-2, -3, 4, -1, -2, 1, 5, -3] # Should be 7
arrB = [-2, -5, 6, -2, -3, 1, 5, -6] # Should be 7
arrC = [2, 3, 4, 5, 7] # Should be 21
arrD = [4, 2, 5, 0, -1, 6] # Should be 16

print("Max Sum ArrA: ", maxSubArraySum(arrA, 0, len(arrA) - 1))
print("Max Sum ArrB: ", maxSubArraySum(arrB, 0, len(arrB) - 1))
print("Max Sum ArrC: ", maxSubArraySum(arrC, 0, len(arrC) - 1))
print("Max Sum ArrD: ", maxSubArraySum(arrD, 0, len(arrD) - 1))


# for i in range(10, 2 - 1):
#     print("iheehhe: ", i)