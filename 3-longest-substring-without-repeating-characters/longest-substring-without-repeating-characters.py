class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_set = set()
        l,r = 0,0
        result = 0
        if len(s) == 1:
            return 1
        while r<=len(s)-1:
            while s[r] in string_set:
                string_set.remove(s[l])
                l+=1
            string_set.add(s[r])
            result = max(result,r-l+1)
            print(result,r-l+1)
            r+=1
        return result
