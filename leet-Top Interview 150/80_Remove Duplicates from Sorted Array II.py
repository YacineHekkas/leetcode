from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nb=0
        current_val= nums[0]
        i=0
        while i < len(nums):
            
            if current_val == nums[i]:
                 
                 nb += 1
                 if nb>2:
                     nums.pop(i)
                 else:
                     i+=1
                
            else:
                current_val = nums[i]
                i+=1
                nb=1
            
