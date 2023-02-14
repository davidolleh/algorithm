class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        cnt = -1
        deleteIndex = []
        for w in range(len(s)):
            tmp = self.checkSpecialCharacter(s=s[w])
            if tmp == 1:
                cnt += 1
                stack.append([w, s[w]])
            elif tmp == 2:
                if cnt == -1:
                    v1 = -100
                    k1 = -100
                else:
                    v1 = stack[cnt][1]
                    k1 = stack[cnt][0]

                check = self.checkMatchedCharacter(s1=v1, s2=s[w])

                if check:
                    stack.pop(cnt)
                    cnt -= 1
                else:
                    if cnt != -1:
                        deleteIndex.append(k1)
                    deleteIndex.append(w)

        for i in stack:
            k1 = i[0]
            deleteIndex.append(k1)

        newC = ''
        for j in range(len(s)):
            if j not in deleteIndex:
                newC += s[j]

        return newC

    def checkMatchedCharacter(self, s1: str, s2: str) -> True:
        if s1 == '(' and s2 == ')':
            return True

        return False

    def checkSpecialCharacter(self, s: str) -> int:
        if s == '(':
            return 1
        elif s == ')':
            return 2
        else:
            return 3


s = Solution()
a = s.minRemoveToMakeValid(s="lee(t(c)o)de)")
print(a)
