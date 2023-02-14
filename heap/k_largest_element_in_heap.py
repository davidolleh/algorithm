import heapq

nums = [11,9,7,5,3,11]

print(nums)

large_nums = []

a = nums
heapq.heapify(nums)
print(a)

for num in nums:
    heapq.heappush(large_nums, num)
    if 3 < len(large_nums):
        heapq.heappop(large_nums)


print(large_nums)