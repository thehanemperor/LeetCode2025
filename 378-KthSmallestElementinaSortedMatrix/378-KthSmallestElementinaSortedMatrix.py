# Last updated: 4/18/2025, 12:22:23 PM
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)

        for row in range(min(n,k)):
            heapq.heappush(heap,(matrix[row][0],row,0))

        for i in range(k):
            curr, row, col = heapq.heappop(heap)
            if col+1 < n:
                heapq.heappush(heap,(matrix[row][col+1], row, col+1))

        return curr