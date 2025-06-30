class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checkDict = {}
        target_pos= [-1,-1]
  
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in checkDict:
                target_pos = [checkDict[nums[i]],i]
                break
            else:
                checkDict[diff] = i
        return target_pos
    
if __name__ == "__main__":
    nums = [4,5,6]
    print(f"Entrada {nums}")
    mySol = Solution()
    print(f"Output: {mySol.twoSum(nums, 10)}")