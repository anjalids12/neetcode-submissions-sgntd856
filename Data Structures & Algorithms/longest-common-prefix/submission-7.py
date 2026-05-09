class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        comon_prefix=""
        for i in range(len(first)):
                if first[i]==last[i]:
                    comon_prefix=comon_prefix+first[i]
                    # continue
                else:
                    return comon_prefix
        return comon_prefix
            

