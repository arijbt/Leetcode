class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 0
        if nums[int(n/2)-1] > nums[int(n/2)]:
            return self.findPeakElement(nums[0:int(n/2)]) 
        elif nums[int(n/2)-1] < nums[int(n/2)]:
            return self.findPeakElement(nums[int(n/2):]) + int(n/2)
        else:
            return int(n/2)-1
   




