def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    tmp = nums1[:m]
    newList = []
    nums1I = 0
    nums2I = 0
    while nums2I < n and nums1I < len(tmp):
        if tmp[nums1I] <= nums2[nums2I]:
            newList.append(tmp[nums1I])
            nums1I += 1
        else:
            newList.append(nums2[nums2I])
            nums2I += 1

    while nums2I < n:
        newList.append(nums2[nums2I])
        nums2I += 1

    while nums1I < len(tmp):
        newList.append(tmp[nums1I])
        nums1I += 1

    for i in range(len(nums1)):
        nums1[i] = newList[i]


def mergeSort(nums1) -> list[int]:
    l = len(nums1)

    if l == 1:
        return nums1

    p = findPivot(l)

    right = mergeSort(nums1[p:])
    left = mergeSort(nums1[:p])

    return merge(left, right)




def findPivot(m: int):
    return m // 2

def merge(nums1: list[int], nums2: list[int]) -> list[int]:
    l1 = 0
    l2 = 0
    newList = []

    while l1 < len(nums1) and l2 < len(nums2):
        if nums1[l1] <= nums2[l2]:
            newList.append(nums1[l1])
            l1 += 1
        else:
            newList.append(nums2[l2])
            l2 += 1

    while l1 < len(nums1):
        newList.append(nums1[l1])
        l1 += 1

    while l2 < len(nums2):
        newList.append(nums2[l2])
        l2 += 1

    return newList





nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# merge(nums1, m=m, nums2=nums2, n=3)
# print(nums1)

j = 0
for i in range(m, m + n):
    nums1[i] = nums2[j]
    j += 1
a = mergeSort(nums1)
print(a)
