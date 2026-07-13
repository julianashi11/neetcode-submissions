class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] #bucket array

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        #n = number and c = count
        for n, c in count.items(): #returns every key value pair
            freq[c].append(n) #value n occurs c number of times
        
        res = []
        for i in range(len(freq) - 1, 0, -1): #-1: last next, go up until 0, we are going to descending order
            for n in freq[i]: #since multiple numbers could have the same freq, you loop through the elements inside that bucket
                res.append(n)
                if len(res) == k: # once the list has exactly k elements, you stop
                    return res