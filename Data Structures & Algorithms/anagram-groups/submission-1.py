class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = dict()
        for ele in strs:
            new_dict = dict()
            for i in ele:
                if i in new_dict:
                    new_dict[i] += 1
                else:
                    new_dict[i] = 1
            print("new_dict: ", new_dict)
            new_ele = ""
            for k in sorted(new_dict):
                new_ele = new_ele + k + str(new_dict[k])
            
            print("new_ele: ", new_ele)
            if new_ele in hash_dict:
                hash_dict[new_ele].append(ele)
            else:
                 hash_dict[new_ele] = [ele]

        return list(hash_dict.values())

        # hash_dict = dict()
        # for ele in strs:
        #     sorted_ele = "".join(sorted(ele.lower()))
        #     if sorted_ele in hash_dict:
        #         hash_dict[sorted_ele].append(ele)
        #     else:
        #         hash_dict[sorted_ele] = [ele]
        # return list(hash_dict.values())