
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Number of elements that are not equal to val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # Replace the remaining elements with an underscore or any placeholder
        for i in range(k, len(nums)):
            nums[i] = "_"
        
        return k

# Example usage
solution = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
output = solution.removeElement(nums, val)

print(output)  # Output: 5
print(nums)  # Output: [0, 1, 3, 0, 4]
