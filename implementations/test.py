class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        
        for i in range(len(temperatures)):
            print(i)
            print(stack)
            print(temperatures , "\n")
            if stack and temperatures[i] > temperatures[stack[-1]]:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    removedIndex = stack.pop()
                    temperatures[removedIndex] = i-removedIndex
            stack.append(i)

        for i in range(len(stack)):
            temperatures[stack[i]] = 0
        
        return temperatures


sol = Solution()
print(sol.dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))


fixed = 10*[0]
fixed.append(1)
print(fixed)