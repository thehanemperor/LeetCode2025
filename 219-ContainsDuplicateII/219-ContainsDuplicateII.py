class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        index = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = [i]
            else:
                seen[nums[i]].append(i)

        for key,v in seen.items():
            if len(v)>1:
                for i in range(len(v)):
                    for j in range(i+1,len(v)):
                        if abs(v[i] - v[j]) <= k:
                            return True

        return False
