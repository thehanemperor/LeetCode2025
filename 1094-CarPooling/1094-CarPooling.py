class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for ppl,start,end in trips:
            timestamp.append([start,ppl])
            timestamp.append([end, -ppl])

        timestamp.sort()
        board = 0
        for time,ppl in timestamp:
            board += ppl
            if board > capacity:
                return False

        return True
            