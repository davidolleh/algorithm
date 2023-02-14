from typing import List

class Solution:
    def findKLargest(self, nums:List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        pivotIdx = self.findPivot(nums)

        self.swapListWithIndex(nums, pivotIdx)

        leftIdx = 0
        rightIdx = len(nums) - 2
        pivot = nums[len(nums) - 1]
        while leftIdx <= rightIdx:
            if nums[leftIdx] <= pivot:
                leftIdx += 1
                continue

            if nums[rightIdx] >= pivot:
                rightIdx -= 1
                continue

            if pivot < nums[leftIdx] and pivot >= nums[rightIdx]:
                nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
                continue

        nums[leftIdx], nums[len(nums) - 1] = nums[len(nums) - 1], nums[leftIdx]

        wantIdx = len(nums) - k
        if leftIdx > wantIdx:
            findIdx = k - (len(nums) - leftIdx)
            return self.findKLargest(nums[:leftIdx], findIdx)

        elif leftIdx < wantIdx:
            return self.findKLargest(nums[leftIdx + 1:], k)
        else:
            return nums[leftIdx]

    def swapListWithIndex(self, nums: List[int], index: int):
        last = len(nums) - 1

        nums[index], nums[last] = nums[last], nums[index]

    def findPivot(self, nums: List[int]):
        return len(nums) // 2


s = Solution()
a = s.findKLargest(nums = [99, 99], k = 1)
print(a)


