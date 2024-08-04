class Solution:
    def removeDuplicates(self, nums:list[int]) -> int:
        k = 0
        
        if (len(nums) == 0):
            return k
        
        for i in range(len(nums)):
            if i < len(nums) - 1:
                if (nums[i] != nums[i+1]):
                    nums[k] = nums[i]
                    k += 1
            else:
                k += 1
                nums[k-1] = nums[i]
                
        for i in range(k, len(nums)):
            nums[i] = "_"
        
        return k
    

solution = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
    
output = solution.removeDuplicates(nums)

print(output, nums)