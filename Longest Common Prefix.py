class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

       

        ans = ""
        strings = sorted(strs)
        
        first = strings[0]
        last = strings[-1]

        
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            else:
                ans += first[i]
        return ans
        
        
