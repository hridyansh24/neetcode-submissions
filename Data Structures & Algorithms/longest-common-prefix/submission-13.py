class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for i in range(1,len(strs)):
            for j in range(len(lcp)): 
                if len(strs[i])<=j:
                        lcp= lcp[:j]
                        print(lcp)
                        break
                
                
                
                elif strs[i][j] != lcp[j]:
                        lcp= lcp[:j]
                        print(lcp)
                        break
                else:
                    continue
        

        return lcp

                    
        