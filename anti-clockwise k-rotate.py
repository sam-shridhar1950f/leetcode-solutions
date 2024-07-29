from typing import List

def anti_rotate_array(nums: List[int], k: int) -> None:
    # TODO: Implement anti-clockwise rotation of the array nums by k steps.
    k = k % len(nums)
    l, r = 0, k - 1
    while l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    
    l, r = k, len(nums) - 1
    while l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    
    l, r = 0, len(nums) - 1
    while l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
        
    return nums
    
    
