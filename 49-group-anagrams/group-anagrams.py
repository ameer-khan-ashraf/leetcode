class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)

        for string in strs:
            sorted_word = ''.join(sorted(string))
            str_map[sorted_word].append(string)

        return list(str_map.values())
