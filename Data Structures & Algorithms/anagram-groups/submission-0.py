class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping character count to list of anagrams; default value is a list

        for s in strs:
            count = [0] * 26 #26 zeros for each character: a...z

            for c in s:
                count[ord(c)- ord("a")] += 1 #ex: a = 80 -> 0 (80-80), b = 81 -> 1 (81-80); 

            res[tuple(count)].append(s) #group all anagrams with that particular count together
        #tuple bc list cannot be keys

        return list(res.values()) 