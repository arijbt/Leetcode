class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            for i in range(len(x_str)):
                if i >= len(x_str)-1-i:
                    return True
                elif x_str[i]!=x_str[len(x_str)-1-i]:
                    return False
                    
        