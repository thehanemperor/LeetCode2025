# Last updated: 4/7/2025, 1:03:43 AM
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substringMap = defaultdict(list)
        for string in arr:
            unique = set()
            for start in range(len(string)):
                for end in range(start,len(string)):
                    tmp = string[start:end+1]
                    unique.add(tmp)
            for substring in unique:
                substringMap[substring].append(string)

        resMap = defaultdict(list)
        for string in arr:
            for substring, stringList in substringMap.items():
                if len(stringList) == 1 and stringList[0] == string:
                    if not resMap[string]:
                        resMap[string].append(substring)
                    else:
                        if len(substring) <= len(resMap[string][0]):
                            if len(substring) < len(resMap[string][0]):
                                resMap[string].pop()
                                resMap[string].append(substring)
                            else:
                                if substring < resMap[string][0]:
                                    resMap[string].pop()
                                    resMap[string].append(substring)

        res = []
        for string in arr:
            if not resMap[string]:
                res.append("")
            else:
                res.append(resMap[string][0])

        return res