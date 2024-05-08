class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {'}':'{',']':'[',')':'('}
        stack=[]
        for i in s:
            # if you get a closing parenthesis
            if i in bmap:
                # check if last element in stack is same as the one in the map for closing parenthesis
                if stack and stack[-1] == bmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                #add to stack if it is an open parenthesis
                stack.append(i)
        # returning true only if stack is empty
        return True if not stack else False

