def productionExceptSelf(nums: list[int]) -> list[int]:
    l = len(nums)
    res = list(range(l))
    tmp = 1
    for leftIndex in range(l):
        res[leftIndex] = tmp
        tmp = tmp * nums[leftIndex]

    tmp = 1
    for rightIndex in reversed(range(l)):
        res[rightIndex] = res[rightIndex] * tmp
        tmp = tmp * nums[rightIndex]


    return res

# a = productionExceptSelf(nums=[1, 2, 3, 4])
a = productionExceptSelf(nums=[-1, 1, 0, -3, 3])
print(a)
