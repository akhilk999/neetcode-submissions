class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqHash = defaultdict(int)
        for item in nums:
            freqHash[item] += 1
        
        sortedHash = sorted(freqHash, key=freqHash.get)
        return sortedHash[-k:]
