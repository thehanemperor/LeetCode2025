class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.phone = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        self.res = []
        self.dfs(0,digits,[])
        return self.res

    def dfs(self,index,digits,arr):
        if index == len(digits):
            self.res.append("".join(arr))
            return 

        for char in self.phone[int(digits[index])]:
            arr.append(char)
            self.dfs(index + 1, digits, arr)
            arr.pop()

