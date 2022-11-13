class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        for char in t:
            if counts[char] == 0:
                return False
            counts[char] -= 1
        return True
        
#                 dic = {}
#         for i in s:
#             if i not in dic:
#                 dic[i] = 1
#             else:
#                 dic[i] += 1
        
#         for j in t:
#             if j not in dic:
#                 return False
#             else:
#                 dic[j] -= 1
        
#         for val in dic.values():
#             if val != 0:
#                 return False
        
#         return True