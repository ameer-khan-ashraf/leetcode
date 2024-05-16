class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] #pair:[index, temp]

        for i,t in enumerate(temperatures):
            # checking if the stack is not empty and curret temp is greater than the rightmost temp in stack
            while stack and t>stack[-1][1]:
                index,temp = stack.pop()
                res[index] = (i - index)
            # if not greater than the current temp, simply add to stack and continue operation
            stack.append([i,t])
        return res

