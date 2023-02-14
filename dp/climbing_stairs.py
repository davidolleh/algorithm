class Solution:
    def climbStairs(self, n: int) -> int:
        wantedArray = n - 1

        if wantedArray == 0:
            return 1
        elif wantedArray == 1:
            return 2

        sub_array = [1, 2]


        for i in range(n - 2):
            new = sub_array[0] + sub_array[1]
            sub_array[0], sub_array[1] = sub_array[1], new


        return sub_array[1]




s = Solution()
a = s.climbStairs(n = 2)
print(a)