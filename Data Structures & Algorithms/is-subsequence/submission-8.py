class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sCounter = 0
        if (len(s)==0):
            return True
        if len(s)>len(t):
            return False
        for char in t:
            if char == s[sCounter]:
                sCounter+=1
            if sCounter == len(s):
                break
        

        if (sCounter == len(s)):
            return True
        else:
            return False
            
        