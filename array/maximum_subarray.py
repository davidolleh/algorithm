def maxSubArray(nums: list[int]) -> int:
    l = len(nums)
    sum = 0
    maxN = nums[0]
    for i in range(l):
        # if nums[i] < 0:
        #     sum = sum + nums[i]
        # else:
        tmp = sum + nums[i]

        checkList = [maxN, tmp, nums[i]]
        newMax = checkList[0]
        for j in checkList:
            if j > newMax:
                newMax = j

        if newMax == maxN:
            if tmp > nums[i]:
                sum = tmp
            else:
                sum = nums[i]
            maxN = newMax

        elif newMax == tmp:
            sum = tmp
            maxN = tmp
        elif newMax == nums[i]:
            sum = nums[i]
            maxN = nums[i]

    return maxN


def bruteForceSolution(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(cur_sum, max_sum)

    return max_sum


def kadanesSolution(nums):
    max_sum = nums[0]
    cur_sum = nums[0]
    for i in range(1, len(nums)):
        cur_sum = max(cur_sum + nums[i], nums[i])
        max_sum = max(cur_sum, max_sum)

    return max_sum


def divideAndConquer(nums: list[int], l=None, r=None):
    if l == None: l = 0
    if r == None: r = len(nums) - 1

    if l == r:
        return nums[l]

    m = (l + r) // 2

    left_subarray_max_sum = divideAndConquer(nums, l, m)
    right_subarray_max_sum = divideAndConquer(nums, m + 1, r)
    max_cross_sum = maxCrossSum(nums, l, m, r)

    return max(left_subarray_max_sum, right_subarray_max_sum, max_cross_sum)


def maxCrossSum(nums: list[int], l: int, m: int, r: int):
    local_sum = 0
    left_sum = nums[m]
    for i in range(m, l - 1, -1):
        local_sum += nums[i]
        left_sum = max(local_sum, left_sum)

    local_sum = 0
    right_sum = nums[m+1]
    for i in range(m + 1, r + 1):
        local_sum += nums[i]
        right_sum = max(local_sum, right_sum)

    cross_sum = left_sum + right_sum
    return max(left_sum, right_sum, cross_sum)


# a = maxSubArray(nums=[8,-19,5,-4,20])
# a = bruteForceSolution(nums=[8,-19,5,-4,20])
# a = kadanesSolution(nums=[8,-19,5,-4,20])
# a = divideAndConquer(nums=[8, -19, 5, -4, 20])
a = divideAndConquer(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(a)
