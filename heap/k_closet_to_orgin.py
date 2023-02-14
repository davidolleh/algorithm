from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heapq.heapify(ans)
        for pt in points:
            d = pt[0]**2 + pt[1]**2
            heapq.heappush(ans, (-d, pt)) #always push
            if len(ans) > k: #pop when
                heapq.heappop(ans)

        print(ans)

        return [y for x, y in ans]
        # pointsD = []
        # closest = []
        # for point in points:
        #     pointDict = {(point[0], point[1]): point[0] * point[0] + point[1] * point[1]}
        #     pointsD.append(pointDict)
        #
        #
        # for point in pointsD:
        #     key = [k for k in point]
        #     value = [v for v in point.values()]
        #     heapq.heappush(closest, (-1 * value[0], key))
        #
        #     if len(closest) > k:
        #         heapq.heappop(closest)
        #
        # result = []
        #
        # for i in closest:
        #     result.append([i[1][0][0], i[1][0][1]])
        #
        # return result

s = Solution()
a = s.kClosest(points = [[2,2],[2,2],[3,3],[2,-2],[1,1]], k = 4)
print(a)