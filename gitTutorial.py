def remove_element(nums, val):
    """Removes all occurrences of val from the nums list in place."""
    write_index = 0  # Index to place non-val elements
    
    # Iterate through each number in nums
    for num in nums:
        if num != val:
            # If the current element is not val, keep it in the list
            nums[write_index] = num
            write_index += 1
    
    # Trim the list to contain only elements up to the new length
    nums[:] = nums[:write_index]
    return write_index  # Returns the new length of the modified list
