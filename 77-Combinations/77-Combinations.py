class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.dfs(1,n,k,[])
        return self.res

    def dfs(self,index,n,k,arr):
        

        if index > n+1:
            return 

        if len(arr) == k:
            self.res.append([x for x in arr])
            return 
        
        arr.append(index)
        self.dfs(index+1,n,k,arr)
        arr.pop()
        self.dfs(index+1,n,k,arr)
        
        

        
        