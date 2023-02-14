class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sD = {}
        tD = {}
        for i in s:
            if i in sD:
                sD[i] = sD[i] + 1

            else:
                sD[i] = 1

        for i in t:
            if i in tD:
                tD[i] = tD[i] + 1

            else:
                tD[i] = 1

        for k, v in tD.items():
            if k in sD:
                if sD[k] == v:
                    continue
                else:
                    return False
            else:
                return False

        return True

s = Solution()
print(s.isAnagram(s = "rat", t = "car"))