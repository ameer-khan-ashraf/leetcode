class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_set = set()
        l,result = 0,0
        for r in range(len(s)):
            while s[r] in string_set:
                string_set.remove(s[l])
                l+=1
            string_set.add(s[r])
            result = max(result,r-l+1)
        return result
