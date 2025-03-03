class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sample = strs[0]
        res = ""
        for i in range(len(sample)):
            curr = sample[i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != curr:
                    return res

            res += curr

        return res
                
        