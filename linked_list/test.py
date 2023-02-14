from typing import List
import random

def quickSort(nums:List[int], beginIdx:int, lastIdx:int)->List[int]:
    length = lastIdx-beginIdx+1
    if length <= 1:
        return nums

    pivotIdx = random.randrange(beginIdx,lastIdx+1) #pivot 선정

    nums[pivotIdx],nums[lastIdx] = nums[lastIdx],nums[pivotIdx] # pivot 숫자와 마지막과 교환

    leftIdx = beginIdx
    rightIdx = lastIdx-1
    pivot = nums[lastIdx]
    while leftIdx <= rightIdx:
        if nums[leftIdx] <= pivot:
            leftIdx += 1
            continue

        if pivot < nums[rightIdx]:
            rightIdx -= 1
            continue

        if pivot < nums[leftIdx] and nums[rightIdx] <= pivot:
            nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
            continue
    nums[leftIdx],nums[lastIdx] = nums[lastIdx],nums[leftIdx]

    quickSort(nums=nums, beginIdx=leftIdx+1,lastIdx = lastIdx)
    quickSort(nums=nums, beginIdx=beginIdx, lastIdx = leftIdx-1)

    return nums

nums = [5,7,9,3,1,5,5,2,4]
quickSort(nums=nums,beginIdx=0,lastIdx=len(nums)-1)
print(nums)
