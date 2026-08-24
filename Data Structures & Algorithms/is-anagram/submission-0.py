class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first={}
        second={}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            #for s
            if s[i] not in first:
                first[s[i]] = 1
            else:
                first[s[i]]+=1
            #for t
            if t[i] not in second:
                second[t[i]] = 1
            else:
                second[t[i]]+=1
           

        for char in s:
            if char in second:
                if first[char]== second[char]:
                    continue
                else:
                     return False 
            else :
                return False
        return True


        