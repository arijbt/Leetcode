class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        temporary_int = x
        reversed_int = 0
        
        while temporary_int > 0:
            
            reversed_int = reversed_int * 10 + temporary_int % 10
            temporary_int = temporary_int//10        
        
        return reversed_int == x
           
            
            
                    
        