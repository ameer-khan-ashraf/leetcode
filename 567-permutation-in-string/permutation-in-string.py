class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1)
        string_len = 0
        sorted_s1 = sorted(s1)

        while r <= len(s2):
            slice_s = slice(l,r)
            sub_s = s2[slice_s]

            if sorted(sub_s) == sorted_s1:
                return True
            r+=1
            l+=1
        return False

            

        
