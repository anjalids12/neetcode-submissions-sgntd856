class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        comon_prefix=""
        for i,j in zip(first, last):
                if i==j:
                    comon_prefix=comon_prefix+i
                    continue
                else:
                    return comon_prefix
        return comon_prefix
            

