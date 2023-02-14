class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for i in range(len(s)):
            if i == 0:
                count[s[i]] = (1, i)

            else:
                if s[i] in count:
                    repeat = count[s[i]][0]
                    index = count[s[i]][1]
                    count[s[i]] = (repeat + 1, index)
                else:
                    count[s[i]] = (1, i)

        key = None
        for k, v in count.items():
            repeat = v[0]
            if repeat == 1:
                key = k
                break

        return count[key][1] if key else -1

s = Solution()
print(s.firstUniqChar(s = "aabb"))