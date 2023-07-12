class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 0
        if nums[n//2-1] > nums[(n//2)]:
            return self.findPeakElement(nums[0:(n//2)]) 
        elif nums[(n//2)-1] < nums[(n//2)]:
            return self.findPeakElement(nums[(n//2):]) + (n//2)
        else:
            return (n//2)-1

        
   




