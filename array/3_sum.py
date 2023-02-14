def threeSum(nums:list[int])->list[list[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while left < right:
            sums = nums[i] + nums[left] + nums[right]

            if sums > 0:
                right -= 1
            elif sums < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1



    return result




a = threeSum(nums=[-1,0,1,2,0,-1,4])
# a = threeSum(nums=[0,1,1])
# a = threeSum(nums=[0,0,0, 0])
print(a)