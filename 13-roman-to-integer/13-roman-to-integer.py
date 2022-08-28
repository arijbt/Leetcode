class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if len(s)==1:
            return d[s]
        else:
            sum = 0
            e = s[0]
            for i in range(1,len(s)):
                if d[e]>=d[s[i]]:
                    sum+=d[e]
                else:
                    sum-=d[e]
                    
                e = s[i]
            sum+=d[s[len(s)-1]]
            return sum
        
        