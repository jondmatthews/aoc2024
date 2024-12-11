#!/usr/bin/env python3

import fileinput

def is_monotonic(numbers):
    """
    Check if a list of integers is either strictly increasing or strictly decreasing,
    with differences between adjacent numbers being at least 1 and at most 3.
    The function also returns True if removing one number would make the sequence monotonic.
    
    Args:
        numbers (list): List of integers to check
        
    Returns:
        bool: True if the list is strictly increasing or strictly decreasing with valid differences,
              or can be made so by removing one number. False otherwise
    """
    if len(numbers) <= 1:
        return True
        
    def check_valid_differences(nums):
        for i in range(len(nums) - 1):
            diff = abs(int(nums[i]) - int(nums[i + 1]))
            if diff < 1 or diff > 3:
                return False
        return True
    
    def is_valid_sequence(nums):
        if not check_valid_differences(nums):
            return False
        increasing = all(int(nums[i]) < int(nums[i + 1]) for i in range(len(nums) - 1))
        decreasing = all(int(nums[i]) > int(nums[i + 1]) for i in range(len(nums) - 1))
        return increasing or decreasing
    
    # Check if already monotonic
    if is_valid_sequence(numbers):
        return True
    
    # Try removing each number one at a time
    for i in range(len(numbers)):
        test_sequence = numbers[:i] + numbers[i+1:]
        if is_valid_sequence(test_sequence):
            return True
            
    return False

valid_count = 0
for line in fileinput.input():
    report = line.split(" ")
    if (is_monotonic(report)):  
        valid_count = valid_count + 1   

print(valid_count) 
