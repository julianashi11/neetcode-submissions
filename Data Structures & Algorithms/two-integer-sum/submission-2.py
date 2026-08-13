class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, n in enumerate(nums): #i is the index, n is the number
            diff = target - n 
            if diff in store:
                return [store[diff], i]
            store[n] = i
        return
            