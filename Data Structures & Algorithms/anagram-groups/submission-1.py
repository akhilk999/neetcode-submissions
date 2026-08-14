class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) # key = sorted value, value = list of anagrams of that word

        # go through entire list
            # for each item, first sort word by letters 
            # check if existing dict key == sorted word
                # if so, add to that key's list value
        for item in strs:
            sorted_item = "".join(sorted(item))
            dict[sorted_item].append(item)
        return list(dict.values())
        