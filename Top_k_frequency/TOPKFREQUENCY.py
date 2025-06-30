class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numFrequent = {}
        for num in nums:
            if not numFrequent.get(num):
                numFrequent[num] = 1
            else:
                numFrequent[num] = numFrequent[num]+1
            print(f"{numFrequent}")
        
        print("")
        while (len(numFrequent)>k):
            holder=(None, None)
            for key, value in numFrequent.items():
                if holder[0] is None or value < holder[1]:
                    holder = (key, value)
            print(f"para popear {holder}")
            numFrequent.pop(holder[0])

        return list(numFrequent.keys())
    
if __name__ == "__main__":
    nums = [1,2,2,3,3]
    k = 2
    print(f"Params nums: {nums} k: {k}")
    mySol = Solution()
    print(f"Output: {mySol.topKFrequent(nums, k)}")
    