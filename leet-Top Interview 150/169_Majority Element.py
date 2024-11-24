from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            print(hash_map)
            if i in hash_map:
                print("-------<")
                hash_map[i] = hash_map.get(i)+1
                print(hash_map)
            else:
                hash_map[i] = 1
                
        sorted_by_values = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        print(sorted_by_values)       
        first_value = next(iter(sorted_by_values.keys()))
        return first_value
###### better solution for hash_map
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         hash = {}
#         res = majority = 0
        
#         for n in nums:
#             hash[n] = 1 + hash.get(n, 0)
#             if hash[n] > majority:
#                 res = n
#                 majority = hash[n]
        
#         return res
    

###### check this solution is great unfortunately i didn't think of it thanks to Soumen Maity for his brain
# class Solution:
#  def majorityElement(self, nums):
#   candidate, count = None, 0
#   for num in nums:
#    if count == 0:
#     candidate = num
#    count += 1 if num == candidate else -1
#   return candidate
