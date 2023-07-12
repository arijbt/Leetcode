class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums) - 1
        left_index, right_index = 0, n
        while right_index > left_index:
            middle_index = (right_index + left_index)//2
            if nums[middle_index]> nums[middle_index+1]:
                right_index = middle_index
            else:
                left_index = middle_index+1
        return left_index

        
   




