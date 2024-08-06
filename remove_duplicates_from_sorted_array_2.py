class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        
        if (len(nums) == 0):
            return k
        
        for i in range(len(nums) - 1):
            print(nums[i], nums[i+1])
            if (nums[i] == nums[i+1]):
                nums[k] = nums[i]
                k += 1
            else:
                nums[k] = nums[i]
                nums[k+1] = nums[i+1]
                k += 1
        
        return k
    
    
solution = Solution()

nums = [0,0,1,1,1,1,2,3,3]

output = solution.removeDuplicates(nums)

print(output, nums)