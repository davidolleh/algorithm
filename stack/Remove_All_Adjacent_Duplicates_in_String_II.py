class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if len(stack) == 0:
                stack.append([c,1])
            else:
                if stack[-1][0] == c:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([c,1])

        newC = ''
        for i in stack:
            l = i[1]
            for j in range(l):
                newC += i[0]

        return newC



s = Solution()
# a = s.removeDuplicates(s = "deeedbbcccbdaa", k = 3)
a = s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2)
print(a)