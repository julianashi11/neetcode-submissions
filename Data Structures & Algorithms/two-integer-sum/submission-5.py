class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)): 
            diff = target - nums[i] 
            if diff in store:
                return [store[diff],i]
            store[nums[i]] = i #
        return # if no pair is found return empty
            