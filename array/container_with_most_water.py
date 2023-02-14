def maxArea(height: list[int])-> int:
    maxA = 0
    start = 0
    last = len(height) - 1
    while start < last:
        usedHeight = height[last] if height[start] > height[last] else height[start]

        area = usedHeight * (last - start)

        if maxA < area:
            maxA = area

        if usedHeight == height[last]:
            last += -1
        else:
            start += 1

    return maxA


a = maxArea(height=[1,8,6,2,5,4,8,3,7])
b = maxArea(height=[1,1])

print(a, b)