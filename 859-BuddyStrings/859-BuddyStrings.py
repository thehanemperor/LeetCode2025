class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count1 = Counter(s)
        count2 = Counter(goal)
        if count1 != count2:
            return False
        
        if s == goal:
            for key,val in count1.items():
                if val >=2:
                    return True

            return False
        
        

        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1

        return diff == 2