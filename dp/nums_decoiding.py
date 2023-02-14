# class Solution:
#     def canBeLargeNumber(self, f: str, s: str):
#         first = int(f)
#         second = int(s)
#         if first == 1:
#             return True
#         elif first == 2:
#             return 0 <= second <= 6
#         else:
#             return False
#
#     def numDecodings(self, s: str) -> int:
#
#         cache = [-1] * len(s)
#
#         for i in range(len(s)):
#
#         if len(s) == 0:
#             return 1
#         if s[0] == '0':
#             return 0-
#
#         if len(s) == 1:
#             return 1
#
#         if self.canBeLargeNumber(f = s[0], s = s[1]):
#             return self.numDecodings(s = s[1:]) + self.numDecodings(s=s[2:])
#         else:
#             return self.numDecodings(s=s[1:])
#
#
# s = Solution()
# print(s.numDecodings(s = "106"))