class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =='':return ''
        window, countT = {},{}
        
        for c in t:
            countT[c] = 1+ countT.get(c,0)
        
        have,need = 0,len(countT)
        l = 0
        resCount,res = float('infinity'),[-1,-1]

        for r in range(len(s)) :
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                if (r-l+1) < resCount:
                    resCount = r-l+1
                    res = [l,r]

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l+=1
        l,r = res

        return s[l:r+1] if resCount != float('infinity') else '' 


