class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = {}
        copy_nums = nums[:]
        for n in nums:
            if n not in t.keys():
                t[n] = 1
        
        for n in copy_nums:
        
            if t[n] < 1:
                nums.remove(n)
                continue
            if n in t.keys():
                t[n] -= 1
                
            
       
        return len(nums)
