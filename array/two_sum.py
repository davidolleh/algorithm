def twoSum(nums: list[int], target: int) -> list[int]:
    requiredInts = dict()
    for i in range(len(nums)):
        needNumber = target - nums[i]
        if needNumber in requiredInts:
            return [requiredInts[needNumber], i]
        else:
            requiredInts[nums[i]] = i

a = twoSum(nums=[2, 11, 7, 15], target=9)
print(a)




