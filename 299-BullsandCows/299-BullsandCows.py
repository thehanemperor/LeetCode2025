# Last updated: 3/30/2025, 2:09:13 AM
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretMap = {}
        for char in secret:
            secretMap[char] = secretMap.get(char,0) + 1

        black = 0
        white = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                black += 1

        for i in range(len(guess)):
            if guess[i] in secretMap and secretMap[guess[i]] >0:
                white += 1
                secretMap[guess[i]] -= 1

        return "{}A{}B".format(black, white - black)