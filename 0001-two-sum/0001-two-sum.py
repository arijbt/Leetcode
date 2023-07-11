class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}
        for i, value in enumerate(nums): 
            remaining = target - nums[i] 
           
            if remaining in seen_values: 
                return [seen_values[remaining], i]  
            else:
                seen_values[value] = i 