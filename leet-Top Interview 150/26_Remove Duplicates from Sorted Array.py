from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        while i < (len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()

    result = solution.removeDuplicates(nums)

    print(f"Number of elements removed: {result}")
    print(f"Modified list: {nums}")

if __name__ == "__main__":
    main()