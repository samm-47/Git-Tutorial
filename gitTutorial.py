def remove_element(nums, val):
    """Removes all occurrences of val from the nums list in place."""
    
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Expected 'nums' to be a list.")
    
    if not nums:  # Check if the list is empty
        return 0  # Return 0 if the list is empty

    write_index = 0  # Index to place non-val elements
    
    # Iterate through each number in nums
    for num in nums:
        if num != val:
            # If the current element is not val, keep it in the list
            nums[write_index] = num
            write_index += 1
    
    # Trim the list to contain only elements up to the new length
    nums[:] = nums[:write_index]

    # Returning both the new length and the modified list
    return write_index, nums[:write_index]  # Returns the new length and modified list

# Example usage
nums_list = [3, 2, 2, 3, 4, 3, 5]
val_to_remove = 3
new_length, modified_list = remove_element(nums_list, val_to_remove)
print(f"New length: {new_length}, Modified list: {modified_list}")
