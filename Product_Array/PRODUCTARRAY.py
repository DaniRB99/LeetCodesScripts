class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1]*len(nums)
        for i, num in enumerate(nums):
            mult = output[i]
            output.pop(i)
            print(f"Mult {num} para {output}")
            output = list(map(lambda x:x*num, output))
            print(output)
            output.insert(i,mult)
            print(f"Después {output}")
        return output
            
if __name__ == "__main__":
    param = [1]
    mySol = Solution()
    
    print(f"output: {mySol.productExceptSelf(param)}")