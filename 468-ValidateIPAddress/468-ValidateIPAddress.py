class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v4 = queryIP.split(".")
        v6 = queryIP.split(":")
        if len(v4) == 4:
            if self.validIpv4(v4):
                return "IPv4"
        if len(v6) == 8:
            if self.validIpv6(v6):
                return "IPv6"

        return "Neither"


    def validIpv4(self,query):
        for num in query:
            if not num.isdigit():
                return False
            if len(num) >1 and num[0] == "0":
                return False
            curr = int(num)
            if curr< 0 or curr>255:
                return False

        return True

    def validIpv6(self,query):
        # 8 segment
        validSeg = "0123456789abcdefABCDEF"
        for seg in query:
            if not 1<=len(seg)<=4:
                return False
            for char in seg:
                if not (char in validSeg):
                    return False
        
        return True