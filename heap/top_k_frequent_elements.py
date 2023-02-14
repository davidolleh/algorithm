from typing import List
import heapq
from collections import defaultdict

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         numsCnt = {}
#         largeNum = []
#
#         for num in nums:
#             if num in numsCnt:
#                 count = numsCnt[num]
#                 numsCnt[num] = count + 1
#             else:
#                 numsCnt[num] = 1
#
#         # for key, value in numsCnt.items():
#         for key, value in numsCnt.items():
#             heapq.heappush(largeNum, value)
#
#             if len(largeNum) > k:
#                 heapq.heappop(largeNum)
#
#         result = []
#         k1 = [key for key in numsCnt]
#         v1 = [value for value in numsCnt.values()]
#         for value in largeNum:
#             vIdx = v1.index(value)
#             result.append(k1[vIdx])
#             del v1[vIdx]
#             del k1[vIdx]
#         return result
#
#
#
# # b = [0,0,0,0,0,0]
# # print(b.index(0))
# # b.remove(0)
# # print(b)
# s = Solution()
# # a  = s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
# # a = s.topKFrequent(nums = [-1, -1], k = 1)
# a = s.topKFrequent(nums = [1, 2], k = 2)
# # a = s.topKFrequent(nums = [1], k = 1)
# print(a)

from typing import List
from collections import defaultdict
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    if k == 0:
        return []

    #hash map
    count_map = defaultdict(int)

    #count over nums
    for num in nums:
        count_map[num] += 1

    #fixed size heap
    topK_heap = []
    for num in count_map:
        heapq.heappush(topK_heap,(count_map[num],num))  #use hashmap count as comp
        if k < len(topK_heap):
            heapq.heappop(topK_heap)

    print(topK_heap)
    #return list
    topK = []
    for count,num in topK_heap:
        topK.append(num)

    return topK


topK = topKFrequent(nums=[1,3,5,3,9,3,7,5], k = 2 )
print(topK)
