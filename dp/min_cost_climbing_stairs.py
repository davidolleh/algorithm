from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sub_array = [cost[0], cost[1]]

        if len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0], cost[1])

        for i in range(len(cost) - 2):
            sub_array.append(cost[i+2] + min(sub_array[i], sub_array[i + 1]))

        return min(sub_array[len(sub_array)-1], sub_array[len(sub_array) - 2])



s = Solution()
print(s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))

