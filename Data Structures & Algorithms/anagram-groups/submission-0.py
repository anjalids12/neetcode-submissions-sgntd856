class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = dict()
        for ele in strs:
            sorted_ele = "".join(sorted(ele.lower()))
            if sorted_ele in hash_dict:
                hash_dict[sorted_ele].append(ele)
            else:
                hash_dict[sorted_ele] = [ele]
        return list(hash_dict.values())