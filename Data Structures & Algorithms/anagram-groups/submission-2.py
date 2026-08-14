class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for item in strs:
            arr = [0] * 26
            for c in item:
                arr[ord(c) - ord('a')] += 1
            group[tuple(arr)].append(item)
        return list(group.values())
        