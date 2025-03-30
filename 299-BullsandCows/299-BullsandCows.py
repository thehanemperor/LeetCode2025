# Last updated: 3/30/2025, 2:01:32 AM
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        seen = {}
        for i in range(len(secret)):
            seen[secret[i]] = seen.get(secret[i],0) + 1

        bull = 0
        cow = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                # seen[secret[i]] -= 1

        for i in range(len(guess)):

            if guess[i] in seen and seen[guess[i]] >0:
                cow += 1
                seen[guess[i]] -= 1

        return "{}A{}B".format(bull,cow-bull)