from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        sub_array = [-1] * (amount + 1)

        for i in range(len(coins)):
            if coins[i] <= amount:
                sub_array[coins[i]] = 1

        for i in range(1, amount + 1):
            if sub_array[i] == -1:
                maxC = -1
                for coin in coins:
                    index1 = i - coin

                    if index1 > 0 and sub_array[index1] != -1:
                        if maxC == -1:
                            maxC = sub_array[index1] + 1
                        else:
                            if maxC > sub_array[index1] + 1:
                                maxC = sub_array[index1] + 1
                sub_array[i] = maxC

        return sub_array[-1]







s = Solution()

print(s.coinChange(coins = [2], amount = 3))