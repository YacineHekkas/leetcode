from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a counter for the number of elements removed
        counter = 0
        i = 0

        # Iterate through the list
        while i < len(nums):
            if nums[i] == val:
                counter += 1
                nums.pop(i) 
                print(nums)
            else:
                i += 1  # Only increment i if no removal

        return counter

def main():
    # Example input
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    # Create an instance of the Solution class
    solution = Solution()

    # Call the removeElement function
    result = solution.removeElement(nums, val)

    # Output the results
    print(f"Number of elements removed: {result}")
    print(f"Modified list: {nums}")

if __name__ == "__main__":
    main()
